"""Subtitle controls adapted from the subtitle tool for the Recap production panel."""
from __future__ import annotations

import tkinter as tk
from tkinter import colorchooser, ttk

from subtitle_fonts import myanmar_fonts
from subtitle_png import style


class SubtitleControls(ttk.Frame):
    def __init__(self, parent, values, on_change):
        super().__init__(parent)
        self.columnconfigure(1, weight=1)
        self.saved = style(values)
        self.position = list(self.saved["position"])
        self.variables = {}
        self.on_change = on_change
        for key, value in self.saved.items():
            if key == "position":
                continue
            cls = tk.BooleanVar if isinstance(value, bool) else tk.StringVar
            self.variables[key] = cls(self, value=value)
        ttk.Checkbutton(self, text="Subtitle ထည့်မယ်", variable=self.variables["enabled"],
                        command=on_change).grid(row=0, column=0, columnspan=2, sticky="w")
        ttk.Label(self, text="Font").grid(row=1, column=0, sticky="w", pady=3)
        fonts = sorted(set(myanmar_fonts()) | {self.saved["font"]})
        combo = ttk.Combobox(self, textvariable=self.variables["font"], values=fonts, state="readonly", width=18)
        combo.grid(row=1, column=1, sticky="ew", pady=3)
        combo.bind("<<ComboboxSelected>>", lambda _e: on_change())
        self._number(2, "Size (px)", "size", 12, 144)
        ttk.Checkbutton(self, text="Bold", variable=self.variables["bold"], command=on_change).grid(
            row=3, column=0, columnspan=2, sticky="w")
        self._colour(4, "Text colour", "color")
        self._colour(5, "Outline colour", "outline_color")
        ttk.Label(self, text="Outline").grid(row=6, column=0, sticky="w", pady=3)
        self.outline = tk.StringVar(self, value="Auto" if self.saved["outline_width"] < 0 else str(self.saved["outline_width"]))
        combo = ttk.Combobox(self, textvariable=self.outline, values=("Auto", *map(str, range(13))),
                             state="readonly", width=8)
        combo.grid(row=6, column=1, sticky="ew", pady=3)
        combo.bind("<<ComboboxSelected>>", lambda _e: on_change())
        self._number(7, "Shadow (px)", "shadow", 0, 12)
        ttk.Checkbutton(self, text="Background box", variable=self.variables["box_enabled"], command=on_change).grid(
            row=8, column=0, columnspan=2, sticky="w")
        self._colour(9, "Box colour", "box_color")
        self._number(10, "Box opacity %", "box_opacity", 0, 100)
        self.width_percent = tk.StringVar(self, value=round(self.saved["width"] * 100))
        ttk.Label(self, text="Width %").grid(row=11, column=0, sticky="w", pady=3)
        width = ttk.Spinbox(self, textvariable=self.width_percent, from_=20, to=100, width=8, command=on_change)
        width.grid(row=11, column=1, sticky="ew", pady=3)
        for event in ("<Return>", "<FocusOut>"):
            width.bind(event, lambda _e: on_change())
        ttk.Label(self, text="Preview မှာ subtitle ကို ဆွဲရွှေ့နိုင်ပါတယ်", wraplength=245).grid(
            row=12, column=0, columnspan=2, sticky="w", pady=(5, 8))

    def _number(self, row, label, key, low, high):
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=3)
        field = ttk.Spinbox(self, textvariable=self.variables[key], from_=low, to=high, width=8,
                            command=self.on_change)
        field.grid(row=row, column=1, sticky="ew", pady=3)
        for event in ("<Return>", "<FocusOut>"):
            field.bind(event, lambda _e: self.on_change())

    def _colour(self, row, label, key):
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=3)
        button = ttk.Button(self, textvariable=self.variables[key], command=lambda: self._choose(key))
        button.grid(row=row, column=1, sticky="ew", pady=3)

    def _choose(self, key):
        value = colorchooser.askcolor(self.variables[key].get(), parent=self.winfo_toplevel())[1]
        if value:
            self.variables[key].set(value)
            self.on_change()

    def values(self):
        values = {key: var.get() for key, var in self.variables.items()}
        values["outline_width"] = -1 if self.outline.get() == "Auto" else int(self.outline.get())
        values["width"] = float(self.width_percent.get()) / 100
        values["position"] = list(self.position)
        return style(values)
