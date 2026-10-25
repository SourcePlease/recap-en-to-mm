"""Media downloading helpers built on yt-dlp.

Only public URLs and content the user is authorized to access should be used.
Site support changes over time; a successful extractor probe is the best
available runtime signal, not a guarantee that every URL will work.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse


VIDEO_EXTENSIONS = {".mp4", ".mkv", ".mov", ".webm", ".avi", ".m4v", ".ts"}
ProgressHook = Callable[[dict[str, Any]], None]


class DownloadError(RuntimeError):
    """A user-facing download failure."""


@dataclass(frozen=True)
class DownloadOptions:
    output_dir: Path
    quality_height: int | None = None
    audio_only: bool = False
    playlist: bool = False
    subtitles: bool = False
    subtitle_languages: tuple[str, ...] = ("en", "my")
    cookies_file: Path | None = None
    write_info_json: bool = True
    write_thumbnail: bool = True
    archive_file: Path | None = None


@dataclass(frozen=True)
class DownloadResult:
    title: str
    files: tuple[Path, ...]
    video_path: Path | None
    metadata: dict[str, Any]


def validate_http_url(url: str) -> str:
    """Validate a web URL before passing it to a third-party extractor."""
    value = (url or "").strip()
    parsed = urlparse(value)
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.hostname:
        raise DownloadError("Please enter a complete http:// or https:// URL.")
    if any(ch in value for ch in ("\r", "\n", "\x00")):
        raise DownloadError("The URL contains invalid control characters.")
    return value


def _format_selector(options: DownloadOptions) -> str:
    if options.audio_only:
        return "bestaudio/best"
    if options.quality_height:
        height = max(144, min(int(options.quality_height), 4320))
        return (
            f"bestvideo[height<={height}]+bestaudio/"
            f"best[height<={height}]/best"
        )
    return "bestvideo*+bestaudio/best"


def build_ytdlp_options(
    options: DownloadOptions,
    progress_hook: ProgressHook | None = None,
) -> dict[str, Any]:
    output_dir = Path(options.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    config: dict[str, Any] = {
        "format": _format_selector(options),
        "outtmpl": str(output_dir / "%(title).160B [%(id)s].%(ext)s"),
        "paths": {"home": str(output_dir)},
        "noplaylist": not options.playlist,
        "continuedl": True,
        "retries": 3,
        "fragment_retries": 3,
        "windowsfilenames": os.name == "nt",
        "quiet": True,
        "no_warnings": False,
        "noprogress": True,
        "ignoreerrors": False,
        "merge_output_format": "mp4",
        "writethumbnail": bool(options.write_thumbnail and not options.audio_only),
        "writeinfojson": bool(options.write_info_json),
    }
    if options.subtitles and not options.audio_only:
        config["writesubtitles"] = True
        config["writeautomaticsub"] = True
        config["subtitleslangs"] = list(options.subtitle_languages)
    if options.cookies_file:
        cookie_path = Path(options.cookies_file).expanduser().resolve()
        if not cookie_path.is_file():
            raise DownloadError(f"Cookies file was not found: {cookie_path}")
        config["cookiefile"] = str(cookie_path)
    if options.archive_file:
        archive_path = Path(options.archive_file).expanduser().resolve()
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        config["download_archive"] = str(archive_path)
    if options.audio_only:
        config["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    if progress_hook:
        config["progress_hooks"] = [progress_hook]
    return config


def _flatten_entries(info: dict[str, Any]) -> list[dict[str, Any]]:
    entries = info.get("entries")
    if entries:
        return [entry for entry in entries if isinstance(entry, dict)]
    return [info]


def _existing_output_paths(info: dict[str, Any]) -> list[Path]:
    found: list[Path] = []
    for entry in _flatten_entries(info):
        candidates: list[Any] = [
            entry.get("filepath"),
            entry.get("_filename"),
        ]
        requested = entry.get("requested_downloads") or []
        for item in requested:
            if isinstance(item, dict):
                candidates.extend((item.get("filepath"), item.get("_filename")))
        for value in candidates:
            if value:
                candidate = Path(str(value))
                if candidate.is_file() and candidate not in found:
                    found.append(candidate)
    return found


def inspect_url(url: str, *, ytdlp_module: Any | None = None) -> dict[str, Any]:
    """Read basic metadata without downloading the media."""
    safe_url = validate_http_url(url)
    if ytdlp_module is None:
        try:
            import yt_dlp as ytdlp_module  # type: ignore[no-redef]
        except ImportError as exc:
            raise DownloadError(
                "yt-dlp is not installed. Run INSTALL_REQUIREMENTS.bat again."
            ) from exc
    try:
        with ytdlp_module.YoutubeDL({"quiet": True, "no_warnings": True, "noplaylist": True}) as ydl:
            data = ydl.extract_info(safe_url, download=False)
    except Exception as exc:
        raise DownloadError(f"Could not read this URL: {exc}") from exc
    if not isinstance(data, dict):
        raise DownloadError("The URL did not return readable media metadata.")
    return {
        "title": str(data.get("title") or data.get("id") or "Downloaded media"),
        "extractor": str(data.get("extractor_key") or data.get("extractor") or "unknown"),
        "duration": data.get("duration"),
        "thumbnail": data.get("thumbnail"),
        "formats": data.get("formats") or [],
        "is_playlist": bool(data.get("_type") == "playlist" or data.get("entries")),
    }


def download_media(
    url: str,
    options: DownloadOptions,
    progress_hook: ProgressHook | None = None,
    *,
    ytdlp_module: Any | None = None,
) -> DownloadResult:
    """Download a URL and return paths that yt-dlp reports as complete."""
    safe_url = validate_http_url(url)
    if ytdlp_module is None:
        try:
            import yt_dlp as ytdlp_module  # type: ignore[no-redef]
        except ImportError as exc:
            raise DownloadError(
                "yt-dlp is not installed. Run INSTALL_REQUIREMENTS.bat again."
            ) from exc

    output_dir = Path(options.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    hooks = [progress_hook] if progress_hook else []
    config = build_ytdlp_options(options, hooks[0] if hooks else None)
    try:
        with ytdlp_module.YoutubeDL(config) as ydl:
            info = ydl.extract_info(safe_url, download=True)
    except Exception as exc:
        raise DownloadError(
            "Download failed. The site may have changed, require a permitted "
            "sign-in, or not be supported by the installed extractor. "
            f"Details: {exc}"
        ) from exc
    if not isinstance(info, dict):
        raise DownloadError("The downloader returned no media metadata.")

    paths = _existing_output_paths(info)
    if not paths:
        # Some extractors return only an ID/metadata after post-processing.
        # Restrict this fallback to media files modified during the current job.
        import time
        cutoff = time.time() - 5
        paths = sorted(
            (
                path for path in output_dir.iterdir()
                if path.is_file()
                and path.suffix.lower() in (VIDEO_EXTENSIONS | {".mp3", ".m4a", ".opus", ".wav"})
                and path.stat().st_mtime >= cutoff
            ),
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )
    paths = list(dict.fromkeys(path.resolve() for path in paths if path.is_file()))
    video_path = next(
        (path for path in paths if path.suffix.lower() in VIDEO_EXTENSIONS),
        None,
    )
    if not paths:
        raise DownloadError(
            "The extractor finished but did not report an output file. "
            "Check the download folder and run log."
        )
    return DownloadResult(
        title=str(info.get("title") or info.get("id") or "Downloaded media"),
        files=tuple(paths),
        video_path=video_path,
        metadata={
            "extractor": info.get("extractor_key") or info.get("extractor"),
            "id": info.get("id"),
            "webpage_url": info.get("webpage_url") or safe_url,
            "duration": info.get("duration"),
        },
    )
