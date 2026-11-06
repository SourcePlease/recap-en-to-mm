"""Manual character-by-character dubbing workspace."""
from __future__ import annotations

import threading
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from studio.dubbing import (
    load_dubbing_project, parse_dialogue_rows, parse_speaker_voices,
    render_character_dubbing, save_dubbing_project,
)
from studio.subtitles import parse_subtitles


class DubbingTab(ttk.Frame):
    def __init__(self, master, *, root_dir: Path, tool):
        super().__init__(master, padding=14)
        self.root_dir = Path(root_dir)
        self.tool = tool
        self.source = tk.StringVar()
        self.subtitle = tk.StringVar()
        self.audio_mode = tk.StringVar(value="Mute source audio")
        self.status = tk.StringVar(value="Import a translated SRT/VTT, assign speakers and voices, then render.")
        self.busy = False
        self._build()

    def _build(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(5, weight=1)
        ttk.Label(self, text="Character Voice Dubbing", font=("Segoe UI Semibold", 17)).grid(
            row=0, column=0, columnspan=3, sticky="w")
        ttk.Label(self, text=(
            "Manual, timestamped dialogue dubbing. Import a translated SRT/VTT, review each line, "
            "assign a speaker, and map each speaker to a stable Edge TTS voice. Automatic diarization is not assumed."
        ), wraplength=1050).grid(row=1, column=0, columnspan=3, sticky="w", pady=(4, 12))
        ttk.Label(self, text="Source video").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Entry(self, textvariable=self.source).grid(row=2, column=1, sticky="ew", padx=8, pady=4)
        ttk.Button(self, text="Browse", command=self._browse_source).grid(row=2, column=2, pady=4)
        ttk.Label(self, text="Translated SRT/VTT").grid(row=3, column=0, sticky="w", pady=4)
        ttk.Entry(self, textvariable=self.subtitle).grid(row=3, column=1, sticky="ew", padx=8, pady=4)
        ttk.Button(self, text="Import", command=self._import_subtitles).grid(row=3, column=2, pady=4)
        ttk.Label(self, text="Dialogue rows (start<TAB>end<TAB>speaker<TAB>translated text)").grid(
            row=4, column=0, columnspan=3, sticky="w", pady=(10, 3))
        self.rows = tk.Text(self, height=13, wrap="none", undo=True)
        self.rows.grid(row=5, column=0, columnspan=3, sticky="nsew")
        ttk.Label(self, text="Speaker voice mapping (one per line: Speaker A=my-MM-ThihaNeural)").grid(
            row=6, column=0, columnspan=3, sticky="w", pady=(10, 3))
        self.voices = tk.Text(self, height=4, wrap="none", undo=True)
        self.voices.grid(row=7, column=0, columnspan=3, sticky="ew")
        self.voices.insert("1.0", "Speaker A=my-MM-ThihaNeural\nSpeaker B=my-MM-NilarNeural")
        controls = ttk.Frame(self)
        controls.grid(row=8, column=0, columnspan=3, sticky="ew", pady=(10, 4))
        ttk.Label(controls, text="Source audio:").pack(side="left")
        ttk.Combobox(
            controls, textvariable=self.audio_mode, state="readonly", width=34,
            values=("Mute source audio", "Keep original dialogue + BGM", "Keep instrumental BGM (Demucs)"),
        ).pack(side="left", padx=6)
        ttk.Button(controls, text="Save Project", command=self._save_project).pack(side="left", padx=(10, 3))
        ttk.Button(controls, text="Load Project", command=self._load_project).pack(side="left", padx=3)
        self.render_button = ttk.Button(controls, text="Render Character Dub", command=self._render)
        self.render_button.pack(side="right")
        ttk.Label(self, textvariable=self.status, wraplength=1050).grid(
            row=9, column=0, columnspan=3, sticky="w", pady=(8, 0))
        ttk.Label(self, text=(
            "Voice profiles are user-selected; no gender or character identity is guessed. "
            "Demucs is needed only for instrumental-only source audio and may use significant CPU/RAM."
        ), wraplength=1050).grid(row=10, column=0, columnspan=3, sticky="w", pady=(6, 0))

    def _browse_source(self):
        path = filedialog.askopenfilename(filetypes=(("Video", "*.mp4 *.mkv *.mov *.webm *.avi *.m4v"), ("All files", "*.*")))
        if path:
            self.source.set(path)

    def _import_subtitles(self):
        path = filedialog.askopenfilename(filetypes=(("Subtitle", "*.srt *.vtt"), ("All files", "*.*")))
        if not path:
            return
        try:
            cues = parse_subtitles(Path(path).read_text(encoding="utf-8-sig", errors="replace"))
            lines = [
                f"{cue.start}\t{cue.end}\tSpeaker A\t{cue.text.replace(chr(9), ' ').replace(chr(10), ' ')}"
                for cue in cues
            ]
            self.rows.delete("1.0", "end")
            self.rows.insert("1.0", "\n".join(lines))
            self.subtitle.set(path)
            self.status.set(f"Imported {len(cues)} dialogue rows. Edit translated text and speaker labels before rendering.")
        except Exception as exc:
            messagebox.showerror("Character Dubbing", str(exc), parent=self)

    def _read_rows(self):
        return parse_dialogue_rows(self.rows.get("1.0", "end"))

    def _read_voices(self):
        return parse_speaker_voices(self.voices.get("1.0", "end"))

    def _save_project(self):
        try:
            rows, voices = self._read_rows(), self._read_voices()
            path = filedialog.asksaveasfilename(
                defaultextension=".dubbing.json", initialfile="CharacterDubbing.dubbing.json",
                filetypes=(("Dubbing project", "*.dubbing.json"), ("JSON", "*.json")),
            )
            if not path:
                return
            save_dubbing_project(Path(path), rows, voices)
            self.status.set(f"Saved character dubbing project: {Path(path).name}")
        except Exception as exc:
            messagebox.showerror("Character Dubbing", str(exc), parent=self)

    def _load_project(self):
        path = filedialog.askopenfilename(filetypes=(("Dubbing project", "*.dubbing.json *.json"), ("All files", "*.*")))
        if not path:
            return
        try:
            rows, voices = load_dubbing_project(Path(path))
            self.rows.delete("1.0", "end")
            self.rows.insert("1.0", "\n".join(
                f"{row.start}\t{row.end}\t{row.speaker}\t{row.text}" for row in rows
            ))
            self.voices.delete("1.0", "end")
            self.voices.insert("1.0", "\n".join(f"{speaker}={voice}" for speaker, voice in voices.items()))
            self.status.set(f"Loaded {len(rows)} dialogue rows from {Path(path).name}")
        except Exception as exc:
            messagebox.showerror("Character Dubbing", str(exc), parent=self)

    def _render(self):
        if self.busy:
            return
        source = Path(self.source.get().strip())
        if not source.is_file():
            messagebox.showwarning("Character Dubbing", "Choose an existing source video.", parent=self)
            return
        try:
            rows, voices = self._read_rows(), self._read_voices()
        except Exception as exc:
            messagebox.showwarning("Character Dubbing", str(exc), parent=self)
            return
        output = filedialog.asksaveasfilename(
            defaultextension=".mp4", initialfile=f"{source.stem}_character_dub.mp4",
            filetypes=(("MP4 video", "*.mp4"),),
        )
        if not output:
            return
        mode = {
            "Mute source audio": "mute",
            "Keep original dialogue + BGM": "keep",
            "Keep instrumental BGM (Demucs)": "instrumental",
        }.get(self.audio_mode.get(), "instrumental")
        self.busy = True
        self.render_button.configure(state="disabled")
        self.status.set("Preparing dialogue voices and rendering…")

        def log(message):
            self.after(0, lambda value=message: self.status.set(value))

        def work():
            try:
                result = render_character_dubbing(
                    ffmpeg=str(self.tool("ffmpeg")), ffprobe=str(self.tool("ffprobe")),
                    source_video=source, rows=rows, speaker_voices=voices,
                    output_video=Path(output), source_audio_mode=mode, log=log,
                )
                self.after(0, lambda: messagebox.showinfo("Character Dubbing", f"Created:\n{result}", parent=self))
            except Exception as exc:
                message = str(exc)
                self.after(0, lambda value=message: messagebox.showerror("Character Dubbing", value, parent=self))
                log(f"Character dubbing failed: {message}")
            finally:
                self.after(0, self._render_finished)

        threading.Thread(target=work, daemon=True).start()

    def _render_finished(self):
        self.busy = False
        self.render_button.configure(state="normal")
