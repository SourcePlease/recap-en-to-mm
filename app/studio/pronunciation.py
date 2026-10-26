"""Local pronunciation substitutions applied immediately before speech synthesis."""
from __future__ import annotations
import json
import re
from pathlib import Path


def load_pronunciations(path: str | Path) -> dict[str, str]:
    file = Path(path)
    if not file.is_file():
        return {}
    try:
        data = json.loads(file.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    if not isinstance(data, dict):
        return {}
    return {str(k).strip(): str(v).strip() for k, v in data.items() if str(k).strip() and str(v).strip()}


def apply_pronunciation_overrides(text: str, path: str | Path) -> str:
    """Replace longest dictionary terms first; subtitles are not modified."""
    value = str(text or "")
    mapping = load_pronunciations(path)
    for source in sorted(mapping, key=len, reverse=True):
        if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 ._+'-]*", source):
            value = re.sub(r"(?<!\w)" + re.escape(source) + r"(?!\w)", lambda _m: mapping[source], value, flags=re.IGNORECASE)
        else:
            value = value.replace(source, mapping[source])
    return value
