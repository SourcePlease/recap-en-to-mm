from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from studio.subtitles import ffmpeg_subtitle_filter


class SubbingModeFilterTests(unittest.TestCase):
    def test_filter_escapes_windows_drive_and_uses_unicode_subtitles(self):
        with patch("studio.subtitles.Path.resolve", return_value=Path("C:/Videos/My Film/မြန်မာ.srt")):
            value = ffmpeg_subtitle_filter(Path("unused.srt"))
        self.assertIn("C\\:/Videos/My Film/မြန်မာ.srt", value)
        self.assertIn("charenc=UTF-8", value)
        self.assertIn("FontName=Myanmar Text", value)

    def test_filter_bounds_font_size_and_sanitizes_font_name(self):
        value = ffmpeg_subtitle_filter("captions.srt", font_name="Font,Name'", font_size=999)
        self.assertIn("FontName=FontName", value)
        self.assertIn("FontSize=72", value)


if __name__ == "__main__":
    unittest.main()
