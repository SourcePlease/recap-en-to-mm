# Recap Studio — Feature Documentation / Feature စာတမ်း

ဤစာတမ်းသည် SourcePlease/recap-en-to-mm repository ၏ feature/studio-expansion branch အတွက် ဖြစ်သည်။ main branch နှင့် မူရင်း upstream repository ကို သီးခြားထားသည်။

This document describes the feature/studio-expansion branch of SourcePlease/recap-en-to-mm. The upstream repository and the fork's main branch remain separate.

## 1. Application Tabs / App ထဲက Tab များ

- **Recap — Video Recap / ဘာသာပြန်အသံဖြင့် Video ထုတ်လုပ်ခြင်း။** မူရင်း Video ကို Whisper ဖြင့် စာသားပြောင်း၊ Target Language ကို ဘာသာပြန်၊ Narrator အသံထုတ်ပြီး Smart Sync ဖြင့် Video နဲ့ အချိန်ညှိပေးသည်။ မြန်မာဘာသာသည် မူလ Default ဖြစ်သည်။  
  **English:** Local Whisper transcription, context-aware translation, narrator TTS and timestamp-aware Smart Sync. Myanmar/Burmese remains the default target.

- **Splitter — Video Part Splitting / Video အပိုင်းခွဲခြင်း။** Video တစ်ခု သို့မဟုတ် အများအပြားကို ကြာချိန်အလိုက် ခွဲပြီး Ratio, Fill, Text နှင့် Part Number များ သတ်မှတ်နိုင်သည်။ Smart Cut သည် စကားပြောနေချိန်တွင် ဖြတ်မိခြင်းကို လျှော့ချရန် စကားခဏရပ်သည့်နေရာကို ရှာနိုင်သည်။  
  **English:** Split one or many videos by duration, configure ratio/fill/text/part numbering, preview cut positions and optionally use Smart Cut around speech pauses.

- **Studio — Downloader & AI Tools / Download နှင့် AI Tools။** yt-dlp ကို အသုံးပြုပြီး ပံ့ပိုးထားသော Public URL များမှ Video သို့မဟုတ် Audio ကို Download လုပ်နိုင်သည်။ Queue, Provider Test, Glossary Editor နှင့် Recap Queue သို့ လွှဲပို့ခြင်းတို့ ပါဝင်သည်။  
  **English:** A yt-dlp downloader for supported public URLs, persistent URL queue, AI provider tester, glossary editor and hand-off to the Recap queue.

- **Thumbnail — Thumbnail Studio / Thumbnail ဖန်တီးခြင်း။** မူရင်း Video Frame များမှ Local Thumbnail ထုတ်ခြင်း၊ Frame ကို ကိုယ်တိုင်ရွေးခြင်း၊ Local Variant ၃ မျိုးဖန်တီးခြင်း၊ မြန်မာခေါင်းစဉ်နှင့် Logo တင်ခြင်း၊ ရွေးချယ်လိုပါက fal.ai ဖြင့် AI Background ဖန်တီးခြင်းတို့ ပါဝင်သည်။  
  **English:** Local frame-based thumbnails, manual frame selection, three local variants, Burmese title/logo composition and optional fal.ai image backgrounds.

- **Subtitles — Subtitle Import & Translation / Subtitle တင်သွင်းပြီး ဘာသာပြန်ခြင်း။** ရှိပြီးသား SRT/VTT ကို Whisper ထပ်မသုံးဘဲ ဘာသာပြန်ပြီး Timestamp များကို ထိန်းထားကာ Translated-only သို့မဟုတ် Bilingual SRT ထုတ်နိုင်သည်။ Export မလုပ်မီ စာသားကို တစ်ကြောင်းချင်း ပြင်နိုင်သည်။  
  **English:** Import SRT/VTT without rerunning Whisper, translate cues while preserving timestamps, review translated lines and export translated-only or bilingual SRT.

- **Project — Project, Audio & Storage / Project၊ Audio နှင့် Storage Tools။** Project Save/Load, Audio Waveform Overview, Pronunciation Dictionary, Intro/Outro Branding, Background Music, Smart Silence Removal, Preflight Check, Output Quality Check နှင့် Storage/Cache Tools ပါဝင်သည်။  
  **English:** Project save/load, waveform overview, pronunciation substitutions, branded intro/outro, optional background music, smart silence removal, preflight, output QC and safe storage/cache tools.

- **Recap Queue — Batch Recap / Recap Queue ဖြင့် အများအပြားလုပ်ဆောင်ခြင်း။** Local Video များကို Queue ထဲထည့်၊ App ပြန်ဖွင့်သည့်အခါ Pending Jobs များကို ပြန်ရယူ၊ Failed Jobs ကို Retry လုပ်ပြီး အလုပ်များကို တစ်ခုချင်း ဆက်တိုက်လုပ်နိုင်သည်။  
  **English:** A persistent local-file queue that recovers interrupted jobs, retries failures and processes videos sequentially.

