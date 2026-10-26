"""Optional Azure Speech and ElevenLabs adapters implementing Recap's WAV interface."""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
from pathlib import Path
from xml.sax.saxutils import escape


class TTSProviderError(RuntimeError):
    pass


def _load_env(path: str | Path | None) -> None:
    try:
        from dotenv import load_dotenv
        if path and Path(path).is_file():
            load_dotenv(Path(path), override=False)
    except Exception:
        pass


def _safe_rate(value: str) -> str:
    return value if re.fullmatch(r"[+-]?\d{1,3}%", str(value or "")) else "+0%"


def _safe_pitch(value: str) -> str:
    return value if re.fullmatch(r"[+-]?\d{1,3}Hz", str(value or "")) else "+0Hz"


class AzureSpeechTTSEngine:
    """Azure REST TTS; requires an Azure Speech key and region in the private .env."""
    def __init__(self, *, ffmpeg: str, work_dir: Path, rate: str = "+0%", pitch: str = "+0Hz",
                 env_file: str = "", log=print, target_language: str = "mm") -> None:
        import requests
        _load_env(env_file)
        self.requests = requests
        self.ffmpeg = ffmpeg
        self.work_dir = Path(work_dir)
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.key = os.getenv("AZURE_SPEECH_KEY", "").strip()
        self.region = os.getenv("AZURE_SPEECH_REGION", "").strip()
        if not self.key or not self.region:
            raise TTSProviderError("Set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION in .env to use Azure TTS.")
        self.rate, self.pitch, self.log = _safe_rate(rate), _safe_pitch(pitch), log
        self.counter = 0
        self.target_language = target_language

    def generate_channel99_voice(self, text: str, voice: str) -> str:
        clean = re.sub(r"\s+", " ", str(text or "")).strip()
        if not clean:
            raise TTSProviderError("Azure TTS received empty narration text.")
        voice_id = str(voice or "").removeprefix("azure:")
        language = "-".join(voice_id.split("-")[:2]) if voice_id.count("-") >= 2 else "en-US"
        ssml = (
            f'<speak version="1.0" xml:lang="{escape(language)}" xmlns="http://www.w3.org/2001/10/synthesis">'
            f'<voice name="{escape(voice_id)}"><prosody rate="{self.rate}" pitch="{self.pitch}">'
            f'{escape(clean)}</prosody></voice></speak>'
        )
        url = f"https://{self.region}.tts.speech.microsoft.com/cognitiveservices/v1"
        response = self.requests.post(url, headers={
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
            "User-Agent": "RecapStudio",
        }, data=ssml.encode("utf-8"), timeout=90)
        if response.status_code >= 400:
            raise TTSProviderError(f"Azure Speech TTS failed ({response.status_code}): {response.text[:400]}")
        self.counter += 1
        digest = hashlib.sha1(clean.encode("utf-8")).hexdigest()[:10]
        target = self.work_dir / f"azure_{self.counter:05d}_{digest}.wav"
        target.write_bytes(response.content)
        if not target.is_file() or target.stat().st_size < 1000 or target.read_bytes()[:4] != b"RIFF":
            target.unlink(missing_ok=True)
            raise TTSProviderError("Azure Speech returned an invalid WAV file.")
        return str(target)

    def fingerprint(self, voice: str) -> str:
        return f"{voice}|azure-speech-v1|{self.rate}|{self.pitch}|{self.target_language}"


class ElevenLabsTTSEngine:
    """ElevenLabs multilingual TTS; voice ID and API key stay in .env."""
    def __init__(self, *, ffmpeg: str, work_dir: Path, rate: str = "+0%", pitch: str = "+0Hz",
                 env_file: str = "", log=print, target_language: str = "mm") -> None:
        import requests
        _load_env(env_file)
        self.requests = requests
        self.ffmpeg = ffmpeg
        self.work_dir = Path(work_dir)
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.key = os.getenv("ELEVENLABS_API_KEY", "").strip()
        self.voice_id = os.getenv("ELEVENLABS_VOICE_ID", "").strip()
        if not self.key or not self.voice_id:
            raise TTSProviderError("Set ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID in .env to use ElevenLabs.")
        self.rate, self.pitch, self.log = _safe_rate(rate), _safe_pitch(pitch), log
        self.counter = 0
        self.target_language = target_language

    def generate_channel99_voice(self, text: str, voice: str = "elevenlabs:default") -> str:
        clean = re.sub(r"\s+", " ", str(text or "")).strip()
        if not clean:
            raise TTSProviderError("ElevenLabs TTS received empty narration text.")
        selected = str(voice or "").removeprefix("elevenlabs:")
        if selected in {"", "default"}:
            selected = self.voice_id
        model = os.getenv("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2").strip()
        response = self.requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{selected}",
            headers={"xi-api-key": self.key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
            json={"text": clean, "model_id": model},
            params={"output_format": "mp3_44100_128"}, timeout=120,
        )
        if response.status_code >= 400:
            raise TTSProviderError(f"ElevenLabs TTS failed ({response.status_code}): {response.text[:400]}")
        self.counter += 1
        digest = hashlib.sha1(clean.encode("utf-8")).hexdigest()[:10]
        mp3 = self.work_dir / f"elevenlabs_{self.counter:05d}_{digest}.mp3"
        wav = mp3.with_suffix(".wav")
        mp3.write_bytes(response.content)
        try:
            subprocess.run(
                [self.ffmpeg, "-y", "-v", "error", "-i", str(mp3), "-ac", "1", "-ar", "24000",
                 "-c:a", "pcm_s16le", str(wav)],
                check=True, capture_output=True, text=True,
            )
        except Exception as exc:
            wav.unlink(missing_ok=True)
            raise TTSProviderError(f"Could not convert ElevenLabs audio to WAV: {exc}") from exc
        if not wav.is_file() or wav.stat().st_size < 1000:
            raise TTSProviderError("ElevenLabs audio conversion produced an empty WAV.")
        return str(wav)

    def fingerprint(self, voice: str) -> str:
        return f"{voice}|elevenlabs-v1|{self.voice_id}|{os.getenv('ELEVENLABS_MODEL_ID', 'eleven_multilingual_v2')}|{self.target_language}"
