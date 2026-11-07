# Ready-to-Test Guide / စမ်းသပ်ရန် ပြင်ဆင်လမ်းညွှန်

**Branch:** `feature/studio-expansion`  
**Scope:** Windows desktop app ကို မူရင်းအတိုင်းထားပြီး Studio feature branch တွင် စမ်းသပ်ရန် ပြင်ဆင်ထားသည်။  
**အရေးကြီး:** Ready to test ဆိုသည်မှာ automated checks နှင့် setup ကို စမ်းသပ်နိုင်ရန် ပြင်ဆင်ထားခြင်းဖြစ်သည်။ Windows PC ပေါ်တွင် GUI, real provider APIs, NVIDIA GPU နှင့် ၂ နာရီကျော် video ကို လက်တွေ့ run မစမ်းရသေးလျှင် release verified ဟု မဆိုလိုပါ။

## 1. စတင်အသုံးပြုရန် / Quick Start

1. Install Python **3.12, 64-bit** and enable Tcl/Tk during setup.
2. Install FFmpeg + FFprobe and ensure both are on PATH, or use the bundled `ffmpeg` folder.
3. Run `INSTALL_REQUIREMENTS.bat`.
4. Copy `.env.example` to `.env`, then add at least one working AI provider key/model.
5. Run `RUN.bat`.

**မြန်မာလို:** Python 3.12 (64-bit) ကို Tcl/Tk ပါအောင် Install လုပ်ပါ။ FFmpeg/FFprobe ကို PATH ထဲထည့်ပါ။ `INSTALL_REQUIREMENTS.bat` ကို run ပြီး `.env.example` ကို `.env` အဖြစ် copy ကူးကာ ကိုယ်သုံးမယ့် AI Provider ရဲ့ Key/Model ထည့်ပါ။ ပြီးရင် `RUN.bat` ကို ဖွင့်ပါ။

## 2. AI Provider Setup

- `RECAP_AI_PROVIDER=auto` uses the first fully configured provider in `RECAP_AI_AUTO_ORDER`.
- Auto routing requires both a model ID and its API key for hosted providers. Ollama requires a model ID and a running local Ollama server.
- When no alternate provider is configured, Auto falls back to Gemini and therefore requires `GEMINI_API_KEY`.
- Do not commit `.env` or share API keys in screenshots/logs.

**မြန်မာလို:** `auto` သည် Key/Model ပြည့်စုံတဲ့ Provider ကို အစဉ်လိုက်ရွေးပါတယ်။ Hosted Provider တွေအတွက် API Key နဲ့ Model ID နှစ်ခုလုံးလိုပါတယ်။ Ollama အတွက် Model ID နဲ့ local server ဖွင့်ထားဖို့လိုပါတယ်။ တခြား Provider မပြည့်စုံရင် Gemini ကို fallback လုပ်တဲ့အတွက် `GEMINI_API_KEY` လိုပါမယ်။

## 3. Recommended Smoke-Test Order / စမ်းသပ်ရန် အစီအစဉ်

- [ ] Launch the app and confirm all tabs open without errors.
- [ ] Run Studio preflight and confirm FFmpeg/FFprobe, source file and output storage checks.
- [ ] Test one short local video (30–90 seconds) through Recap using one configured AI provider and Edge TTS.
- [ ] Stop a Recap job, restart/resume it, and verify completed transcript/TTS checkpoints are reused.
- [ ] Import an existing SRT and VTT, translate, manually edit, export translated + bilingual SRT.
- [ ] Render a Subbing video and confirm original audio remains; confirm the UI stays responsive during render.
- [ ] Render Character Dubbing with two manually assigned speakers; test Mute, Keep Original Mix, and Demucs instrumental modes separately.
- [ ] Split one short clip with exact cuts and Smart Cut; verify no gaps/overlaps between outputs.
- [ ] Test Downloader with a URL you own or are authorized to download; confirm queue retry and restart recovery.
- [ ] Generate standalone Thumbnail Studio output and verify auto-thumbnail uses the original source video's frame.
- [ ] Test Project Save/Load, pronunciation rules, waveform analysis, Intro/Outro and Smart Silence Removal.
- [ ] Test Batch Queue with multiple short clips.
- [ ] Test GPU and CPU separately where compatible hardware is available.
- [ ] Only after short clips pass, test long videos (including 2+ hours) and monitor RAM, VRAM, disk space, sync drift and output integrity.

