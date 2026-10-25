"""Configurable AI client used by the recap planner.

Gemini remains the default provider and retains its existing model/key fallback
behavior. Optional OpenAI-compatible providers are selected explicitly with
RECAP_AI_PROVIDER=groq|openrouter|ollama. Optional provider fallbacks are only
attempted when RECAP_AI_FALLBACKS explicitly lists them.
"""
import os
import socket
from types import SimpleNamespace

from google import genai
from google.genai import types  # noqa: F401  (the planner reads ai_service.types)

_LOCAL_PROXY = "http://127.0.0.1:10808"
_SUPPORTED_ALTERNATES = {"groq", "openrouter", "ollama"}


def gemini_proxy() -> str:
    configured = str(os.getenv("GEMINI_PROXY") or "").strip()
    if configured:
        return "" if configured.lower() in {"none", "off", "direct", "0"} else configured
    try:
        with socket.create_connection(("127.0.0.1", 10808), timeout=0.2):
            return _LOCAL_PROXY
    except OSError:
        return ""


class _OpenAICompatibleModels:
    def __init__(self, service):
        self.service = service

    def generate_content(self, model, contents):
        from studio.ai_providers import AIProviderError, PROVIDERS, chat_completion_with_fallback

        primary = self.service.provider
        allowed = [primary]
        for candidate in str(os.getenv("RECAP_AI_FALLBACKS") or "").split(","):
            candidate = candidate.strip().lower()
            if candidate in _SUPPORTED_ALTERNATES and candidate not in allowed:
                allowed.append(candidate)

        candidates = []
        for provider in allowed:
            spec = PROVIDERS[provider]
            model_id = str(os.getenv(spec.model_env) or "").strip()
            if provider == primary:
                model_id = str(model or model_id).strip()
            if not model_id:
                continue
            item = {"provider": provider, "model": model_id}
            if provider == "ollama":
                item["base_url"] = os.getenv("OLLAMA_BASE_URL") or None
            candidates.append(item)
        if not candidates:
            raise AIProviderError(
                "No model is configured for the selected provider or its explicit fallbacks."
            )

        answer, used_provider, used_model, errors = chat_completion_with_fallback(
            candidates,
            [{"role": "user", "content": str(contents)}],
            timeout=float(os.getenv("RECAP_AI_TIMEOUT_SECONDS", "120")),
        )
        self.service._last_provider = used_provider
        self.service._last_provider_model = used_model
        self.service._last_provider_fallback_errors = errors
        return SimpleNamespace(text=answer)


class _OpenAICompatibleClient:
    def __init__(self, service):
        self.models = _OpenAICompatibleModels(service)


class AIService:
    def __init__(self):
        self.provider = str(os.getenv("RECAP_AI_PROVIDER") or "gemini").strip().lower()
        self.proxy = ""
        self._last_provider = self.provider
        self._last_provider_model = ""
        self._last_provider_fallback_errors = []

        if self.provider == "gemini":
            self.api_key = os.getenv("GEMINI_API_KEY")
            if not self.api_key:
                raise ValueError("⚠️ GEMINI_API_KEY မတွေ့ပါ! .env ဖိုင်ကို စစ်ဆေးပါ။")
            self.proxy = gemini_proxy()
            self._enable_proxy()
            self.client = genai.Client(api_key=self.api_key)
            self._disable_proxy()
            self.text_model = os.getenv("GEMINI_TEXT_MODEL", "gemini-3.5-flash")
            self._last_provider_model = self.text_model
            return

        if self.provider not in _SUPPORTED_ALTERNATES:
            supported = ", ".join(sorted({"gemini"} | _SUPPORTED_ALTERNATES))
            raise ValueError(
                f"Unsupported RECAP_AI_PROVIDER={self.provider!r}. Choose one of: {supported}."
            )

        from studio.ai_providers import PROVIDERS

        spec = PROVIDERS[self.provider]
        self.api_key = os.getenv(spec.api_key_env) if spec.api_key_env else None
        if spec.requires_api_key and not self.api_key:
            raise ValueError(f"{spec.api_key_env} is required when RECAP_AI_PROVIDER={self.provider}.")
        self.text_model = str(os.getenv(spec.model_env) or "").strip()
        if not self.text_model:
            raise ValueError(f"{spec.model_env} is required when RECAP_AI_PROVIDER={self.provider}.")
        self.client = _OpenAICompatibleClient(self)

    def _enable_proxy(self):
        if self.proxy:
            os.environ["HTTPS_PROXY"] = self.proxy
            os.environ["HTTP_PROXY"] = self.proxy

    def _disable_proxy(self):
        if self.proxy:
            os.environ.pop("HTTPS_PROXY", None)
            os.environ.pop("HTTP_PROXY", None)