## 2. Recap & Editing / Recap နှင့် Editor

**ပါဝင်သည့်အရာများ / Included**
- Whisper ဖြင့် Source Audio ကို Local Transcription လုပ်ခြင်း (Model ပထမဆုံးအသုံးပြုချိန်တွင် Download လိုနိုင်သည်)။
- Gemini ကို Default သုံးပြီး Story Context, Translation နှင့် Translation Audit လုပ်ခြင်း။ Groq, OpenRouter နှင့် Local Ollama ကို ရွေးချယ်သုံးနိုင်သည်။
- Source Language နဲ့ Target Language ကို သီးခြားရွေးခြင်း။ Target Options များတွင် Myanmar, English, Chinese, Japanese, Korean, Hindi, Thai, Vietnamese, Indonesian, Malay, Filipino, Spanish, Portuguese, French, German, Italian, Russian, Turkish, Arabic, Bengali, Tamil, Telugu နှင့် Urdu ပါဝင်သည်။
- Edge TTS, Gemini TTS နှင့် Optional Azure Speech/ElevenLabs TTS Provider များ။
- Smart Sync, TTS Segment Cache, Safe Stop/Resume, Log/Progress နှင့် Folder Batch Processing။
- Preview Frame ရွှေ့ကြည့်ခြင်း၊ Title/Logo/Extra Text ကို Drag လုပ်ခြင်း၊ Blur Box ဆွဲခြင်း၊ Zoom/Mirror, Ratio/Fill, 1080p/720p/480p Quality။
- Subtitle ကို Video ထဲ Burn-in လုပ်ခြင်းနှင့် Upload အတွက် SRT ထုတ်ခြင်း။

**English:** The Recap pipeline combines local Whisper transcription, context-aware translation and audit, selectable target language and TTS providers, cached narration segments, Smart Sync, safe Stop/Resume, folder batch processing, draggable preview overlays, blur boxes, video layout/quality controls and subtitle/SRT output.

## 3. Downloader & Automated Workflow / Downloader နှင့် အလိုအလျောက် Workflow

- Quality ရွေးချယ်မှု၊ MP3-only, Playlist Download, ရနိုင်သော Subtitle Download, Progress နှင့် Authorized Cookie File ပံ့ပိုးမှု။
- URL အများကြီးကို Persistent Queue ထဲထည့်ခြင်း၊ Interrupted Download များကို Pending အဖြစ် ပြန်ရယူခြင်း၊ Failed URL များကို Retry လုပ်ခြင်း။
- Download ပြီးသော Video ကို Recap Queue ထဲ အလိုအလျောက်ထည့်နိုင်သည်။ Option သီးခြားဖွင့်ပါက Download Queue ပြီးနောက် Recap Queue ကို အလိုအလျောက် စတင်နိုင်သည်။
- Download ပြီးချိန်မှာ Thumbnail ကို အလိုအလျောက်ဖန်တီးနိုင်သည်။

**English:** Download options include quality selection, MP3-only, playlists, available subtitles, progress and authorized cookies. URLs persist across restarts, failed downloads can be retried, and downloads may be automatically enqueued for Recap. Auto-starting Recap after the download queue is an independent opt-in setting.

**ကန့်သတ်ချက် / Limitations:** yt-dlp သည် ပံ့ပိုးထားသော Extractor များပေါ် မူတည်သည်။ Website ပြောင်းလဲမှု၊ Login/Region/CAPTCHA/URL Removed အခြေအနေများကြောင့် URL တစ်ခုချင်းစီ အလုပ်လုပ်မည်ဟု အာမမခံနိုင်ပါ။ DRM သို့မဟုတ် Access Control ကို ကျော်ဖြတ်ရန် မရည်ရွယ်ထားပါ။  
**English:** Site support changes over time; some links may fail because of extractor changes, login, regional restrictions, CAPTCHA or removed media. This app does not bypass DRM or access controls.

## 4. Thumbnail Studio / Thumbnail ဖန်တီးခြင်း

