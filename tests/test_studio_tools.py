from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT_DIR = Path(__file__).resolve().parents[1]
APP_DIR = ROOT_DIR / "app"
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from studio.ai_providers import AIProviderError, chat_completion, provider_options
from studio.downloader import (
    DownloadError, DownloadOptions, build_ytdlp_options, download_media, validate_http_url,
)
from studio.thumbnail import (
    build_fal_thumbnail_prompt, generate_fal_thumbnail, thumbnail_size,
)
from studio.title_generator import ai_title_ideas, builtin_title_ideas, TITLE_STYLES
import gemini_tts
from studio.download_queue import PersistentDownloadQueue
from studio.recap_queue import PersistentRecapQueue
from studio.quality import inspect_output_quality, preflight_check, write_quality_report
from recap_runtime.services.ai_service import AIService
from recap_planner import _user_glossary_context


class StudioDownloaderTests(unittest.TestCase):
    def test_http_urls_are_accepted(self):
        self.assertEqual(validate_http_url(" https://example.com/video "), "https://example.com/video")

    def test_non_web_urls_are_rejected(self):
        for value in ("file:///etc/passwd", "ftp://example.com/a", "", "https:///missing-host"):
            with self.subTest(value=value), self.assertRaises(DownloadError):
                validate_http_url(value)

    def test_quality_selector_is_capped_by_requested_height(self):
        with tempfile.TemporaryDirectory() as temp:
            options = DownloadOptions(output_dir=Path(temp), quality_height=720)
            self.assertIn("height<=720", build_ytdlp_options(options)["format"])

    def test_missing_cookie_file_is_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            options = DownloadOptions(
                output_dir=Path(temp), cookies_file=Path(temp) / "missing-cookies.txt",
            )
            with self.assertRaises(DownloadError):
                build_ytdlp_options(options)

    def test_download_returns_existing_output_path(self):
        with tempfile.TemporaryDirectory() as temp:
            output_path = Path(temp) / "demo.mp4"

            class FakeYoutubeDL:
                def __init__(self, config):
                    self.config = config
                def __enter__(self):
                    return self
                def __exit__(self, *args):
                    return False
                def extract_info(self, url, download=True):
                    output_path.write_bytes(b"fake video")
                    return {"title": "demo", "id": "123", "filepath": str(output_path), "extractor_key": "test"}

            fake_module = Mock()
            fake_module.YoutubeDL = FakeYoutubeDL
            result = download_media(
                "https://example.com/video", DownloadOptions(output_dir=Path(temp)),
                ytdlp_module=fake_module,
            )
            self.assertEqual(result.title, "demo")
            self.assertEqual(result.video_path, output_path.resolve())
            self.assertTrue(output_path.exists())


class StudioAIProviderTests(unittest.TestCase):
    def test_cloud_provider_requires_a_key(self):
        with self.assertRaises(AIProviderError):
            chat_completion("groq", "sample-model", [{"role": "user", "content": "hi"}], api_key="")

    def test_ollama_can_be_configured_without_key(self):
        class Response:
            def raise_for_status(self):
                return None
            def json(self):
                return {"choices": [{"message": {"content": "OK"}}]}

        post = Mock(return_value=Response())
        answer = chat_completion(
            "ollama", "test-model", [{"role": "user", "content": "hi"}], post=post,
        )
        self.assertEqual(answer, "OK")
        self.assertEqual(post.call_args.args[0], "http://127.0.0.1:11434/v1/chat/completions")
        self.assertNotIn("Authorization", post.call_args.kwargs["headers"])

    def test_provider_catalog_includes_openrouter(self):
        keys = {provider["key"] for provider in provider_options()}
        self.assertTrue({"groq", "openrouter", "ollama"}.issubset(keys))


class AIServiceProviderRoutingTests(unittest.TestCase):
    def test_ollama_is_an_explicit_recaps_provider_without_gemini_key(self):
        with patch.dict(os.environ, {"RECAP_AI_PROVIDER": "ollama", "OLLAMA_MODEL": "test-model"}, clear=True):
            service = AIService()
            self.assertEqual(service.provider, "ollama")
            self.assertEqual(service.text_model, "test-model")
            with patch(
                "studio.ai_providers.chat_completion_with_fallback",
                return_value=("OK", "ollama", "test-model", []),
            ):
                response = service.client.models.generate_content(model="test-model", contents="return JSON")
            self.assertEqual(response.text, "OK")
            self.assertEqual(service._last_provider, "ollama")