**မြန်မာလို:** အရင်ဆုံး ၃၀–၉၀ စက္ကန့် Video တစ်ခုနဲ့ Recap ကိုစမ်းပါ။ ပြီးမှ Stop/Resume, Subtitle, Subbing, Character Dubbing, Splitter, Downloader, Thumbnail, Project Tools နဲ့ Batch Queue ကို တစ်ခုချင်းစီ စစ်ပါ။ Short clip တွေ အောင်မှသာ ၂ နာရီကျော် Video ကို စမ်းပါ။ RAM/VRAM, Disk Space, Sync Drift နဲ့ Output ပျက်/မပျက်ကို ကြည့်ပါ။

## 4. GPU Behavior / GPU အသုံးပြုပုံ

- Whisper can use NVIDIA CUDA when the compatible faster-whisper/CTranslate2 runtime, cuBLAS and cuDNN are installed; otherwise it falls back to CPU.
- Demucs selects CUDA when PyTorch reports it available, then retries on CPU after a GPU failure.
- Main Recap and Splitter have NVENC/CPU fallback paths.
- Subbing and Character Dubbing use a real NVENC smoke test before selecting NVENC and retry with libx264 if the hardware render fails.
- Hosted AI, Edge TTS, Azure Speech, ElevenLabs and fal.ai execute remotely; they do not use the PC's local GPU.

**မြန်မာလို:** GPU ရှိရုံနဲ့ Feature အားလုံး GPU သုံးတာမဟုတ်ပါ။ Whisper, Demucs နဲ့ FFmpeg NVENC တို့မှာသာ သက်ဆိုင်ရာ Driver/Runtime ပြည့်စုံရင် GPU သုံးနိုင်ပါတယ်။ Subbing နဲ့ Character Dubbing မှာလည်း NVENC ကို တကယ်အလုပ်လုပ်မလုပ် စမ်းပြီး မရရင် CPU encoder ကို ပြန်သုံးပါတယ်။ Hosted AI/TTS တွေက Cloud ပေါ်မှာ run တာဖြစ်ပြီး PC GPU ကို မသုံးပါဘူး။

See [GPU_SETUP.md](GPU_SETUP.md) for Windows NVIDIA setup.

## 5. Known Scope Limits / လက်ရှိ မပါသေးသောအရာများ

The following are not part of this test-ready implementation and must not be treated as completed:
- Automatic speaker diarization / character identity detection.
- Automatic scene detection, face/character tracking and subject-aware auto reframe.
- Editable subtitle timestamps directly on the preview timeline.
- Full multitrack video/audio timeline editor (current waveform feature is analysis, not a full timeline).
- Cloud team sync and direct social-platform publishing.

**မြန်မာလို:** အလိုအလျောက် Speaker ခွဲခြားခြင်း၊ Character tracking, Scene detection, Preview timeline ပေါ်က Subtitle timestamp edit, Multitrack Timeline, Cloud Sync နဲ့ Social upload တို့ကို ဒီ branch မှာ ပြီးစီးပြီးသား feature အဖြစ် မယူဆပါနဲ့။

## 6. Automated Test Coverage / အလိုအလျောက် စမ်းသပ်မှု

GitHub Actions runs:
- Python compile check for `app`, `recap_runtime` and `tests`.
- Full `unittest` discovery, including Studio, Downloader, Thumbnail, Provider, Subbing, Character Dubbing and Splitter regression tests.
- FFmpeg-backed regression tests run when FFmpeg is available on the runner.

The CI workflow does not validate real API credentials, Windows GUI behavior, actual NVIDIA hardware, all downloader sites, or multi-hour videos. Those require the manual checklist above.

**မြန်မာလို:** CI က Python compile နဲ့ Unit/Regression tests တွေကို စစ်ပေးနိုင်ပေမဲ့ သင့် Windows PC ရဲ့ GUI, ကိုယ်ပိုင် API Key, NVIDIA GPU, Website တစ်ခုချင်းစီရဲ့ Downloader နဲ့ ၂ နာရီကျော် Video ကို အစားထိုးပြီး မစမ်းနိုင်ပါဘူး။ အဲဒီအပိုင်းတွေကို လက်တွေ့စမ်းဖို့လိုပါတယ်။
