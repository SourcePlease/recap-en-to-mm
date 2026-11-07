from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from studio.dubbing import (
    DialogueRow, load_dubbing_project, parse_dialogue_rows, parse_speaker_voices,
    render_character_dubbing, save_dubbing_project,
)


class CharacterDubbingModelTests(unittest.TestCase):
    def test_parse_timestamped_dialogue_rows(self):
        rows = parse_dialogue_rows(
            "00:00:01,000\t00:00:03,500\tSpeaker A\tမင်္ဂလာပါ\n"
            "00:00:04.000\t00:00:06.000\tSpeaker B\tနေကောင်းလား"
        )
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], DialogueRow("00:00:01,000", "00:00:03,500", "Speaker A", "မင်္ဂလာပါ"))

    def test_invalid_rows_are_rejected(self):
        with self.assertRaises(ValueError):
            parse_dialogue_rows("00:00:03,000\t00:00:01,000\tSpeaker A\tစာ")
        with self.assertRaises(ValueError):
            parse_dialogue_rows("bad row")

    def test_voice_mapping_is_stable_and_validated(self):
        mapping = parse_speaker_voices("Speaker A=my-MM-ThihaNeural\nSpeaker B=my-MM-NilarNeural")
        self.assertEqual(mapping["Speaker A"], "my-MM-ThihaNeural")
        with self.assertRaises(ValueError):
            parse_speaker_voices("Speaker A")

    def test_project_save_and_load_round_trip(self):
        rows = [DialogueRow("00:00:01,000", "00:00:02,000", "A", "မင်္ဂလာပါ")]
        voices = {"A": "my-MM-ThihaNeural"}
        with tempfile.TemporaryDirectory() as temp:
            path = save_dubbing_project(Path(temp) / "project.dubbing.json", rows, voices)
            loaded_rows, loaded_voices = load_dubbing_project(path)
        self.assertEqual(loaded_rows, rows)
        self.assertEqual(loaded_voices, voices)


class CharacterDubbingRenderTests(unittest.TestCase):
    def test_render_builds_timestamped_voice_mix(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source.mp4"
            source.write_bytes(b"source-video")
            output = root / "dubbed.mp4"
            rows = [DialogueRow("00:00:02,000", "00:00:04,000", "A", "Hello")]
            voices = {"A": "my-MM-ThihaNeural"}

            def fake_tts(text, voice, destination):
                destination.write_bytes(b"mp3" * 500)

            captured = {}

            def fake_encode(ffmpeg, command_for_encoder, destination, *, log=None, min_output_bytes=5000):
                captured["command"] = command_for_encoder("libx264")
                Path(destination).write_bytes(b"final-video" * 100)
                return "libx264"

            with patch("studio.dubbing._edge_tts_save", side_effect=fake_tts), \
                 patch("studio.dubbing._duration", side_effect=[30.0, 2.5]), \
                 patch("studio.dubbing.run_video_encode", side_effect=fake_encode):
                result = render_character_dubbing(
                    ffmpeg="ffmpeg", ffprobe="ffprobe", source_video=source, rows=rows,
                    speaker_voices=voices, output_video=output, source_audio_mode="mute",
                )
            self.assertEqual(result, output.resolve())
            command = captured["command"]
            graph = command[command.index("-filter_complex") + 1]
            self.assertIn("adelay=2000|2000", graph)
            self.assertIn("amix=inputs=1", graph)
            self.assertTrue(output.is_file())

    def test_render_requires_a_voice_for_every_speaker(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.mp4"
            source.write_bytes(b"source")
            with self.assertRaisesRegex(ValueError, "Missing voice mapping"):
                render_character_dubbing(
                    ffmpeg="ffmpeg", ffprobe="ffprobe", source_video=source,
                    rows=[DialogueRow("0", "2", "Unknown", "Hello")],
                    speaker_voices={}, output_video=Path(temp) / "out.mp4", source_audio_mode="mute",
                )


if __name__ == "__main__":
    unittest.main()