class PersistentDownloadQueueTests(unittest.TestCase):
    def test_queue_persists_status_and_resets_interrupted_download(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "queue.json"
            queue_model = PersistentDownloadQueue(path)
            added, skipped = queue_model.add([
                "https://example.com/a",
                "https://example.com/a",
                "https://example.com/b",
            ])
            self.assertEqual(len(added), 2)
            self.assertEqual(len(skipped), 1)
            queue_model.update(added[0].id, status="downloading")
            queue_model.update(added[1].id, status="completed", title="B")
            reloaded = PersistentDownloadQueue(path)
            statuses = {item.url: item.status for item in reloaded.items()}
            self.assertEqual(statuses["https://example.com/a"], "pending")
            self.assertEqual(statuses["https://example.com/b"], "completed")

    def test_failed_jobs_can_be_retried_and_completed_jobs_cleared(self):
        with tempfile.TemporaryDirectory() as temp:
            queue_model = PersistentDownloadQueue(Path(temp) / "queue.json")
            added, _ = queue_model.add(["https://example.com/a", "https://example.com/b"])
            queue_model.update(added[0].id, status="failed", error="network down")
            queue_model.update(added[1].id, status="completed")
            self.assertEqual(queue_model.retry_failed(), 1)
            statuses = {item.url: item.status for item in queue_model.items()}
            self.assertEqual(statuses["https://example.com/a"], "pending")
            self.assertEqual(queue_model.clear_finished(), 1)
            self.assertEqual(len(queue_model.items()), 1)


class TranslationGlossaryTests(unittest.TestCase):
    def test_glossary_adds_consistent_burmese_terms(self):
        with tempfile.TemporaryDirectory() as temp:
            glossary = Path(temp) / "glossary.json"
            glossary.write_text(
                '{"characters":{"Asta":"အက်စတာ"},"terms":{"Magic Knight":"မေဂျစ်နိုက်"},'
                '"places":{},"notes":["Use natural Burmese"]}',
                encoding="utf-8",
            )
            with patch.dict(os.environ, {"RECAP_GLOSSARY_PATH": str(glossary)}):
                prompt_prefix = _user_glossary_context()
            self.assertIn("Asta => အက်စတာ", prompt_prefix)
            self.assertIn("Magic Knight => မေဂျစ်နိုက်", prompt_prefix)
            self.assertIn("Use natural Burmese", prompt_prefix)

    def test_invalid_glossary_is_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            glossary = Path(temp) / "glossary.json"
            glossary.write_text("{invalid", encoding="utf-8")
            with patch.dict(os.environ, {"RECAP_GLOSSARY_PATH": str(glossary)}):
                with self.assertRaises(RuntimeError):
                    _user_glossary_context()


class FalThumbnailTests(unittest.TestCase):
    def test_ai_prompt_requests_no_baked_in_text(self):
        prompt = build_fal_thumbnail_prompt(
            "Black Clover", "A young mage discovers forbidden power", "Overpowered / Action",
        )
        self.assertIn("Black Clover", prompt)
        self.assertIn("forbidden power", prompt)
        self.assertIn("no text", prompt.lower())
        self.assertIn("original", prompt.lower())

    def test_fal_image_is_downloaded_and_title_is_overlaid(self):
        with tempfile.TemporaryDirectory() as temp:
            image_bytes = __import__("io").BytesIO()
            from PIL import Image
            Image.new("RGB", (320, 180), (22, 35, 50)).save(image_bytes, format="PNG")
            response = Mock()
            response.content = image_bytes.getvalue()
            response.raise_for_status = Mock()
            getter = Mock(return_value=response)
            client = Mock()
            client.run.return_value = {"images": [{"url": "https://v3.fal.media/files/out.png"}]}
            destination = Path(temp) / "generated.jpg"
            old_key = os.environ.get("FAL_KEY")
            try:
                os.environ.pop("FAL_KEY", None)
                result = generate_fal_thumbnail(
                    destination, title="အင်အားအကြီးဆုံးသူ",
                    api_key="test-key-not-real", fal_client_module=client, http_get=getter,
                )
            finally:
                if old_key is not None:
                    os.environ["FAL_KEY"] = old_key
                else:
                    os.environ.pop("FAL_KEY", None)
            self.assertEqual(result, destination.resolve())
            self.assertTrue(result.is_file())
            self.assertEqual(client.run.call_args.args[0], "fal-ai/fast-sdxl")
            self.assertEqual(client.run.call_args.kwargs["arguments"]["num_images"], 1)
            getter.assert_called_once()
            with Image.open(result) as output:
                self.assertEqual(output.size, (1280, 720))
                self.assertEqual(output.format, "JPEG")

    def test_fal_rejects_untrusted_image_url(self):
        with tempfile.TemporaryDirectory() as temp:
            client = Mock()
            client.run.return_value = {"images": [{"url": "https://example.com/not-fal.png"}]}
            getter = Mock()
            with self.assertRaises(Exception):
                generate_fal_thumbnail(
                    Path(temp) / "bad.jpg", title="Test", api_key="test-key-not-real",
                    fal_client_module=client, http_get=getter,
                )
            getter.assert_not_called()


class BurmeseTitleTests(unittest.TestCase):
    def test_builtin_ideas_are_burmese_and_keep_source_title(self):
        ideas = builtin_title_ideas("Black_Clover_S2_1080p", "Isekai / Reincarnation")
        self.assertGreaterEqual(len(ideas), 4)
        self.assertTrue(any("Black Clover S2" in idea for idea in ideas))
        self.assertTrue(all(len(idea) < 150 for idea in ideas))
        self.assertIn("Anime Recap", TITLE_STYLES)

    def test_ai_title_ideas_parse_bullets(self):
        class Response:
            def raise_for_status(self):
                return None
            def json(self):
                return {"choices": [{"message": {"content": "၁။ အားလုံးကို အံ့ဩစေခဲ့သူ\n- မထင်မှတ်ထားတဲ့ အဆုံးသတ်"}}]}

        post = Mock(return_value=Response())
        ideas = ai_title_ideas(
            "Black Clover", provider="groq", model="test-model", api_key="fake-key",
            post=post,
        )
        self.assertEqual(ideas, ["အားလုံးကို အံ့ဩစေခဲ့သူ", "မထင်မှတ်ထားတဲ့ အဆုံးသတ်"])

    def test_gemini_voice_catalog_has_thirty_distinct_choices(self):
        self.assertEqual(len(gemini_tts.GEMINI_VOICE_CATALOG), 30)
        self.assertEqual(len(set(name for name, _style in gemini_tts.GEMINI_VOICE_CATALOG)), 30)
        self.assertEqual(gemini_tts.voice_id("gemini:Zephyr — Bright"), "Zephyr")
        prompt = gemini_tts.narrator_prompt("မင်္ဂလာပါ။", "gemini:Zephyr — Bright")
        self.assertIn("prebuilt voice Zephyr", prompt)


class StudioThumbnailTests(unittest.TestCase):
    def test_thumbnail_sizes(self):
        self.assertEqual(thumbnail_size("16:9"), (1280, 720))
        self.assertEqual(thumbnail_size("9:16"), (720, 1280))
        self.assertEqual(thumbnail_size("1:1"), (1080, 1080))

    def test_unknown_thumbnail_ratio_fails_fast(self):
        with self.assertRaises(ValueError):
            thumbnail_size("4:3")



from studio.pronunciation import apply_pronunciation_overrides
from studio.subtitles import SubtitleCue, format_srt, parse_subtitles


class ImportedSubtitleTests(unittest.TestCase):
    def test_srt_import_preserves_cue_times_and_text(self):
        source = "1\n00:00:01,250 --> 00:00:02,900\nHello there!\n\n2\n00:00:03,000 --> 00:00:04,250\nGoodbye.\n"
        cues = parse_subtitles(source)
        self.assertEqual(len(cues), 2)
        self.assertEqual(cues[0].start, "00:00:01,250")
        self.assertEqual(cues[0].end, "00:00:02,900")
        self.assertEqual(cues[0].text, "Hello there!")

    def test_vtt_import_and_bilingual_export_keep_time_codes(self):
        source = "WEBVTT\n\n00:00:01.000 --> 00:00:02.000 align:start\nHello world.\n"
        cues = parse_subtitles(source)
        result = format_srt(cues, ["မင်္ဂလာပါ။"], bilingual=True)
        self.assertIn("00:00:01,000 --> 00:00:02,000", result)
        self.assertIn("Hello world.\nမင်္ဂလာပါ။", result)

    def test_empty_subtitle_file_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_subtitles("WEBVTT\n\nNo timestamps here")


class PronunciationTests(unittest.TestCase):
    def test_pronunciation_override_is_applied_before_tts(self):
        with tempfile.TemporaryDirectory() as temp:
            dictionary = Path(temp) / "pronunciation.json"
            dictionary.write_text(
                '{"Black Clover":"ဘလက် ကလိုဗာ","Asta":"အက်စတာ"}',
                encoding="utf-8",
            )
            output = apply_pronunciation_overrides("Asta watched Black Clover.", dictionary)
            self.assertIn("အက်စတာ", output)
            self.assertIn("ဘလက် ကလိုဗာ", output)

    def test_gemini_tts_prompt_respects_non_burmese_target(self):
        prompt = gemini_tts.narrator_prompt("Hello there.", "gemini:Zephyr — Bright", target_language="en")
        self.assertIn("English narrator", prompt)
        self.assertIn("native English pronunciation", prompt)


class PersistentRecapQueueTests(unittest.TestCase):
    def test_queue_persists_items_and_recovers_interrupted_processing(self):
        with tempfile.TemporaryDirectory() as temp:
            queue_path = Path(temp) / "recap_queue.json"
            item_file = Path(temp) / "video.mp4"
            item_file.write_bytes(b"video")
            model = PersistentRecapQueue(queue_path)
            added, skipped = model.add([item_file, item_file])
            self.assertEqual(len(added), 1)
            self.assertEqual(len(skipped), 1)
            model.update(added[0].id, status="processing")
            reloaded = PersistentRecapQueue(queue_path)
            self.assertEqual(reloaded.items()[0].status, "pending")
            self.assertEqual(reloaded.items()[0].path, str(item_file.resolve()))

    def test_queue_retries_failures_and_removes_only_completed_items(self):
        with tempfile.TemporaryDirectory() as temp:
            model = PersistentRecapQueue(Path(temp) / "recap_queue.json")
            added, _ = model.add(["missing-one.mp4", "missing-two.mp4"])
            model.update(added[0].id, status="failed", error="bad video")
            model.update(added[1].id, status="completed", output_path="final.mp4")
            self.assertEqual(model.retry_failed(), 1)
            statuses = {Path(item.path).name: item.status for item in model.items()}
            self.assertEqual(statuses["missing-one.mp4"], "pending")
            self.assertEqual(statuses["missing-two.mp4"], "completed")
            self.assertEqual(model.clear_finished(), 1)
            self.assertEqual(len(model.items()), 1)


class QualityCheckTests(unittest.TestCase):
    def test_missing_video_is_reported_as_output_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            report = inspect_output_quality(Path(temp) / "missing.mp4", ffprobe="ffprobe")
            self.assertFalse(report["pass"])
            self.assertGreater(report["failures"], 0)
            self.assertEqual(report["checks"][0]["status"], "FAIL")

    def test_preflight_reports_missing_source_without_exposing_secrets(self):
        with tempfile.TemporaryDirectory() as temp:
            env = Path(temp) / ".env"
            env.write_text("GEMINI_API_KEY=do-not-disclose\n", encoding="utf-8")
            report = preflight_check(
                Path(temp) / "missing.mp4", ffmpeg="missing-ffmpeg", ffprobe="missing-ffprobe",
                env_path=env, target_language="mm",
            )
            serialized = json.dumps(report, ensure_ascii=False)
            self.assertFalse(report["pass"])
            self.assertIn("Source video", serialized)
            self.assertNotIn("do-not-disclose", serialized)

    def test_quality_report_is_written_as_json(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "quality.json"
            report = {"pass": True, "checks": [{"status": "PASS", "name": "test"}]}
            self.assertEqual(write_quality_report(path, report), path)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), report)


if __name__ == "__main__":
    unittest.main()