- FFmpeg ဖြင့် မူရင်း Video ထဲမှ Frame များထုတ်ပြီး Contrast/Detail အပေါ်အခြေခံကာ Frame ရွေးပေးသည်။
- **Choose Frame** ဖြင့် Contact Sheet ထဲမှ မိမိလိုချင်သည့် Video အချိန်နားက Frame ကိုရွေးနိုင်သည်။ Automatic Best Frame သို့လည်း ပြန်ပြောင်းနိုင်သည်။
- **Create 3 Local Variants** သည် Frame, Title Idea နှင့် Layout မတူသော Thumbnail ၃ မျိုး ဖန်တီးသည်။ Local Mode သည် AI Credits မသုံးပါ။
- **Auto-thumbnail after Recap** သည် Default အားဖြင့် ဖွင့်ထားသည်။ Recap Final Video ထွက်ပြီးနောက် Original Source Video မှ Frame များကို အသုံးပြုပြီး Final Output ဘေးတွင် JPG သိမ်းပေးသည်။
- 16:9, 9:16, 1:1 Aspect Ratio များ၊ မြန်မာ Title Styles နှင့် Logo Overlay ပါဝင်သည်။
- **AI generated (fal.ai)** ကိုရွေးပါက AI Background ကို ဖန်တီးပြီး Title/Logo ကို Local မှာ ထပ်တင်သည်။ FAL_KEY နှင့် Account Credits လိုနိုင်သည်။

**English:** Thumbnail Studio supports source-frame analysis, manual frame selection, three local variants, Burmese title templates, local logo/text composition, 16:9/9:16/1:1 layouts and automatic thumbnail generation after Recap. Optional fal.ai mode generates an image background and may consume paid credits.

## 5. Subtitle Tools / Subtitle ပြုပြင်ရေး

- SRT/VTT ကို Import လုပ်ခြင်း၊ Timestamp နှင့် မူရင်းစာသားကို Preview ကြည့်ခြင်း။
- ရှိပြီးသား Cue များကို AI Provider ဖြင့် Translate လုပ်ခြင်း၊ Whisper ကို ထပ်မခေါ်ခြင်း။
- Local glossary.json သို့မဟုတ် ရှိလျှင် glossary.example.json မှ Character Names, Terms, Places နှင့် Style Notes များကို ဘာသာပြန်ရာတွင် အသုံးပြုနိုင်ခြင်း။
- ဘာသာပြန်စာကို Cue တစ်ခုစီ ပြင်ပြီး Original Cue Count နှင့် ကိုက်ညီသည့်အခါ Translated-only နှင့် Bilingual SRT Export လုပ်ခြင်း။

**English:** Subtitle import/translation preserves cue timing and can reuse the same glossary as Recap. A review step allows one edited target-language line per cue before exporting translated-only and bilingual SRT files.

## 6. Project, Audio, Preflight & Storage / Project၊ Audio၊ စစ်ဆေးမှုနှင့် Storage

- Project Settings နဲ့ File Paths များကို Save/Load လုပ်သည်။ API Secret တန်ဖိုးကို Project JSON ထဲ မကူးပါ။
- Audio Waveform ကို အကြမ်းဖျဉ်းပြသည်။ ၎င်းသည် Multitrack Timeline Editor မဟုတ်ပါ။
- Pronunciation Dictionary ဖြင့် TTS ထွက်လာမည့် အသံထွက်ကို ပြင်သည်။ မြင်ရသော Subtitle စာသားကို မပြင်ပါ။
- Channel Name/Logo ပါသော Intro/Outro Card များကို ထည့်နိုင်သည်။ Default ပိတ်ထားသည်။
- Optional Background Music ကို Narration အောက်တွင် Loop လုပ်ပြီး Volume ကို 0–50% အတွင်း ချိန်နိုင်သည်။ Default ပိတ်ထားသည်။
- Smart Silence Removal သည် Narration ထဲက Silence ကို လျှော့နိုင်သော်လည်း အသံတိုးတိုးပြောထားသည့်နေရာများကို ထိခိုက်နိုင်သောကြောင့် Default ပိတ်ထားသည်။
- Preflight သည် Source File, FFmpeg/FFprobe, Credential ရှိ/မရှိ (Key မှန်/မမှန်ကို မစစ်နိုင်), Duration/Streams နှင့် Disk Space ကို စစ်သည်။
- Output Quality Report သည် Final Video ရှိ/မရှိ၊ Audio/Video Stream, Duration, Resolution နှင့် မျှော်လင့်ထားသော SRT/Thumbnail ရှိ/မရှိ စစ်သည်။ Report ကို JSON အဖြစ် သိမ်းနိုင်သည်။
- Storage Scan က Jobs, Downloads, Logs နှင့် Runtime Folder အရွယ်အစားကို ခန့်မှန်းပြသည်။ Safe Cache Cleanup သည် __pycache__ နှင့် သတ်မှတ်ထားသော Preview/Subtitle Render Cache များကိုသာ ဖယ်ရှားပြီး Final Video, Download, Checkpoint များကို မဖျက်ပါ။
- Platform Presets: YouTube 16:9, Shorts/Reels/TikTok 9:16, Square Feed 1:1 နှင့် Lightweight 720p။

**English:** Project tools include save/load, a low-memory waveform overview, pronunciation mappings, optional branded cards/music/silence compression, advisory preflight checks, objective media QC reports, storage estimates, safe cache cleanup and platform-oriented ratio/quality presets.

