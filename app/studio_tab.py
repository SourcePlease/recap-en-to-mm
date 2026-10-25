from __future__ import annotations

import json
import os
import queue
import threading
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

try:
    from dotenv import load_dotenv
except ImportError:  # keep the tool useful if the optional dotenv helper is absent
    load_dotenv = None

from studio.ai_providers import AIProviderError, chat_completion
from studio.downloader import DownloadError, DownloadOptions, DownloadResult, download_media, validate_http_url
from studio.download_queue import PersistentDownloadQueue
from studio.thumbnail import ThumbnailError, generate_fal_thumbnail, generate_thumbnail
from studio.title_generator import TITLE_STYLES, ai_title_ideas, builtin_title_ideas


PROVIDER_LABEL_TO_KEY = {
    "Groq": "groq",
    "OpenRouter": "openrouter",
    "Ollama (local)": "ollama",
}
PROVIDER_KEY_TO_LABEL = {value: key for key, value in PROVIDER_LABEL_TO_KEY.items()}


class StudioTab(ttk.Frame):
    """Downloader, automatic thumbnail generator, and optional AI-provider tester."""

    def __init__(self, master, *, root_dir: Path, cfg: dict, save, tool, on_video_ready=None, env_path=None):
        super().__init__(master, padding=12)
        self.root_dir = Path(root_dir)
        self.cfg = cfg
        self.save_config = save
        self.tool = tool
        self.on_video_ready = on_video_ready
        self.env_path = env_path or (lambda: self.root_dir / ".env")
        self.last_video_path: Path | None = None
        self.queue_model = PersistentDownloadQueue(self.root_dir / "jobs" / "studio_download_queue.json")
        self.queue_stop = threading.Event()
        self.queue_running = False
        self.events: queue.Queue[tuple[str, object]] = queue.Queue()
        self.busy = False
        self._current_provider = None
        self._key_cache: dict[str, str] = {}

        if load_dotenv:
            try:
                configured_env = Path(self.env_path()).expanduser()
                if configured_env.is_file():
                    load_dotenv(configured_env, override=False)
            except (OSError, TypeError, ValueError):
                pass

        default_output = self.cfg.get("studio_output_dir") or str(self.root_dir / "Downloads")
        self.url_var = tk.StringVar(value="")
        self.output_var = tk.StringVar(value=default_output)
        self.quality_var = tk.StringVar(value="Best available")
        self.playlist_var = tk.BooleanVar(value=False)
        self.auto_thumbnail_var = tk.BooleanVar(value=True)
        self.thumbnail_aspect_var = tk.StringVar(value=str(self.cfg.get("studio_thumbnail_aspect") or "16:9"))
        self.thumbnail_title_var = tk.StringVar(value="")
        self.thumbnail_samples_var = tk.StringVar(value=str(self.cfg.get("studio_thumbnail_samples") or "8"))
        self.thumbnail_mode_var = tk.StringVar(value=str(self.cfg.get("studio_thumbnail_mode") or "Frame-based (local)"))
        self.thumbnail_style_var = tk.StringVar(value=str(self.cfg.get("studio_thumbnail_title_style") or "Anime Recap"))
        self.thumbnail_prompt_var = tk.StringVar(value=str(self.cfg.get("studio_thumbnail_scene_prompt") or ""))
        self.fal_model_var = tk.StringVar(value=str(self.cfg.get("fal_image_model") or os.getenv("FAL_IMAGE_MODEL") or "fal-ai/fast-sdxl"))
        self.fal_key_var = tk.StringVar(value=os.getenv("FAL_KEY", ""))
        self.fal_status_var = tk.StringVar(value="fal.ai AI background is optional and may use paid credits.")
        self.subtitle_var = tk.BooleanVar(value=False)
        self.cookies_var = tk.StringVar(value="")
        self.status_var = tk.StringVar(value="Ready — paste a supported media URL or select a local video.")
        self.progress_var = tk.DoubleVar(value=0)
        saved_provider = str(self.cfg.get("studio_provider") or "groq")
        self.provider_var = tk.StringVar(value=PROVIDER_KEY_TO_LABEL.get(saved_provider, "Groq"))
        self.model_var = tk.StringVar(value=str(
            self.cfg.get(f"studio_model_{saved_provider}") or self.cfg.get("studio_model") or ""))
        self.key_var = tk.StringVar(value="")
        self.ai_status_var = tk.StringVar(value="AI provider testing is optional; no request is sent until you press Test AI.")

        self._build()
        self._provider_changed()
        self.after(180, self._poll_events)

    def _build(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        ttk.Label(self, text="Recap Studio", font=("Segoe UI Semibold", 17)).grid(
            row=0, column=0, sticky="w")
        ttk.Label(
            self,
            text="Download media, create a local auto-thumbnail, and configure optional AI providers.",
            wraplength=1050,
        ).grid(row=1, column=0, sticky="w", pady=(2, 12))

        download = ttk.LabelFrame(self, text="Universal Downloader", padding=10)
        download.grid(row=2, column=0, sticky="ew")
        download.columnconfigure(1, weight=1)
        ttk.Label(download, text="Video URL").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=4)
        self.url_entry = ttk.Entry(download, textvariable=self.url_var)
        self.url_entry.grid(row=0, column=1, columnspan=3, sticky="ew", pady=4)

        ttk.Label(download, text="Save to").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=4)
        ttk.Entry(download, textvariable=self.output_var).grid(row=1, column=1, sticky="ew", pady=4)
        ttk.Button(download, text="Browse", command=self._browse_output).grid(row=1, column=2, padx=(6, 0), pady=4)

        ttk.Label(download, text="Quality").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=4)
        ttk.Combobox(
            download, textvariable=self.quality_var, state="readonly",
            values=("Best available", "1080p", "720p", "480p", "Audio only (MP3)"),
        ).grid(row=2, column=1, sticky="ew", pady=4)
        ttk.Checkbutton(download, text="Download playlist", variable=self.playlist_var).grid(
            row=2, column=2, sticky="w", padx=(8, 0), pady=4)
        ttk.Checkbutton(download, text="Auto-generate thumbnail after download",
                        variable=self.auto_thumbnail_var).grid(row=2, column=3, sticky="w", padx=(8, 0), pady=4)

        ttk.Label(download, text="Optional cookies.txt (for content you are allowed to access)").grid(
            row=3, column=0, sticky="w", padx=(0, 8), pady=4)
        ttk.Entry(download, textvariable=self.cookies_var).grid(row=3, column=1, sticky="ew", pady=4)
        ttk.Button(download, text="Browse", command=self._browse_cookies).grid(row=3, column=2, padx=(6, 0), pady=4)
        ttk.Checkbutton(download, text="Save available subtitles", variable=self.subtitle_var).grid(
            row=3, column=3, sticky="w", padx=(8, 0), pady=4)

        ttk.Label(download, text="Thumbnail format").grid(row=4, column=0, sticky="w", padx=(0, 8), pady=4)
        ttk.Combobox(
            download, textvariable=self.thumbnail_aspect_var, state="readonly",
            values=("16:9", "9:16", "1:1"),
        ).grid(row=4, column=1, sticky="ew", pady=4)
        ttk.Label(download, text="Custom title (optional)").grid(row=4, column=2, sticky="w", padx=(8, 8), pady=4)
        ttk.Entry(download, textvariable=self.thumbnail_title_var).grid(row=4, column=3, sticky="ew", pady=4)

        ttk.Label(download, text="Frame samples").grid(row=5, column=0, sticky="w", padx=(0, 8), pady=4)
        ttk.Combobox(
            download, textvariable=self.thumbnail_samples_var, state="readonly",
            values=("4", "8", "12", "16", "24"),
        ).grid(row=5, column=1, sticky="ew", pady=4)
        ttk.Label(download, text="Title style").grid(row=5, column=2, sticky="w", padx=(8, 8), pady=4)
        ttk.Combobox(
            download, textvariable=self.thumbnail_style_var, state="readonly",
            values=tuple(TITLE_STYLES.keys()),
        ).grid(row=5, column=3, sticky="ew", pady=4)

        ttk.Label(download, text="Thumbnail method").grid(row=6, column=0, sticky="w", padx=(0, 8), pady=4)
        ttk.Combobox(
            download, textvariable=self.thumbnail_mode_var, state="readonly",
            values=("Frame-based (local)", "AI generated (fal.ai)"),
        ).grid(row=6, column=1, sticky="ew", pady=4)
        ttk.Label(download, text="AI scene / plot notes (optional)").grid(
            row=6, column=2, sticky="w", padx=(8, 8), pady=4)
        ttk.Entry(download, textvariable=self.thumbnail_prompt_var).grid(
            row=6, column=3, sticky="ew", pady=4)

        action_row = ttk.Frame(download)
        action_row.grid(row=7, column=0, columnspan=4, sticky="ew", pady=(8, 2))
        self.download_button = ttk.Button(action_row, text="Download", command=self._start_download)
        self.download_button.pack(side="left")
        ttk.Button(action_row, text="Thumbnail from local video…", command=self._start_local_thumbnail).pack(
            side="left", padx=(8, 0))
        self.use_video_button = ttk.Button(action_row, text="Use downloaded video in Recap", command=self._use_downloaded_video, state="disabled")
        self.use_video_button.pack(side="left", padx=(8, 0))
        self.progress = ttk.Progressbar(action_row, maximum=100, variable=self.progress_var, length=220)
        self.progress.pack(side="left", fill="x", expand=True, padx=(14, 0))
        ttk.Label(download, textvariable=self.status_var, wraplength=1150).grid(
            row=8, column=0, columnspan=4, sticky="w", pady=(7, 0))

        lower = ttk.Frame(self)
        lower.grid(row=3, column=0, sticky="nsew", pady=(12, 0))
        lower.columnconfigure(0, weight=3)
        lower.columnconfigure(1, weight=2)
        lower.rowconfigure(0, weight=1)

        notes = ttk.LabelFrame(lower, text="Platform coverage", padding=10)
        notes.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        ttk.Label(
            notes,
            text=(
                "The downloader uses yt-dlp's installed extractors for YouTube, Facebook, TikTok, "
                "Instagram, Reddit, X/Twitter and many other sites when supported. Extractors change "
                "as websites change, so some URLs may stop working or require permitted login cookies. "
                "RedNote/Xiaohongshu support is not guaranteed by the generic extractor and needs "
                "site-specific validation. The app will report unsupported links rather than bypass "
                "access controls or DRM."
            ),
            wraplength=700, justify="left",
        ).pack(anchor="w", fill="x")
        ttk.Label(
            notes,
            text="Auto-thumbnail extracts several local video frames, ranks them by contrast/detail, then applies a title layout. "
                 "It works without a remote image-generation API.",
            wraplength=700, justify="left",
        ).pack(anchor="w", fill="x", pady=(10, 0))
        ttk.Separator(notes, orient="horizontal").pack(fill="x", pady=(12, 8))
        ttk.Label(notes, text="Persistent URL Queue", font=("Segoe UI Semibold", 10)).pack(anchor="w")
        ttk.Label(
            notes,
            text="Paste several URLs (one per line), queue them, then start the queue. Progress is saved locally under jobs/ and pending items survive app restarts.",
            wraplength=700, justify="left",
        ).pack(anchor="w", fill="x", pady=(3, 6))
        queue_list_frame = ttk.Frame(notes)
        queue_list_frame.pack(fill="both", expand=True)
        self.queue_listbox = tk.Listbox(
            queue_list_frame, height=5, background="#0a0c10", foreground="#e7eaf0",
            selectbackground="#33445f", relief="flat", highlightthickness=1,
        )
        self.queue_listbox.pack(side="left", fill="both", expand=True)
        queue_scroll = ttk.Scrollbar(queue_list_frame, orient="vertical", command=self.queue_listbox.yview)
        queue_scroll.pack(side="right", fill="y")
        self.queue_listbox.configure(yscrollcommand=queue_scroll.set)
        queue_buttons = ttk.Frame(notes)
        queue_buttons.pack(fill="x", pady=(6, 0))
        self.queue_add_button = ttk.Button(queue_buttons, text="Add Current URL", command=self._queue_current_url)
        self.queue_add_button.pack(side="left")
        self.queue_paste_button = ttk.Button(queue_buttons, text="Paste URL List…", command=self._queue_url_list)
        self.queue_paste_button.pack(side="left", padx=(5, 0))
        self.queue_start_button = ttk.Button(queue_buttons, text="Start Queue", command=self._start_queue)
        self.queue_start_button.pack(side="left", padx=(5, 0))
        self.queue_stop_button = ttk.Button(
            queue_buttons, text="Stop after current", command=self._stop_queue, state="disabled")
        self.queue_stop_button.pack(side="left", padx=(5, 0))
        self.queue_retry_button = ttk.Button(queue_buttons, text="Retry Failed", command=self._retry_failed)
        self.queue_retry_button.pack(side="left", padx=(5, 0))
        self.queue_clear_button = ttk.Button(queue_buttons, text="Clear Finished", command=self._clear_finished)
        self.queue_clear_button.pack(side="left", padx=(5, 0))

        ai = ttk.LabelFrame(lower, text="Optional AI Provider", padding=10)
        ai.grid(row=0, column=1, sticky="nsew")
        ai.columnconfigure(1, weight=1)
        ttk.Label(ai, text="Provider").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=4)
        provider_combo = ttk.Combobox(
            ai, textvariable=self.provider_var, state="readonly",
            values=tuple(PROVIDER_LABEL_TO_KEY.keys()),
        )
        provider_combo.grid(row=0, column=1, sticky="ew", pady=4)
        provider_combo.bind("<<ComboboxSelected>>", lambda _event: self._provider_changed())

        ttk.Label(ai, text="Model ID").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=4)
        ttk.Entry(ai, textvariable=self.model_var).grid(row=1, column=1, sticky="ew", pady=4)
        ttk.Label(ai, text="API key").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=4)
        ttk.Entry(ai, textvariable=self.key_var, show="•").grid(row=2, column=1, sticky="ew", pady=4)
        ai_buttons = ttk.Frame(ai)
        ai_buttons.grid(row=3, column=1, sticky="e", pady=(6, 4))
        ttk.Button(ai_buttons, text="Test AI", command=self._test_ai).pack(side="left")
        ttk.Button(ai_buttons, text="Use for Recap", command=self._apply_provider_to_recap).pack(side="left", padx=(6, 0))
        ttk.Button(ai_buttons, text="Edit Glossary", command=self._edit_glossary).pack(side="left", padx=(6, 0))
        ttk.Label(ai, textvariable=self.ai_status_var, wraplength=430, justify="left").grid(
            row=4, column=0, columnspan=2, sticky="w", pady=(5, 0))
        ttk.Label(
            ai,
            text="Free tiers have account-specific limits. Choose a model you know is free. Use for Recap saves the provider/model to your local .env and routes story-context, translation, and audit requests through it. "
                 "Fallback providers are opt-in through RECAP_AI_FALLBACKS.",
            wraplength=430, justify="left",
        ).grid(row=5, column=0, columnspan=2, sticky="w", pady=(8, 0))

        ttk.Separator(ai, orient="horizontal").grid(row=6, column=0, columnspan=2, sticky="ew", pady=(10, 6))
        ttk.Label(ai, text="fal.ai key").grid(row=7, column=0, sticky="w", padx=(0, 8), pady=3)
        ttk.Entry(ai, textvariable=self.fal_key_var, show="•").grid(row=7, column=1, sticky="ew", pady=3)
        ttk.Label(ai, text="Image model").grid(row=8, column=0, sticky="w", padx=(0, 8), pady=3)
        ttk.Entry(ai, textvariable=self.fal_model_var).grid(row=8, column=1, sticky="ew", pady=3)
        fal_buttons = ttk.Frame(ai)
        fal_buttons.grid(row=9, column=1, sticky="e", pady=(5, 3))
        ttk.Button(fal_buttons, text="Save FAL Key", command=self._save_fal_key).pack(side="left")
        ttk.Button(fal_buttons, text="Suggest Burmese Titles", command=self._suggest_title_ideas).pack(side="left", padx=(6, 0))
        ttk.Label(ai, textvariable=self.fal_status_var, wraplength=430, justify="left").grid(
            row=10, column=0, columnspan=2, sticky="w", pady=(5, 0))
        ttk.Label(
            ai,
            text="AI image generation uses fal.ai account credits and may be paid. Frame-based thumbnails remain local and free. "
                 "Burmese title text is overlaid locally so the spelling stays correct.",
            wraplength=430, justify="left",
        ).grid(row=11, column=0, columnspan=2, sticky="w", pady=(6, 0))
        self._refresh_queue_view()

    def _browse_output(self) -> None:
        folder = filedialog.askdirectory(initialdir=self.output_var.get() or str(self.root_dir))
        if folder:
            self.output_var.set(folder)
            self.cfg["studio_output_dir"] = folder
            self.save_config()

    def _browse_cookies(self) -> None:
        value = filedialog.askopenfilename(
            title="Select a cookies.txt file",
            filetypes=(("Cookie text file", "*.txt"), ("All files", "*.*")),
        )
        if value:
            self.cookies_var.set(value)

    def _provider_changed(self) -> None:
        provider = PROVIDER_LABEL_TO_KEY.get(self.provider_var.get(), "groq")
        if self._current_provider:
            self._key_cache[self._current_provider] = self.key_var.get()
            self.cfg[f"studio_model_{self._current_provider}"] = self.model_var.get().strip()
        api_env = {"groq": "GROQ_API_KEY", "openrouter": "OPENROUTER_API_KEY", "ollama": ""}[provider]
        model_env = {"groq": "GROQ_MODEL", "openrouter": "OPENROUTER_MODEL", "ollama": "OLLAMA_MODEL"}[provider]
        if provider != self._current_provider:
            stored_model = self.cfg.get(f"studio_model_{provider}") or os.getenv(model_env, "")
            self.model_var.set(str(stored_model or ""))
            self.key_var.set(self._key_cache.get(provider, os.getenv(api_env, "") if api_env else ""))
            self._current_provider = provider
        self.ai_status_var.set(
            "Uses the local Ollama endpoint; no API key is needed." if provider == "ollama"
            else f"Key variable: {api_env}. The key is kept in memory only and is not saved in config.json."
        )

    def _use_downloaded_video(self) -> None:
        if self.last_video_path and self.last_video_path.is_file() and callable(self.on_video_ready):
            self.on_video_ready(self.last_video_path)

    def _refresh_queue_view(self) -> None:
        if not hasattr(self, "queue_listbox"):
            return
        self.queue_listbox.delete(0, "end")
        items = self.queue_model.items()
        for item in items:
            label = item.title or item.url
            if len(label) > 88:
                label = label[:85] + "..."
            entry = f"{item.status.upper():10} | {label}"
            if item.error:
                error = item.error.replace("\n", " ")
                entry += f" — {error[:90]}"
            self.queue_listbox.insert("end", entry)
        if hasattr(self, "queue_start_button"):
            self.queue_start_button.configure(
                state="normal" if not self.busy and self.queue_model.pending() else "disabled"
            )

    def _queue_current_url(self) -> None:
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Studio Queue", "Paste a media URL first.", parent=self)
            return
        try:
            url = validate_http_url(url)
        except DownloadError as exc:
            messagebox.showerror("Studio Queue", str(exc), parent=self)
            return
        added, skipped = self.queue_model.add([url])
        self._refresh_queue_view()
        self.status_var.set(
            f"Added {len(added)} URL to queue." if added
            else "That URL is already in the queue."
        )

    def _queue_url_list(self) -> None:
        window = tk.Toplevel(self)
        window.title("Add multiple URLs to queue")
        window.transient(self.winfo_toplevel())
        window.geometry("680x460")
        window.minsize(480, 320)
        window.columnconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        ttk.Label(
            window,
            text="Paste one URL per line. Blank lines and lines starting with # are ignored. Up to 100 URLs per batch.",
            wraplength=640,
        ).grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 6))
        editor = tk.Text(window, wrap="word", undo=True)
        editor.grid(row=1, column=0, sticky="nsew", padx=12, pady=6)
        buttons = ttk.Frame(window, padding=12)
        buttons.grid(row=2, column=0, sticky="ew")
        def save_urls() -> None:
            raw_urls = [
                line.strip() for line in editor.get("1.0", "end-1c").splitlines()
                if line.strip() and not line.strip().startswith("#")
            ]
            if not raw_urls:
                messagebox.showwarning("Studio Queue", "Paste at least one URL.", parent=window)
                return
            if len(raw_urls) > 100:
                messagebox.showwarning("Studio Queue", "Add no more than 100 URLs at a time.", parent=window)
                return
            valid: list[str] = []
            invalid: list[str] = []
            for raw in raw_urls:
                try:
                    valid.append(validate_http_url(raw))
                except DownloadError:
                    invalid.append(raw)
            if invalid:
                messagebox.showerror(
                    "Invalid URL(s)",
                    "Every line must be an http:// or https:// URL. Fix these lines and try again:\n\n"
                    + "\n".join(invalid[:12]),
                    parent=window,
                )
                return
            added, skipped = self.queue_model.add(valid)
            self._refresh_queue_view()
            self.status_var.set(f"Queued {len(added)} URL(s); skipped {len(skipped)} duplicate(s).")
            window.destroy()
        ttk.Button(buttons, text="Add to Queue", command=save_urls).pack(side="right")
        ttk.Button(buttons, text="Cancel", command=window.destroy).pack(side="right", padx=(0, 8))

    def _start_queue(self) -> None:
        if self.busy or self.queue_running:
            return
        items = self.queue_model.pending()
        if not items:
            messagebox.showinfo("Studio Queue", "No pending URLs. Add URLs or press Retry Failed.", parent=self)
            self._refresh_queue_view()
            return
        output_dir = Path(self.output_var.get().strip() or self.root_dir / "Downloads")
        quality = self.quality_var.get()
        audio_only = quality == "Audio only (MP3)"
        height = {"1080p": 1080, "720p": 720, "480p": 480}.get(quality)
        cookies = self.cookies_var.get().strip()
        options = DownloadOptions(
            output_dir=output_dir,
            quality_height=height,
            audio_only=audio_only,
            playlist=self.playlist_var.get(),
            subtitles=self.subtitle_var.get(),
            cookies_file=Path(cookies) if cookies else None,
        )
        try:
            sample_count = max(1, min(24, int(self.thumbnail_samples_var.get() or "8")))
        except ValueError:
            sample_count = 8
        aspect = self.thumbnail_aspect_var.get()
        title = self.thumbnail_title_var.get().strip()
        auto_thumbnail = self.auto_thumbnail_var.get()
        self.cfg["studio_thumbnail_aspect"] = aspect
        self.cfg["studio_thumbnail_samples"] = str(sample_count)
        self.save_config()
        self.queue_stop.clear()
        self.queue_running = True
        self._set_busy(True)
        self.progress_var.set(0)
        self.status_var.set(f"Starting download queue: {len(items)} pending item(s)…")
        self._refresh_queue_view()
        threading.Thread(
            target=self._queue_worker,
            args=(items, options, auto_thumbnail, aspect, title, sample_count),
            daemon=True,
        ).start()

    def _queue_worker(
        self, items, options: DownloadOptions, auto_thumbnail: bool,
        aspect: str, custom_title: str, sample_count: int,
    ) -> None:
        completed = failed = processed = 0
        try:
            total = len(items)
            for index, item in enumerate(items, start=1):
                if self.queue_stop.is_set():
                    break
                self.queue_model.update(item.id, status="downloading", error="")
                self.events.put(("queue_refresh", None))
                self.events.put(("status", f"Queue item {index}/{total}: starting download…"))
                try:
                    result = download_media(item.url, options, progress_hook=self._on_download_progress)
                    thumbnail_error = ""
                    if auto_thumbnail and result.video_path:
                        try:
                            thumbnail_path = (
                                Path(options.output_dir) / "thumbnails"
                                / f"{result.video_path.stem}_thumbnail.jpg"
                            )
                            created = generate_thumbnail(
                                result.video_path, thumbnail_path,
                                title=custom_title or result.title, aspect=aspect,
                                sample_count=sample_count,
                                ffmpeg=self.tool("ffmpeg"), ffprobe=self.tool("ffprobe"),
                                font_path=self.cfg.get("thumbnail_font_path") or self.cfg.get("title_font_path"),
                                logo_path=(self.cfg.get("logo_path") if self.cfg.get("logo_enabled") else None),
                            )
                            self.events.put(("thumbnail", created))
                        except (ThumbnailError, OSError, ValueError) as exc:
                            thumbnail_error = str(exc)
                    self.queue_model.update(
                        item.id,
                        status="completed",
                        title=result.title,
                        error=(f"Thumbnail: {thumbnail_error}" if thumbnail_error else ""),
                        output_files=[str(path) for path in result.files],
                    )
                    completed += 1
                    self.events.put(("download_result", result))
                    self.events.put((
                        "status",
                        f"Queue {index}/{total}: downloaded {result.title}"
                        + (f" (thumbnail warning: {thumbnail_error})" if thumbnail_error else ""),
                    ))
                except Exception as exc:
                    self.queue_model.update(item.id, status="failed", error=str(exc))
                    failed += 1
                    self.events.put(("queue_item_failed", f"{item.url}\n{exc}"))
                finally:
                    processed += 1
                    self.events.put(("queue_refresh", None))
        finally:
            stopped = self.queue_stop.is_set()
            self.events.put((
                "queue_done",
                f"Queue {'stopped after current item' if stopped else 'finished'} — "
                f"{completed} completed, {failed} failed, {max(0, len(items) - processed)} pending.",
            ))

    def _stop_queue(self) -> None:
        if self.queue_running:
            self.queue_stop.set()
            self.status_var.set("Stop requested — current download and thumbnail will finish first.")

    def _retry_failed(self) -> None:
        if self.busy:
            return
        count = self.queue_model.retry_failed()
        self._refresh_queue_view()
        self.status_var.set(f"Reset {count} failed item(s) to pending.")
        self._refresh_queue_view()

    def _clear_finished(self) -> None:
        if self.busy:
            return
        count = self.queue_model.clear_finished()
        self._refresh_queue_view()
        self.status_var.set(f"Removed {count} completed queue item(s).")

    def _start_download(self) -> None:
        if self.busy:
            return
        url = self.url_var.get().strip()
        output_dir = Path(self.output_var.get().strip() or self.root_dir / "Downloads")
        if not url:
            messagebox.showwarning("Studio", "Paste a media URL first.", parent=self)
            return
        quality = self.quality_var.get()
        audio_only = quality == "Audio only (MP3)"
        height = {"1080p": 1080, "720p": 720, "480p": 480}.get(quality)
        cookies = self.cookies_var.get().strip()
        options = DownloadOptions(
            output_dir=output_dir,
            quality_height=height,
            audio_only=audio_only,
            playlist=self.playlist_var.get(),
            subtitles=self.subtitle_var.get(),
            cookies_file=Path(cookies) if cookies else None,
        )
        self._set_busy(True)
        self.progress_var.set(0)
        self.status_var.set("Starting downloader…")
        self.cfg["studio_thumbnail_aspect"] = self.thumbnail_aspect_var.get()
        self.cfg["studio_thumbnail_samples"] = self.thumbnail_samples_var.get()
        self.save_config()
        threading.Thread(
            target=self._download_worker,
            args=(
                url, options, self.auto_thumbnail_var.get(),
                self.thumbnail_aspect_var.get(), self.thumbnail_title_var.get().strip(),
                int(self.thumbnail_samples_var.get() or "8"),
            ),
            daemon=True,
        ).start()

    def _download_worker(
        self, url: str, options: DownloadOptions, auto_thumbnail: bool,
        thumbnail_aspect: str, thumbnail_title: str, thumbnail_samples: int,
    ) -> None:
        try:
            result = download_media(url, options, progress_hook=self._on_download_progress)
            self.events.put(("download_result", result))
            thumbnail_error = ""
            if auto_thumbnail and result.video_path:
                try:
                    thumbnail_dir = Path(options.output_dir) / "thumbnails"
                    thumbnail_path = thumbnail_dir / f"{result.video_path.stem}_thumbnail.jpg"
                    created = generate_thumbnail(
                        result.video_path, thumbnail_path,
                        title=thumbnail_title or result.title, aspect=thumbnail_aspect,
                        sample_count=thumbnail_samples,
                        ffmpeg=self.tool("ffmpeg"), ffprobe=self.tool("ffprobe"),
                        font_path=self.cfg.get("thumbnail_font_path") or self.cfg.get("title_font_path"),
                        logo_path=(self.cfg.get("logo_path") if self.cfg.get("logo_enabled") else None),
                    )
                    self.events.put(("thumbnail", created))
                except (ThumbnailError, OSError, ValueError) as exc:
                    thumbnail_error = str(exc)
            self.events.put((
                "status",
                f"Download completed: {len(result.files)} file(s)."
                + (f" Thumbnail warning: {thumbnail_error}" if thumbnail_error else ""),
            ))
        except (DownloadError, ThumbnailError, OSError, ValueError) as exc:
            self.events.put(("error", str(exc)))
        except Exception as exc:
            self.events.put(("error", f"Unexpected error: {exc}"))
        finally:
            self.events.put(("busy", False))

    def _on_download_progress(self, data: dict) -> None:
        status = data.get("status")
        if status == "downloading":
            total = data.get("total_bytes") or data.get("total_bytes_estimate")
            downloaded = data.get("downloaded_bytes", 0)
            percent = (float(downloaded) / float(total) * 100) if total else 0
            speed = data.get("speed")
            eta = data.get("eta")
            self.events.put(("progress", (percent, speed, eta)))
        elif status == "finished":
            self.events.put(("status", "Media downloaded; finalizing file…"))

    def _start_local_thumbnail(self) -> None:
        if self.busy:
            return
        video = filedialog.askopenfilename(
            title="Select a local video",
            filetypes=(("Video files", "*.mp4 *.mkv *.mov *.webm *.avi *.m4v"), ("All files", "*.*")),
        )
        if not video:
            return
        destination = filedialog.asksaveasfilename(
            title="Save thumbnail",
            defaultextension=".jpg",
            initialfile=f"{Path(video).stem}_thumbnail.jpg",
            filetypes=(("JPEG image", "*.jpg *.jpeg"),),
        )
        if not destination:
            return
        aspect = self.thumbnail_aspect_var.get()
        title = self.thumbnail_title_var.get().strip() or Path(video).stem
        try:
            sample_count = int(self.thumbnail_samples_var.get() or "8")
        except ValueError:
            sample_count = 8
        self.cfg["studio_thumbnail_aspect"] = aspect
        self.cfg["studio_thumbnail_samples"] = str(sample_count)
        self.save_config()
        self._set_busy(True)
        self.status_var.set("Selecting a clear frame and generating the thumbnail…")
        threading.Thread(
            target=self._thumbnail_worker,
            args=(video, destination, aspect, title, sample_count),
            daemon=True,
        ).start()

    def _thumbnail_worker(
        self, video: str, destination: str, aspect: str, title: str, sample_count: int,
    ) -> None:
        try:
            result = generate_thumbnail(
                video, destination, title=title, aspect=aspect, sample_count=sample_count,
                ffmpeg=self.tool("ffmpeg"), ffprobe=self.tool("ffprobe"),
                font_path=self.cfg.get("thumbnail_font_path") or self.cfg.get("title_font_path"),
                logo_path=(self.cfg.get("logo_path") if self.cfg.get("logo_enabled") else None),
            )
            self.events.put(("thumbnail", result))
            self.events.put(("status", f"Thumbnail saved: {result}"))
        except (ThumbnailError, OSError, ValueError) as exc:
            self.events.put(("error", str(exc)))
        finally:
            self.events.put(("busy", False))

    def _edit_glossary(self) -> None:
        """Edit the local glossary used by recap context, translation, and audit prompts."""
        local_path = self.root_dir / "glossary.json"
        example_path = self.root_dir / "glossary.example.json"
        default_data = {"characters": {}, "terms": {}, "places": {}, "notes": []}
        try:
            if local_path.is_file():
                initial = json.loads(local_path.read_text(encoding="utf-8"))
            elif example_path.is_file():
                initial = json.loads(example_path.read_text(encoding="utf-8"))
            else:
                initial = default_data
            if not isinstance(initial, dict):
                initial = default_data
        except (OSError, json.JSONDecodeError):
            initial = default_data

        window = tk.Toplevel(self)
        window.title("Myanmar Translation Glossary")
        window.transient(self.winfo_toplevel())
        window.geometry("760x560")
        window.minsize(560, 400)
        window.columnconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        ttk.Label(
            window,
            text="Edit character names, terms, places, and short style preferences. "
                 "Save writes to local glossary.json, which is ignored by Git.",
            wraplength=720,
        ).grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 6))
        editor = tk.Text(window, wrap="none", undo=True, font=("Consolas", 10))
        editor.grid(row=1, column=0, sticky="nsew", padx=12, pady=6)
        vertical = ttk.Scrollbar(window, orient="vertical", command=editor.yview)
        vertical.grid(row=1, column=1, sticky="ns", pady=6)
        editor.configure(yscrollcommand=vertical.set)
        horizontal = ttk.Scrollbar(window, orient="horizontal", command=editor.xview)
        horizontal.grid(row=2, column=0, sticky="ew", padx=12)
        editor.configure(xscrollcommand=horizontal.set)
        editor.insert("1.0", json.dumps(initial, ensure_ascii=False, indent=2))

        def save_glossary() -> None:
            try:
                value = json.loads(editor.get("1.0", "end-1c"))
                if not isinstance(value, dict):
                    raise ValueError("The top-level value must be a JSON object.")
                for section in ("characters", "terms", "places"):
                    mapping = value.get(section, {})
                    if not isinstance(mapping, dict):
                        raise ValueError(f"'{section}' must be a JSON object of original term to preferred Burmese.")
                    if len(mapping) > 500:
                        raise ValueError(f"'{section}' has too many entries (maximum 500).")
                    for source, preferred in mapping.items():
                        if not isinstance(source, str) or not isinstance(preferred, str):
                            raise ValueError(f"All '{section}' entries must map strings to strings.")
                        if len(source) > 160 or len(preferred) > 240:
                            raise ValueError(f"Terms in '{section}' must be at most 160 source / 240 target characters.")
                notes = value.get("notes", [])
                if not isinstance(notes, list) or any(not isinstance(note, str) for note in notes):
                    raise ValueError("'notes' must be a list of short text preferences.")
                temp_path = local_path.with_suffix(".json.tmp")
                temp_path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                temp_path.replace(local_path)
                self.ai_status_var.set("Glossary saved. It will be applied to the next Recap START/RESUME.")
                window.destroy()
            except (ValueError, OSError) as exc:
                messagebox.showerror("Invalid glossary", str(exc), parent=window)

        footer = ttk.Frame(window, padding=12)
        footer.grid(row=3, column=0, columnspan=2, sticky="ew")
        ttk.Button(footer, text="Save Glossary", command=save_glossary).pack(side="right")
        ttk.Button(footer, text="Close", command=window.destroy).pack(side="right", padx=(0, 8))

    def _apply_provider_to_recap(self) -> None:
        provider = PROVIDER_LABEL_TO_KEY.get(self.provider_var.get(), "groq")
        model = self.model_var.get().strip()
        if not model:
            messagebox.showwarning("Studio", "Enter the model ID before applying this provider.", parent=self)
            return
        if not messagebox.askyesno(
            "Use AI provider for Recap",
            "This will route story context, translation, and translation-audit requests through "
            f"{provider}/{model} after the next START/RESUME. Hosted providers may have quotas or charges; "
            "choose a model explicitly listed as free if you do not want paid usage. Continue?",
            parent=self,
        ):
            return
        api_env = {"groq": "GROQ_API_KEY", "openrouter": "OPENROUTER_API_KEY", "ollama": ""}[provider]
        model_env = {"groq": "GROQ_MODEL", "openrouter": "OPENROUTER_MODEL", "ollama": "OLLAMA_MODEL"}[provider]
        key_value = self.key_var.get().strip()
        if provider in {"groq", "openrouter"} and not (key_value or os.getenv(api_env, "").strip()):
            messagebox.showwarning("Studio", f"Enter {api_env} or configure it in the .env file first.", parent=self)
            return
        values = {"RECAP_AI_PROVIDER": provider, model_env: model}
        if api_env and key_value:
            values[api_env] = key_value
        for name, value in values.items():
            if "\n" in value or "\r" in value:
                messagebox.showerror("Studio", f"{name} contains a newline and cannot be saved.", parent=self)
                return

        env_path = Path(self.env_path()).expanduser().resolve()
        try:
            env_path.parent.mkdir(parents=True, exist_ok=True)
            if env_path.is_file():
                lines = env_path.read_text(encoding="utf-8").splitlines()
            else:
                example = self.root_dir / ".env.example"
                lines = example.read_text(encoding="utf-8").splitlines() if example.is_file() else []
            import re
            for name, value in values.items():
                pattern = re.compile(rf"^\s*(?:export\s+)?{re.escape(name)}\s*=")
                indexes = [i for i, line in enumerate(lines) if pattern.match(line)]
                replacement = f"{name}={value}"
                if indexes:
                    lines[indexes[0]] = replacement
                    for duplicate in reversed(indexes[1:]):
                        del lines[duplicate]
                else:
                    lines.append(replacement)
            temp_path = env_path.with_suffix(".env.tmp")
            temp_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
            temp_path.replace(env_path)
            self.cfg["studio_provider"] = provider
            self.cfg["studio_model"] = model
            self.cfg[f"studio_model_{provider}"] = model
            self.save_config()
            if load_dotenv:
                load_dotenv(env_path, override=True)
            self.ai_status_var.set(f"Recap provider saved: {provider}/{model}. The next START/RESUME will use it.")
            messagebox.showinfo("Studio", f"Saved {provider}/{model} to the local .env file.", parent=self)
        except OSError as exc:
            messagebox.showerror("Studio", f"Could not update .env: {exc}", parent=self)

    def _test_ai(self) -> None:
        if self.busy:
            return
        provider = PROVIDER_LABEL_TO_KEY.get(self.provider_var.get(), "groq")
        model = self.model_var.get().strip()
        api_key = self.key_var.get().strip() or None
        self.cfg["studio_provider"] = provider
        self.cfg["studio_model"] = model
        self.cfg[f"studio_model_{provider}"] = model
        self.save_config()
        self._set_busy(True)
        self.ai_status_var.set(f"Testing {provider} with a tiny prompt…")
        threading.Thread(
            target=self._ai_worker,
            args=(provider, model, api_key),
            daemon=True,
        ).start()

    def _ai_worker(self, provider: str, model: str, api_key: str | None) -> None:
        try:
            answer = chat_completion(
                provider, model,
                [{"role": "user", "content": "Reply with the single word OK."}],
                api_key=api_key,
                base_url=os.getenv("OLLAMA_BASE_URL") if provider == "ollama" else None,
                timeout=25,
            )
            self.events.put(("ai_result", f"{provider}/{model}: {answer[:300]}"))
        except AIProviderError as exc:
            self.events.put(("ai_error", str(exc)))
        finally:
            self.events.put(("busy", False))

    def _set_busy(self, value: bool) -> None:
        self.busy = value
        state = "disabled" if value else "normal"
        self.download_button.configure(state=state)
        self.url_entry.configure(state=state)
        for name in ("queue_add_button", "queue_paste_button", "queue_retry_button", "queue_clear_button"):
            widget = getattr(self, name, None)
            if widget is not None:
                widget.configure(state=state)
        queue_start = getattr(self, "queue_start_button", None)
        if queue_start is not None:
            queue_start.configure(state="disabled" if value or not self.queue_model.pending() else "normal")
        queue_stop = getattr(self, "queue_stop_button", None)
        if queue_stop is not None:
            queue_stop.configure(state="normal" if value and self.queue_running else "disabled")

    def _poll_events(self) -> None:
        try:
            while True:
                kind, value = self.events.get_nowait()
                if kind == "progress":
                    percent, speed, eta = value
                    self.progress_var.set(max(0, min(float(percent), 100)))
                    speed_text = f"{float(speed) / 1024 / 1024:.2f} MB/s" if speed else ""
                    eta_text = f"ETA {int(eta)}s" if eta is not None else ""
                    self.status_var.set("Downloading… " + " · ".join(part for part in (f"{percent:.1f}%", speed_text, eta_text) if part))
                elif kind == "download_result":
                    result: DownloadResult = value
                    self.last_video_path = result.video_path
                    self.use_video_button.configure(state=("normal" if self.last_video_path else "disabled"))
                    self.status_var.set(
                        f"Downloaded: {result.title} — "
                        + ", ".join(path.name for path in result.files[:3])
                    )
                elif kind == "thumbnail":
                    self.status_var.set(f"Thumbnail created: {value}")
                elif kind == "queue_refresh":
                    self._refresh_queue_view()
                elif kind == "queue_item_failed":
                    # Continue the queue, but preserve the failure in queue.json and the run log.
                    self.status_var.set("Queue item failed; continuing with the next URL.")
                elif kind == "queue_done":
                    self.queue_running = False
                    self._set_busy(False)
                    self._refresh_queue_view()
                    self.status_var.set(str(value))
                elif kind == "status":
                    self.status_var.set(str(value))
                elif kind == "error":
                    self.status_var.set("Operation failed.")
                    messagebox.showerror("Studio", str(value), parent=self)
                elif kind == "ai_result":
                    self.ai_status_var.set(f"AI test succeeded — {value}")
                elif kind == "ai_error":
                    self.ai_status_var.set(str(value))
                elif kind == "busy":
                    self._set_busy(bool(value))
        except queue.Empty:
            pass
        self.after(180, self._poll_events)
