"""UI for the persistent local Recap job queue."""
from __future__ import annotations

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from studio.recap_queue import PersistentRecapQueue

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".mov", ".webm", ".avi", ".m4v", ".mpeg", ".mpg"}


class RecapQueueTab(ttk.Frame):
    def __init__(self, master, *, root_dir: Path, queue_model: PersistentRecapQueue, on_start, on_stop):
        super().__init__(master, padding=14)
        self.root_dir = Path(root_dir)
        self.queue_model = queue_model
        self.on_start, self.on_stop = on_start, on_stop
        self.running = False
        self.status = tk.StringVar(value="Queue local videos here. Pending jobs survive an app restart.")
        self._build()
        self.refresh()

    def _build(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        ttk.Label(self, text="Recap Queue", font=("Segoe UI Semibold", 17)).grid(row=0, column=0, sticky="w")
        ttk.Label(self, text="Queue local videos for sequential Recap processing. This queue is saved separately from downloads.",
                  wraplength=1050).grid(row=1, column=0, sticky="w", pady=(3, 10))
        frame = ttk.Frame(self)
        frame.grid(row=2, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        self.listbox = tk.Listbox(frame, height=16, background="#0a0c10", foreground="#e7eaf0",
                                  selectbackground="#33445f", relief="flat", highlightthickness=1)
        self.listbox.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.listbox.configure(yscrollcommand=scrollbar.set)
        buttons = ttk.Frame(self)
        buttons.grid(row=3, column=0, sticky="ew", pady=(8, 5))
        self.add_files_button = ttk.Button(buttons, text="Add Videos…", command=self.add_files)
        self.add_files_button.pack(side="left")
        self.add_folder_button = ttk.Button(buttons, text="Add Folder…", command=self.add_folder)
        self.add_folder_button.pack(side="left", padx=(6, 0))
        self.start_button = ttk.Button(buttons, text="Start Queue", command=self.start)
        self.start_button.pack(side="left", padx=(12, 0))
        self.stop_button = ttk.Button(buttons, text="Stop Safely", command=self.stop, state="disabled")
        self.stop_button.pack(side="left", padx=(6, 0))
        self.retry_button = ttk.Button(buttons, text="Retry Failed", command=self.retry_failed)
        self.retry_button.pack(side="left", padx=(6, 0))
        self.clear_button = ttk.Button(buttons, text="Clear Finished", command=self.clear_finished)
        self.clear_button.pack(side="left", padx=(6, 0))
        ttk.Label(self, textvariable=self.status, wraplength=1050).grid(row=4, column=0, sticky="w", pady=(5, 0))

    def enqueue_video(self, path: str | Path) -> int:
        added, _skipped = self.queue_model.add([path])
        self.refresh()
        return len(added)

    def add_files(self):
        paths = filedialog.askopenfilenames(
            title="Add videos to Recap queue",
            filetypes=(("Video files", "*.mp4 *.mkv *.mov *.webm *.avi *.m4v *.mpeg *.mpg"), ("All files", "*.*")),
        )
        if paths:
            added, skipped = self.queue_model.add(paths)
            self.refresh()
            self.status.set(f"Added {len(added)} video(s); skipped {len(skipped)} duplicate(s).")

    def add_folder(self):
        folder = filedialog.askdirectory(initialdir=str(self.root_dir))
        if not folder:
            return
        root = Path(folder)
        paths = sorted(path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS)
        if not paths:
            messagebox.showinfo("Recap Queue", "No supported video files found in that folder.", parent=self)
            return
        added, skipped = self.queue_model.add(paths)
        self.refresh()
        self.status.set(f"Added {len(added)} video(s) from folder; skipped {len(skipped)} duplicate(s).")

    def start(self):
        if self.running:
            return
        if not self.queue_model.pending():
            messagebox.showinfo("Recap Queue", "No pending videos. Add videos or press Retry Failed.", parent=self)
            return
        self.on_start()

    def stop(self):
        if self.running:
            self.on_stop()

    def retry_failed(self):
        count = self.queue_model.retry_failed()
        self.refresh()
        self.status.set(f"Reset {count} failed video(s) to pending.")

    def clear_finished(self):
        count = self.queue_model.clear_finished()
        self.refresh()
        self.status.set(f"Removed {count} completed queue item(s).")

    def set_running(self, value: bool):
        self.running = bool(value)
        state = "disabled" if self.running else "normal"
        for name in ("add_files_button", "add_folder_button", "retry_button", "clear_button", "start_button"):
            getattr(self, name).configure(state=state)
        self.stop_button.configure(state="normal" if self.running else "disabled")
        self.refresh()

    def refresh(self):
        if not hasattr(self, "listbox") or not self.winfo_exists():
            return
        self.listbox.delete(0, "end")
        items = self.queue_model.items()
        counts = {name: sum(item.status == name for item in items) for name in ("pending", "processing", "completed", "failed")}
        for index, item in enumerate(items, 1):
            marker = {"pending": "WAIT", "processing": "RUN", "completed": "DONE", "failed": "FAIL"}[item.status]
            display = f"[{marker}] {index:03d}. {Path(item.path).name} — {item.path}"
            self.listbox.insert("end", display[:1000])
        self.status.set(
            f"Pending {counts['pending']} · Processing {counts['processing']} · "
            f"Completed {counts['completed']} · Failed {counts['failed']}."
        )
        if hasattr(self, "start_button"):
            self.start_button.configure(state="disabled" if self.running or not self.queue_model.pending() else "normal")