## 7. AI / TTS Providers & API Keys / Provider များနှင့် API Key များ

| Provider / ဝန်ဆောင်မှု | အသုံးပြုပုံ / Usage |
|---|---|
| Gemini | Default translation/context/audit provider; Gemini TTS is optional. |
| Groq | Optional text generation/translation provider; account/model quota applies. |
| OpenRouter | Optional model gateway; model pricing and limits vary. |
| Ollama | Optional local model endpoint; a suitable model must be installed locally. |
| Microsoft Edge TTS | Online TTS; voice availability/service access may change. No separate API key is configured by this app. |
| Azure Speech | Requires AZURE_SPEECH_KEY and AZURE_SPEECH_REGION. |
| ElevenLabs | Requires ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID; account quota/plan applies. |
| fal.ai | Optional AI thumbnail background; requires FAL_KEY and may use credits. |

API key များကို Local .env ထဲတွင်သာ ထည့်ပါ။ .env, Personal glossary.json, pronunciation.json နဲ့ ကိုယ်ရေးကိုယ်တာ Path ပါသော Project ဖိုင်များကို GitHub ပေါ် မတင်ပါနှင့်။  
**English:** Keep credentials in the local .env. Do not commit .env, personal glossary/pronunciation files, or project files containing private paths.

## 8. Testing Status / စမ်းသပ်မှုအခြေအနေ

Feature branch GitHub Actions သည် Python compilation နှင့် automated regression tests ကို လုပ်ဆောင်သည်။ Latest verified run before this documentation update: **Run #45 — success**.  
**မြန်မာ:** Automated Tests အောင်မြင်ထားခြင်းသည် Windows GUI, သင့် API Key/Quota, Website တစ်ခုချင်းစီ သို့မဟုတ် Video အရှည်ကြီး၏ အသံ/ရုပ် Sync အားလုံး အောင်မြင်ကြောင်း မဆိုလိုပါ။

**အသုံးပြုသူ စမ်းသပ်ရန် အကြံပြုအစီအစဉ် / Suggested user test order**
1. Video အတိုတစ်ခု (၁–၃ မိနစ်) နဲ့ Recap ကို စမ်းပါ။
2. Target Language, Narrator Voice, Subtitle နှင့် Smart Sync ကို စစ်ပါ။
3. Auto Thumbnail၊ JPG နဲ့ JSON Quality Report ဖန်တီးထားခြင်းကို စစ်ပါ။
4. Stop/Resume နဲ့ Recap Queue ကို Video အတိုများနဲ့ စမ်းပါ။
5. Download URL များကို တစ်ခုချင်း စမ်းပါ။ YouTube/Facebook/TikTok/RedNote က URL တိုင်း အမြဲအလုပ်လုပ်မယ်လို့ မယူဆပါနှင့်။
6. Background Music, Intro/Outro, Smart Silence Removal တို့ကို တစ်ခုပြီးတစ်ခု စမ်းပါ။
7. နောက်ဆုံးမှ Video အရှည်ကြီးကို အစအဆုံးလုပ်ပြီး Audio/Video Sync, Disk Space နှင့် Memory ကို စစ်ပါ။

Error ပြန်ပို့မယ်ဆိုရင် Log/Traceback နဲ့ ဘာလုပ်နေချိန်မှာ ဖြစ်တယ်ဆိုတာ ပို့ပါ။ API Key သို့မဟုတ် Cookie အချက်အလက်ကို မပို့ပါနှင့်။  
**English:** Report the error message/log and the operation that failed, but never share API keys or cookies.

## 9. Optional Future Ideas / နောက်ပိုင်း ထပ်တိုးနိုင်သည့် အကြံပြုချက်များ

အောက်ပါအရာများသည် လက်ရှိ Features အဖြစ် မကြေညာထားသေးဘဲ နောက်ပိုင်းတိုးချဲ့နိုင်သည့် အကြံပြုချက်များဖြစ်သည်။

These are future extension ideas, not claims about currently implemented functionality.

- AI Scene/Subject-Aware Reframing — စကားပြောသူ/ဇာတ်ကောင်ကို အခြေခံပြီး Vertical Video Crop ကို အလိုအလျောက်ရွေးခြင်း။
- Audio Source Separation — မူရင်း Background Music ကို Narration မှ ခွဲထုတ်ပြီး ထိန်းသိမ်းနိုင်ရေး။
- Chapter/Scene Markers — ဇာတ်လမ်းအခန်းလိုက် Timestamp နှင့် Export Chapter များ။
- Publish Integrations — YouTube သို့မဟုတ် အခြား Platform များသို့ Upload လုပ်ခြင်း (OAuth/API Setup လိုအပ်နိုင်သည်)။
- Advanced Timeline Editor — Video, Voice, BGM, Subtitle Track များကို အချိန်လိုက် ခွဲပြင်ခြင်း။
