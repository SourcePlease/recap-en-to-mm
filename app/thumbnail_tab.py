"""Dedicated Thumbnail tab, separated from Downloader/Studio controls."""
from __future__ import annotations

import os
import re
import threading
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from studio.thumbnail import generate_fal_thumbnail, generate_thumbnail, sample_thumbnail_frames
from studio.title_generator import TITLE_STYLES, ai_title_ideas, builtin_title_ideas


class ThumbnailTab(ttk.Frame):
    def __init__(self, master, *, root_dir: Path, cfg: dict, save, tool, env_path=None):
        super().__init__(master, padding=14)
        self.root_dir, self.cfg, self.save, self.tool = Path(root_dir), cfg, save, tool
        self.env_path = env_path or (lambda: self.root_dir / ".env")
        self.video = tk.StringVar()
        self.output = tk.StringVar(value=str(self.root_dir / "Downloads" / "thumbnail.jpg"))
        self.title = tk.StringVar()
        self.aspect = tk.StringVar(value=str(cfg.get("studio_thumbnail_aspect") or "16:9"))
        self.mode = tk.StringVar(value=str(cfg.get("studio_thumbnail_mode") or "Frame-based (local)"))
        self.samples = tk.StringVar(value=str(cfg.get("studio_thumbnail_samples") or "8"))
        self.style = tk.StringVar(value=str(cfg.get("studio_thumbnail_title_style") or "Anime Recap"))
        self.scene = tk.StringVar(value=str(cfg.get("studio_thumbnail_scene_prompt") or ""))
        self.model = tk.StringVar(value=str(cfg.get("fal_image_model") or os.getenv("FAL_IMAGE_MODEL") or "fal-ai/fast-sdxl"))
        self.auto_after_recap = tk.BooleanVar(value=bool(cfg.get("auto_thumbnail_after_recap", True)))
        try:
            saved_fraction = cfg.get("studio_thumbnail_selected_fraction")
            self.selected_frame_fraction = float(saved_fraction) if saved_fraction is not None else None
        except (TypeError, ValueError):
            self.selected_frame_fraction = None
        self.fal_key = tk.StringVar(value=os.getenv("FAL_KEY", ""))
        self.provider = tk.StringVar(value=str(cfg.get("studio_provider") or "groq"))
        self.ai_model = tk.StringVar(value=str(cfg.get("studio_model") or os.getenv("GROQ_MODEL") or ""))
        self.ai_key = tk.StringVar(value="")
        self.status = tk.StringVar(value="Choose a video for a frame thumbnail, or describe a scene for an AI background.")
        self.busy = False
        self._build()

    def _build(self):
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text="Thumbnail Studio", font=("Segoe UI Semibold", 17)).grid(
            row=0, column=0, columnspan=3, sticky="w")
        ttk.Label(self, text="Standalone thumbnail generator — separate from Splitter and Downloader.",
                  wraplength=1000).grid(row=1, column=0, columnspan=3, sticky="w", pady=(2, 12))
        ttk.Label(self, text="Source video (needed for frame-based mode)").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.video).grid(row=2, column=1, sticky="ew", padx=8, pady=5)
        ttk.Button(self, text="Browse", command=self._browse_video).grid(row=2, column=2, pady=5)
        ttk.Label(self, text="Save thumbnail as").grid(row=3, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.output).grid(row=3, column=1, sticky="ew", padx=8, pady=5)
        ttk.Button(self, text="Browse", command=self._browse_output).grid(row=3, column=2, pady=5)
        ttk.Label(self, text="Aspect ratio").grid(row=4, column=0, sticky="w", pady=5)
        ttk.Combobox(self, textvariable=self.aspect, state="readonly", values=("16:9", "9:16", "1:1"), width=20).grid(
            row=4, column=1, sticky="w", padx=8, pady=5)
        ttk.Label(self, text="Method").grid(row=5, column=0, sticky="w", pady=5)
        ttk.Combobox(self, textvariable=self.mode, state="readonly",
                     values=("Frame-based (local)", "AI generated (fal.ai)"), width=28).grid(
            row=5, column=1, sticky="w", padx=8, pady=5)
        ttk.Label(self, text="Frame samples").grid(row=6, column=0, sticky="w", pady=5)
        ttk.Combobox(self, textvariable=self.samples, state="readonly", values=("4", "8", "12", "16", "24"), width=20).grid(
            row=6, column=1, sticky="w", padx=8, pady=5)
        ttk.Label(self, text="Title style").grid(row=7, column=0, sticky="w", pady=5)
        ttk.Combobox(self, textvariable=self.style, state="readonly", values=tuple(TITLE_STYLES), width=28).grid(
            row=7, column=1, sticky="w", padx=8, pady=5)
        ttk.Label(self, text="Burmese thumbnail title").grid(row=8, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.title, font=("Myanmar Text", 11)).grid(
            row=8, column=1, sticky="ew", padx=8, pady=5)
        ttk.Button(self, text="Suggest titles", command=self._suggest).grid(row=8, column=2, pady=5)
        ttk.Label(self, text="AI scene / plot notes").grid(row=9, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.scene).grid(row=9, column=1, columnspan=2, sticky="ew", padx=8, pady=5)
        ttk.Separator(self).grid(row=10, column=0, columnspan=3, sticky="ew", pady=12)
        ttk.Label(self, text="fal.ai API key").grid(row=11, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.fal_key, show="•").grid(row=11, column=1, sticky="ew", padx=8, pady=5)
        ttk.Label(self, text="Image model").grid(row=12, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.model).grid(row=12, column=1, sticky="ew", padx=8, pady=5)
        ttk.Button(self, text="Save fal.ai key locally", command=self._save_key).grid(row=12, column=2, pady=5)
        ttk.Label(self, text="AI title provider").grid(row=13, column=0, sticky="w", pady=5)
        ttk.Combobox(self, textvariable=self.provider, state="readonly",
                     values=("groq", "openrouter", "ollama"), width=20).grid(row=13, column=1, sticky="w", padx=8, pady=5)
        ttk.Label(self, text="Text model ID").grid(row=14, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.ai_model).grid(row=14, column=1, sticky="ew", padx=8, pady=5)
        ttk.Label(self, text="Text API key (session only)").grid(row=15, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.ai_key, show="•").grid(row=15, column=1, sticky="ew", padx=8, pady=5)
        actions = ttk.Frame(self)
        actions.grid(row=16, column=0, columnspan=3, sticky="ew", pady=(12, 4))
        self.choose_frame_button = ttk.Button(actions, text="Choose Frame…", command=self._choose_frame)
        self.choose_frame_button.pack(side="left")
        self.generate_button = ttk.Button(actions, text="Generate Thumbnail", command=self._generate)
        self.generate_button.pack(side="left", padx=(6, 0))
        self.variations_button = ttk.Button(actions, text="Create 3 Local Variants", command=self._generate_variations)
        self.variations_button.pack(side="left", padx=(6, 0))
        ttk.Checkbutton(actions, text="Auto-thumbnail after Recap", variable=self.auto_after_recap,
                        command=self._save_auto_setting).pack(side="left", padx=(12, 0))
        ttk.Label(actions, textvariable=self.status, wraplength=880).pack(side="left", padx=12)
        ttk.Label(self, text="Frame-based mode is local/free. fal.ai image inference may use account credits. "
                  "Correct Burmese title/logo text is composited locally.",
                  wraplength=1050).grid(row=17, column=0, columnspan=3, sticky="w", pady=(12, 0))

    def _browse_video(self):
        path = filedialog.askopenfilename(
            title="Select source video",
            filetypes=(("Video files", "*.mp4 *.mkv *.mov *.webm *.avi *.m4v"), ("All files", "*.*")))
        if path:
            self.video.set(path)
            self.selected_frame_fraction = None
            self.cfg.pop("studio_thumbnail_selected_fraction", None)
            if not self.title.get().strip():
                self.title.set(builtin_title_ideas(Path(path).stem, self.style.get())[0])
            self.output.set(str(Path(path).with_name(Path(path).stem + "_thumbnail.jpg")))

    def _browse_output(self):
        path = filedialog.asksaveasfilename(defaultextension=".jpg", initialfile="thumbnail.jpg",
            filetypes=(("JPEG image", "*.jpg *.jpeg"),))
        if path:
            self.output.set(path)

    def _suggest(self):
        source = Path(self.video.get()).stem if self.video.get().strip() else "Anime Recap"
        style, provider, model = self.style.get() or "Anime Recap", self.provider.get(), self.ai_model.get().strip()
        key = self.ai_key.get().strip() or None
        if not model or (provider in {"groq", "openrouter"} and not key):
            self._show_ideas(builtin_title_ideas(source, style), "Built-in Burmese title suggestions loaded.")
            return
        self.status.set("Asking the selected AI provider for Burmese title ideas…")
        summary = self.scene.get().strip()
        def work():
            try:
                ideas = ai_title_ideas(source, style=style, summary=summary,
                    provider=provider, model=model, api_key=key)
                status = "AI-generated title suggestions loaded."
            except Exception as exc:
                ideas = builtin_title_ideas(source, style)
                status = f"AI unavailable; built-in titles used: {str(exc)[:180]}"
            self.after(0, lambda: self._show_ideas(ideas, status))
        threading.Thread(target=work, daemon=True).start()

    def _show_ideas(self, ideas, status):
        self.title.set(ideas[0] if ideas else "")
        self.status.set(status)
        if not ideas:
            return
        menu = tk.Menu(self, tearoff=False)
        for idea in ideas:
            menu.add_command(label=idea[:70], command=lambda value=idea: self.title.set(value))
        try:
            menu.tk_popup(self.winfo_pointerx(), self.winfo_pointery())
        finally:
            menu.grab_release()

    def _save_key(self):
        key = self.fal_key.get().strip()
        if not key:
            messagebox.showwarning("fal.ai", "Enter FAL_KEY first.", parent=self)
            return
        model = self.model.get().strip() or "fal-ai/fast-sdxl"
        if any("\n" in value or "\r" in value for value in (key, model)):
            messagebox.showerror("fal.ai", "Key/model must not contain line breaks.", parent=self)
            return
        env = Path(self.env_path()).expanduser()
        try:
            env.parent.mkdir(parents=True, exist_ok=True)
            lines = env.read_text(encoding="utf-8").splitlines() if env.is_file() else []
            for name, value in (("FAL_KEY", key), ("FAL_IMAGE_MODEL", model)):
                pattern = re.compile(rf"^\s*(?:export\s+)?{re.escape(name)}\s*=")
                found = [i for i, line in enumerate(lines) if pattern.match(line)]
                if found:
                    lines[found[0]] = f"{name}={value}"
                    for index in reversed(found[1:]):
                        del lines[index]
                else:
                    lines.append(f"{name}={value}")
            temp = env.with_suffix(".env.tmp")
            temp.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
            temp.replace(env)
            os.environ["FAL_KEY"], os.environ["FAL_IMAGE_MODEL"] = key, model
            self.cfg["fal_image_model"] = model
            self.save()
            self.status.set("fal.ai key saved to the local .env file.")
        except OSError as exc:
            messagebox.showerror("fal.ai", str(exc), parent=self)

    def _generate(self):
        if self.busy:
            return
        video, destination, mode = self.video.get().strip(), self.output.get().strip(), self.mode.get()
        if mode == "Frame-based (local)" and (not video or not Path(video).is_file()):
            messagebox.showwarning("Thumbnail", "Select a local video for frame-based mode.", parent=self)
            return
        if not destination:
            messagebox.showwarning("Thumbnail", "Choose an output filename.", parent=self)
            return
        title = self.title.get().strip() or builtin_title_ideas(
            Path(video).stem if video else "Anime Recap", self.style.get())[0]
        fal_key = self.fal_key.get().strip() or os.getenv("FAL_KEY", "").strip() or None
        if mode == "AI generated (fal.ai)" and not fal_key:
            messagebox.showwarning("fal.ai", "Enter FAL_KEY and save it to .env.", parent=self)
            return
        try:
            samples = max(1, min(24, int(self.samples.get() or "8")))
        except ValueError:
            samples = 8
        aspect, style = self.aspect.get(), self.style.get()
        scene, model = self.scene.get().strip(), self.model.get().strip() or "fal-ai/fast-sdxl"
        self.cfg.update({
            "auto_thumbnail_after_recap": bool(self.auto_after_recap.get()),
            "studio_thumbnail_selected_fraction": self.selected_frame_fraction,
            "studio_thumbnail_aspect": aspect, "studio_thumbnail_samples": str(samples),
            "studio_thumbnail_mode": mode, "studio_thumbnail_title_style": style,
            "studio_thumbnail_scene_prompt": scene, "studio_thumbnail_title": title,
            "fal_image_model": model,
        })
        self.save()
        self.busy = True
        self.generate_button.configure(state="disabled")
        self.variations_button.configure(state="disabled")
        self.status.set("Generating thumbnail…")
        def work():
            try:
                target = Path(destination)
                target.parent.mkdir(parents=True, exist_ok=True)
                font = self.cfg.get("thumbnail_font_path") or self.cfg.get("title_font_path")
                logo = self.cfg.get("logo_path") if self.cfg.get("logo_enabled") else None
                if mode == "AI generated (fal.ai)":
                    result = generate_fal_thumbnail(target, title=title, scene_prompt=scene, aspect=aspect,
                        style=style, model_id=model, api_key=fal_key, font_path=font, logo_path=logo)
                else:
                    result = generate_thumbnail(video, target, title=title, aspect=aspect, sample_count=samples,
                        ffmpeg=self.tool("ffmpeg"), ffprobe=self.tool("ffprobe"), font_path=font, logo_path=logo,
                        selected_fraction=self.selected_frame_fraction)
                self.after(0, lambda: self._done(str(result), None))
            except Exception as exc:
                message = str(exc)
                self.after(0, lambda message=message: self._done("", message))
        threading.Thread(target=work, daemon=True).start()

    def _choose_frame(self):
        if self.busy:
            return
        video = self.video.get().strip()
        if not video or not Path(video).is_file():
            messagebox.showwarning("Thumbnail Frame Picker", "Choose a valid local video first.", parent=self)
            return
        try:
            samples = max(1, min(24, int(self.samples.get() or "8")))
        except ValueError:
            samples = 8
        window = tk.Toplevel(self)
        window.title("Choose Thumbnail Frame")
        window.transient(self.winfo_toplevel())
        window.geometry("820x640")
        window.minsize(640, 420)
        status = ttk.Label(window, text="Extracting preview frames…")
        status.pack(fill="x", padx=12, pady=12)

        def extract():
            try:
                frames = sample_thumbnail_frames(
                    video, sample_count=samples, ffmpeg=self.tool("ffmpeg"), ffprobe=self.tool("ffprobe"),
                )
                self.after(0, lambda: self._show_frame_picker(window, status, frames, None))
            except Exception as exc:
                message = str(exc)
                self.after(0, lambda message=message: self._show_frame_picker(window, status, [], message))

        threading.Thread(target=extract, daemon=True).start()

    def _show_frame_picker(self, window, status, frames, error):
        try:
            if not window.winfo_exists():
                return
        except tk.TclError:
            return
        status.configure(text=f"Could not load frames: {error}" if error else "Choose a frame or switch back to automatic best-frame selection.")
        if error:
            return
        canvas_host = ttk.Frame(window)
        canvas_host.pack(fill="both", expand=True, padx=10, pady=(0, 8))
        canvas = tk.Canvas(canvas_host, highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_host, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        grid = ttk.Frame(canvas)
        window_id = canvas.create_window((0, 0), window=grid, anchor="nw")
        grid.bind("<Configure>", lambda _event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda event: canvas.itemconfigure(window_id, width=event.width))
        photos = []
        try:
            from PIL import ImageTk
            for index, (frame, fraction) in enumerate(frames, start=1):
                preview = frame.copy()
                preview.thumbnail((170, 96))
                photo = ImageTk.PhotoImage(preview, master=window)
                photos.append(photo)
                button = ttk.Button(
                    grid, image=photo, text=f"Frame {index} · {fraction * 100:.0f}%",
                    compound="top", command=lambda value=fraction: self._select_frame(value, window),
                )
                button.grid(row=(index - 1) // 4, column=(index - 1) % 4, padx=5, pady=5, sticky="nsew")
            for column in range(4):
                grid.columnconfigure(column, weight=1)
        except Exception as exc:
            status.configure(text=f"Could not display frame previews: {exc}")
            return
        window._thumbnail_photos = photos
        footer = ttk.Frame(window, padding=10)
        footer.pack(fill="x")
        ttk.Button(footer, text="Use Automatic Best Frame",
                   command=lambda: self._select_frame(None, window)).pack(side="left")
        if self.selected_frame_fraction is not None:
            ttk.Label(footer, text=f"Current pick: {self.selected_frame_fraction * 100:.0f}% of video").pack(side="left", padx=10)

    def _select_frame(self, fraction, window):
        self.selected_frame_fraction = fraction
        if fraction is None:
            self.cfg.pop("studio_thumbnail_selected_fraction", None)
            self.status.set("Thumbnail frame selection cleared; automatic best-frame selection will be used.")
        else:
            self.cfg["studio_thumbnail_selected_fraction"] = round(float(fraction), 5)
            self.status.set(f"Selected frame near {float(fraction) * 100:.0f}% of the source video.")
        self.save()
        try:
            window.destroy()
        except tk.TclError:
            pass

    def _save_auto_setting(self):
        self.cfg["auto_thumbnail_after_recap"] = bool(self.auto_after_recap.get())
        self.save()
        self.status.set(
            "Automatic local thumbnail generation after Recap is ON."
            if self.auto_after_recap.get() else "Automatic thumbnail generation after Recap is OFF."
        )

    def _generate_variations(self):
        if self.busy:
            return
        video, destination = self.video.get().strip(), self.output.get().strip()
        if self.mode.get() != "Frame-based (local)":
            messagebox.showinfo("Thumbnail Variants", "Local variants are free and do not spend AI credits. Switch Method to Frame-based (local) first.", parent=self)
            return
        if not video or not Path(video).is_file():
            messagebox.showwarning("Thumbnail Variants", "Choose a local source video first.", parent=self)
            return
        if not destination:
            messagebox.showwarning("Thumbnail Variants", "Choose an output filename first.", parent=self)
            return
        title = self.title.get().strip() or builtin_title_ideas(Path(video).stem, self.style.get())[0]
        ideas = builtin_title_ideas(Path(video).stem, self.style.get())
        titles = [title] + [idea for idea in ideas if idea != title]
        while len(titles) < 3:
            titles.append(f"{title} {len(titles) + 1}")
        titles = titles[:3]
        aspect, style = self.aspect.get(), self.style.get()
        target = Path(destination)
        self.busy = True
        self.generate_button.configure(state="disabled")
        self.variations_button.configure(state="disabled")
        self.status.set("Creating 3 local thumbnail variants with different frames, titles and layouts…")
        def work():
            outputs = []
            error = None
            try:
                font = self.cfg.get("thumbnail_font_path") or self.cfg.get("title_font_path")
                logo = self.cfg.get("logo_path") if self.cfg.get("logo_enabled") else None
                fractions = [
                    self.selected_frame_fraction if self.selected_frame_fraction is not None else 0.22,
                    0.50,
                    0.78,
                ]
                for index, (fraction, variant_title) in enumerate(zip(fractions, titles), start=1):
                    variant = target.with_name(f"{target.stem}_variant_{index}{target.suffix or '.jpg'}")
                    outputs.append(str(generate_thumbnail(
                        video, variant, title=variant_title, aspect=aspect, sample_count=12,
                        ffmpeg=self.tool("ffmpeg"), ffprobe=self.tool("ffprobe"),
                        font_path=font, logo_path=logo,
                        selected_fraction=fraction, template_variant=index - 1,
                    )))
            except Exception as exc:
                error = str(exc)
            self.after(0, lambda: self._done_variations(outputs, error))
        threading.Thread(target=work, daemon=True).start()

    def _done_variations(self, outputs, error):
        self.busy = False
        self.generate_button.configure(state="normal")
        self.variations_button.configure(state="normal")
        if error:
            self.status.set(f"Variants failed: {error}")
            messagebox.showerror("Thumbnail Variants", error, parent=self)
        else:
            self.status.set(f"Created {len(outputs)} local variants: " + ", ".join(Path(x).name for x in outputs))
            messagebox.showinfo("Thumbnail Variants", "Created local variants:\n" + "\n".join(outputs), parent=self)

    def _done(self, result, error):
        self.busy = False
        self.generate_button.configure(state="normal")
        self.variations_button.configure(state="normal")
        self.status.set(f"Failed: {error}" if error else f"Thumbnail saved: {result}")
        if error:
            messagebox.showerror("Thumbnail", error, parent=self)
