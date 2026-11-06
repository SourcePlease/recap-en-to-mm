from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from core import ffmpeg_encoder_works


class EncoderProbeTests(unittest.TestCase):
    def test_nvenc_smoke_test_passes_when_driver_is_usable(self):
        with patch("core.subprocess.run", return_value=Mock(returncode=0)) as run:
            self.assertTrue(ffmpeg_encoder_works("ffmpeg", "h264_nvenc"))
        self.assertIn("h264_nvenc", run.call_args.args[0])

    def test_nvenc_smoke_test_fails_safely_when_driver_is_missing(self):
        with patch("core.subprocess.run", return_value=Mock(returncode=1)):
            self.assertFalse(ffmpeg_encoder_works("ffmpeg", "h264_nvenc"))

    def test_cpu_encoder_does_not_need_a_smoke_test(self):
        with patch("core.subprocess.run") as run:
            self.assertTrue(ffmpeg_encoder_works("ffmpeg", "libx264"))
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
