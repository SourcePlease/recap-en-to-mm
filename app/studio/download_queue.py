"""Small persistent URL-download queue.

Queue metadata lives under the ignored jobs/ directory. URLs are stored locally
so queued work can resume after a restart; do not add secrets/tokens to URLs
unless you understand that they will be stored in plain text on this computer.
"""
from __future__ import annotations

import hashlib
import json
import os
import threading
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


STATUSES = {"pending", "downloading", "completed", "failed"}


@dataclass
class QueueItem:
    id: str
    url: str
    status: str = "pending"
    title: str = ""
    error: str = ""
    output_files: list[str] | None = None


class PersistentDownloadQueue:
    def __init__(self, path: str | Path):
        self.path = Path(path).expanduser().resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._items: list[QueueItem] = []
        self._load()

    @staticmethod
    def _make_id(url: str) -> str:
        return hashlib.sha256(url.strip().encode("utf-8")).hexdigest()[:20]

    def _load(self) -> None:
        if not self.path.is_file():
            return
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            # Preserve the bad file for diagnosis rather than silently overwriting it.
            return
        items = payload.get("items", []) if isinstance(payload, dict) else []
        if not isinstance(items, list):
            return
        loaded: list[QueueItem] = []
        for item in items:
            if not isinstance(item, dict):
                continue
            url = str(item.get("url") or "").strip()
            if not url:
                continue
            status = str(item.get("status") or "pending")
            if status not in STATUSES or status == "downloading":
                status = "pending"
            loaded.append(QueueItem(
                id=str(item.get("id") or self._make_id(url)),
                url=url,
                status=status,
                title=str(item.get("title") or ""),
                error=str(item.get("error") or ""),
                output_files=[str(v) for v in (item.get("output_files") or [])],
            ))
        self._items = loaded

    def _save(self) -> None:
        temp_path = self.path.with_suffix(self.path.suffix + ".tmp")
        payload = {"version": 1, "items": [asdict(item) for item in self._items]}
        temp_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(temp_path, self.path)

    def items(self) -> list[QueueItem]:
        with self._lock:
            return [QueueItem(**asdict(item)) for item in self._items]

    def add(self, urls: Iterable[str]) -> tuple[list[QueueItem], list[str]]:
        """Add unique URL strings; caller handles URL scheme validation."""
        added: list[QueueItem] = []
        skipped: list[str] = []
        with self._lock:
            existing = {item.url for item in self._items}
            for raw in urls:
                url = str(raw or "").strip()
                if not url:
                    continue
                if url in existing:
                    skipped.append(url)
                    continue
                item = QueueItem(id=self._make_id(url), url=url)
                self._items.append(item)
                added.append(item)
                existing.add(url)
            if added:
                self._save()
        return added, skipped

    def pending(self, *, include_failed: bool = False) -> list[QueueItem]:
        statuses = {"pending"} | ({"failed"} if include_failed else set())
        with self._lock:
            return [
                QueueItem(**asdict(item)) for item in self._items
                if item.status in statuses
            ]

    def update(
        self,
        item_id: str,
        *,
        status: str,
        title: str | None = None,
        error: str | None = None,
        output_files: list[str] | None = None,
    ) -> None:
        if status not in STATUSES:
            raise ValueError(f"Unknown queue status: {status}")
        with self._lock:
            for item in self._items:
                if item.id != item_id:
                    continue
                item.status = status
                if title is not None:
                    item.title = str(title)
                if error is not None:
                    item.error = str(error)
                if output_files is not None:
                    item.output_files = list(output_files)
                self._save()
                return
            raise KeyError(f"Queue item not found: {item_id}")

    def retry_failed(self) -> int:
        count = 0
        with self._lock:
            for item in self._items:
                if item.status == "failed":
                    item.status = "pending"
                    item.error = ""
                    count += 1
            if count:
                self._save()
        return count

    def clear_finished(self) -> int:
        with self._lock:
            before = len(self._items)
            self._items = [item for item in self._items if item.status not in {"completed"}]
            removed = before - len(self._items)
            if removed:
                self._save()
            return removed
