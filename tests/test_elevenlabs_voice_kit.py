from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from tts_providers import ElevenLabsTTSEngine


class ElevenLabsVoiceKitTests(unittest.TestCase):
    def _engine(self, work: Path, target_language: str):
        env = {
            "ELEVENLABS_API_KEY": "test-key",
            "ELEVENLABS_VOICE_ID": "test-voice",
            "ELEVENLABS_MODEL_ID": "eleven_v4",
            "ELEVENLABS_BURMESE_VOICE_KIT": "1",
        }
        with patch.dict(os.environ, env):
            return ElevenLabsTTSEngine(
                ffmpeg="ffmpeg", work_dir=work, env_file="", log=lambda _message: None,
                target_language=target_language,
            )

    def test_burmese_request_uses_eleven_v4_language_code_and_prepared_text(self):
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp)
            engine = self._engine(work, "mm")
            response = Mock(status_code=200, content=b"mp3-data", text="")

            def fake_ffmpeg(command, **kwargs):
                Path(command[-1]).write_bytes(b"RIFF" + b"x" * 1024)
                return Mock(returncode=0)

            with patch.object(engine.requests, "post", return_value=response) as post, patch(
                "tts_providers.subprocess.run", side_effect=fake_ffmpeg
            ):
                output = engine.generate_channel99_voice("အပိုင်း 12 နည်း", "elevenlabs:default")

            payload = post.call_args.kwargs["json"]
            self.assertEqual(payload["model_id"], "eleven_v4")
            self.assertEqual(payload["language_code"], "my")
            self.assertIn("ဆယ့်နှစ်", payload["text"])
            self.assertIn("နဲ", payload["text"])
            self.assertTrue(Path(output).is_file())

    def test_non_burmese_request_does_not_apply_burmese_language_code(self):
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp)
            engine = self._engine(work, "en")
            response = Mock(status_code=200, content=b"mp3-data", text="")

            def fake_ffmpeg(command, **kwargs):
                Path(command[-1]).write_bytes(b"RIFF" + b"x" * 1024)
                return Mock(returncode=0)

            with patch.object(engine.requests, "post", return_value=response) as post, patch(
                "tts_providers.subprocess.run", side_effect=fake_ffmpeg
            ):
                engine.generate_channel99_voice("Episode 12", "elevenlabs:default")

            payload = post.call_args.kwargs["json"]
            self.assertNotIn("language_code", payload)
            self.assertEqual(payload["text"], "Episode 12")


if __name__ == "__main__":
    unittest.main()
