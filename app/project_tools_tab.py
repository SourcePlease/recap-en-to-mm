"""Project save/load, audio waveform preview, pronunciation dictionary, and output options."""
from __future__ import annotations

import array
import json
import math
import os
import subprocess
import tempfile
import threading
import wave
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class ProjectToolsTab(ttk.Frame):
    def __init__(self, master, *, root_dir: Path, cfg: dict, save, tool, get_state, apply_state):
        super().__init__(master, padding=14)
        self.root_dir, self.cfg, self.save = Path(root_dir), cfg, save
        self.tool, self.get_state, self.apply_state = tool, get_state, apply_state
        self.wave_video = tk.StringVar()
        self.channel_name = tk.StringVar(value=str(cfg.get("brand_channel_name") or "My Channel"))
        self.brand_logo = tk.StringVar(value=str(cfg.get("brand_logo_path") or ""))
        self.enable_brand = tk.BooleanVar(value=bool(cfg.get("brand_intro_outro_enabled", False)))
        self.intro_seconds = tk.StringVar(value=str(cfg.get("brand_intro_seconds") or "3"))
        self.outro_seconds = tk.StringVar(value=str(cfg.get("brand_outro_seconds") or "5"))
        self.silence_enabled = tk.BooleanVar(value=bool(cfg.get("smart_silence_removal", False)))
        self.silence_threshold = tk.StringVar(value=str(cfg.get("smart_silence_threshold_db") or "-45"))
        self.status = tk.StringVar(value="Project settings are local. API keys remain in your private .env file.")
        self._build()

    def _build(self):
        self.columnconfigure(0, weight=1)
        ttk.Label(self, text="Project & Audio Tools", font=("Segoe UI Semibold", 17)).grid(row=0, column=0, sticky="w")
        ttk.Label(self, text="Save/load projects, inspect audio, edit pronunciations, and configure branded cards/silence rules.",
                  wraplength=1050).grid(row=1, column=0, sticky="w", pady=(3, 12))
        tabs = ttk.Notebook(self)
        tabs.grid(row=2, column=0, sticky="nsew")
        self.rowconfigure(2, weight=1)
        project = ttk.Frame(tabs, padding=12)
        audio = ttk.Frame(tabs, padding=12)
        brand = ttk.Frame(tabs, padding=12)
        tabs.add(project, text="Project Save / Load")
        tabs.add(audio, text="Audio Waveform")
        tabs.add(brand, text="Audio & Intro / Outro")
        ttk.Label(project, text="Project files include local editing configuration and file paths; API secrets are never copied.").grid(
            row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))
        ttk.Button(project, text="Save Current Project…", command=self._save_project).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Button(project, text="Load Project…", command=self._load_project).grid(row=1, column=1, sticky="w", padx=8, pady=5)
        ttk.Label(project, text="Pronunciation dictionary: one source => spoken replacement per line").grid(
            row=2, column=0, columnspan=3, sticky="w", pady=(16, 4))
        self.pronunciation = tk.Text(project, height=14, wrap="none")
        self.pronunciation.grid(row=3, column=0, columnspan=3, sticky="nsew")
        project.rowconfigure(3, weight=1)
        project.columnconfigure(0, weight=1)
        project.columnconfigure(1, weight=1)
        ttk.Button(project, text="Load Dictionary", command=self._load_pronunciation).grid(row=4, column=0, sticky="w", pady=8)
        ttk.Button(project, text="Save Dictionary", command=self._save_pronunciation).grid(row=4, column=1, sticky="w", padx=8, pady=8)

        ttk.Label(audio, text="Choose a video/audio file to draw a mono RMS waveform. Analysis streams PCM in small blocks to limit memory.").grid(
            row=0, column=0, columnspan=3, sticky="w", pady=(0, 8))
        ttk.Entry(audio, textvariable=self.wave_video).grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
        ttk.Button(audio, text="Browse", command=self._browse_wave_video).grid(row=1, column=2, padx=6, pady=5)
        self.wave_canvas = tk.Canvas(audio, height=250, background="#090c12", highlightthickness=1, highlightbackground="#303744")
        self.wave_canvas.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=8)
        audio.rowconfigure(2, weight=1)
        audio.columnconfigure(0, weight=1)
        ttk.Button(audio, text="Analyze Waveform", command=self._analyze_waveform).grid(row=3, column=0, sticky="w")
        self.wave_status = tk.StringVar(value="No waveform loaded.")
        ttk.Label(audio, textvariable=self.wave_status).grid(row=3, column=1, columnspan=2, sticky="w", padx=8)

        ttk.Checkbutton(brand, text="Enable automatic branded intro and outro cards", variable=self.enable_brand).grid(
            row=0, column=0, columnspan=3, sticky="w", pady=5)
        ttk.Label(brand, text="Channel name").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Entry(brand, textvariable=self.channel_name).grid(row=1, column=1, columnspan=2, sticky="ew", pady=5)
        ttk.Label(brand, text="Logo image").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Entry(brand, textvariable=self.brand_logo).grid(row=2, column=1, sticky="ew", pady=5)
        ttk.Button(brand, text="Browse", command=self._browse_brand_logo).grid(row=2, column=2, padx=6, pady=5)
        ttk.Label(brand, text="Intro seconds").grid(row=3, column=0, sticky="w", pady=5)
        ttk.Entry(brand, textvariable=self.intro_seconds, width=8).grid(row=3, column=1, sticky="w", pady=5)
        ttk.Label(brand, text="Outro seconds").grid(row=4, column=0, sticky="w", pady=5)
        ttk.Entry(brand, textvariable=self.outro_seconds, width=8).grid(row=4, column=1, sticky="w", pady=5)
        ttk.Separator(brand).grid(row=5, column=0, columnspan=3, sticky="ew", pady=10)
        ttk.Checkbutton(brand, text="Smart silence removal for generated narration", variable=self.silence_enabled).grid(
            row=6, column=0, columnspan=3, sticky="w", pady=5)
        ttk.Label(brand, text="Silence threshold (dB)").grid(row=7, column=0, sticky="w", pady=5)
        ttk.Entry(brand, textvariable=self.silence_threshold, width=8).grid(row=7, column=1, sticky="w", pady=5)
        ttk.Button(brand, text="Save Options", command=self._save_options).grid(row=8, column=0, sticky="w", pady=10)
        ttk.Label(brand, text="Silence removal compresses detected silence inside narration clips; Smart Sync recalculates against the shorter audio. "
                  "It is off by default. Try it on a short clip first.",
                  wraplength=800).grid(row=9, column=0, columnspan=3, sticky="w")
        brand.columnconfigure(1, weight=1)
        ttk.Label(self, textvariable=self.status, wraplength=1000).grid(row=3, column=0, sticky="w", pady=(10, 0))
        self._load_pronunciation()

    def _save_project(self):
        path = filedialog.asksaveasfilename(defaultextension=".recapproject.json",
            initialfile="MyProject.recapproject.json",
            filetypes=(("Recap project", "*.recapproject.json"), ("JSON", "*.json")))
        if not path:
            return
        try:
            document = {"format": "recap-studio-project-v1", "state": self.get_state()}
            Path(path).write_text(json.dumps(document, ensure_ascii=False, indent=2), encoding="utf-8")
            self.status.set(f"Project saved: {path}")
        except Exception as exc:
            messagebox.showerror("Project", f"Could not save project: {exc}", parent=self)

    def _load_project(self):
        path = filedialog.askopenfilename(filetypes=(("Recap project", "*.recapproject.json *.json"), ("All files", "*.*")))
        if not path:
            return
        try:
            document = json.loads(Path(path).read_text(encoding="utf-8"))
            state = document.get("state") if isinstance(document, dict) else None
            if not isinstance(state, dict):
                raise ValueError("Invalid Recap project file.")
            self.apply_state(state)
            self.status.set(f"Project loaded: {Path(path).name}")
        except Exception as exc:
            messagebox.showerror("Project", f"Could not load project: {exc}", parent=self)

    def _dictionary_path(self):
        return self.root_dir / "pronunciation.json"

    def _load_pronunciation(self):
        path = self._dictionary_path()
        try:
            data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
        except Exception:
            data = {}
        self.pronunciation.delete("1.0", "end")
        if isinstance(data, dict):
            for source, spoken in data.items():
                self.pronunciation.insert("end", f"{source} => {spoken}\n")

    def _save_pronunciation(self):
        mapping = {}
        for line in self.pronunciation.get("1.0", "end").splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if "=>" not in line:
                messagebox.showwarning("Pronunciation", f"Use source => spoken replacement:\n{line}", parent=self)
                return
            source, target = (part.strip() for part in line.split("=>", 1))
            if source and target:
                mapping[source] = target
        try:
            self._dictionary_path().write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")
            self.status.set(f"Saved {len(mapping)} pronunciation rule(s).")
        except OSError as exc:
            messagebox.showerror("Pronunciation", str(exc), parent=self)

    def _browse_wave_video(self):
        path = filedialog.askopenfilename(filetypes=(("Video/audio", "*.mp4 *.mkv *.mov *.webm *.avi *.mp3 *.wav"), ("All files", "*.*")))
        if path:
            self.wave_video.set(path)

    def _analyze_waveform(self):
        source = Path(self.wave_video.get().strip())
        if not source.is_file():
            messagebox.showwarning("Waveform", "Choose a video/audio file first.", parent=self)
            return
        self.wave_status.set("Analyzing waveform…")
        def work():
            try:
                with tempfile.TemporaryDirectory(prefix="recap_wave_") as temp:
                    pcm = Path(temp) / "wave.wav"
                    subprocess.run([self.tool("ffmpeg"), "-y", "-v", "error", "-i", str(source),
                        "-vn", "-ac", "1", "-ar", "8000", "-c:a", "pcm_s16le", str(pcm)],
                        check=True, capture_output=True, text=True)
                    with wave.open(str(pcm), "rb") as audio:
                        rate, frames_total, width = audio.getframerate(), audio.getnframes(), audio.getsampwidth()
                        if width != 2 or rate <= 0:
                            raise ValueError("FFmpeg returned an unexpected PCM format.")
                        bucket = max(1, frames_total // 900)
                        amplitudes = []
                        remaining = frames_total
                        while remaining:
                            count = min(bucket, remaining)
                            samples = array.array("h")
                            samples.frombytes(audio.readframes(count))
                            if os.sys.byteorder != "little":
                                samples.byteswap()
                            if samples:
                                amplitudes.append(math.sqrt(sum(v * v for v in samples) / len(samples)) / 32768.0)
                            remaining -= count
                    duration = frames_total / float(rate)
                    self.after(0, lambda values=amplitudes, dur=duration: self._draw_waveform(values, dur, None))
            except Exception as exc:
                message = str(exc)
                self.after(0, lambda message=message: self._draw_waveform([], 0, message))
        threading.Thread(target=work, daemon=True).start()

    def _draw_waveform(self, values, duration, error):
        self.wave_canvas.delete("all")
        if error:
            self.wave_status.set(f"Waveform failed: {error}")
            return
        width = max(1, self.wave_canvas.winfo_width())
        height = max(1, self.wave_canvas.winfo_height())
        mid = height // 2
        self.wave_canvas.create_line(0, mid, width, mid, fill="#4b5668")
        if not values:
            self.wave_status.set("No waveform values could be read.")
            return
        step = width / len(values)
        for index, level in enumerate(values):
            x = int(index * step)
            amp = max(1, int(level * (height * 0.44)))
            self.wave_canvas.create_line(x, mid - amp, x, mid + amp, fill="#66a3ff")
        self.wave_canvas.create_text(8, 8, anchor="nw", fill="#dbe4f0",
            text=f"0:00 — {int(duration // 60):02d}:{int(duration % 60):02d}")
        self.wave_status.set(f"Waveform ready · {duration:.1f}s · quiet areas sit near the center line.")

    def _browse_brand_logo(self):
        path = filedialog.askopenfilename(filetypes=(("Images", "*.png *.jpg *.jpeg *.webp"), ("All files", "*.*")))
        if path:
            self.brand_logo.set(path)

    def _save_options(self):
        try:
            intro = max(1, min(15, int(self.intro_seconds.get() or "3")))
            outro = max(1, min(30, int(self.outro_seconds.get() or "5")))
            threshold = max(-70, min(-20, int(self.silence_threshold.get() or "-45")))
        except ValueError:
            messagebox.showwarning("Options", "Durations must be integers; threshold must be between -70 and -20 dB.", parent=self)
            return
        logo = self.brand_logo.get().strip()
        if logo and not Path(logo).is_file():
            messagebox.showwarning("Options", "Logo image path was not found.", parent=self)
            return
        self.cfg.update({
            "brand_intro_outro_enabled": bool(self.enable_brand.get()),
            "brand_channel_name": self.channel_name.get().strip() or "My Channel",
            "brand_logo_path": logo,
            "brand_intro_seconds": intro, "brand_outro_seconds": outro,
            "smart_silence_removal": bool(self.silence_enabled.get()),
            "smart_silence_threshold_db": threshold,
        })
        self.save()
        self.status.set("Intro/outro and smart silence options saved. They apply to new runs/resumes.")
