"""Persistent local Recap queue (independent of the URL download queue)."""
from __future__ import annotations

import hashlib
import json
import os
import threading
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class RecapQueueItem:
    id: str
    path: str
    status: str = "pending"
    error: str = ""
    output_path: str = ""


class PersistentRecapQueue:
    STATUSES = {"pending", "processing", "completed", "failed"}

    def __init__(self, path: str | Path):
        self.path = Path(path).expanduser().resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._items: list[RecapQueueItem] = []
        self._load()

    @staticmethod
    def _normalize(path: str | Path) -> str:
        try:
            return str(Path(path).expanduser().resolve())
        except (OSError, RuntimeError):
            return str(Path(path).expanduser())

    @classmethod
    def _make_id(cls, path: str | Path) -> str:
        return hashlib.sha256(cls._normalize(path).casefold().encode("utf-8")).hexdigest()[:20]

    def _load(self) -> None:
        if not self.path.is_file():
            return
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return
        rows = payload.get("items", []) if isinstance(payload, dict) else []
        loaded: list[RecapQueueItem] = []
        seen: set[str] = set()
        for row in rows if isinstance(rows, list) else []:
            if not isinstance(row, dict) or not row.get("path"):
                continue
            path = self._normalize(row["path"])
            ident = str(row.get("id") or self._make_id(path))
            if ident in seen:
                continue
            seen.add(ident)
            status = str(row.get("status") or "pending")
            if status not in self.STATUSES:
                status = "pending"
            # A killed app must not leave an item permanently stuck in processing.
            if status == "processing":
                status = "pending"
            loaded.append(RecapQueueItem(
                id=ident, path=path, status=status, error=str(row.get("error") or ""),
                output_path=str(row.get("output_path") or ""),
            ))
        self._items = loaded

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        payload = {"version": 1, "items": [asdict(item) for item in self._items]}
        temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(temporary, self.path)

    def items(self) -> list[RecapQueueItem]:
        with self._lock:
            return [RecapQueueItem(**asdict(item)) for item in self._items]

    def pending(self, *, include_failed: bool = False) -> list[RecapQueueItem]:
        statuses = {"pending"} | ({"failed"} if include_failed else set())
        with self._lock:
            return [RecapQueueItem(**asdict(item)) for item in self._items if item.status in statuses]

    def add(self, paths: Iterable[str | Path]) -> tuple[list[RecapQueueItem], list[str]]:
        added: list[RecapQueueItem] = []
        skipped: list[str] = []
        with self._lock:
            existing = {item.path.casefold() for item in self._items}
            for raw in paths:
                path = self._normalize(raw)
                if path.casefold() in existing:
                    skipped.append(path)
                    continue
                item = RecapQueueItem(id=self._make_id(path), path=path)
                self._items.append(item)
                existing.add(path.casefold())
                added.append(RecapQueueItem(**asdict(item)))
            if added:
                self._save()
        return added, skipped

    def update(self, item_id: str, *, status: str, error: str | None = None,
               output_path: str | None = None) -> None:
        if status not in self.STATUSES:
            raise ValueError(f"Unsupported Recap queue status: {status}")
        with self._lock:
            for item in self._items:
                if item.id == item_id:
                    item.status = status
                    if error is not None:
                        item.error = str(error)
                    if output_path is not None:
                        item.output_path = str(output_path)
                    self._save()
                    return
        raise KeyError(f"Recap queue item not found: {item_id}")

    def retry_failed(self) -> int:
        count = 0
        with self._lock:
            for item in self._items:
                if item.status == "failed":
                    item.status, item.error = "pending", ""
                    count += 1
            if count:
                self._save()
        return count

    def clear_finished(self) -> int:
        with self._lock:
            before = len(self._items)
            self._items = [item for item in self._items if item.status != "completed"]
            removed = before - len(self._items)
            if removed:
                self._save()
            return removed
