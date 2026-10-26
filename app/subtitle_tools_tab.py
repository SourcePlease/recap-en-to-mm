"""Standalone imported-subtitle translation and bilingual SRT export."""
from __future__ import annotations

import os
import threading
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from studio.subtitles import SubtitleCue, parse_subtitles, translate_subtitles, write_srt

TARGETS = {
    "mm": "Myanmar (Burmese)", "en": "English", "zh": "Chinese", "ja": "Japanese", "ko": "Korean",
    "hi": "Hindi", "th": "Thai", "vi": "Vietnamese", "id": "Indonesian", "ms": "Malay",
    "tl": "Filipino (Tagalog)", "es": "Spanish", "pt": "Portuguese", "fr": "French", "de": "German",
    "it": "Italian", "ru": "Russian", "tr": "Turkish", "ar": "Arabic", "bn": "Bengali",
    "ta": "Tamil", "te": "Telugu", "ur": "Urdu",
}


class SubtitleToolsTab(ttk.Frame):
    def __init__(self, master, *, root_dir: Path, cfg: dict, save, env_path=None):
        super().__init__(master, padding=14)
        self.root_dir, self.cfg, self.save = Path(root_dir), cfg, save
        self.env_path = env_path or (lambda: self.root_dir / ".env")
        self.input_path = tk.StringVar()
        self.output_dir = tk.StringVar(value=str(self.root_dir / "Downloads"))
        self.source_lang = tk.StringVar(value="Auto-detect")
        self.target_lang = tk.StringVar(value="Myanmar (Burmese)")
        self.provider = tk.StringVar(value=str(cfg.get("subtitle_provider") or "gemini"))
        self.model = tk.StringVar(value=str(cfg.get("subtitle_model") or os.getenv("GEMINI_TEXT_MODEL") or "gemini-3.5-flash"))
        self.api_key = tk.StringVar(value="")
        self.status = tk.StringVar(value="Import an existing .srt or .vtt file. This tool does not run Whisper.")
        self.cues: list[SubtitleCue] = []
        self.translations: list[str] = []
        self.busy = False
        self._build()

    def _build(self):
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text="Subtitle Import / Translate", font=("Segoe UI Semibold", 17)).grid(
            row=0, column=0, columnspan=3, sticky="w")
        ttk.Label(self, text="Translate an existing subtitle file directly, preserve timestamps, and export translated or bilingual SRT.",
                  wraplength=1000).grid(row=1, column=0, columnspan=3, sticky="w", pady=(3, 12))
        ttk.Label(self, text="Subtitle file").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.input_path).grid(row=2, column=1, sticky="ew", padx=8, pady=5)
        ttk.Button(self, text="Browse", command=self._browse_input).grid(row=2, column=2, pady=5)
        ttk.Label(self, text="Output folder").grid(row=3, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.output_dir).grid(row=3, column=1, sticky="ew", padx=8, pady=5)
        ttk.Button(self, text="Browse", command=self._browse_output).grid(row=3, column=2, pady=5)
        ttk.Label(self, text="Source language").grid(row=4, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.source_lang).grid(row=4, column=1, sticky="ew", padx=8, pady=5)
        ttk.Label(self, text="Target language").grid(row=5, column=0, sticky="w", pady=5)
        ttk.Combobox(self, textvariable=self.target_lang, state="readonly", values=tuple(TARGETS.values())).grid(
            row=5, column=1, sticky="ew", padx=8, pady=5)
        ttk.Label(self, text="AI provider").grid(row=6, column=0, sticky="w", pady=5)
        ttk.Combobox(self, textvariable=self.provider, state="readonly",
                     values=("gemini", "groq", "openrouter", "ollama")).grid(
            row=6, column=1, sticky="ew", padx=8, pady=5)
        ttk.Label(self, text="Model ID").grid(row=7, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.model).grid(row=7, column=1, sticky="ew", padx=8, pady=5)
        ttk.Label(self, text="API key (optional only for Ollama)").grid(row=8, column=0, sticky="w", pady=5)
        ttk.Entry(self, textvariable=self.api_key, show="•").grid(row=8, column=1, sticky="ew", padx=8, pady=5)
        self.preview = tk.Text(self, height=10, wrap="word")
        self.preview.grid(row=9, column=0, columnspan=3, sticky="nsew", pady=(10, 8))
        self.rowconfigure(9, weight=1)
        actions = ttk.Frame(self)
        actions.grid(row=10, column=0, columnspan=3, sticky="ew", pady=5)
        ttk.Button(actions, text="Import / Preview", command=self._import).pack(side="left")
        self.translate_button = ttk.Button(actions, text="Translate", command=self._translate)
        self.translate_button.pack(side="left", padx=8)
        self.export_button = ttk.Button(actions, text="Export translated + bilingual SRT", command=self._export, state="disabled")
        self.export_button.pack(side="left")
        ttk.Label(self, textvariable=self.status, wraplength=1050).grid(
            row=11, column=0, columnspan=3, sticky="w", pady=(8, 0))

    def _browse_input(self):
        path = filedialog.askopenfilename(filetypes=(("Subtitle files", "*.srt *.vtt"), ("All files", "*.*")))
        if path:
            self.input_path.set(path)
            self._import()

    def _browse_output(self):
        path = filedialog.askdirectory(initialdir=self.output_dir.get() or str(self.root_dir))
        if path:
            self.output_dir.set(path)

    def _import(self):
        path = Path(self.input_path.get().strip())
        if not path.is_file():
            messagebox.showwarning("Subtitles", "Choose an existing SRT/VTT file.", parent=self)
            return
        try:
            self.cues = parse_subtitles(path.read_text(encoding="utf-8-sig", errors="replace"))
            self.translations = []
            self.preview.delete("1.0", "end")
            self.preview.insert("1.0", "\n\n".join(
                f"{cue.index}. {cue.start} --> {cue.end}\n{cue.text}" for cue in self.cues[:60]))
            self.status.set(f"Imported {len(self.cues)} cues. Whisper is not invoked.")
            self.export_button.configure(state="disabled")
        except Exception as exc:
            messagebox.showerror("Subtitles", str(exc), parent=self)

    def _translate(self):
        if self.busy:
            return
        if not self.cues:
            self._import()
        if not self.cues:
            return
        provider, model = self.provider.get(), self.model.get().strip()
        key = self.api_key.get().strip() or None
        if provider in {"groq", "openrouter"} and not key:
            messagebox.showwarning("Subtitles", "Enter the API key for the selected provider.", parent=self)
            return
        if provider == "gemini" and not key:
            try:
                from dotenv import load_dotenv
                env = Path(self.env_path())
                if env.is_file():
                    load_dotenv(env, override=False)
            except Exception:
                pass
            key = os.getenv("GEMINI_API_KEY", "").strip() or None
        if provider == "gemini" and not key:
            messagebox.showwarning("Subtitles", "Set GEMINI_API_KEY in .env or enter a key.", parent=self)
            return
        target, source = self.target_lang.get(), self.source_lang.get().strip() or "Auto-detect"
        self.busy = True
        self.translate_button.configure(state="disabled")
        self.status.set(f"Translating {len(self.cues)} cues into {target}…")
        def work():
            try:
                translated = translate_subtitles(
                    self.cues, provider=provider, model=model, target_language=target,
                    source_language=source, api_key=key,
                    progress=lambda done, total: self.after(
                        0, lambda done=done, total=total: self.status.set(f"Translated {done}/{total} cues…")),
                )
                self.after(0, lambda: self._translated(translated, None))
            except Exception as exc:
                message = str(exc)
                self.after(0, lambda message=message: self._translated([], message))
        threading.Thread(target=work, daemon=True).start()

    def _translated(self, values, error):
        self.busy = False
        self.translate_button.configure(state="normal")
        if error:
            self.status.set(f"Translation failed: {error}")
            messagebox.showerror("Subtitles", error, parent=self)
            return
        self.translations = values
        preview = [f"{cue.index}. {cue.start} --> {cue.end}\n{cue.text}\n{translated}"
                   for cue, translated in list(zip(self.cues, values))[:60]]
        self.preview.delete("1.0", "end")
        self.preview.insert("1.0", "\n\n".join(preview))
        self.export_button.configure(state="normal")
        self.status.set(f"Translated {len(values)} cues. Export creates translated-only and bilingual SRT files.")

    def _export(self):
        if not self.cues or len(self.translations) != len(self.cues):
            return
        source_path = Path(self.input_path.get())
        folder = Path(self.output_dir.get().strip() or source_path.parent)
        try:
            folder.mkdir(parents=True, exist_ok=True)
            target_code = next((code for code, label in TARGETS.items() if label == self.target_lang.get()), "mm")
            translated = write_srt(folder / f"{source_path.stem}_{target_code}_translated.srt", self.cues, self.translations)
            bilingual = write_srt(folder / f"{source_path.stem}_{target_code}_bilingual.srt",
                                  self.cues, self.translations, bilingual=True)
            self.cfg["subtitle_provider"] = self.provider.get()
            self.cfg["subtitle_model"] = self.model.get().strip()
            self.save()
            self.status.set(f"Saved {translated.name} and {bilingual.name}.")
            messagebox.showinfo("Subtitles", f"Created:\n{translated}\n{bilingual}", parent=self)
        except Exception as exc:
            messagebox.showerror("Subtitles", str(exc), parent=self)
