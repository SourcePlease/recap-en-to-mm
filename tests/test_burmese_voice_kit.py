from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from studio.burmese_voice_kit import prepare_burmese_text, replace_numbers, to_words


class BurmeseVoiceKitTests(unittest.TestCase):
    def test_integer_number_conversion(self):
        self.assertEqual(to_words(0), "သုည")
        self.assertEqual(to_words(15), "ဆယ့်ငါး")
        self.assertEqual(to_words(100), "တစ်ရာ")
        self.assertEqual(to_words(1234), "တစ်ထောင့်နှစ်ရာ့သုံးဆယ့်လေး")
        with self.assertRaises(ValueError):
            to_words(10_000_000)

    def test_number_conversion_preserves_unsupported_values(self):
        value, flags = replace_numbers("အပိုင်း 12၊ ၁၅%၊ 1.5")
        self.assertIn("ဆယ့်နှစ်", value)
        self.assertIn("ဆယ့်ငါး ရာခိုင်နှုန်း", value)
        self.assertIn("1.5", value)
        self.assertTrue(any("decimal" in flag for flag in flags))

    def test_custom_lexicon_and_number_preparation(self):
        with tempfile.TemporaryDirectory() as temp:
            lexicon = Path(temp) / "lexicon.tsv"
            lexicon.write_text("# test\nသန်းရာချီ\tသန်းပေါင်းရာချီ\n", encoding="utf-8")
            result, flags = prepare_burmese_text("သန်းရာချီ ရှိတယ် 12", lexicon)
        self.assertEqual(result, "သန်းပေါင်းရာချီ ရှိတယ် ဆယ့်နှစ်")
        self.assertEqual(flags, [])

    def test_empty_and_unsupported_inputs_are_safe(self):
        self.assertEqual(prepare_burmese_text("")[0], "")
        value, flags = replace_numbers("ID A12 and 0007")
        self.assertIn("A12", value)
        self.assertTrue(flags)


if __name__ == "__main__":
    unittest.main()
