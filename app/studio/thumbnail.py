"""Automatic video-thumbnail generation using FFmpeg and Pillow.

This module uses local frame extraction and layout templates; it does not need
a remote image-generation API. The generated image is a design starting point,
not a guarantee that the selected frame is the most semantically relevant.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse
from typing import Iterable

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat
import requests


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
    candidates: list[Path | str] = []
    if font_path:
        candidates.append(Path(font_path))
    candidates.extend([
        Path(r"C:\Windows\Fonts\mmrtext.ttf"),
        Path(r"C:\Windows\Fonts\pyidaungsu.ttf"),
        Path(r"C:\Windows\Fonts\notosansmyanmar.ttf"),
        Path("/usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansMyanmar-Regular.ttf"),
        "arial.ttf",
    ])
    for candidate in candidates:
        try:
            return ImageFont.truetype(str(candidate), size=size)
        except OSError:
            continue
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


def candidate_frame_fraction(candidate: str | Path, sample_count: int) -> float:
    """Return the normalized timeline position represented by a sampled frame path."""
    count = max(1, min(int(sample_count), 24))
    try:
        index = int(Path(candidate).stem.rsplit("_", 1)[-1])
    except (TypeError, ValueError):
        index = 0
    index = max(0, min(index, count - 1))
    return 0.08 + (0.84 * (index + 0.5) / count)


def choose_candidate_frame(
    candidates: list[Path], selected_fraction: float, sample_count: int
) -> Path:
    """Choose the extracted candidate closest to the user's requested timeline position."""
    if not candidates:
        raise ThumbnailError("No candidate frames are available.")
    target = max(0.08, min(0.92, float(selected_fraction)))
    return min(candidates, key=lambda candidate: abs(
        candidate_frame_fraction(candidate, sample_count) - target
    ))


def sample_thumbnail_frames(
    video_path: str | Path, *, sample_count: int = 8,
    ffmpeg: str = "ffmpeg", ffprobe: str = "ffprobe",
) -> list[tuple[Image.Image, float]]:
    """Extract small preview images for the Thumbnail tab's frame picker."""
    source = Path(video_path).expanduser().resolve()
    if not source.is_file():
        raise ThumbnailError(f"Video file does not exist: {source}")
    if not shutil.which(ffmpeg) and not Path(ffmpeg).is_file():
        raise ThumbnailError(f"FFmpeg executable was not found: {ffmpeg}")
    if not shutil.which(ffprobe) and not Path(ffprobe).is_file():
        raise ThumbnailError(f"FFprobe executable was not found: {ffprobe}")
    count = max(1, min(int(sample_count), 24))
    duration = _video_duration(source, ffprobe)
    previews: list[tuple[Image.Image, float]] = []
    with tempfile.TemporaryDirectory(prefix="recap_thumbnail_preview_") as temp:
        candidates = _extract_candidate_frames(source, duration, ffmpeg, Path(temp), count)
        for candidate in candidates:
            try:
                with Image.open(candidate) as image:
                    previews.append((image.convert("RGB").copy(), candidate_frame_fraction(candidate, count)))
            except OSError:
                continue
    if not previews:
        raise ThumbnailError("No readable frame previews were extracted.")
    return previews


