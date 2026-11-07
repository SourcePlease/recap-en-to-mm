"""Manual timestamped character dubbing with stable speaker-to-voice mapping.

This deliberately starts with user-reviewed speaker labels. It does not pretend to
perform automatic diarization or character identity detection.
"""
from __future__ import annotations

import asyncio
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

from .compute import run_demucs
from .encoding import run_video_encode, video_encoder_args


@dataclass(frozen=True)
class DialogueRow:
    start: str
    end: str
    speaker: str
    text: str


def timestamp_seconds(value: str) -> float:
    value = str(value or "").strip().replace(",", ".")
    parts = value.split(":")
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + float(seconds)
    return float(value)


def parse_dialogue_rows(text: str) -> list[DialogueRow]:
    rows: list[DialogueRow] = []
    for number, raw in enumerate(str(text or "").splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        fields = raw.split("\t", 3)
        if len(fields) != 4:
            raise ValueError(f"Dialogue row {number}: expected start<TAB>end<TAB>speaker<TAB>translated text.")
        start, end, speaker, dialogue = (item.strip() for item in fields)
        start_s, end_s = timestamp_seconds(start), timestamp_seconds(end)
        if start_s < 0 or end_s <= start_s:
            raise ValueError(f"Dialogue row {number}: end time must be after start time.")
        if not speaker or not dialogue:
            raise ValueError(f"Dialogue row {number}: speaker and translated text are required.")
        rows.append(DialogueRow(start, end, speaker, dialogue))
    if not rows:
        raise ValueError("No dialogue rows found. Import subtitles or enter timestamped dialogue first.")
    return rows


def parse_speaker_voices(text: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for number, raw in enumerate(str(text or "").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ValueError(f"Voice mapping line {number}: use Speaker A=my-MM-ThihaNeural.")
        speaker, voice = (part.strip() for part in line.split("=", 1))
        if not speaker or not voice:
            raise ValueError(f"Voice mapping line {number}: speaker and voice are required.")
        mapping[speaker] = voice
    return mapping


def _run(command: list[str]) -> subprocess.CompletedProcess:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError((result.stderr or result.stdout or "External command failed.")[-3500:])
    return result


def _duration(ffprobe: str, path: Path) -> float:
    result = _run([ffprobe, "-v", "error", "-show_entries", "format=duration",
                   "-of", "default=noprint_wrappers=1:nokey=1", str(path)])
    try:
        return float(result.stdout.strip())
    except ValueError as exc:
        raise RuntimeError(f"Could not read media duration: {path}") from exc


def _has_audio(ffprobe: str, path: Path) -> bool:
    result = _run([ffprobe, "-v", "error", "-select_streams", "a:0",
                   "-show_entries", "stream=index", "-of", "csv=p=0", str(path)])
    return bool(result.stdout.strip())


def _edge_tts_save(text: str, voice: str, destination: Path) -> None:
    try:
        import edge_tts
    except ImportError as exc:
        raise RuntimeError("Character Dubbing needs edge-tts. Run: pip install -U edge-tts") from exc

    async def save() -> None:
        await edge_tts.Communicate(text=text, voice=voice).save(str(destination))

    asyncio.run(save())


def render_character_dubbing(
    *,
    ffmpeg: str,
    ffprobe: str,
    source_video: Path,
    rows: list[DialogueRow],
    speaker_voices: dict[str, str],
    output_video: Path,
    source_audio_mode: str = "instrumental",
    log: Callable[[str], None] | None = None,
) -> Path:
    """Render user-reviewed dialogue rows using Edge TTS and exact cue start times.

    source_audio_mode: mute | keep | instrumental. Instrumental uses Demucs' no_vocals stem.
    """
    log = log or (lambda _message: None)
    source_video = Path(source_video).resolve()
    output_video = Path(output_video).resolve()
    if not source_video.is_file():
        raise FileNotFoundError(f"Source video not found: {source_video}")
    if source_audio_mode not in {"mute", "keep", "instrumental"}:
        raise ValueError("source_audio_mode must be mute, keep, or instrumental.")
    missing = sorted({row.speaker for row in rows if row.speaker not in speaker_voices})
    if missing:
        raise ValueError("Missing voice mapping for: " + ", ".join(missing))

    work = output_video.parent / f".{output_video.stem}_dubbing_work"
    work.mkdir(parents=True, exist_ok=True)
    duration = _duration(ffprobe, source_video)
    clips: list[tuple[Path, DialogueRow]] = []
    for index, row in enumerate(rows, 1):
        start, end = timestamp_seconds(row.start), timestamp_seconds(row.end)
        if end > duration + 0.25:
            raise ValueError(f"Dialogue row {index} ends after the source video duration.")
        clip = work / f"dialogue_{index:04d}.mp3"
        _edge_tts_save(row.text, speaker_voices[row.speaker], clip)
        if not clip.is_file() or clip.stat().st_size < 500:
            raise RuntimeError(f"TTS did not produce audio for dialogue row {index}.")
        clips.append((clip, row))
        log(f"🎙️ TTS {index}/{len(rows)} · {row.speaker} · {speaker_voices[row.speaker]}")

    source_bed: Path | None = None
    if source_audio_mode == "keep":
        if _has_audio(ffprobe, source_video):
            source_bed = source_video
        else:
            log("ℹ️ Source video has no audio stream; rendering dialogue voices only.")
    elif source_audio_mode == "instrumental":
        if not _has_audio(ffprobe, source_video):
            raise RuntimeError("Source video has no audio stream to separate.")
        separation = work / "separation"
        no_vocals = separation / "htdemucs" / source_video.stem / "no_vocals.wav"
        if not no_vocals.is_file() or no_vocals.stat().st_size < 1000:
            separation.mkdir(parents=True, exist_ok=True)
            log("🎚️ Separating source instrumental bed with Demucs…")
            run_demucs([sys.executable, "-m", "demucs", "-n", "htdemucs", "--two-stems", "vocals",
                        "-o", str(separation), str(source_video)], log=log)
        if not no_vocals.is_file():
            raise RuntimeError("Demucs did not create no_vocals.wav. Install Demucs or choose Keep/Mute source audio.")
        source_bed = no_vocals

    command = [ffmpeg, "-y", "-hide_banner", "-loglevel", "error", "-i", str(source_video)]
    for clip, _row in clips:
        command += ["-i", str(clip)]
    source_index = None
    if source_bed is not None:
        if source_bed == source_video:
            source_index = 0
        else:
            command += ["-i", str(source_bed)]
            source_index = len(clips) + 1

    graph: list[str] = []
    mix_labels: list[str] = []
    for index, (clip, row) in enumerate(clips, 1):
        start_ms = max(0, round(timestamp_seconds(row.start) * 1000))
        slot = timestamp_seconds(row.end) - timestamp_seconds(row.start)
        clip_duration = _duration(ffprobe, clip)
        tempo = max(1.0, min(1.5, clip_duration / slot))
        if clip_duration / slot > 1.5:
            log(f"⚠️ Dialogue row {index} is longer than its cue; it may be trimmed after the 1.5x speed cap.")
        label = f"dlg{index}"
        graph.append(
            f"[{index}:a]atempo={tempo:.6f},apad,atrim=duration={slot:.6f},"
            f"adelay={start_ms}|{start_ms},volume=1.0[{label}]"
        )
        mix_labels.append(f"[{label}]")
    if source_index is not None:
        graph.append(f"[{source_index}:a]volume=0.25[srcbed]")
        mix_labels.append("[srcbed]")
    graph.append("".join(mix_labels) + f"amix=inputs={len(mix_labels)}:duration=longest:normalize=0,"
                 "alimiter=limit=0.95:level=disabled[mixed]")
    def command_for_encoder(encoder: str) -> list[str]:
        return command + [
            "-filter_complex", ";".join(graph), "-map", "0:v:0", "-map", "[mixed]",
            *video_encoder_args(encoder),
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-t", f"{duration:.3f}",
            "-movflags", "+faststart", str(output_video),
        ]

    log("🎬 Rendering character-dubbed video…")
    run_video_encode(ffmpeg, command_for_encoder, output_video, log=log)
    if not output_video.is_file() or output_video.stat().st_size < 5000:
        output_video.unlink(missing_ok=True)
        raise RuntimeError("Character dubbing render did not produce a valid output video.")
    log(f"✅ Character dubbing ready: {output_video}")
    # Successful renders no longer need intermediate TTS clips or separation files.
    import shutil
    shutil.rmtree(work, ignore_errors=True)
    return output_video


def save_dubbing_project(path: Path, rows: list[DialogueRow], speaker_voices: dict[str, str]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "format": "recap-character-dubbing-v1",
        "rows": [asdict(row) for row in rows],
        "speaker_voices": speaker_voices,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def load_dubbing_project(path: Path) -> tuple[list[DialogueRow], dict[str, str]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("format") != "recap-character-dubbing-v1":
        raise ValueError("Unsupported character dubbing project format.")
    rows = [DialogueRow(**item) for item in data.get("rows", [])]
    voices = {str(key): str(value) for key, value in data.get("speaker_voices", {}).items()}
    if not rows:
        raise ValueError("The dubbing project contains no dialogue rows.")
    return rows, voices
