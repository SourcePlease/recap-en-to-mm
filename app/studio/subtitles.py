"""SRT/VTT import, timestamp-preserving translation, and bilingual subtitle export."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from studio.ai_providers import AIProviderError, chat_completion


@dataclass(frozen=True)
class SubtitleCue:
    index: int
    start: str
    end: str
    text: str


TIMESTAMP_RE = re.compile(
    r"(?P<start>\d{1,2}:\d{2}(?::\d{2})?[,.]\d{3})\s*-->\s*"
    r"(?P<end>\d{1,2}:\d{2}(?::\d{2})?[,.]\d{3})(?:\s+.*)?"
)


def parse_subtitles(text: str) -> list[SubtitleCue]:
    """Parse common SRT/VTT cues without modifying timestamps or cue order."""
    source = (text or "").replace("\ufeff", "").replace("\r\n", "\n").replace("\r", "\n")
    cues: list[SubtitleCue] = []
    for block in re.split(r"\n\s*\n", source):
        lines = [line.rstrip() for line in block.split("\n")]
        index = next((i for i, line in enumerate(lines) if TIMESTAMP_RE.search(line)), None)
        if index is None:
            continue
        match = TIMESTAMP_RE.search(lines[index])
        if not match:
            continue
        body = "\n".join(lines[index + 1:]).strip()
        if body:
            cues.append(SubtitleCue(len(cues) + 1, match.group("start"), match.group("end"), body))
    if not cues:
        raise ValueError("No valid SRT/VTT subtitle cues were found.")
    return cues


def _time_to_srt(value: str) -> str:
    value = value.strip().replace(",", ".")
    parts = value.split(":")
    if len(parts) == 2:
        parts = ["00", *parts]
    if len(parts) != 3:
        raise ValueError(f"Unsupported subtitle timestamp: {value}")
    hh, mm, ss = parts
    if "." not in ss:
        ss += ".000"
    whole, ms = ss.split(".", 1)
    return f"{int(hh):02d}:{int(mm):02d}:{int(whole):02d},{(ms + '000')[:3]}"


def format_srt(cues: list[SubtitleCue], translations: list[str] | None = None, *, bilingual: bool = False) -> str:
    blocks = []
    for index, cue in enumerate(cues, 1):
        target = translations[index - 1] if translations and index <= len(translations) else ""
        text = f"{cue.text}\n{target}" if bilingual and target else (target or cue.text)
        blocks.append(f"{index}\n{_time_to_srt(cue.start)} --> {_time_to_srt(cue.end)}\n{text.strip()}")
    return "\n\n".join(blocks) + "\n"


def _strip_code_fence(value: str) -> str:
    fence = chr(96) * 3
    text = str(value or "").strip()
    if text.startswith(fence):
        text = text[len(fence):]
        if text[:4].lower() == "json":
            text = text[4:]
        text = text.strip()
        if text.endswith(fence):
            text = text[:-len(fence)]
    return text.strip()


def _translate_gemini_batch(rows: list[SubtitleCue], *, model: str, target_language: str,
                            source_language: str, api_key: str) -> list[str]:
    try:
        from google import genai
    except ImportError as exc:
        raise AIProviderError("Gemini SDK is missing; rerun INSTALL_REQUIREMENTS.bat.") from exc
    if not api_key:
        raise AIProviderError("Set GEMINI_API_KEY in .env or enter the key in the subtitle tool.")
    prompt = (
        f"Translate subtitle dialogue from {source_language} into {target_language}. "
        "Keep meaning, names, tone and concise subtitle phrasing. Never summarize. "
        'Return JSON only: {"items":[{"id":1,"translation":"..."}]}. '
        "Return exactly one translated item for each supplied ID, in order. No explanations or timestamps.\n\n"
        + json.dumps([{"id": row.index, "text": row.text} for row in rows], ensure_ascii=False)
    )
    response = genai.Client(api_key=api_key).models.generate_content(model=model, contents=prompt)
    data = json.loads(_strip_code_fence(str(getattr(response, "text", "") or "")))
    items = data.get("items") if isinstance(data, dict) else None
    if not isinstance(items, list) or len(items) != len(rows):
        raise AIProviderError("Gemini returned the wrong number of subtitle cues.")
    result = []
    for expected, item in enumerate(items, 1):
        if not isinstance(item, dict) or str(item.get("id")) != str(expected) or not str(item.get("translation") or "").strip():
            raise AIProviderError("Gemini returned missing, empty, or reordered subtitle IDs.")
        result.append(str(item["translation"]).strip())
    return result


def translate_subtitles(
    cues: list[SubtitleCue], *, provider: str, model: str, target_language: str,
    source_language: str = "Auto-detect", api_key: str | None = None,
    base_url: str | None = None, progress: Callable[[int, int], None] | None = None,
) -> list[str]:
    """Translate imported subtitle text only; does not invoke Whisper or alter timestamps."""
    if not cues:
        raise ValueError("Import a subtitle file first.")
    target = (target_language or "Myanmar (Burmese)").strip()
    output: list[str] = []
    for start in range(0, len(cues), 20):
        batch = cues[start:start + 20]
        rows = [SubtitleCue(i + 1, x.start, x.end, x.text) for i, x in enumerate(batch)]
        if provider == "gemini":
            translated = _translate_gemini_batch(
                rows, model=model or "gemini-3.5-flash", target_language=target,
                source_language=source_language, api_key=(api_key or "").strip(),
            )
        else:
            prompt = (
                f"Translate subtitle dialogue from {source_language} into {target}. "
                "Keep meaning, names, emotional tone and short subtitle phrasing. Never summarize. "
                'Return JSON only: {"items":[{"id":1,"translation":"..."}]}. '
                "Keep every ID exactly once and in order; no explanations or timestamps.\n\n"
                + json.dumps([{"id": row.index, "text": row.text} for row in rows], ensure_ascii=False)
            )
            answer = chat_completion(
                provider, model, [{"role": "user", "content": prompt}],
                api_key=api_key, base_url=base_url, timeout=90,
            )
            data = json.loads(_strip_code_fence(answer))
            items = data.get("items") if isinstance(data, dict) else None
            if not isinstance(items, list) or len(items) != len(rows):
                raise AIProviderError("AI returned the wrong number of subtitle cues.")
            translated = []
            for expected, item in enumerate(items, 1):
                if not isinstance(item, dict) or str(item.get("id")) != str(expected) or not str(item.get("translation") or "").strip():
                    raise AIProviderError("AI returned missing, empty, or reordered subtitle IDs.")
                translated.append(str(item["translation"]).strip())
        output.extend(translated)
        if progress:
            progress(min(start + len(batch), len(cues)), len(cues))
    return output


def write_srt(path: str | Path, cues: list[SubtitleCue], translations: list[str] | None = None, *,
              bilingual: bool = False) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(format_srt(cues, translations, bilingual=bilingual), encoding="utf-8-sig")
    return target
