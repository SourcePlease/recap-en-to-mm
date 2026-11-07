from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from studio.encoding import choose_video_encoder, run_video_encode


class VideoEncodingTests(unittest.TestCase):
    def test_cpu_is_selected_when_ffmpeg_does_not_advertise_nvenc(self):
        with patch("studio.encoding.subprocess.run", return_value=Mock(returncode=0, stdout="libx264", stderr="")):
            self.assertEqual(choose_video_encoder("ffmpeg"), "libx264")

    def test_nvenc_render_failure_retries_with_cpu_and_removes_partial_file(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "render.mp4"
            calls = []

            def fake_run(command, **kwargs):
                calls.append(command)
                if "-encoders" in command:
                    return Mock(returncode=0, stdout=" V.... h264_nvenc", stderr="")
                if "color=c=black" in command:
                    return Mock(returncode=0, stdout="", stderr="")
                if "h264_nvenc" in command:
                    output.write_bytes(b"partial")
                    return Mock(returncode=1, stdout="", stderr="NVENC device unavailable")
                output.write_bytes(b"valid-output" * 1000)
                return Mock(returncode=0, stdout="", stderr="")

            messages = []
            with patch("studio.encoding.subprocess.run", side_effect=fake_run):
                used = run_video_encode(
                    "ffmpeg", lambda encoder: ["ffmpeg", "-c:v", encoder, str(output)],
                    output, log=messages.append,
                )
            self.assertEqual(used, "libx264")
            self.assertTrue(output.is_file())
            self.assertGreater(output.stat().st_size, 5000)
            render_commands = [cmd for cmd in calls if "-c:v" in cmd]
            self.assertEqual(render_commands[-1][render_commands[-1].index("-c:v") + 1], "libx264")
            self.assertTrue(any("retrying with libx264" in item for item in messages))


if __name__ == "__main__":
    unittest.main()
