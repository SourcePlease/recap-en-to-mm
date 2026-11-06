from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from core import atempo_filter, has_audio_stream, mux_audio, render_source_audio_part


class SourceAudioTests(unittest.TestCase):
    def test_atempo_chain_supports_slow_and_fast_speeds(self):
        self.assertEqual(atempo_filter(1.0), "atempo=1.00000000")
        self.assertEqual(atempo_filter(4.0), "atempo=2.00000000,atempo=2.00000000")
        self.assertEqual(atempo_filter(0.25), "atempo=0.50000000,atempo=0.50000000")
        with self.assertRaises(ValueError):
            atempo_filter(0)

    def test_source_audio_probe_detects_audio_stream(self):
        with patch("core.subprocess.run", return_value=Mock(returncode=0, stdout="1\n", stderr="")) as run:
            self.assertTrue(has_audio_stream("ffprobe", Path("source.mp4")))
        self.assertIn("a:0", run.call_args.args[0])
        with patch("core.subprocess.run", return_value=Mock(returncode=0, stdout="", stderr="")):
            self.assertFalse(has_audio_stream("ffprobe", Path("silent.mp4")))

    def test_source_audio_part_uses_same_segment_speed_and_target_duration(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "part.wav"

            def fake_run(command, **kwargs):
                output.write_bytes(b"w" * 2048)
                return Mock(returncode=0, stdout="", stderr="")

            segment = {"video_start": 12.5, "video_end": 17.5}
            with patch("core.subprocess.run", side_effect=fake_run) as run:
                result = render_source_audio_part(
                    "ffmpeg", Path("source.mp4"), output, segment, 4.0, 1.25,
                )
            self.assertEqual(result, output)
            command = run.call_args.args[0]
            self.assertIn("12.500000", command)
            self.assertIn("5.000000", command)
            self.assertIn("atempo=1.25000000", command[command.index("-af") + 1])
            self.assertIn("atrim=duration=4.000000", command[command.index("-af") + 1])

    def test_mux_ducks_source_audio_under_narration_and_keeps_bgm_optional(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            video, voice, original, bgm = (root / name for name in ("v.mp4", "voice.wav", "source.wav", "music.mp3"))
            for path in (video, voice, original, bgm):
                path.write_bytes(b"x")
            with patch("core.subprocess.run", return_value=Mock(returncode=0, stderr="")) as run:
                mux_audio(
                    "ffmpeg", video, voice, root / "out.mp4",
                    original_audio_path=original, original_audio_volume_percent=70,
                    background_music_path=bgm, background_music_volume_percent=12,
                )
            command = run.call_args.args[0]
            graph = command[command.index("-filter_complex") + 1]
            self.assertIn("sidechaincompress", graph)
            self.assertIn("amix=inputs=3", graph)
            self.assertIn(str(original), command)
            self.assertIn(str(bgm), command)

    def test_mux_without_original_audio_remains_narration_only(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            video, voice = root / "v.mp4", root / "voice.wav"
            video.write_bytes(b"x")
            voice.write_bytes(b"x")
            with patch("core.subprocess.run", return_value=Mock(returncode=0, stderr="")) as run:
                mux_audio("ffmpeg", video, voice, root / "out.mp4")
            graph = run.call_args.args[0][run.call_args.args[0].index("-filter_complex") + 1]
            self.assertIn("amix=inputs=1", graph)
            self.assertNotIn("sidechaincompress", graph)


if __name__ == "__main__":
    unittest.main()
