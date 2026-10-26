# Recap Studio — feature branch

Work in this document belongs to SourcePlease/recap-en-to-mm on feature/studio-expansion. The fork's main branch and the upstream source repository are kept separate.

## Main application tabs

- **Recap** — local Whisper source transcription, configurable target language, context-aware translation, narrator TTS and timestamp-locked Smart Sync. Myanmar remains the default output.
- **Splitter** — the original long-video splitter and its editing controls.
- **Studio** — universal URL downloader, persistent queue, optional provider test, glossary editor and direct hand-off of a downloaded video to Recap.
- **Thumbnail** — standalone tab for local frame-based thumbnails or optional fal.ai-generated backgrounds, Burmese title templates, AI title ideas, 16:9 / 9:16 / 1:1 output, and local logo/title composition.
- **Subtitles** — import SRT/VTT, translate without running Whisper, preview the translated text and export translated-only or bilingual SRT while retaining cue timing.
- **Project** — save/load Recap configuration and paths, preview an audio waveform, edit pronunciation substitutions, and configure optional branded intro/outro cards and smart silence removal.

## Downloading and thumbnails

yt-dlp handles public media URLs supported by the installed extractors. Available options include quality selection, audio-only MP3, playlists, optional subtitle downloads, authorized user cookies, progress, resumable downloads, and a persistent queue with retry-failed support. Website extractors can fail after website changes, login requirements, region restrictions, CAPTCHA or removed media. This tool does not bypass DRM or access controls.

Local thumbnail generation extracts candidate frames with FFmpeg and applies the title/logo locally; it does not require a remote API. fal.ai creates an optional generated background and the app composites text/logo locally to protect Burmese spelling. fal.ai inference can consume credits and may be paid. Title idea generation falls back to local Burmese templates when an AI provider is unavailable.

## AI and multilingual narration

Gemini remains the default Recap text provider. Groq, OpenRouter and local Ollama are optional text providers, selected explicitly through the existing provider settings. Free models and quotas vary by model/account; there is no silent fallback to a paid provider.

Target language can be selected independently of source language in Recap. The selection is used by the translation prompt, output file suffix, subtitle plan and TTS narration profile. Current choices cover Myanmar/Burmese, English, Chinese, Japanese, Korean, Hindi, Thai, Vietnamese, Indonesian, Malay, Filipino, Spanish, Portuguese, French, German, Italian, Russian, Turkish, Arabic, Bengali and Tamil/Telugu/Urdu. Voice options include Edge TTS voices, Gemini voice styles, optional Azure Speech voices and an ElevenLabs multilingual voice configured by voice ID. A voice/language combination must be validated with a short sample before processing a long video.

- **Microsoft Edge TTS** has no separate API key but is an online service; voice availability can change.
- **Gemini TTS** uses the selected Gemini voice style and account access/quota; the catalogue styles are not all distinct native Burmese voices.
- **Azure Speech** requires AZURE_SPEECH_KEY and AZURE_SPEECH_REGION.
- **ElevenLabs** requires ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID; plan/quota depends on the account.

## Extra editing features

- **Subtitle import / bilingual export:** translating an existing SRT/VTT uses its cues directly and does not invoke Whisper. Exported timestamps are preserved.
- **Project save/load:** project JSON stores local paths and Recap configuration, not API key values. Keep project files private if they contain private local paths.
- **Audio waveform:** FFmpeg converts audio to low-rate mono PCM and the UI renders a compact RMS waveform, streaming data in small blocks to limit memory. It is a waveform overview, not a full multitrack timeline editor.
- **Pronunciation editor:** pronunciation.json maps a source term to the preferred spoken replacement. Rules are applied before TTS and do not modify visible subtitles.
- **Auto intro/outro:** locally rendered channel-name/logo cards are added to the final video only when enabled. Intro/outro durations are reflected in the uploaded SRT time offset.
- **Smart silence removal:** optional FFmpeg silence compression runs on generated narration and then Smart Sync uses the shorter audio duration. It is off by default because aggressive thresholds can trim quiet speech; test on a short clip first.

## Secrets and configuration

Use the local .env file for API secrets. Do not commit .env or local pronunciation.json. Supported variables include:

- GEMINI_API_KEY, GEMINI_TEXT_MODEL, GEMINI_PROXY
- RECAP_AI_PROVIDER, RECAP_AI_FALLBACKS, GROQ_API_KEY, GROQ_MODEL, OPENROUTER_API_KEY, OPENROUTER_MODEL
- OLLAMA_BASE_URL, OLLAMA_MODEL
- FAL_KEY, FAL_IMAGE_MODEL
- AZURE_SPEECH_KEY, AZURE_SPEECH_REGION
- ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, ELEVENLABS_MODEL_ID

## Validation status and limitations

Automated regression tests and Python compilation are run by the feature-branch GitHub Actions workflow. Those tests do not prove that an online provider key/quota works, that every site-specific URL is downloadable, or that a long video finishes without sync issues. Before treating a provider or site as production-ready, test a short real example, inspect the output audio/subtitles and then test a longer video. Do not share API keys when reporting errors.
