# Recap Studio — feature branch notes

This document describes the work on feature/studio-expansion. The upstream repository and its main branch are left unchanged.

## Added in the first integration step

- **Studio tab** in the existing Windows desktop application.
- **URL downloader** using yt-dlp, with best available / 1080p / 720p / 480p / MP3 choices, playlist mode, subtitle download option, optional user-provided cookies.txt, download progress and resume support provided by yt-dlp.
- **Thumbnail modes:** local frame-based generation remains free/offline (after FFmpeg is installed); optional **fal.ai AI image generation** creates a fresh background then overlays the title and logo locally. fal.ai image inference consumes account credits and may be paid; an API key is never required for the local method.
- **Burmese title tools:** built-in title styles for general recap, isekai/reincarnation, overpowered action, dark fantasy/survival, mystery/twist, and romance/betrayal; optional AI suggestions use the selected text provider. Burmese typography is rendered locally rather than asking the image model to spell Burmese text.
- **Narrator choices:** 2 Microsoft Edge Burmese voices plus 30 Gemini prebuilt voice styles in the selector. The Gemini catalogue is a set of voice styles, not 30 independently recorded Burmese native voices; actual output quality and free-tier quotas depend on the model/account.
- **Optional AI provider tester** for Groq, OpenRouter, and local Ollama through OpenAI-compatible chat-completion endpoints. API keys are read from the environment or typed into the UI; the Studio UI does not store typed API keys in config.json.
- **Reusable engine modules** in app/studio so future work can connect these tools to batch jobs and other front ends.
- **Unit tests** that do not need live websites, API keys, or a running local model.

## Important limitations

- Gemini remains the default, but the selected Groq, OpenRouter, or Ollama provider can now be applied to story context, translation, and audit requests through the same planner interface. The integration needs real long-video validation; output structure, context limits, and translation quality can differ by model.
- yt-dlp supports many sites, including common video platforms, but site extractors can stop working when websites change. The app must report failures instead of promising every URL always works.
- The dependency minimum uses a yt-dlp release that includes the newer RedNote/Xiaohongshu extractor. The application routes those URLs through yt-dlp, but individual links still need live validation because redirects, login requirements, region restrictions, CAPTCHA, or site changes can make them fail.
- Private, age-restricted, DRM-protected, or otherwise gated content is not unlocked by this application. Cookies can only be supplied by the user for content they are authorized to access.
- The auto-thumbnail generator is local template/frame selection, not AI image synthesis. A later stage can add selectable image-generation backends where a usable free API or local model is configured.
- Cloud provider free quotas/models can change and are account-specific. The app requires an explicit model choice and does not automatically switch a free provider to paid usage.

## Next implementation steps

1. Validate alternate providers against the real story-context, translation, and audit prompts on short and long videos; measure JSON validity, name consistency, and cost/quota behavior.
2. Validate live downloads for YouTube, Facebook, TikTok, Reddit, X/Twitter, and RedNote/Xiaohongshu on permitted public URLs; improve per-extractor diagnostics and playlist item progress.
3. Add batch thumbnail generation, more title wrapping/templates, and an optional gallery/cover-image downloader.
4. Add SRT/VTT import and translation, bilingual subtitles, and an explicit audio/background-music preservation option using optional source-separation tooling.
5. Add one-click export presets, scene/storyboard review, and optional subject-aware vertical reframing.
6. Validate alternate AI providers on short and long videos, then add project save/load and end-to-end Download → Recap integration tests.

## Provider configuration

Optional environment variables:

- GROQ_API_KEY, GROQ_MODEL
- OPENROUTER_API_KEY, OPENROUTER_MODEL
- OLLAMA_BASE_URL (defaults to http://127.0.0.1:11434/v1), OLLAMA_MODEL

Do not commit API keys. Hosted free tiers have limits; Ollama runs locally if Ollama and a suitable model are installed.
