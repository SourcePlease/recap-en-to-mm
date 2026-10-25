from __future__ import annotations

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
from studio.downloader import DownloadError, DownloadOptions, DownloadResult, download_media
from studio.thumbnail import ThumbnailError, generate_thumbnail


PROVIDER_LABEL_TO_KEY = {
    "Groq": "groq",
    "OpenRouter": "openrouter",
    "Ollama (local)": "ollama",
}
PROVIDER_KEY_TO_LABEL = {value: key for key, value in PROVIDER_LABEL_TO_KEY.items()}


class StudioTab(ttk.Frame):
    """Downloader, automatic thumbnail generator, and optional AI-provider tester."""

    def __init__(self, master, *, root_dir: Path, cfg: dict, save, tool):
        super().__init__(master, padding=12)
        self.root_dir = Path(root_dir)
        self.cfg = cfg
        self.save_config = save
        self.tool = tool
        self.events: queue.Queue[tuple[str, object]] = queue.Queue()
        self.busy = False

        if load_dotenv:
            load_dotenv(self.root_dir / ".env", override=False)

        default_output = self.cfg.get("studio_output_dir") or str(self.root_dir / "Downloads")
        self.url_var = tk.StringVar(value="")
        self.output_var = tk.StringVar(value=default_output)
        self.quality_var = tk.StringVar(value="Best available")
        self.playlist_var = tk.BooleanVar(value=False)
        self.auto_thumbnail_var = tk.BooleanVar(value=True)
        self.subtitle_var = tk.BooleanVar(value=False)
        self.cookies_var = tk.StringVar(value="")
        self.status_var = tk.StringVar(value="Ready — paste a supported media URL or select a local video.")
        self.progress_var = tk.DoubleVar(value=0)
        self.provider_var = tk.StringVar(value=PROVIDER_KEY_TO_LABEL.get(
            str(self.cfg.get("studio_provider") or "groq"), "Groq"))
        self.model_var = tk.StringVar(value=str(self.cfg.get("studio_model") or ""))
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

        action_row = ttk.Frame(download)
        action_row.grid(row=4, column=0, columnspan=4, sticky="ew", pady=(8, 2))
        self.download_button = ttk.Button(action_row, text="Download", command=self._start_download)
        self.download_button.pack(side="left")
        ttk.Button(action_row, text="Thumbnail from local video…", command=self._start_local_thumbnail).pack(
            side="left", padx=(8, 0))
        self.progress = ttk.Progressbar(action_row, maximum=100, variable=self.progress_var, length=220)
        self.progress.pack(side="left", fill="x", expand=True, padx=(14, 0))
        ttk.Label(download, textvariable=self.status_var, wraplength=1150).grid(
            row=5, column=0, columnspan=4, sticky="w", pady=(7, 0))

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
        ttk.Button(ai, text="Test AI", command=self._test_ai).grid(row=3, column=1, sticky="e", pady=(6, 4))
        ttk.Label(ai, textvariable=self.ai_status_var, wraplength=430, justify="left").grid(
            row=4, column=0, columnspan=2, sticky="w", pady=(5, 0))
        ttk.Label(
            ai,
            text="Free tiers have account-specific limits. Choose a free model explicitly; this tester never silently switches to paid usage. "
                 "The existing Gemini recap pipeline remains unchanged in this first integration step.",
            wraplength=430, justify="left",
        ).grid(row=5, column=0, columnspan=2, sticky="w", pady=(8, 0))

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
        api_env = {"groq": "GROQ_API_KEY", "openrouter": "OPENROUTER_API_KEY", "ollama": ""}[provider]
        model_env = {"groq": "GROQ_MODEL", "openrouter": "OPENROUTER_MODEL", "ollama": "OLLAMA_MODEL"}[provider]
        if not self.model_var.get().strip():
            self.model_var.set(os.getenv(model_env, ""))
        else:
            self.model_var.set(os.getenv(model_env, "") or self.model_var.get())
        self.key_var.set(os.getenv(api_env, "") if api_env else "")
        self.ai_status_var.set(
            "Uses the local Ollama endpoint; no API key is needed." if provider == "ollama"
            else f"Key variable: {api_env}. The key is not saved in config.json."
        )

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
        threading.Thread(target=self._download_worker, args=(url, options), daemon=True).start()

    def _download_worker(self, url: str, options: DownloadOptions) -> None:
        try:
            result = download_media(url, options, progress_hook=self._on_download_progress)
            self.events.put(("download_result", result))
            if self.auto_thumbnail_var.get() and result.video_path:
                thumbnail_dir = Path(options.output_dir) / "thumbnails"
                thumbnail_path = thumbnail_dir / f"{result.video_path.stem}_thumbnail.jpg"
                created = generate_thumbnail(
                    result.video_path, thumbnail_path, title=result.title,
                    ffmpeg=self.tool("ffmpeg"), ffprobe=self.tool("ffprobe"),
                )
                self.events.put(("thumbnail", created))
            self.events.put(("status", f"Download completed: {len(result.files)} file(s)."))
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
        self._set_busy(True)
        self.status_var.set("Selecting a clear frame and generating the thumbnail…")
        threading.Thread(
            target=self._thumbnail_worker,
            args=(video, destination),
            daemon=True,
        ).start()

    def _thumbnail_worker(self, video: str, destination: str) -> None:
        try:
            result = generate_thumbnail(
                video, destination, title=Path(video).stem,
                ffmpeg=self.tool("ffmpeg"), ffprobe=self.tool("ffprobe"),
            )
            self.events.put(("thumbnail", result))
            self.events.put(("status", f"Thumbnail saved: {result}"))
        except (ThumbnailError, OSError, ValueError) as exc:
            self.events.put(("error", str(exc)))
        finally:
            self.events.put(("busy", False))

    def _test_ai(self) -> None:
        if self.busy:
            return
        provider = PROVIDER_LABEL_TO_KEY.get(self.provider_var.get(), "groq")
        model = self.model_var.get().strip()
        api_key = self.key_var.get().strip() or None
        self.cfg["studio_provider"] = provider
        self.cfg["studio_model"] = model
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
        self.download_button.configure(state="disabled" if value else "normal")
        self.url_entry.configure(state="disabled" if value else "normal")

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
                    self.status_var.set(
                        f"Downloaded: {result.title} — "
                        + ", ".join(path.name for path in result.files[:3])
                    )
                elif kind == "thumbnail":
                    self.status_var.set(f"Thumbnail created: {value}")
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
