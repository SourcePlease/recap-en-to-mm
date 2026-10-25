from __future__ import annotations

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
from studio.thumbnail import thumbnail_size
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


class StudioThumbnailTests(unittest.TestCase):
    def test_thumbnail_sizes(self):
        self.assertEqual(thumbnail_size("16:9"), (1280, 720))
        self.assertEqual(thumbnail_size("9:16"), (720, 1280))
        self.assertEqual(thumbnail_size("1:1"), (1080, 1080))

    def test_unknown_thumbnail_ratio_fails_fast(self):
        with self.assertRaises(ValueError):
            thumbnail_size("4:3")


if __name__ == "__main__":
    unittest.main()
