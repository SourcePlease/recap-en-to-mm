# Recap Studio — feature branch notes

This document describes the work on feature/studio-expansion. The upstream repository and its main branch are left unchanged.

## Added in the first integration step

- **Studio tab** in the existing Windows desktop application.
- **URL downloader** using yt-dlp, with best available / 1080p / 720p / 480p / MP3 choices, playlist mode, subtitle download option, optional user-provided cookies.txt, download progress and resume support provided by yt-dlp.
- **Automatic thumbnail generator** using local FFmpeg frame extraction and Pillow layouts. It ranks candidate frames by visual contrast/detail and can export landscape, portrait, or square designs with an optional title and logo.
- **Optional AI provider tester** for Groq, OpenRouter, and local Ollama through OpenAI-compatible chat-completion endpoints. API keys are read from the environment or typed into the UI; the Studio UI does not store typed API keys in config.json.
- **Reusable engine modules** in app/studio so future work can connect these tools to batch jobs and other front ends.
- **Unit tests** that do not need live websites, API keys, or a running local model.

## Important limitations

- This first step does not mark the whole project complete. The current Recap → Myanmar pipeline still uses its existing Gemini translation path; the new provider helper and UI currently provide an explicit provider test/entry point, not automatic replacement of the translation engine.
- yt-dlp supports many sites, including common video platforms, but site extractors can stop working when websites change. The app must report failures instead of promising every URL always works.
- RedNote/Xiaohongshu needs separate live validation and, if the installed extractor cannot handle a URL, a site-specific adapter or other permitted extractor. It is not claimed as verified in this first step.
- Private, age-restricted, DRM-protected, or otherwise gated content is not unlocked by this application. Cookies can only be supplied by the user for content they are authorized to access.
- The auto-thumbnail generator is local template/frame selection, not AI image synthesis. A later stage can add selectable image-generation backends where a usable free API or local model is configured.
- Cloud provider free quotas/models can change and are account-specific. The app requires an explicit model choice and does not automatically switch a free provider to paid usage.

## Next implementation steps

1. Add a provider adapter contract and route translation through an explicit provider selection while preserving Gemini as the default.
2. Add URL capability probing, clearer per-extractor errors, a persistent download queue, playlist item progress, and user-controlled cookies handling.
3. Verify RedNote support against permitted test URLs and add a dedicated extractor adapter only if necessary.
4. Add an optional gallery/image downloader and allow choosing a downloaded cover or local frame for the thumbnail.
5. Add template packs, Burmese-font discovery, title wrapping preview, logo placement, and thumbnail batch generation.
6. Add integration tests around recap-from-downloaded-video without needing network access.

## Provider configuration

Optional environment variables:

- GROQ_API_KEY, GROQ_MODEL
- OPENROUTER_API_KEY, OPENROUTER_MODEL
- OLLAMA_BASE_URL (defaults to http://127.0.0.1:11434/v1), OLLAMA_MODEL

Do not commit API keys. Hosted free tiers have limits; Ollama runs locally if Ollama and a suitable model are installed.
