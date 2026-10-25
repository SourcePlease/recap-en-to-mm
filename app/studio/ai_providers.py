"""Small client for configurable OpenAI-compatible AI endpoints.

The existing Gemini pipeline is left unchanged. This module adds an explicit,
opt-in route for Groq, OpenRouter, and local Ollama models. Free quotas and
model names change; users must choose a model that is currently available to
their own account. No provider is silently switched to paid usage.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Callable, Iterable

import requests


class AIProviderError(RuntimeError):
    """A user-facing provider/configuration error."""


@dataclass(frozen=True)
class ProviderSpec:
    key: str
    label: str
    endpoint: str
    api_key_env: str | None
    model_env: str
    default_model: str
    requires_api_key: bool
    notes: str


PROVIDERS: dict[str, ProviderSpec] = {
    "groq": ProviderSpec(
        key="groq",
        label="Groq",
        endpoint="https://api.groq.com/openai/v1/chat/completions",
        api_key_env="GROQ_API_KEY",
        model_env="GROQ_MODEL",
        default_model="",
        requires_api_key=True,
        notes="Hosted API; free limits depend on the current account and model.",
    ),
    "openrouter": ProviderSpec(
        key="openrouter",
        label="OpenRouter",
        endpoint="https://openrouter.ai/api/v1/chat/completions",
        api_key_env="OPENROUTER_API_KEY",
        model_env="OPENROUTER_MODEL",
        default_model="",
        requires_api_key=True,
        notes="Choose a currently listed free model; free-model quotas can change.",
    ),
    "ollama": ProviderSpec(
        key="ollama",
        label="Ollama (local)",
        endpoint="http://127.0.0.1:11434/v1/chat/completions",
        api_key_env=None,
        model_env="OLLAMA_MODEL",
        default_model="",
        requires_api_key=False,
        notes="Local inference; install Ollama and download a compatible model first.",
    ),
}


def provider_options() -> list[dict[str, str | bool]]:
    return [
        {
            "key": spec.key,
            "label": spec.label,
            "api_key_env": spec.api_key_env or "",
            "model_env": spec.model_env,
            "default_model": spec.default_model,
            "requires_api_key": spec.requires_api_key,
            "notes": spec.notes,
        }
        for spec in PROVIDERS.values()
    ]


def _endpoint_for(provider: str, base_url: str | None = None) -> str:
    if provider == "ollama":
        base = (base_url or os.getenv("OLLAMA_BASE_URL") or "http://127.0.0.1:11434/v1").strip().rstrip("/")
        if not base.startswith(("http://", "https://")):
            raise AIProviderError("Ollama base URL must start with http:// or https://.")
        if base.endswith("/chat/completions"):
            return base
        return base + "/chat/completions"
    if base_url:
        raise AIProviderError("A custom endpoint is only supported for local Ollama.")
    return PROVIDERS[provider].endpoint


def chat_completion(
    provider: str,
    model: str,
    messages: list[dict[str, str]],
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    timeout: float = 60.0,
    post: Callable[..., Any] | None = None,
) -> str:
    """Return one chat completion text or raise AIProviderError with safe details."""
    key = (provider or "").strip().lower()
    if key not in PROVIDERS:
        raise AIProviderError(f"Unknown AI provider: {provider}")
    spec = PROVIDERS[key]
    chosen_model = (model or os.getenv(spec.model_env, "")).strip()
    if not chosen_model:
        raise AIProviderError(
            f"Choose a model for {spec.label}. Free model names and availability can change."
        )
    secret = (api_key or (os.getenv(spec.api_key_env, "") if spec.api_key_env else "")).strip()
    if spec.requires_api_key and not secret:
        raise AIProviderError(f"Set {spec.api_key_env} in .env or enter the API key in Studio.")
    if not messages:
        raise AIProviderError("At least one chat message is required.")

    headers = {"Content-Type": "application/json"}
    if secret:
        headers["Authorization"] = f"Bearer {secret}"
    endpoint = _endpoint_for(key, base_url)
    body = {"model": chosen_model, "messages": messages, "stream": False}
    sender = post or requests.post
    try:
        response = sender(endpoint, json=body, headers=headers, timeout=timeout)
        response.raise_for_status()
        payload = response.json()
    except requests.Timeout as exc:
        raise AIProviderError(f"{spec.label} request timed out after {timeout:g} seconds.") from exc
    except requests.HTTPError as exc:
        status = getattr(getattr(exc, "response", None), "status_code", None)
        if status == 401 or status == 403:
            detail = "Authentication failed; check the API key and model access."
        elif status == 429:
            detail = "The provider rate/quota limit was reached. Try later or choose another configured provider."
        else:
            detail = f"The provider returned HTTP {status or 'error'}."
        raise AIProviderError(f"{spec.label}: {detail}") from exc
    except requests.RequestException as exc:
        raise AIProviderError(f"{spec.label} request failed: {exc}") from exc
    except (ValueError, TypeError) as exc:
        raise AIProviderError(f"{spec.label} returned invalid JSON.") from exc

    try:
        content = payload["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise AIProviderError(f"{spec.label} returned an unexpected chat-completion response.") from exc
    if not isinstance(content, str) or not content.strip():
        raise AIProviderError(f"{spec.label} returned an empty answer.")
    return content.strip()


def chat_completion_with_fallback(
    candidates: Iterable[dict[str, Any]],
    messages: list[dict[str, str]],
    *,
    timeout: float = 60.0,
) -> tuple[str, str, str, list[str]]:
    """Try only explicitly configured candidates, returning text/provider/model/errors."""
    errors: list[str] = []
    for candidate in candidates:
        provider = str(candidate.get("provider") or "").strip().lower()
        model = str(candidate.get("model") or "").strip()
        if not provider or not model:
            continue
        try:
            text = chat_completion(
                provider,
                model,
                messages,
                api_key=candidate.get("api_key"),
                base_url=candidate.get("base_url"),
                timeout=timeout,
            )
            return text, provider, model, errors
        except AIProviderError as exc:
            errors.append(f"{provider}/{model}: {exc}")
    raise AIProviderError(
        "No configured AI provider succeeded. " + (" | ".join(errors) if errors else "Add at least one provider/model.")
    )
