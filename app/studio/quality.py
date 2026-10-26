"""Preflight and output-quality checks for Recap Studio.

Checks are deliberately advisory: they report objective file/stream conditions
without claiming to judge translation quality or subtitle semantic accuracy.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any


def _binary_available(value: str | Path | None) -> bool:
    text = str(value or "").strip()
    return bool(text and (Path(text).is_file() or shutil.which(text)))


def _read_env(path: str | Path | None) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path:
        return env
    source = Path(path).expanduser()
    if not source.is_file():
        return env
    try:
        from dotenv import dotenv_values
        return {str(k): str(v or "") for k, v in dotenv_values(source).items() if k}
    except Exception:
        pass
    try:
        for line in source.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            env[key.strip().removeprefix("export ").strip()] = value.strip().strip("'\"")
    except OSError:
        return {}
    return env


def preflight_check(
    source: str | Path,
    *,
    ffmpeg: str | Path,
    ffprobe: str | Path,
    env_path: str | Path | None = None,
    target_language: str = "mm",
    provider: str | None = None,
    output_dir: str | Path | None = None,
    minimum_free_gb: float = 3.0,
) -> dict[str, Any]:
    """Return a checklist; no API calls are made and no secrets are returned."""
    source_path = Path(source).expanduser() if str(source or "").strip() else None
    checks: list[dict[str, str]] = []

    def add(name: str, status: str, detail: str) -> None:
        checks.append({"name": name, "status": status, "detail": detail})

    add("Source video", "PASS" if source_path and source_path.is_file() else "FAIL",
        str(source_path) if source_path and source_path.is_file() else "Choose an existing local video.")
    add("FFmpeg", "PASS" if _binary_available(ffmpeg) else "FAIL",
        str(ffmpeg) if _binary_available(ffmpeg) else "FFmpeg executable not found.")
    add("FFprobe", "PASS" if _binary_available(ffprobe) else "FAIL",
        str(ffprobe) if _binary_available(ffprobe) else "FFprobe executable not found.")

    if source_path and source_path.is_file() and _binary_available(ffprobe):
        try:
            result = subprocess.run(
                [str(ffprobe), "-v", "error", "-show_entries", "format=duration:stream=codec_type",
                 "-of", "json", str(source_path)],
                capture_output=True, text=True, timeout=30, check=True,
            )
            metadata = json.loads(result.stdout or "{}")
            duration = float((metadata.get("format") or {}).get("duration") or 0)
            streams = [str(x.get("codec_type")) for x in metadata.get("streams", [])]
            good = duration > 0 and "video" in streams
            add("Source media probe", "PASS" if good else "FAIL",
                f"Duration {duration / 60:.1f} min; streams: {', '.join(streams) or 'none'}.")
            if "audio" not in streams:
                add("Source audio", "WARN", "No audio stream detected; transcription may fail.")
        except Exception as exc:
            add("Source media probe", "FAIL", f"Could not read media metadata: {str(exc)[:240]}")

    env = _read_env(env_path)
    chosen_provider = str(provider or env.get("RECAP_AI_PROVIDER") or "gemini").lower()
    if chosen_provider in {"ollama", "local"}:
        add("AI credentials", "WARN", "Local provider selected; ensure Ollama is running and the model is installed.")
    elif chosen_provider in {"groq", "openrouter"}:
        variable = "GROQ_API_KEY" if chosen_provider == "groq" else "OPENROUTER_API_KEY"
        add("AI credentials", "PASS" if (env.get(variable) or os.getenv(variable)) else "WARN",
            f"{variable} is configured." if (env.get(variable) or os.getenv(variable)) else f"{variable} is not present in the selected .env or environment.")
    else:
        configured = bool(env.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY"))
        add("AI credentials", "PASS" if configured else "WARN",
            "Gemini key is present (quota is not tested)." if configured else "GEMINI_API_KEY not found; verify selected provider and .env.")
    add("Target language", "PASS" if target_language else "WARN",
        f"Selected target: {target_language or 'not set'}; TTS support still depends on the chosen voice/provider.")

    folder = Path(output_dir).expanduser() if str(output_dir or "").strip() else (
        source_path.parent if source_path else Path.cwd())
    try:
        existing = folder if folder.exists() else folder.parent
        while not existing.exists() and existing != existing.parent:
            existing = existing.parent
        free_gb = shutil.disk_usage(existing).free / (1024 ** 3)
        status = "PASS" if free_gb >= minimum_free_gb else "WARN"
        add("Disk space", status, f"{free_gb:.1f} GB free at {existing}; long videos may need several GB.")
    except OSError as exc:
        add("Disk space", "WARN", f"Unable to read free space: {exc}")

    failures = sum(item["status"] == "FAIL" for item in checks)
    warnings = sum(item["status"] == "WARN" for item in checks)
    return {
        "kind": "preflight",
        "source": str(source_path) if source_path else "",
        "checks": checks,
        "pass": failures == 0,
        "failures": failures,
        "warnings": warnings,
    }


def inspect_output_quality(
    video_path: str | Path,
    *,
    ffprobe: str | Path = "ffprobe",
    subtitle_path: str | Path | None = None,
    thumbnail_path: str | Path | None = None,
) -> dict[str, Any]:
    """Check output file, stream metadata, duration, optional SRT and thumbnail."""
    path = Path(video_path).expanduser()
    checks: list[dict[str, str]] = []

    def add(name: str, status: str, detail: str) -> None:
        checks.append({"name": name, "status": status, "detail": detail})

    if not path.is_file() or path.stat().st_size <= 1024:
        add("Output file", "FAIL", "Output video is missing or unexpectedly small.")
        metadata: dict[str, Any] = {}
    else:
        add("Output file", "PASS", f"{path.stat().st_size / (1024 ** 2):.1f} MiB")
        metadata = {}
        try:
            result = subprocess.run(
                [str(ffprobe), "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height",
                 "-of", "json", str(path)],
                capture_output=True, text=True, timeout=60, check=True,
            )
            metadata = json.loads(result.stdout or "{}")
            streams = metadata.get("streams") or []
            kinds = [str(x.get("codec_type")) for x in streams]
            duration = float((metadata.get("format") or {}).get("duration") or 0)
            add("Video stream", "PASS" if "video" in kinds else "FAIL",
                "Video stream detected." if "video" in kinds else "No video stream found.")
            add("Audio stream", "PASS" if "audio" in kinds else "FAIL",
                "Audio stream detected." if "audio" in kinds else "No audio stream found.")
            add("Duration", "PASS" if duration > 0 else "FAIL", f"{duration:.2f} seconds.")
            video_stream = next((x for x in streams if x.get("codec_type") == "video"), {})
            if video_stream.get("width") and video_stream.get("height"):
                add("Resolution", "PASS", f"{video_stream['width']} × {video_stream['height']}")
        except Exception as exc:
            add("FFprobe metadata", "FAIL", f"Could not inspect output: {str(exc)[:240]}")

    if subtitle_path:
        sp = Path(subtitle_path)
        add("Subtitle file", "PASS" if sp.is_file() and sp.stat().st_size > 0 else "WARN",
            str(sp) if sp.is_file() else "Expected subtitle file was not found.")
    if thumbnail_path:
        tp = Path(thumbnail_path)
        add("Thumbnail", "PASS" if tp.is_file() and tp.stat().st_size > 0 else "WARN",
            str(tp) if tp.is_file() else "Expected thumbnail was not found.")
    failures = sum(item["status"] == "FAIL" for item in checks)
    warnings = sum(item["status"] == "WARN" for item in checks)
    return {
        "kind": "output-quality",
        "video": str(path),
        "size_bytes": path.stat().st_size if path.is_file() else 0,
        "metadata": metadata,
        "checks": checks,
        "pass": failures == 0,
        "failures": failures,
        "warnings": warnings,
    }


def write_quality_report(path: str | Path, report: dict[str, Any]) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, destination)
    return destination


def directory_size(path: str | Path, *, max_files: int = 100_000) -> tuple[int, int, bool]:
    """Measure a directory without following symlinks; returns bytes, files, truncated."""
    root = Path(path)
    total = count = 0
    if not root.is_dir():
        return 0, 0, False
    truncated = False
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = [name for name in dirs if name not in {".git", ".venv", "venv", "node_modules"}]
        for name in files:
            count += 1
            if count > max_files:
                truncated = True
                return total, count - 1, truncated
            try:
                file_path = Path(current) / name
                if not file_path.is_symlink():
                    total += file_path.stat().st_size
            except OSError:
                continue
    return total, count, truncated


def scan_storage(root: str | Path) -> list[dict[str, Any]]:
    base = Path(root).expanduser().resolve()
    candidates = [base / "jobs", base / "Downloads", base / "logs", base / "recap_runtime"]
    results = []
    for path in candidates:
        if path.exists():
            size, count, truncated = directory_size(path)
            results.append({"path": str(path), "bytes": size, "files": count, "truncated": truncated})
    return results


def cleanup_safe_cache(root: str | Path) -> list[str]:
    """Delete disposable Python bytecode and preview renders only; never touch jobs or media."""
    base = Path(root).expanduser().resolve()
    removed: list[str] = []
    for parent in (base / "app", base / "recap_runtime", base / "tests"):
        if not parent.is_dir():
            continue
        for current, dirs, _files in os.walk(parent, topdown=True, followlinks=False):
            dirs[:] = [name for name in dirs if name != ".git"]
            if "__pycache__" in dirs:
                target = Path(current) / "__pycache__"
                try:
                    shutil.rmtree(target)
                    removed.append(str(target))
                except OSError:
                    pass
                dirs.remove("__pycache__")
    for target in (base / "logs" / "subtitle_preview", base / "logs" / "preview"):
        if target.is_dir():
            try:
                shutil.rmtree(target)
                removed.append(str(target))
            except OSError:
                pass
    return removed