def _draw_thumbnail(frame: Image.Image, output_path: Path, title: str,
                    aspect: str, font_path: str | Path | None,
                    logo_path: str | Path | None, template_variant: int = 0) -> None:
    width, height = thumbnail_size(aspect)
    image = ImageOps.fit(frame.convert("RGB"), (width, height), method=Image.Resampling.LANCZOS)
    # Darken the lower portion behind the title, without obscuring the whole frame.
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    variant = int(template_variant) % 3
    for y in range(height):
        position = y / max(1, height - 1)
        if variant == 1:
            strength = (1.0 - position) ** 1.7
        elif variant == 2:
            strength = 0.72 if 0.27 <= position <= 0.76 else 0.08
        else:
            strength = position ** 1.7
        alpha = int(170 * strength)
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
    if variant == 1:
        text_y = max(margin, margin // 2)
    elif variant == 2:
        text_y = max(margin, (height - block_height) // 2)
    else:
        text_y = max(margin, height - margin - block_height)
    title_top = text_y
    for line in lines:
        draw.text(
            (margin, text_y), line, font=font, fill="white",
            stroke_width=max(2, font_size // 18), stroke_fill=(0, 0, 0, 230),
        )
        text_y += line_height
    # Accent stripe adds a clear title anchor without claiming the image is AI artwork.
    if variant == 1:
        stripe_y = min(height - margin // 2, title_top + block_height + 12)
        stripe_color = (80, 220, 190, 255)
    elif variant == 2:
        stripe_y = max(margin // 2, title_top - 16)
        stripe_color = (255, 176, 72, 255)
    else:
        stripe_y = max(margin // 2, title_top - 16)
        stripe_color = (95, 140, 255, 255)
    draw.rounded_rectangle(
        (margin, stripe_y, margin + max(52, int(width * 0.11)), stripe_y + max(5, int(height * 0.009))),
        radius=4, fill=stripe_color,
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
    selected_fraction: float | None = None,
    template_variant: int = 0,
) -> Path:
    """Select a clear frame or a user-picked timeline point, then render a JPEG thumbnail."""
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

    count = max(1, min(int(sample_count), 24))
    duration = _video_duration(source, ffprobe)
    with tempfile.TemporaryDirectory(prefix="recap_thumbnail_") as temp:
        candidates = _extract_candidate_frames(source, duration, ffmpeg, Path(temp), count)
        if selected_fraction is not None:
            best = choose_candidate_frame(candidates, selected_fraction, count)
        else:
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
                image, destination, title or source.stem, aspect, font_path, logo_path,
                template_variant=template_variant,
            )
    return destination


FAL_IMAGE_MODEL = "fal-ai/fast-sdxl"
FAL_IMAGE_SIZES = {
    "16:9": "landscape_16_9",
    "9:16": "portrait_16_9",
    "1:1": "square_hd",
}


def build_fal_thumbnail_prompt(title: str, scene_prompt: str = "", style: str = "Anime Recap") -> str:
    """Describe the background image only; Burmese typography is rendered locally afterward."""
    title = (title or "").strip()[:160]
    scene_prompt = (scene_prompt or "").strip()[:1200]
    style_hint = {
        "Anime Recap": "dramatic anime recap poster, clean focal point, cinematic lighting",
        "Isekai / Reincarnation": "fantasy portal, magical atmosphere, a sense of a new life and discovery",
        "Overpowered / Action": "dynamic action pose, powerful energy effects, high-contrast action composition",
        "Dark Fantasy / Survival": "dark fantasy environment, tense survival atmosphere, dramatic shadows",
        "Mystery / Twist": "mysterious cinematic scene, symbolic clues, atmospheric light and shadow",
        "Romance / Betrayal": "emotional anime-drama atmosphere, expressive original characters, contrasting warm and cold light",
    }.get(style, "cinematic anime recap poster")
    components = [
        "Create a high-impact YouTube anime-recap thumbnail BACKGROUND, wide clean composition, "
        "professional key art, detailed original anime-inspired illustration, strong focal subject, "
        "cinematic depth, dramatic lighting, rich but controlled colors, legible visual hierarchy.",
        f"Visual style direction: {style_hint}.",
    ]
    if title:
        components.append(f"Story/title reference for mood only: {title}.")
    if scene_prompt:
        components.append(f"User's scene description: {scene_prompt}.")
    components.append(
        "Create original characters and scenery; do not reproduce a specific existing character. "
        "Absolutely no text, letters, subtitles, typography, logos, watermarks, signatures or UI. "
        "Leave some calmer negative space for a title that will be added afterward."
    )
    return " ".join(components)


def generate_fal_thumbnail(
    output_path: str | Path,
    *,
    title: str,
    scene_prompt: str = "",
    aspect: str = "16:9",
    style: str = "Anime Recap",
    model_id: str = FAL_IMAGE_MODEL,
    api_key: str | None = None,
    font_path: str | Path | None = None,
    logo_path: str | Path | None = None,
    fal_client_module=None,
    http_get=None,
) -> Path:
    """Generate an AI background on fal.ai and render accurate local title/logo overlays.

    fal.ai inference consumes account credits and may be paid. The caller invokes this
    only when the user explicitly selects the AI mode. This function never falls back
    silently to a different remote provider.
    """
    destination = Path(output_path).expanduser().resolve()
    if destination.suffix.lower() not in {".jpg", ".jpeg"}:
        destination = destination.with_suffix(".jpg")
    thumbnail_size(aspect)
    fal_size = FAL_IMAGE_SIZES[aspect]
    model = (model_id or FAL_IMAGE_MODEL).strip()
    if not model.startswith("fal-ai/") or ".." in model or any(ch in model for ch in "\r\n"):
        raise ThumbnailError("Model ID must be a valid fal-ai/... endpoint.")
    key = (api_key or os.getenv("FAL_KEY") or "").strip()
    if not key:
        raise ThumbnailError(
            "FAL_KEY မတွေ့ပါ။ Studio ထဲမှာ fal.ai key ထည့်ပြီး Save FAL Key ကိုနှိပ်ပါ။ "
            "AI image generation may use paid fal.ai credits."
        )
    if fal_client_module is None:
        try:
            import fal_client as fal_client_module  # type: ignore[no-redef]
        except ImportError as exc:
            raise ThumbnailError(
                "fal-client is not installed. Run INSTALL_REQUIREMENTS.bat again."
            ) from exc

    prompt = build_fal_thumbnail_prompt(title, scene_prompt, style)
    arguments = {
        "prompt": prompt,
        "negative_prompt": "text, typography, letters, words, captions, logo, watermark, signature, low quality, blurry, malformed anatomy",
        "image_size": fal_size,
        "num_images": 1,
        "num_inference_steps": 25,
    }
    old_key = os.environ.get("FAL_KEY")
    os.environ["FAL_KEY"] = key
    try:
        try:
            result = fal_client_module.run(model, arguments=arguments)
        except Exception as exc:
            detail = str(exc).replace(key, "[redacted]")
            raise ThumbnailError(
                "fal.ai image generation failed. Check the FAL key, available credits, "
                f"model endpoint and connection. Details: {detail[:900]}"
            ) from exc
    finally:
        if old_key is None:
            os.environ.pop("FAL_KEY", None)
        else:
            os.environ["FAL_KEY"] = old_key

    images = result.get("images") if isinstance(result, dict) else None
    image_url = images[0].get("url") if images and isinstance(images[0], dict) else None
    parsed = urlparse(str(image_url or ""))
    if parsed.scheme != "https" or not parsed.hostname or not (
        parsed.hostname == "fal.media"
        or parsed.hostname.endswith(".fal.media")
        or parsed.hostname == "fal.ai"
        or parsed.hostname.endswith(".fal.ai")
    ):
        raise ThumbnailError("fal.ai returned an invalid image URL; no file was downloaded.")

    downloader = http_get or requests.get
    try:
        response = downloader(str(image_url), timeout=(10, 90))
        response.raise_for_status()
        data = getattr(response, "content", b"")
        if not data or len(data) > 40 * 1024 * 1024:
            raise ThumbnailError("Generated image was empty or unexpectedly large (>40 MB).")
        with Image.open(BytesIO(data)) as generated:
            frame = generated.convert("RGB")
            _draw_thumbnail(
                frame, destination, title, aspect,
                font_path=font_path, logo_path=logo_path,
            )
    except ThumbnailError:
        raise
    except Exception as exc:
        raise ThumbnailError(f"Could not download/render fal.ai image: {exc}") from exc
    return destination
