"""Automatic video-thumbnail generation using FFmpeg and Pillow.

This module uses local frame extraction and layout templates; it does not need
a remote image-generation API. The generated image is a design starting point,
not a guarantee that the selected frame is the most semantically relevant.
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat


ASPECT_SIZES = {
    "16:9": (1280, 720),
    "9:16": (720, 1280),
    "1:1": (1080, 1080),
}


class ThumbnailError(RuntimeError):
    """A user-facing thumbnail generation failure."""


def thumbnail_size(aspect: str = "16:9") -> tuple[int, int]:
    try:
        return ASPECT_SIZES[aspect]
    except KeyError as exc:
        raise ValueError(f"Unsupported thumbnail aspect ratio: {aspect}") from exc


def _run(command: list[str]) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(command, capture_output=True, text=True, check=True)
    except FileNotFoundError as exc:
        raise ThumbnailError(
            "FFmpeg/FFprobe was not found. Install it or set the executable path."
        ) from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "unknown FFmpeg error").strip()
        raise ThumbnailError(detail[-1200:]) from exc


def _video_duration(video_path: Path, ffprobe: str) -> float:
    result = _run([
        ffprobe, "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(video_path),
    ])
    try:
        duration = float(result.stdout.strip())
    except (TypeError, ValueError) as exc:
        raise ThumbnailError("Could not read the video duration.") from exc
    if duration <= 0:
        raise ThumbnailError("The selected video has no usable duration.")
    return duration


def _frame_score(image: Image.Image) -> float:
    small = image.convert("L").resize((160, 90))
    contrast = ImageStat.Stat(small).stddev[0]
    edges = small.filter(ImageFilter.FIND_EDGES)
    edge_detail = ImageStat.Stat(edges).mean[0]
    return float(contrast + edge_detail * 0.22)


def _wrap_title(text: str, draw: ImageDraw.ImageDraw, font: ImageFont.ImageFont,
                max_width: int, max_lines: int = 4) -> list[str]:
    words = (text or "").split()
    if not words:
        return []
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if current and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while last and draw.textbbox((0, 0), last + "…", font=font)[2] > max_width:
            last = last[:-1]
        lines[-1] = last.rstrip() + "…"
    return lines


def _load_font(font_path: str | Path | None, size: int) -> ImageFont.ImageFont:
    if font_path:
        try:
            return ImageFont.truetype(str(font_path), size=size)
        except OSError:
            pass
    try:
        return ImageFont.truetype("arial.ttf", size=size)
    except OSError:
        return ImageFont.load_default()


def _extract_candidate_frames(video_path: Path, duration: float, ffmpeg: str,
                              temp_dir: Path, sample_count: int) -> list[Path]:
    count = max(1, min(int(sample_count), 24))
    # Skip the very first and last frames, which are often fades or title cards.
    fractions = [0.08 + (0.84 * (i + 0.5) / count) for i in range(count)]
    candidates: list[Path] = []
    for index, fraction in enumerate(fractions):
        timestamp = min(max(0.0, duration * fraction), max(0.0, duration - 0.1))
        frame_path = temp_dir / f"frame_{index:02d}.jpg"
        try:
            _run([
                ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
                "-ss", f"{timestamp:.3f}", "-i", str(video_path),
                "-frames:v", "1", "-vf", "scale=480:-2", "-q:v", "3",
                str(frame_path),
            ])
        except ThumbnailError:
            continue
        if frame_path.is_file() and frame_path.stat().st_size > 0:
            candidates.append(frame_path)
    if not candidates:
        raise ThumbnailError("FFmpeg could not extract any frames from this video.")
    return candidates


def _draw_thumbnail(frame: Image.Image, output_path: Path, title: str,
                    aspect: str, font_path: str | Path | None,
                    logo_path: str | Path | None) -> None:
    width, height = thumbnail_size(aspect)
    image = ImageOps.fit(frame.convert("RGB"), (width, height), method=Image.Resampling.LANCZOS)
    # Darken the lower portion behind the title, without obscuring the whole frame.
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    for y in range(height):
        alpha = int(170 * (y / max(1, height - 1)) ** 1.7)
        overlay_draw.line((0, y, width, y), fill=(0, 0, 0, alpha))
    image = Image.alpha_composite(image.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(image)
    margin = max(28, int(width * 0.055))
    font_size = max(24, int(min(width, height) * (0.065 if aspect == "9:16" else 0.072)))
    font = _load_font(font_path, font_size)
    lines = _wrap_title(title, draw, font, width - margin * 2, max_lines=5 if aspect == "9:16" else 3)
    line_sizes = [draw.textbbox((0, 0), line, font=font, stroke_width=max(1, font_size // 18)) for line in lines]
    line_height = max(font_size + 8, max((box[3] - box[1] for box in line_sizes), default=font_size) + 8)
    block_height = line_height * len(lines)
    text_y = max(margin, height - margin - block_height)
    for line in lines:
        draw.text(
            (margin, text_y), line, font=font, fill="white",
            stroke_width=max(2, font_size // 18), stroke_fill=(0, 0, 0, 230),
        )
        text_y += line_height
    # Accent stripe adds a clear title anchor without claiming the image is AI artwork.
    stripe_y = max(margin // 2, height - margin - block_height - 16)
    draw.rounded_rectangle(
        (margin, stripe_y, margin + max(52, int(width * 0.11)), stripe_y + max(5, int(height * 0.009))),
        radius=4, fill=(95, 140, 255, 255),
    )
    if logo_path:
        logo_file = Path(logo_path)
        if logo_file.is_file():
            try:
                logo = Image.open(logo_file).convert("RGBA")
                logo.thumbnail((int(width * 0.19), int(height * 0.14)), Image.Resampling.LANCZOS)
                image.alpha_composite(logo, (width - margin - logo.width, margin))
            except OSError:
                pass
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(output_path, quality=95, optimize=True)


def generate_thumbnail(
    video_path: str | Path,
    output_path: str | Path | None = None,
    *,
    title: str | None = None,
    aspect: str = "16:9",
    sample_count: int = 8,
    ffmpeg: str = "ffmpeg",
    ffprobe: str = "ffprobe",
    font_path: str | Path | None = None,
    logo_path: str | Path | None = None,
) -> Path:
    """Select a clear frame, apply a title template, and save a JPEG thumbnail."""
    source = Path(video_path).expanduser().resolve()
    if not source.is_file():
        raise ThumbnailError(f"Video file does not exist: {source}")
    thumbnail_size(aspect)  # Validate the requested output size before running tools.
    destination = (
        Path(output_path).expanduser().resolve()
        if output_path else source.with_name(f"{source.stem}_thumbnail.jpg")
    )
    if destination.suffix.lower() not in {".jpg", ".jpeg"}:
        destination = destination.with_suffix(".jpg")
    if not shutil.which(ffmpeg) and not Path(ffmpeg).is_file():
        raise ThumbnailError(f"FFmpeg executable was not found: {ffmpeg}")
    if not shutil.which(ffprobe) and not Path(ffprobe).is_file():
        raise ThumbnailError(f"FFprobe executable was not found: {ffprobe}")

    duration = _video_duration(source, ffprobe)
    with tempfile.TemporaryDirectory(prefix="recap_thumbnail_") as temp:
        candidates = _extract_candidate_frames(source, duration, ffmpeg, Path(temp), sample_count)
        ranked: list[tuple[float, Path]] = []
        for candidate in candidates:
            try:
                with Image.open(candidate) as image:
                    ranked.append((_frame_score(image), candidate))
            except OSError:
                continue
        if not ranked:
            raise ThumbnailError("Extracted frames could not be read.")
        best = max(ranked, key=lambda item: item[0])[1]
        with Image.open(best) as image:
            _draw_thumbnail(
                image, destination, title or source.stem, aspect, font_path, logo_path
            )
    return destination
