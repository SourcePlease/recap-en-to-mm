"""Daily Gemini model rotation and .env chain configuration tests."""
import os
import sys
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1] / "app"
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

import recap_planner as rp  # noqa: E402


MODELS = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.6-flash",
]


class GeminiDailyRotationTests(unittest.TestCase):
    def test_anchor_date_starts_with_latest_model(self):
        self.assertEqual(
            rp.rotate_gemini_model_chain(
                MODELS, start_date="2026-11-07", today=date(2026, 11, 7)
            ),
            MODELS,
        )

    def test_each_new_day_moves_to_the_next_model(self):
        self.assertEqual(
            rp.rotate_gemini_model_chain(
                MODELS, start_date="2026-11-07", today=date(2026, 11, 8)
            ),
            ["gemini-3.7-flash", "gemini-3.6-flash", "gemini-3.8-flash"],
        )

    def test_rotation_cycles_after_the_last_model(self):
        self.assertEqual(
            rp.rotate_gemini_model_chain(
                MODELS, start_date="2026-11-07", today=date(2026, 11, 10)
            ),
            MODELS,
        )

    def test_rotation_can_be_disabled(self):
        self.assertEqual(
            rp.rotate_gemini_model_chain(
                MODELS, rotation="off", start_date="2026-11-07", today=date(2026, 11, 8)
            ),
            MODELS,
        )

    def test_duplicate_and_empty_models_are_removed(self):
        self.assertEqual(
            rp.rotate_gemini_model_chain(
                ["gemini-3.8-flash", "", "gemini-3.8-flash", "gemini-3.7-flash"],
                rotation="off",
                today=date(2026, 11, 7),
            ),
            ["gemini-3.8-flash", "gemini-3.7-flash"],
        )

    def test_env_model_list_is_daily_rotated(self):
        env = {
            "GEMINI_TEXT_MODELS": ",".join(MODELS),
            "GEMINI_MODEL_ROTATION": "daily",
            "GEMINI_MODEL_ROTATION_START_DATE": "2026-11-07",
        }
        with patch.dict(os.environ, env, clear=False):
            chain = rp.configured_gemini_model_chain(today=date(2026, 11, 9))
        self.assertEqual(
            chain,
            ["gemini-3.6-flash", "gemini-3.8-flash", "gemini-3.7-flash"],
        )

    def test_empty_env_list_uses_default_latest_first(self):
        env = {
            "GEMINI_TEXT_MODELS": "",
            "GEMINI_TEXT_MODEL": "gemini-3.8-flash",
            "GEMINI_MODEL_ROTATION": "off",
        }
        with patch.dict(os.environ, env, clear=False):
            chain = rp.configured_gemini_model_chain(today=date(2026, 11, 7))
        self.assertEqual(chain[0], "gemini-3.8-flash")
        self.assertIn("gemini-3.7-flash", chain)


if __name__ == "__main__":
    unittest.main()
