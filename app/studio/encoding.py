"""GPU-first FFmpeg video encoding with a reliable libx264 fallback."""
from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Callable


def video_encoder_args(encoder: str) -> list[str]:
    """Return conservative H.264 settings for the selected hardware/software encoder."""
    if encoder == "h264_nvenc":
        return ["-c:v", "h264_nvenc", "-preset", "p5", "-rc", "vbr", "-cq", "21", "-b:v", "0"]
    return ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20"]


def choose_video_encoder(ffmpeg: str, log: Callable[[str], None] | None = None) -> str:
    """Use NVENC only after encoder discovery and a real one-frame smoke test."""
    emit = log or (lambda _message: None)
    try:
        listed = subprocess.run(
            [ffmpeg, "-hide_banner", "-encoders"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20,
        )
        if listed.returncode == 0 and "h264_nvenc" in (listed.stdout or "") + (listed.stderr or ""):
            smoke = subprocess.run(
                [
                    ffmpeg, "-hide_banner", "-loglevel", "error",
                    "-f", "lavfi", "-i", "color=c=black:s=64x64:r=1:d=0.1",
                    "-frames:v", "1", "-an", "-c:v", "h264_nvenc", "-f", "null", "-",
                ],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20,
            )
            if smoke.returncode == 0:
                emit("⚡ Video encoder: NVIDIA NVENC")
                return "h264_nvenc"
            detail = (smoke.stderr or smoke.stdout or "NVENC smoke test failed").strip()
            emit(f"⚠️ NVENC is listed but not usable ({detail[-500:]}); using libx264 CPU.")
        else:
            emit("🖥️ NVENC unavailable; using libx264 CPU.")
    except (OSError, subprocess.SubprocessError) as exc:
        emit(f"⚠️ Could not probe NVENC ({exc}); using libx264 CPU.")
    return "libx264"


def run_video_encode(
    ffmpeg: str,
    command_for_encoder: Callable[[str], list[str]],
    output: str | Path,
    *,
    log: Callable[[str], None] | None = None,
    min_output_bytes: int = 5000,
) -> str:
    """Run with usable NVENC first, retry once with CPU on hardware failure.

    A partial NVENC file is removed before retry. The function returns the encoder
    actually used and raises a concise error if the CPU render also fails.
    """
    emit = log or (lambda _message: None)
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    preferred = choose_video_encoder(ffmpeg, emit)
    candidates = [preferred, "libx264"] if preferred == "h264_nvenc" else ["libx264"]
    last_error = ""
    for index, encoder in enumerate(candidates):
        output_path.unlink(missing_ok=True)
        try:
            result = subprocess.run(
                command_for_encoder(encoder),
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
            if result.returncode == 0:
                last_error = "FFmpeg did not create a valid output file."
            else:
                last_error = (
                    result.stderr or result.stdout
                    or f"FFmpeg exited with status {result.returncode}"
                )[-3500:]
            valid = (
                result.returncode == 0
                and output_path.is_file()
                and output_path.stat().st_size >= int(min_output_bytes)
            )
            if valid:
                emit(f"✅ Video render completed with {encoder}.")
                return encoder
        except OSError as exc:
            last_error = str(exc)
        output_path.unlink(missing_ok=True)
        if encoder == "h264_nvenc" and index + 1 < len(candidates):
            emit(f"⚠️ NVENC render failed; retrying with libx264 CPU. {last_error[-500:]}")
            continue
        break
    raise RuntimeError("FFmpeg video render failed: " + (last_error or "No valid output was created."))
