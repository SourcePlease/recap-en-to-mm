# Recap → Myanmar (+ Splitter)

**English၊ တရုတ်၊ ဟိန္ဒီ၊ ကိုရီးယား … ဘယ်ဘာသာနဲ့ ပြောထားတဲ့ recap / ဇာတ်လမ်းပြော video ကိုမဆို မြန်မာအသံနဲ့ ပြန်ထုတ်ပေးတဲ့ Windows tool**
Narrator only · Whisper + Gemini · Microsoft Edge TTS (Myanmar) · Smart Sync
**Splitter** tab — ရှည်တဲ့ video ကို မိနစ်အလိုက် အပိုင်းခွဲ (Ratio + blur နောက်ခံ၊ စာ၊ Part နံပါတ်)

> English: turns a recap/story video narrated in English, Chinese, Hindi, Korean … (detected by itself)
> into the same video narrated in Myanmar (Burmese). The Myanmar voice leads, and the picture of every
> line is re-timed to it ("Smart Sync"). A second tab, **Splitter**, cuts long videos into parts.
> See the [English section](#english) below.

---

## ဘာလုပ်ပေးလဲ

1. **နားထောင်** — video ထဲက အသံကို စက်ထဲမှာပဲ Whisper နဲ့ စာသားပြောင်းတယ်။ စကားလုံးတိုင်းရဲ့ အချိန်ကို ယူထားတယ်။
   - **Source language** = Auto-detect ဆိုရင် Whisper က ဘယ်ဘာသာလဲ အရင် နားထောင်ကြည့်တယ် (ပထမ ၈ မိနစ်)။ ကိုယ်တိုင်လည်း ရွေးလို့ရတယ်။
   - English ဆို `small.en` (~460 MB)၊ တခြားဘာသာဆို `medium` (~1.5 GB, multilingual) နဲ့ နားထောင်တယ်။ Model တွေကို ပထမဆုံးအကြိမ်ပဲ download လုပ်ရတယ်။
   - ဟိန္ဒီနဲ့ Urdu က အသံတူလို့ Auto-detect မှာ Urdu ထွက်ရင် ဟိန္ဒီအဖြစ် ရေးတယ်။
2. **အပိုင်းခွဲ** — စာကြောင်း၊ အပိုဒ်၊ အသံရပ်တဲ့နေရာတွေမှာ ခွဲပြီး အပိုင်းတိုင်းကို ၄.၂ စက္ကန့်လောက် (အများဆုံး ၅.၆ စက္ကန့်) ထားတယ်။ အပိုင်းများလေ ရုပ်နဲ့ အသံ ပိုကိုက်လေပါ။
3. **ဇာတ်လမ်း မှတ်ဉာဏ်** — Gemini က ဇာတ်လမ်းတစ်ခုလုံးကို အရင်ဖတ်ပြီး ဇာတ်ကောင်နာမည်၊ ဆက်နွယ်မှု၊ နေရာတွေကို မှတ်ထားတယ်။ ဒါကြောင့် နာမည်တွေ တစ်ပုဒ်လုံး တစ်မျိုးတည်း ဖြစ်တယ်။
4. **ဘာသာပြန်** — Gemini က တစ်ခါမှာ အပိုင်း ၄၀ စီ မြန်မာလို ပြန်တယ်။
   - ဇာတ်ကြောင်းပြောသူလို သဘာဝကျတဲ့ စကားပြောပုံစံနဲ့ ပြန်တယ်။
   - အကျဉ်းမချုပ်ဘူး၊ ချန်မထားဘူး။ အပိုင်းတစ်ခုရဲ့ အကြောင်းအရာကို ဘေးအပိုင်းထဲ မရွှေ့ဘူး။
   - ပြန်ပြီးတိုင်း စစ်ဆေးတဲ့အဆင့် (audit) က ချန်ခဲ့တာ၊ နေရာလွဲတာ၊ ထပ်နေတာတွေကို ပြန်ပြင်တယ်။
   - မြန်မာစာလုံးထဲ တခြားဘာသာ စာလုံး ညှပ်ဝင်လာရင် (ဥပမာ "ဧည့်ခန်း" နေရာမှာ "မისခန်း") Gemini ကို ပြန်မေးတယ်။
5. **အသံထုတ်** — Edge TTS မြန်မာအသံ (Thiha ယောက်ျားသံ / Nilar မိန်းမသံ) နဲ့ ထုတ်တယ်။ "Short pauses" ဖွင့်ထားရင် Edge ထည့်တတ်တဲ့ အသံတိတ်ကို ဖြတ်လို့ စာကြောင်းကြားမှာ ~၀.၂၅ စက္ကန့်ပဲ နားတယ်။
6. **Smart Sync** — မြန်မာအသံက အချိန်ကို ဦးဆောင်ပြီး ရုပ်က လိုက်ညှိတယ်။ အသေးစိတ်ကို [Smart Sync ဘယ်လိုအလုပ်လုပ်လဲ](#smart-sync-ဘယ်လိုအလုပ်လုပ်လဲ) မှာ ကြည့်ပါ။
7. **ဖြည့်စွက်** — Blur box (မူရင်း watermark/စာတန်းဖုံးဖို့)၊ Title၊ Logo၊ Extra text၊ Zoom၊ Flip တွေကို preview ပေါ်မှာ နေရာချပြီး ထည့်လို့ရတယ်။ Video အချိုး (**16:9 / 9:16 / 1:1 / Original**) ကိုလည်း ရွေးလို့ရတယ်။

ထွက်လာတဲ့ video မှာ **မြန်မာအသံပဲ** ပါတယ်။ မူရင်း English အသံနဲ့ နောက်ခံသီချင်း မပါဘူး။

## လိုအပ်တာ

| | |
|---|---|
| Windows | 10 / 11 (64-bit) |
| Python | **3.12, 64-bit** — [python.org](https://www.python.org/downloads/) ကနေ သွင်းပါ။ "Add python.exe to PATH" နဲ့ "tcl/tk" ကို အမှန်ခြစ်ပါ |
| FFmpeg | `ffmpeg.exe` + `ffprobe.exe` — မရှိရင် `INSTALL_REQUIREMENTS.bat` က အလိုလို download လုပ်ပေးတယ် ([gyan.dev builds](https://www.gyan.dev/ffmpeg/builds/)) |
| Gemini API key | အခမဲ့ ရတယ် — [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| Internet | Gemini နဲ့ Edge TTS အတွက် |
| NVIDIA GPU | မဖြစ်မနေ မလိုဘူး။ ရှိရင် Whisper နဲ့ video render ပိုမြန်တယ် (NVENC)။ မရှိရင် CPU နဲ့ အလိုလို လုပ်တယ် |

## ထည့်သွင်းနည်း (တစ်ခါပဲ လုပ်ရ)

1. ဒီ repo ကို download လုပ်ပါ (**Code → Download ZIP** ပြီးရင် ဖြည်ပါ၊ သို့မဟုတ် `git clone`)။
2. Python 3.12 ကို သွင်းပါ (အပေါ်က ဇယားကို ကြည့်ပါ)။
3. **`INSTALL_REQUIREMENTS.bat`** ကို double-click နှိပ်ပါ။ အောက်ပါတွေကို သွင်းပေးပါမယ်:
   - Python package တွေ
   - Title စာရေးဖို့ လိုတဲ့ Chromium
   - **FFmpeg** — စက်ထဲမှာ မရှိရင် (~100 MB) download လုပ်ပြီး ဒီ folder ထဲက `ffmpeg\` ထဲ ထည့်ပေးပါမယ်။ PATH ထဲ (သို့) `C:\ffmpeg\bin\` မှာ ရှိပြီးသားဆိုရင် အဲ့ဒါကိုပဲ သုံးပါတယ်။
4. **`.env.example`** ကို **`.env`** လို့ copy ကူးပါ။ ပြီးရင် ဖွင့်ပြီး key ထည့်ပါ:
   ```ini
   GEMINI_API_KEY=ကိုယ့်_key
   ```
   Key တစ်ခုထက် ပိုရှိရင် (Google project တစ်ခုစီက key) ဒီလို ထည့်လို့ရပါတယ်။ တစ်ခုရဲ့ ကန့်သတ်ချက် ပြည့်ရင် နောက်တစ်ခုကို အလိုလို ပြောင်းသုံးပါတယ်။
   ```ini
   GEMINI_IMAGE_PROJECT_1_KEY=...
   GEMINI_IMAGE_PROJECT_2_KEY=...
   ```

> ⚠️ `.env` ထဲမှာ ကိုယ့် key ရှိလို့ ဘယ်သူ့ကိုမှ မပို့ပါနဲ့၊ GitHub ပေါ်လည်း မတင်ပါနဲ့ (`.gitignore` ထဲမှာ ထည့်ထားပြီးသားပါ)။

## သုံးနည်း

**`RUN.bat`** ကို double-click နှိပ်ပါ။ Window မှာ အကွက် ၃ ကွက် ပါပါတယ်။

| နေရာ | လုပ်ရမယ့်အရာ |
|---|---|
| အပေါ် | **Source Video → Browse** နဲ့ video ကို ရွေးပါ။ **Folder** နှိပ်ရင် folder ထဲက video တွေကို တစ်ခုပြီးတစ်ခု လုပ်ပါတယ် (ပြီးပြီးသား video တွေကို ကျော်ပါတယ်)။ **Gemini .env** မှာ `.env` ဖိုင်ကို ရွေးပါ (default က ဒီ folder ထဲက `.env`)။ **Save final to** — folder ရွေးထားရင် ပြီးတဲ့ video ကို `<video နာမည်>_Myanmar.mp4` နဲ့ အဲ့ folder ထဲ ထည့်ပေးပါတယ် (ဗလာထားရင် job folder ထဲမှာပဲ)။ |
| ဘယ်ဘက် | **Source language** (Auto-detect / English / Chinese / Hindi / Korean / …)၊ **Edge TTS Voice** (`my-MM-ThihaNeural` / `my-MM-NilarNeural`) နဲ့ **Edge TTS Speed** (−50% … +100%) ကို ရွေးပါ။ အောက်က **Run Logs** မှာ အလုပ်လုပ်နေတာတွေ ပြပါတယ်။ |
| အလယ် | **Preview** — slider နဲ့ `◀ 5s` / `5s ▶` နဲ့ ကြည့်ချင်တဲ့ အချိန်ကို ရွှေ့ပြီး **Refresh Frame** နှိပ်ပါ။ Title၊ Logo၊ Extra text ကို ဆွဲရွှေ့ပြီး နေရာချလို့ရပါတယ်။ Blur box ကို ဆွဲလို့ရပါတယ်။ |
| ညာဘက် | **Production Tools** — Zoom (1.00–1.25×)၊ Flip (ဘယ်ညာ ပြောင်းပြန်)၊ Voice vol (50–300%)၊ Short pauses၊ **Ratio** (16:9 / 9:16 / 1:1 / Original) နဲ့ **Fill** (Blur background / Black bars / Crop to fill)၊ **+ Draw Blur Box** / Delete Selected၊ Title (စာ၊ အရွယ်)၊ Logo (ဖိုင်၊ အရွယ်၊ အလင်းဖောက်မှု)၊ Extra Text Box။ |
| အောက်ခြေ | **START / RESUME** — စတယ် (ရပ်ထားတာဆိုရင် ဆက်လုပ်တယ်)။ **STOP SAFELY** — အခု လုပ်နေတဲ့ အဆင့်ပြီးမှ ရပ်ပြီး လုပ်ပြီးသမျှ သိမ်းထားတယ်။ **Open Job Folder** — ထွက်လာတဲ့ ဖိုင်တွေ ဖွင့်ကြည့်ဖို့။ **Edit Text** — မြန်မာ narration ကို စာကြောင်းလိုက် ပြင်ဖို့ (အောက်မှာ ကြည့်ပါ)။ |

**ထွက်လာတဲ့ ဖိုင်:** `jobs\<video နာမည်>_<code>\edge_tts_smart_sync\final_edge_tts_smart_sync.mp4`

Job folder ထဲမှာ ကြည့်လို့ရတဲ့ ဖိုင်တွေ:
- `whisper_transcript.txt` — မူရင်းဘာသာ စာသား
- `timestamp_translations.json` — စာပိုင်းတိုင်းရဲ့ မူရင်း နဲ့ မြန်မာ
- `smart_sync_plan.json` — အချိန်ညှိထားတဲ့ plan
- `run.log` — အလုပ်လုပ်သွားတဲ့ မှတ်တမ်း

## Splitter (ဗီဒီယို အပိုင်းခွဲ)

Window ထိပ်က **Splitter** tab ကို နှိပ်ပါ။ ရှည်တဲ့ video ကို မိနစ်အလိုက် အပိုင်းတွေ ခွဲပေးပါတယ် (TikTok / Reels / Facebook အတွက်)။

| | |
|---|---|
| **+ Videos / + Folder** | Video တစ်ခု (သို့) အများကြီး ထည့်ပါ။ အားလုံးကို setting တူတူနဲ့ တစ်ခုပြီးတစ်ခု ခွဲပါတယ်။ |
| **Save to** | ဗလာထားရင် video ဘေးက `<video နာမည်>_parts\` ထဲ သိမ်းပါတယ်။ Folder ရွေးထားရင် `<ရွေးထားတဲ့ folder>\<video နာမည်>_parts\` ထဲ။ ဖိုင်နာမည် `<video နာမည်>_part_01.mp4`, `_part_02.mp4` … |
| **Each part** | အပိုင်းတစ်ပိုင်း ဘယ်နှမိနစ်လဲ (0.5 … 60)။ နောက်ဆုံး အပိုင်းက အရမ်းတိုရင် (အပိုင်းအရှည်ရဲ့ ¼ နဲ့ 20 s အောက်) ရှေ့အပိုင်းထဲ ပေါင်းပါတယ်။ |
| **Smart cut** | ဖွင့်ထားရင် — အချိန်ပြည့်ချိန်မှာ စကားမဆုံးသေးရင် အများဆုံး **N စက္ကန့်** (default 20) အထိ စောင့်ပြီး စကားရပ်တဲ့နေရာ (စာကြောင်းဆုံး ဖြစ်နိုင်ခြေ အများဆုံး) မှာ ဖြတ်ပါတယ်။ ဥပမာ 3 မိနစ် ရွေးထားရင် 3:00 – 3:20 ကြားမှာ ဖြတ်ပါတယ်။ ပိတ်ထားရင် — 3:00 အတိ ဖြတ်ပါတယ်။ နောက်ခံ သီချင်း ရှိရင်လည်း စကားရပ်တာကို ရှာပါတယ်။ |
| **Check cuts** | ရွေးထားတဲ့ video ကို ဘယ်မှာ ဖြတ်မလဲ Parts ဇယားမှာ ကြိုကြည့်ဖို့။ |
| **Ratio / Fill** | **Original** = မူရင်းအတိုင်း။ **16:9 / 9:16 / 1:1** ဆိုရင် ကွက်လပ်ကို **Blur background** (နောက်ခံ ဝါးထားတဲ့ ပုံ) / Black bars / Crop to fill နဲ့ ဖြည့်ပါတယ်။ |
| **Text Box** | အပိုင်းတိုင်းမှာ ပေါ်မယ့် စာ (မြန်မာစာ ရပါတယ်)။ အရွယ်၊ Opacity၊ နောက်ခံ အမည်းကွက်။ Preview ပေါ်မှာ ဆွဲရွှေ့ပါ။ |
| **Part Number** | **Show** ကို ဖွင့်/ပိတ်ပါ။ `{n}` = 1, 2, 3 · `{mm}` = ၁, ၂, ၃ · `{total}` = အပိုင်း စုစုပေါင်း (`{mm}` သုံးရင် မြန်မာဂဏန်းနဲ့)။ ဥပမာ `Part {n}/{total}` → Part 2/5၊ `အပိုင်း {mm}/{total}` → အပိုင်း ၂/၅။ Preview ပေါ်မှာ ဆွဲရွှေ့ပါ။ |
| **START SPLIT / STOP** | STOP ပြီး ပြန် START ရင် ပြီးပြီးသား အပိုင်းတွေကို ချန်ပြီး ကျန်တာပဲ ဆက်လုပ်ပါတယ်။ Setting ပြောင်းရင် အပိုင်းတွေကို ပြန်လုပ်ပါတယ်။ |

အပိုင်းတိုင်းကို ပြန် encode လုပ်လို့ ဖြတ်တဲ့နေရာ အတိအကျ ဖြစ်ပါတယ် (NVIDIA GPU ရှိရင် NVENC နဲ့ မြန်ပါတယ် — 31 မိနစ် video ကို 9:16 + စာ + Part နံပါတ်နဲ့ 10 ပိုင်း ~4 မိနစ်)။

## Gemini TTS အသံ

**Narrator Voice** မှာ Edge (my-MM-Thiha / Nilar) အပြင် `gemini:Charon`, `gemini:Kore` … (ယောက်ျားသံ ၅ မျိုး၊ မိန်းမသံ ၅ မျိုး)
ရွေးလို့ရပါတယ်။ ဘာသာပြန်တဲ့ `.env` ထဲက key တွေကိုပဲ သုံးပါတယ်။
- စာကြောင်းတိုင်းကို တစ်ခါစီ မေးရတာမို့ request တိုင်းမှာ "narrator တစ်ယောက်တည်း — အသံ၊ အသက်၊ pitch၊ အမြန်နှုန်း
  တစ်ကားလုံး မပြောင်းရ၊ dialogue လည်း အဲ့ narrator ပဲ ဖတ်" ဆိုတဲ့ ညွှန်ကြားချက် အတူတူကို ထည့်ပေးပါတယ် (တစ်ကားလုံး
  အသံမပြောင်းအောင်)။
- **Gemini voice style** အကွက်မှာ ပြောပုံ (ဥပမာ calm storyteller) ရေးလို့ရပါတယ် — အသံကိုယ်တိုင်တော့ မပြောင်းပါ။
- Key တစ်ခုရဲ့ ဒီနေ့ quota ကုန်ရင် နောက် key ကို ပြောင်းသုံးပါတယ်။ အကုန်ကုန်ရင် ရပ်ပြီး ပြီးသားစာကြောင်းတွေ သိမ်းထားလို့
  မနက် START/RESUME နှိပ်ရင် ကျန်တာပဲ ဆက်လုပ်ပါတယ်။ VPN လိုပါတယ် (Gemini က မြန်မာကနေ တိုက်ရိုက် မရ)။

## စာတန်း (Narration Subtitle) နဲ့ Video quality

**Narration Subtitle** (ညာဘက် Production Tools အောက်ဆုံး) — အသံပြောနေတဲ့ မြန်မာစာကို video ပေါ်မှာ စာတန်းအဖြစ် ထည့်ပေးပါတယ်။
- Font (စက်ထဲမှာ ရှိတဲ့ မြန်မာ font တွေ)၊ အရွယ်၊ Bold၊ စာလုံးအရောင်၊ အနားကွပ် (Outline)၊ အရိပ်၊ နောက်ခံ box အရောင် / opacity၊ အကျယ်
  ရွေးလို့ရပါတယ်။ Preview ပေါ်မှာ ဆွဲရွှေ့ပြီး နေရာ ချထားပါ။
- စာကြောင်းရှည်ရင် ၂ ကြောင်းစီ ကတ်တွေ ခွဲပြီး အသံနဲ့ အချိန်ကိုက် ပြပါတယ်။ ကွင်းထဲက English (ဥပမာ "(Zombie)") ကို မပြပါ။
- SRT ဖိုင်ကိုလည်း ထုတ်ပေးပါတယ် — `SRT_for_upload\` folder ထဲမှာ (video ဘေးမှာ မထားပါ၊ နာမည်တူ .srt ရှိရင် VLC / PotPlayer က
  စာတန်း ၂ ထပ် ပြလို့ပါ)။ Subtitle ပိတ်ထားလည်း SRT ထုတ်ပေးပါတယ် (upload လုပ်ဖို့)။

**Quality** (Ratio အောက်) — စက်နိမ့်ရင် video ထုတ်တာ အရမ်းကြာတဲ့ ပြဿနာအတွက်:

| Quality | ဘာလဲ | 20 စက္ကန့် video (CPU, NVIDIA မပါ) |
|---|---|---|
| 1080p — best | အရင်အတိုင်း | ~52 စက္ကန့် |
| 720p — faster | Facebook Reel / TikTok အတွက် လုံလောက် | ~9 စက္ကန့် (~၅.၆ ဆ မြန်) |
| 480p — fastest | စက်နိမ့်အတွက် (ဖုန်းမှာ နည်းနည်း ဝါး) | ~3.6 စက္ကန့် (~၁၄ ဆ မြန်) |

Title / Logo / စာ / စာတန်း အရွယ်တွေကို frame နဲ့ အချိုးကျ လျှော့ပေးလို့ ဘယ် quality မှာမဆို ပုံစံတူပါတယ်။ Quality ပြောင်းရင် video
အပိုင်းတွေပဲ ပြန်လုပ်ပြီး ဘာသာပြန်တာ / အသံ ပြန်မလုပ်ပါ။ Splitter tab မှာလည်း Quality ရွေးလို့ရပါတယ်။

## Smart Sync ဘယ်လိုအလုပ်လုပ်လဲ

- **ရုပ်ကို အပိုင်းခွဲ** — စာပိုင်းတိုင်းက မူရင်း video ရဲ့ ရုပ်တစ်ပိုင်းကို ပိုင်တယ်။ စာပိုင်း ၂ ခုကြားက အသံတိတ်နေရာကို အလယ်ကနေ ခွဲပြီး ဘေးက စာပိုင်း ၂ ခုကို ဝေပေးတယ်။ Video ရဲ့ ပထမ frame ကနေ နောက်ဆုံး frame အထိ ဘာမှ မကျန်ပါဘူး (V2 full coverage)။
- **အရှည်ကို အသံနဲ့ ညှိ** — ရုပ်တစ်ပိုင်းစီကို မြန်မာအသံ အရှည်အတိုင်း ဖြစ်အောင် နှေးတာ / မြန်တာ (`setpts`) လုပ်တယ်။
- **အမြန်ဆုံး ၁.၂၅ ဆ** — ရုပ်ကို ၁.၂၅ ဆထက် ပိုမမြန်စေဘူး (`max_video_speed`)။ အသံက ဒီထက်တိုနေသေးရင် အဲ့အပိုင်းရဲ့ နောက်ဆုံးက ရုပ်နည်းနည်းကို ဖြတ်တယ်။ အသံက ပိုရှည်ရင် ရုပ်ကို နှေးပေးတယ်။
- **Frame ကို တွဲတွက်** — အပိုင်းတိုင်းရဲ့ frame အရေအတွက်ကို အသံရဲ့ စုစုပေါင်း အချိန်နဲ့ တွက်တယ် (30 fps)။ အပိုင်း ရာနဲ့ချီ ရှိနေတောင် ရုပ်နဲ့ အသံ frame တစ်ဝက်ထက် ပိုမကွာဘူး။ အဆုံးမှာ log က `SYNC OK: picture=… narration=… diff=…` လို့ ပြပါတယ်။
- **ပုံစံ (Ratio / Fill)** — NVIDIA ရှိရင် NVENC၊ မရှိရင် libx264 နဲ့ ထုတ်တယ်။

  | Ratio | Video အရွယ် |
  |---|---|
  | 16:9 (default) | 1920×1080 |
  | 9:16 (TikTok / Reels / Shorts) | 1080×1920 |
  | 1:1 | 1080×1080 |
  | Original | မူရင်း video ရဲ့ ပုံစံအတိုင်း (အရှည်ဘက် အများဆုံး 1920) |

  မူရင်းနဲ့ ပုံစံမတူရင် (ဥပမာ 16:9 video ကို 9:16 လုပ်ရင်) **Fill** နဲ့ ရွေးပါ:
  - **Blur background** — ပုံတစ်ခုလုံး မြင်ရပြီး ဘေးကွက်လပ်မှာ အဲ့ပုံကိုပဲ ဝါးပြီး ဖြည့်တယ်။
  - **Black bars** — ဘေးကွက်လပ်ကို အမည်းနဲ့ ဖြည့်တယ်။
  - **Crop to fill** — ပုံကို ချဲ့ပြီး frame ပြည့်အောင် လုပ်တယ်။ ဘေးက ပိုတဲ့အပိုင်းကို ဖြတ်တယ်။

  Zoom / Flip နဲ့ Title၊ Logo၊ Blur box တွေက ရွေးထားတဲ့ Ratio အတိုင်း ထွက်ပြီး preview မှာလည်း ဒီအတိုင်း ပြတယ်။

## Gemini key နဲ့ ကန့်သတ်ချက်

- Gemini ကို **ဘာသာပြန်ဖို့ပဲ** သုံးတယ်။ English ကို စာသားပြောင်းတာက စက်ထဲမှာ Whisper နဲ့ လုပ်တယ်။
- အခမဲ့ key မှာ တစ်ရက်ကို သုံးလို့ရတဲ့ အကြိမ်ရေ ကန့်သတ်ထားတယ် (Google project တစ်ခုချင်းစီ အလိုက်)။ ပြည့်ရင်:
  - နောက် key ကို အလိုလို ပြောင်းတယ်။
  - Key တွေ အကုန်ပြည့်ရင် နောက် model ကို ပြောင်းတယ် (`gemini-3.5-flash → 3.5-flash-lite → 3.6-flash → 3.7-flash → 3.1-flash-lite`)။
  - အကုန်ပြည့်သွားရင် ရပ်သွားပေမဲ့ ပြီးသမျှ မပျောက်ဘူး။ နောက်နေ့ (သို့) key အသစ်ထည့်ပြီး **START / RESUME** နှိပ်ရင် ရပ်ခဲ့တဲ့နေရာကနေ ဆက်တယ်။
- Gemini ကို VPN / proxy နဲ့မှ သုံးလို့ရတဲ့ စက်ဆိုရင် `.env` ထဲမှာ `GEMINI_PROXY=http://127.0.0.1:10808` (ကိုယ့် proxy လိပ်စာ) ထည့်ပါ။ `127.0.0.1:10808` (v2rayN) ဖွင့်ထားရင် အလိုလို သုံးပါတယ်။ အမြဲ တိုက်ရိုက်ပဲ သုံးချင်ရင် `GEMINI_PROXY=none` ထည့်ပါ။ Edge TTS ကတော့ proxy မသုံးဘဲ တိုက်ရိုက် အရင်စမ်းပါတယ်။

## အဆင့်မြင့် ပြင်ဆင်ချက် (`config.json`)

Tool ဖွင့်ပြီး START နှိပ်လိုက်ရင် `config.json` ကို အလိုလို ဖန်တီးပေးပါတယ် (UI မှာ ရွေးထားတာတွေ သိမ်းဖို့ပါ)။ လိုမှပဲ ပြင်ပါ:

| Key | Default | အဓိပ္ပာယ် |
|---|---|---|
| `ffmpeg_path`, `ffprobe_path` | (အလိုလို ရှာ) | FFmpeg ဖိုင် လမ်းကြောင်း |
| `python_path` | (အလိုလို ရှာ) | `RUN.bat` သုံးမယ့် Python |
| `max_video_speed` | `1.25` | ရုပ်ကို မြန်စေနိုင်တဲ့ အများဆုံး ဆ |
| `translation_batch_max_items` | `40` | Gemini တစ်ခါမေးရင် ပါမယ့် စာပိုင်းအရေအတွက် |
| `atomic_target_duration`, `atomic_max_duration` | `4.2`, `5.6` | စာပိုင်းတစ်ပိုင်းရဲ့ အရှည် (စက္ကန့်) |
| `translation_audit` | `true` | ပြန်ပြီးတိုင်း စစ်ဆေးတဲ့ အဆင့် |
| `title_font_path` | `C:\Windows\Fonts\mmrtext.ttf` | Title / Extra text ဖောင့် |
| `overlay_blur_strength` | `18` | Blur box ရဲ့ ဝါးအား |
| `whisper_model_other` | `medium` | English မဟုတ်တဲ့ ဘာသာအတွက် Whisper model (NVIDIA GPU မရှိတဲ့ စက်မှာ `small` က ပိုမြန်တယ်) |

## စာကြောင်း ခွဲပုံ

English စာကို **စာကြောင်း (sentence) တစ်ကြောင်းချင်း** ခွဲပြီး ဘာသာပြန်ပါတယ် (VoxCPM recap လိုပါပဲ)။ စာကြောင်း တစ်ဝက်ကနေ မဖြတ်တော့လို့ Gemini က စာကြောင်းတစ်ကြောင်းကို နှစ်ခါ မပြောတော့ပါဘူး။ စာကြောင်းရှည်ရင် ကော်မာ (သို့) အသက်ရှူတဲ့ နေရာမှာ ဖြတ်ပါတယ် (အများဆုံး ၂၄ စက္ကန့်)။ Version အဟောင်းနဲ့ ဘာသာပြန်ပြီးသား job ကို resume လုပ်ရင်တော့ ဖြတ်ပုံဟောင်း (၄–၆ စက္ကန့်) နဲ့ပဲ ဆက်လုပ်ပါတယ် — ဘာသာပြန်ပြီးသားနဲ့ အသံတွေ မပျက်အောင်ပါ။

## စာသား ပြင်နည်း (Edit Text)

ဘာသာပြန်ပြီးသွားရင် **Edit Text** နှိပ်ပြီး စာကြောင်းတိုင်းရဲ့ English မူရင်းနဲ့ မြန်မာ narration ကို ဘေးချင်းယှဉ် ကြည့်ပြီး ပြင်လို့ရပါတယ်။
- **Prev / Next / Go** — စာကြောင်း ရွှေ့ကြည့်ပါ။ **Next problem** — English စာလုံး၊ တခြားဘာသာ စာလုံး ရောနေတဲ့ စာကြောင်းကို ရှာပေးပါတယ်။
- ပြင်ပြီး **Save** နှိပ်ပါ → **START / RESUME** နှိပ်ရင် ပြင်ထားတဲ့ စာကြောင်းကိုပဲ အသံ အသစ်ထုတ်ပြီး ကျန်တာ ပြန်သုံးပါတယ်။
- Render လုပ်နေရင်း စာကြောင်းတစ်ကြောင်း အသံထွက်မလာလို့ ရပ်သွားရင် (ဥပမာ English နဲ့ မြန်မာ ရောနေလို့) ဘယ်စာကြောင်းမှာ ရပ်လဲ ပြပြီး Edit Text ကို အဲ့စာကြောင်းမှာ ဖွင့်ပေးပါတယ်။

## ပြဿနာ ဖြေရှင်းနည်း

| တွေ့ရတာ | လုပ်ရမယ့်အရာ |
|---|---|
| `Python with the required packages was not found` | `INSTALL_REQUIREMENTS.bat` ကို ပြန် run ပါ။ Python 3.12 ကို PATH ထဲ ထည့်ထားဖို့ လိုပါတယ်။ |
| `Gemini API key မတွေ့ပါ` | `.env` ရှိမရှိ၊ `GEMINI_API_KEY=` နောက်မှာ key ပါမပါ စစ်ပါ။ UI ရဲ့ **Gemini .env** မှာ မှန်ကန်တဲ့ ဖိုင်ကို ရွေးပါ။ |
| `key pool exhausted` / 429 | ဒီနေ့ ကန့်သတ်ချက် ပြည့်သွားလို့ပါ။ Key ထပ်ထည့်ပါ (သို့) နောက်နေ့ **START / RESUME** နှိပ်ပါ။ |
| `open() got an unexpected keyword argument 'metadata_errors'` | `av` version အသစ် (19) ကြောင့်ပါ။ Repo အသစ်ကို ပြန် download လုပ်ပြီး `INSTALL_REQUIREMENTS.bat` ကို ပြန် run ပါ (`av==18.0.0` ကို သွင်းပေးပါမယ်)။ |
| Log မှာ `GPU Whisper failed … using the CPU instead` | NVIDIA GPU ရှိပေမဲ့ CUDA 12 library (cuBLAS/cuDNN) မရှိလို့ CPU နဲ့ ဆက်လုပ်တာပါ။ အလုပ်ပြီးပါတယ်၊ နည်းနည်းပဲ ပိုကြာပါတယ်။ |
| `You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN…` ပြပြီး ရပ်နေသလို ဖြစ်နေတယ် | HF token **မလိုပါဘူး**။ Warning သက်သက်ပါ။ ပထမဆုံးအကြိမ်မှာ Whisper model (English ~460 MB၊ တခြားဘာသာ ~1.5 GB) ကို download လုပ်နေတာပါ။ Log မှာ `⬇️ Whisper model: … MB downloaded` လို့ ၅ စက္ကန့်တစ်ခါ ပြပါတယ်။ တစ်ခါပဲ download လုပ်ရပါတယ်။ huggingface.co မဖွင့်ရတဲ့ စက်ဆိုရင် VPN သုံးပါ (သို့) `.env` ထဲမှာ `HF_ENDPOINT=https://hf-mirror.com` ထည့်ပါ။ |
| Edge TTS `NoAudioReceived` | Internet ကို စစ်ပါ။ Tool က တိုက်ရိုက် ၂ ကြိမ်၊ system proxy နဲ့ ၂ ကြိမ် ပြန်စမ်းပါတယ်။ English စာလုံး ရောနေတဲ့ စာကြောင်းဆိုရင် English စာလုံးတွေ ချန်ပြီး တစ်ခါ ထပ်စမ်းပါတယ်။ |
| `403, message='Invalid response status'` (`WSServerHandshakeError`) | Microsoft ရဲ့ အသံ service က ချိတ်ဆက်မှုကို ငြင်းတာပါ — VPN / proxy server တော်တော်များများကို ငြင်းပါတယ်။ **VPN ဖွင့်ထားရင် ပိတ်ပါ** (သို့) server ပြောင်းပါ။ ကွန်ပျူတာ နာရီ/Time zone ကို Settings → Time & language → Set time automatically နဲ့ မှန်အောင်ထားပါ။ မရသေးရင် `INSTALL_REQUIREMENTS.bat` ကို ပြန် run ပါ (edge-tts ကို update လုပ်ပါတယ်)။ ပြီးရင် **START / RESUME**။ VPN မပါရင် မရတဲ့ network ဆိုရင် `.env` ထဲမှာ `EDGE_TTS_PROXY=http://127.0.0.1:<port>` ထည့်ပါ။ |
| `Whisper က … စကားကို ကောင်းကောင်း မကြားရပါဘူး` (သို့) `whisper_transcript.txt` ထဲမှာ "I'm not going to do it." လို စာကြောင်း တူတူတွေ ထပ်ခါထပ်ခါ ရေးထားတယ် | Whisper က ဘာသာ မှားပြီး နားထောင်နေတာပါ (ဥပမာ ဟိန္ဒီ video ကို English လို)။ **Source language** မှာ မှန်တဲ့ ဘာသာကို ရွေးပြီး (သို့) Auto-detect နဲ့ **START / RESUME** ပြန်နှိပ်ပါ။ ဘာသာ မှန်ပါလျက် ဒီ error တက်ရင် `whisper_transcript.txt` ကို စစ်ပါ (သီချင်း / ဆူညံသံ များတာ ဖြစ်နိုင်ပါတယ်)။ ဘာသာပြန်မစခင် ရပ်တာမို့ Gemini quota မကုန်ပါဘူး။ |
| `The video already speaks Burmese` | Auto-detect က မြန်မာစကားလို့ ကြားတာပါ။ မှားရင် Source language မှာ ရွေးပါ။ |
| Gemini `User location is not supported for the API use` | Gemini က ကိုယ့် internet (VPN server) ရဲ့ နိုင်ငံကို လက်မခံတာပါ။ VPN server (နိုင်ငံ) ပြောင်းပြီး **START / RESUME** ပြန်နှိပ်ပါ။ |
| `Edge TTS FAILED at segment 123` | အဲ့စာကြောင်းမှာ အသံ မထွက်လို့ ရပ်တာပါ။ **Yes** နှိပ်ရင် Edit Text ပွင့်လာပါမယ် — မြန်မာလို ပြင်ပြီး Save → **START / RESUME**။ |
| `Gemini JSON response failed after 3 attempts` | Gemini ရဲ့ အဖြေ ပျက်နေတာပါ။ **START / RESUME** ပြန်နှိပ်ရင် ဆက်လုပ်ပါတယ်။ (Story context အဆင့်မှာဆိုရင် အခု version က အဲ့အပိုင်းကို ချန်ပြီး ဆက်သွားလို့ မရပ်တော့ပါ။) |
| `[WinError 2] The system cannot find the file specified` (သို့) `ffmpeg.exe မတွေ့ပါ` (Preview မှာ `00:00 / 00:00`) | FFmpeg မရှိလို့ပါ။ `INSTALL_REQUIREMENTS.bat` ကို ပြန် run ပါ (FFmpeg ကို `ffmpeg\` ထဲ ထည့်ပေးပါမယ်)။ (သို့) gyan.dev ကနေ download လုပ်ပြီး `ffmpeg.exe`၊ `ffprobe.exe` ကို `RUN.bat` ဘေးက `ffmpeg` folder ထဲ ထည့်ပါ။ |
| Title မြန်မာစာ မပေါ်ဘူး | `py -3.12 -m playwright install chromium` ကို run ပါ။ ဖောင့်ကို `RECAP_MM_FONT` (environment variable) (သို့) `title_font_path` နဲ့ ပြောင်းလို့ရပါတယ်။ |
| Log မှာ `⚠️ ID 00012: removed letters of another script` | Gemini က မြန်မာစာထဲ တခြားဘာသာ စာလုံး ထည့်ခဲ့လို့ ဖယ်ထားတာပါ။ အဲ့စာကြောင်းကို `timestamp_translations.json` ထဲမှာ ကြည့်ပါ။ |

## Folder ဖွဲ့စည်းပုံ

```
RUN.bat                    UI ဖွင့်ဖို့
INSTALL_REQUIREMENTS.bat   Python package + Chromium သွင်းဖို့
.env.example               Gemini key ပုံစံ (.env လို့ copy ကူးပါ)
requirements.txt
app/
  controller.py            UI (tkinter): preview၊ overlay၊ job တွေ စီမံတာ
  planner_worker.py        အဆင့် ၁: Whisper → story context → ဘာသာပြန် → Smart Sync plan
  recap_planner.py         Planner (စာပိုင်းခွဲ၊ Gemini prompt၊ audit၊ ID စစ်တာ)
  render_worker.py         အဆင့် ၂: Edge TTS → Smart Sync render
  core.py                  Edge TTS, Short pauses, Smart Sync, overlay, mux
  preview_tools.py         Preview frame / logo
  splitter.py              Splitter: ဘယ်မှာ ဖြတ်မလဲ (smart cut)၊ အပိုင်း render
  splitter_tab.py          Splitter tab UI
  subtitle_png.py          Narration subtitle: Chromium နဲ့ စာတန်းပုံ (PNG) ထုတ်၊ အချိန်ကိုက်၊ SRT
  subtitle_fonts.py        စက်ထဲက မြန်မာ font စာရင်း
  recap_subtitles.py       Narration Subtitle UI (font / အရောင် / box …)
  gemini_tts.py            Gemini TTS narrator (တစ်ကားလုံး narrator တစ်ယောက်တည်း)
  launch.ps1               Python ရှာပြီး UI ဖွင့်တာ
recap_runtime/services/
  whisper_service.py       faster-whisper (GPU / CPU)
  ai_service.py            Gemini client (proxy option)
services/
  text_overlay_service.py  မြန်မာ title စာကို Chromium နဲ့ ပုံထုတ်တာ
tests/                     python -m unittest discover -s tests
```

## Test

```bat
py -3.12 -m unittest discover -s tests
```
Internet မလိုပါဘူး။ Gemini ကို အတုနဲ့ အစားထိုး စမ်းပါတယ်။

## သတိပြုရန်

- Edge TTS က Microsoft ရဲ့ online ဝန်ဆောင်မှုပါ။ Gemini ကတော့ Google ရဲ့ API ပါ။ သူတို့ရဲ့ စည်းကမ်းချက်တွေကို လိုက်နာပါ။
- သုံးမယ့် video ရဲ့ မူပိုင်ခွင့်ကို ကိုယ်တိုင် တာဝန်ယူပါ။

---

## English

**Recap → Myanmar** turns a recap/story video narrated in any language Whisper knows (English, Chinese,
Hindi, Korean, Japanese, Thai, …) into a Myanmar-narrated one on Windows. The **Splitter** tab cuts long
videos into parts.

### How it works
1. **Listen** — local Whisper (faster-whisper; NVIDIA GPU or CPU) writes the speech with word timestamps.
   **Source language** = Auto-detect lets the multilingual `base` model listen to the first 8 minutes
   first; English is heard by `small.en` (~460 MB), any other language by the multilingual `medium`
   (~1.5 GB; `"whisper_model_other": "small"` in config.json is faster on a PC without an NVIDIA GPU).
   Hindi and Urdu sound alike, so an Auto-detected "Urdu" is written as Hindi (choose Urdu to keep Urdu
   letters). Where Whisper writes few sentence marks, the end of a Whisper segment counts as a sentence end.
2. **Split** — sentence/clause/pause boundaries give short sync units (about 4.2 s, at most 5.6 s);
   more units = more sync anchors.
3. **Story memory** — Gemini reads the whole transcript first and keeps names, relationships and
   places consistent.
4. **Translate** — Gemini translates 40 units per request into natural spoken Burmese narration
   (no summary, no shortening, every unit keeps its own content), then an audit pass repairs
   omissions/shifts/duplicates. Letters of another script inside the Burmese (e.g. Georgian "მის"
   inside "ဧည့်ခန်း") are asked again, and if still there removed and logged.
5. **Voice** — Microsoft Edge TTS Myanmar voices (Thiha / Nilar). "Short pauses" trims the silence
   Edge puts around each clip (~0.25 s between lines instead of ~1 s).
6. **Smart Sync** — every unit owns a window of the original picture (the silence between two units
   is split at its middle, so the whole video is used). Each window is slowed down or sped up to the
   length of its Myanmar voice; it never plays faster than 1.25× (`max_video_speed`), and when the
   voice is shorter still the end of that window is cut. Frame counts are cumulative at 30 fps, so
   even hundreds of parts stay within half a frame of the voice (`SYNC OK … diff=…` in the log).
   Output ratio **16:9** (1920×1080), **9:16** (1080×1920), **1:1** (1080×1080) or **Original**
   (the source shape, long side at most 1920); when the source has another shape, **Fill** decides:
   Blur background, Black bars or Crop to fill. Optional zoom/flip; NVENC or libx264.
7. **Production tools** — blur boxes, title, logo and an extra text box placed on the preview.

The output has only the Myanmar voice (no original audio or music).

### Requirements
Windows 10/11 64-bit · Python 3.12 64-bit (with tcl/tk, on PATH) · FFmpeg (`ffmpeg.exe` +
`ffprobe.exe` on PATH, in `C:\ffmpeg\bin`, or in a folder named `ffmpeg` here) · a free Gemini API
key ([aistudio.google.com/apikey](https://aistudio.google.com/apikey)) · internet. An NVIDIA GPU is
optional (without the CUDA 12 libraries Whisper falls back to the CPU by itself).

### Install
1. Download the repo (Code → Download ZIP) and unzip it.
2. Run **`INSTALL_REQUIREMENTS.bat`** (pip packages, Chromium for the Myanmar title renderer, and
   FFmpeg: when it is not on PATH or in `C:\ffmpeg\bin`, about 100 MB is downloaded into `ffmpeg\`).
   `[WinError 2] The system cannot find the file specified` means FFmpeg is missing — run it again.
3. Copy **`.env.example`** to **`.env`** and set `GEMINI_API_KEY=`. More keys
   (`GEMINI_IMAGE_PROJECT_1_KEY`, `GEMINI_IMAGE_PROJECT_2_KEY`, …) are used in turn when one is used
   up; after all keys the next model is tried
   (`gemini-3.5-flash → 3.5-flash-lite → 3.6-flash → 3.7-flash → 3.1-flash-lite`).
   If Gemini needs a proxy, add `GEMINI_PROXY=http://host:port` (a running v2rayN on
   `127.0.0.1:10808` is used automatically; `GEMINI_PROXY=none` forces direct).

Never share or commit your `.env` (it is in `.gitignore`).

The first run downloads the Whisper model (~460 MB for English, ~1.5 GB for other languages) from
huggingface.co; the log shows
`⬇️ Whisper model: … MB downloaded`. No account or HF_TOKEN is needed — the "unauthenticated
requests" line is only a warning. If huggingface.co does not open, use a VPN or set
`HF_ENDPOINT=https://hf-mirror.com` in `.env`.

### Use
Double-click **`RUN.bat`**:
- **Source Video** → Browse (or **Folder** for a batch; finished videos are skipped).
- **Save final to** — when a folder is chosen, each finished video is also saved there as
  `<video name>_Myanmar.mp4`.
- **Source language** (Auto-detect, English, Chinese, Hindi, …), **Edge TTS Voice / Speed** on the left.
- **Preview** in the middle: seek, Refresh Frame, drag the title/logo/text, draw blur boxes.
- **Production Tools** on the right: Zoom, Flip, Voice vol, Short pauses, Ratio + Fill, blur,
  title, logo, extra text.
- **START / RESUME** — starts or continues; **STOP SAFELY** — stops at a safe point and keeps
  everything; **Open Job Folder**; **Edit Text** — read each English line next to its Burmese narration,
  fix the Burmese and Save; START / RESUME then re-voices only the edited lines. When a line gets no
  audio (e.g. English and Burmese mixed), the error names the line and offers to open Edit Text on it.
- Lines are whole English sentences (like the VoxCPM recap tool), so a sentence is never cut in two and told
  twice; a long sentence ends at a comma or a breath (24 s at most). A job translated with an older version
  keeps its 4-6 s lines when resumed.
- When Whisper listens for the wrong language it writes a few phrases again and again ("I'm not going to do
  it." ×40); when a quarter of the Whisper lines repeat, the job stops before translating (no Gemini quota
  used) — choose the right Source language (or Auto-detect) and start again.
- Gemini `User location is not supported for the API use`: Gemini refuses the country of your internet /
  VPN server — change the VPN server and START / RESUME.

### Splitter tab
- **+ Videos / + Folder**, **Save to** (empty = `<video folder>\<name>_parts\`; files `<name>_part_01.mp4` …).
- **Each part** N minutes. **Smart cut** on: when the time is up in the middle of speech, it waits up to
  20 s (adjustable) and cuts in the pause most likely to end a sentence (also under background music); off:
  exact cuts. A last piece shorter than a quarter part (and 20 s) joins the part before it.
  **Check cuts** lists where the selected video will be cut.
- **Ratio** Original / 16:9 / 9:16 / 1:1 with **Fill** Blur background / Black bars / Crop to fill.
- **Text Box** and **Part Number** (`{n}` 1 2 3, `{mm}` ၁ ၂ ၃, `{total}` — in Myanmar digits too when `{mm}` is
  used), size / opacity / dark box, dragged on the preview.
- **START SPLIT / STOP**: a stopped split goes on from the first unfinished part; changed settings remake
  the parts. Every part is re-encoded so cuts are exact (NVENC when available).
- Edge TTS `403 Invalid response status`: Microsoft refuses many VPN / proxy servers — turn the VPN off (or
  change server), set the Windows clock automatically, or run INSTALL_REQUIREMENTS.bat again; on a network that
  needs a proxy put `EDGE_TTS_PROXY=http://127.0.0.1:<port>` in the .env.

Result: `jobs\<name>_<code>\edge_tts_smart_sync\final_edge_tts_smart_sync.mp4`
(plus `whisper_transcript.txt`, `timestamp_translations.json`, `smart_sync_plan.json`, `run.log`).

### Gemini TTS voice
**Narrator Voice** also lists `gemini:Charon`, `gemini:Kore`, … (5 male, 5 female) next to the Edge voices; they use the
keys of the same `.env`. Every line is its own request, so each one carries the same "one continuous narrator"
direction (same voice, age, pitch and pace for the whole video; dialogue read by that narrator). **Gemini voice
style** adds a delivery preference (e.g. calm storyteller) without changing the voice. A key whose daily quota is
used up is skipped; when all are, the run stops and finished lines are kept for START/RESUME. Needs a VPN in
Myanmar.

### Narration subtitles and video quality
**Narration Subtitle** (bottom of Production Tools): the spoken Burmese is burned in as subtitles — installed
Myanmar font, size, bold, text / outline colour, outline width, shadow, box colour and opacity, width; drag it on
the preview. Long lines become two-line cards timed on the voice; English glosses in ( ) are not shown. An SRT is
always written to `SRT_for_upload\` (not next to the video, where players would show it twice).

**Quality** (under Ratio): 1080p (as before) / 720p / 480p. Measured on 4 CPU threads without an NVIDIA card,
20 s of video: 1080p 52 s, 720p 9 s, 480p 3.6 s. Title, logo, text and subtitle sizes are scaled so the look is
the same; changing it re-renders only the video parts (translation and voice are kept). Splitter has it too.

### Advanced (`config.json`, created on the first START)
`ffmpeg_path`, `ffprobe_path`, `python_path`, `max_video_speed` (1.25),
`translation_batch_max_items` (40), `atomic_target_duration` / `atomic_max_duration` (4.2 / 5.6),
`translation_audit` (true), `title_font_path`, `overlay_blur_strength` (18),
`whisper_model_other` ("medium"; the Whisper model for languages other than English).

### Tests
`py -3.12 -m unittest discover -s tests` (offline; Gemini is mocked).

### Notes
Edge TTS is a Microsoft online service and Gemini is a Google API — follow their terms. You are
responsible for the rights to the videos you process.


---

---

---

## Recap Studio Tools / Recap Studio ကိရိယာများ (Feature Branch)

ဒီအပိုင်းမှာ **feature/studio-expansion branch** ထဲ ထည့်ထားတဲ့ Feature အသစ်တွေကို မြန်မာလို အသေးစိတ်ရှင်းပြထားပါတယ်။ အောက်မှာ English ရှင်းလင်းချက်ကိုလည်း တွဲဖော်ပြထားပါတယ်။

**အရေးကြီး / Branch အခြေအနေ:** ဒီ Feature တွေဟာ \`feature/studio-expansion\` branch မှာပဲ ရှိပါသေးတယ်။ \`main\` branch ထဲကို မပေါင်းရသေးသလို မူရင်း upstream repository ကိုလည်း မပြောင်းထားပါဘူး။ စမ်းသပ်ပြီးမှ Merge လုပ်ဖို့ သီးခြားထားတာပါ။

**English:** The new Studio features described below are available on \`feature/studio-expansion\`. They have not been merged into this fork's \`main\` branch, and the original upstream repository remains separate.

### Feature Branch ကို ဘယ်လိုရယူမလဲ / How to Get This Branch

1. [ဒီ Repository ကိုဖွင့်ပါ](https://github.com/SourcePlease/recap-en-to-mm)။
2. GitHub ရဲ့ **Branch** ရွေးတဲ့နေရာမှာ \`main\` အစား **\`feature/studio-expansion\`** ကို ရွေးပါ။
3. **Code → Download ZIP** ကိုနှိပ်ပြီး ZIP ဖိုင်ကို ဖြည်ပါ။
4. အောက်က မူလ Install လုပ်နည်းအတိုင်း လိုအပ်တဲ့ Python, FFmpeg နဲ့ API Key တွေ ပြင်ဆင်ပြီး \`INSTALL_REQUIREMENTS.bat\` ကို အရင်ဖွင့်ပါ။ ပြီးရင် \`RUN.bat\` နဲ့ App ကို စတင်နိုင်ပါတယ်။

**English:** Open the repository, switch the branch selector to \`feature/studio-expansion\`, then choose **Code → Download ZIP**. Extract it and follow the installation instructions above before launching \`RUN.bat\`.

### App ထဲမှာ ပါဝင်တဲ့ Tab များ / Tabs Included

#### 1. Recap — ဘာသာပြန်အသံဖြင့် Video ပြန်ထုတ်ခြင်း

**မြန်မာ:** ဒီ Tab က မူရင်း Video ထဲက ပြောထားတဲ့ ဘာသာစကားကို Whisper နဲ့ စာသားပြောင်းပြီး၊ ရွေးထားတဲ့ Target Language နဲ့ ပြန်ရေးပေးပါတယ်။ ပြီးရင် ရွေးထားတဲ့ TTS အသံနဲ့ ပြန်ဖတ်စေပြီး မူရင်း Video ရဲ့ ရုပ်ပုံနဲ့ အသံအသစ်ကို အချိန်ကိုက်ညှိကာ Video အသစ် ထုတ်ပေးပါတယ်။ မူလ Default က Myanmar (Burmese) ဖြစ်ပါတယ်။

- **Source Language:** မူရင်း Video မှာ ဘယ်ဘာသာစကား ပြောထားလဲ ရွေးနိုင်ပါတယ်။ မသိရင် Auto-detect သုံးနိုင်ပါတယ်။ မှားယွင်းသိရှိနေတယ်လို့ ထင်ရင် ကိုယ်တိုင် မှန်ကန်တဲ့ ဘာသာစကားကို ရွေးပေးပါ။
- **Target Language:** နောက်ဆုံးထွက်လာမယ့် ဘာသာစကားကို ရွေးတာပါ။ Myanmar ကိုသာမက English နဲ့ အခြားဘာသာစကားတွေလည်း ရွေးနိုင်ပါတယ်။
- **Story Context:** ဘာသာပြန်မစခင် ဇာတ်လမ်းထဲက ဇာတ်ကောင်အမည်၊ အချင်းချင်း ဆက်နွယ်မှု၊ နေရာနဲ့ အသုံးအနှုန်းတွေကို မှတ်သားထားပါတယ်။ ဒါကြောင့် အမည်တစ်ခုတည်းကို Video တစ်လျှောက် ပုံစံတစ်မျိုးတည်းနဲ့ သုံးနိုင်ဖို့ ကူညီပေးပါတယ်။
- **Translation Audit:** ပြန်ထားတဲ့စာမှာ အကြောင်းအရာ ပျောက်သွားတာ၊ တစ်ပိုင်းရဲ့အကြောင်းအရာ နောက်တစ်ပိုင်းထဲ ရွှေ့သွားတာ၊ ထပ်ပြောထားတာတွေ ရှိမရှိ စစ်ဆေးပါတယ်။ Myanmar ကို ရွေးထားတဲ့အခါ မြန်မာစကားပြောပုံ သဘာဝကျမကျကိုလည်း စစ်ပြီး မသဘာဝကျတဲ့ စာကြောင်းတွေကို ပြန်ပြင်ဖို့ ညွှန်ကြားထားပါတယ်။
- **Narrator TTS:** Edge TTS နဲ့ Gemini TTS အပြင် API Key ထည့်ထားမှ အသုံးပြုနိုင်တဲ့ Azure Speech နဲ့ ElevenLabs လည်း ရွေးနိုင်ပါတယ်။ Provider တစ်ခုချင်းစီရဲ့ အသံအရည်အသွေး၊ ဘာသာစကားပံ့ပိုးမှုနဲ့ Quota က မတူနိုင်ပါဘူး။
- **Smart Sync:** မြန်မာအသံ (သို့မဟုတ် ရွေးထားတဲ့ Target Language အသံ) ရဲ့ အရှည်ကို အခြေခံပြီး မူရင်း Video အပိုင်းတွေကို လိုအပ်သလို အမြန်နှုန်းညှိ၊ ဖြတ်တောက်ကာ အသံနဲ့ ရုပ်ကို ကိုက်ညီအောင် လုပ်ပါတယ်။
- **Stop / Resume:** အလုပ်လုပ်နေတုန်း လုံခြုံစွာ ရပ်ထားပြီး နောက်မှ ပြန်ဆက်နိုင်ပါတယ်။ ပြီးထားတဲ့ Transcript, Translation နဲ့ TTS Cache တွေကို အခြေအနေအလိုက် ပြန်သုံးနိုင်ပါတယ်။
- **Folder Batch:** Video တစ်ခုချင်း Browse လုပ်မယ့်အစား Folder တစ်ခုလုံး ရွေးပြီး တစ်ခုပြီးတစ်ခု လုပ်နိုင်ပါတယ်။
- **Preview Editor:** Video Frame ကို အချိန်ရွှေ့ကြည့်ပြီး Title, Logo, Extra Text နဲ့ Blur Box တွေကို Preview ပေါ်မှာ နေရာရွှေ့ပြင်နိုင်ပါတယ်။
- **Subtitle / Quality:** Narration စာတန်းကို Video ထဲ ထည့်နိုင်ပြီး Upload သုံးဖို့ SRT ဖိုင်လည်း ရရှိနိုင်ပါတယ်။ 1080p, 720p, 480p Quality ကို စက်စွမ်းဆောင်ရည်နဲ့ ကိုက်ညီအောင် ရွေးနိုင်ပါတယ်။

**မြန်မာစာ ဘာသာပြန်ပုံစံ:** Myanmar ကို Target အဖြစ် ရွေးထားတဲ့အခါ စာပေ/ရုံးသုံးဆန်တဲ့ တိုက်ရိုက်ဘာသာပြန်မဟုတ်ဘဲ မြန်မာလူတစ်ယောက်က ဇာတ်လမ်းကို ပရိသတ်ကို ပြောပြနေသလို ရှင်းလင်းသဘာဝကျတဲ့ စကားပြောပုံစံကို ဦးစားပေးဖို့ Prompt ထဲမှာ ညွှန်ကြားထားပါတယ်။ ဒါပေမဲ့ AI ရဲ့ အဖြေတိုင်းကို လူကဖတ်စစ်ဖို့ လိုနိုင်ပါသေးတယ်။ ဘာသာပြန်အရည်အသွေးဟာ မူရင်းအသံ ရှင်းလင်းမှု၊ ဇာတ်လမ်း Context နဲ့ အသုံးပြုတဲ့ AI Model ပေါ်လည်း မူတည်ပါတယ်။

**English:** Recap transcribes the source audio, translates it into the selected target language, generates narration with the chosen TTS provider, and adjusts the source footage to match the new narration. It includes story context, translation checks, safe Stop/Resume, folder batch processing, draggable preview overlays, blur boxes, subtitles and output-quality options. Myanmar output has a dedicated spoken-Burmese style guide, but AI translations should still be proofread.

#### 2. Splitter — Video ကို အပိုင်းခွဲခြင်း

**မြန်မာ:** ရှည်လျားတဲ့ Video တစ်ခုကို TikTok, Reels, Facebook သို့မဟုတ် အခြား Platform တွေမှာ တင်ရလွယ်အောင် သတ်မှတ်ထားတဲ့ မိနစ်အလိုက် အပိုင်းငယ်တွေ ခွဲပေးတဲ့ Tab ဖြစ်ပါတယ်။

- **Videos / Folder:** Video တစ်ခုတည်းဖြစ်ဖြစ်၊ Folder တစ်ခုထဲက Video အများအပြားဖြစ်ဖြစ် ထည့်နိုင်ပါတယ်။
- **Each Part:** အပိုင်းတစ်ပိုင်းစီရဲ့ ကြာချိန်ကို 0.5 မိနစ်ကနေ 60 မိနစ်အထိ သတ်မှတ်နိုင်ပါတယ်။
- **Smart Cut:** သတ်မှတ်ထားတဲ့ အချိန်တိတိမှာ စကားပြောနေဆဲဖြစ်ရင် ချက်ချင်းမဖြတ်ဘဲ သတ်မှတ်ထားတဲ့ အများဆုံးစောင့်ချိန်အတွင်း စကားခဏရပ်တဲ့နေရာကို ရှာပြီး ဖြတ်ပေးပါတယ်။ ဥပမာ 3 မိနစ် သတ်မှတ်ပြီး 20 စက္ကန့် စောင့်ခွင့်ပေးထားရင် 3:00 နဲ့ 3:20 ကြားက သင့်တော်တဲ့ နေရာမှာ ဖြတ်နိုင်ပါတယ်။ ပိတ်ထားရင် သတ်မှတ်ချိန်အတိအကျမှာ ဖြတ်ပါတယ်။
- **Check Cuts:** Video ကို တကယ်မခွဲခင် ဘယ်အချိန်တွေမှာ ဖြတ်မလဲ ကြိုတင်ကြည့်နိုင်ပါတယ်။
- **Ratio / Fill:** Original, 16:9, 9:16, 1:1 အချိုးတွေထဲက ရွေးနိုင်ပါတယ်။ ပုံမပြည့်တဲ့ နေရာကို Blur Background, Black Bars သို့မဟုတ် Crop to Fill နဲ့ ဖြည့်နိုင်ပါတယ်။
- **Text Box / Part Number:** အပိုင်းတိုင်းမှာ ပေါ်စေချင်တဲ့ စာသား၊ အပိုင်းနံပါတ်နဲ့ စုစုပေါင်းအရေအတွက်ကို ထည့်နိုင်ပါတယ်။ Preview ပေါ်မှာ ဆွဲရွှေ့ပြီး နေရာချနိုင်ပါတယ်။
- **Stop / Resume:** ခွဲနေတုန်း ရပ်ထားရင် ပြန်စတဲ့အခါ မပြီးသေးတဲ့ အပိုင်းကနေ ဆက်လုပ်နိုင်ပါတယ်။ Setting ပြောင်းထားရင် သက်ဆိုင်ရာ အပိုင်းတွေကို ပြန်ထုတ်ပေးပါတယ်။

**English:** Splitter cuts one or many videos into configurable durations. It supports optional speech-aware Smart Cut, cut previews, aspect-ratio/fill controls, text overlays, part numbering and resumable processing.

#### 3. Studio — Downloader နဲ့ Download Queue

**မြန်မာ:** ဒီ Tab က ပံ့ပိုးထားတဲ့ Website တွေရဲ့ Public Video URL တွေကို App ထဲကနေ Download လုပ်ဖို့ ဖြစ်ပါတယ်။ Download လုပ်ပြီးတဲ့ Video ကို Recap လုပ်ဖို့ Queue ထဲ တိုက်ရိုက်ပို့နိုင်ပါတယ်။

- **URL ထည့်ခြင်း:** Website က Video Link ကို ထည့်ပြီး Download လုပ်နိုင်ပါတယ်။ URL အများအပြားကိုလည်း Queue ထဲ တစ်ခါတည်း ထည့်နိုင်ပါတယ်။
- **Video / Audio:** ပံ့ပိုးထားတဲ့ Format အလိုက် Video အဖြစ်ဖြစ်စေ၊ Audio သီးသန့် MP3 အဖြစ်ဖြစ်စေ ရွေးနိုင်ပါတယ်။
- **Quality:** ရနိုင်တဲ့ Video Quality ထဲက လိုချင်တဲ့ Resolution ကို ရွေးနိုင်ပါတယ်။ Website တစ်ခုနဲ့တစ်ခု ရနိုင်တဲ့ Quality မတူနိုင်ပါဘူး။
- **Playlist / Subtitles:** Website နဲ့ Link က ပံ့ပိုးထားရင် Playlist တစ်ခုလုံး သို့မဟုတ် ရရှိနိုင်တဲ့ Subtitle ဖိုင်တွေကို Download လုပ်နိုင်ပါတယ်။
- **Cookie File:** ကိုယ်ပိုင် Account နဲ့ ဝင်ကြည့်ခွင့်ရှိတဲ့ Content အတွက် ကိုယ်တိုင်ပေးထားတဲ့ Cookie File ကို သုံးနိုင်ပါတယ်။ Cookie ဖိုင်ကို အခြားသူထံ မပို့ပါနဲ့။
- **Download Queue:** Link အများအပြားကို စာရင်းထဲ ထည့်ထားပြီး တစ်ခုချင်းစီ အစဉ်လိုက် Download လုပ်ပါတယ်။ App ပိတ်သွားလည်း Queue အခြေအနေကို သိမ်းထားပြီး ပြန်ဖွင့်တဲ့အခါ Pending ဖြစ်နေတဲ့အလုပ်တွေကို ပြန်ရယူနိုင်ပါတယ်။
- **Retry:** မအောင်မြင်တဲ့ Download ကို ပြန်ကြိုးစားနိုင်ပါတယ်။ Download ပြီးတဲ့ Video ကို Recap Queue ထဲ အလိုအလျောက်ပို့ဖို့လည်း ရွေးချယ်နိုင်ပါတယ်။
- **Provider Test / Glossary:** အသုံးပြုမယ့် AI Provider ကို စမ်းသပ်နိုင်ပြီး ဇာတ်ကောင်အမည်၊ နေရာအမည်နဲ့ ဝေါဟာရတွေ တစ်သမတ်တည်းဖြစ်စေဖို့ Glossary ကို ပြင်ဆင်နိုင်ပါတယ်။

**သတိပြုရန်:** Downloader က yt-dlp ပံ့ပိုးထားတဲ့ Website/Extractor တွေအပေါ် မူတည်ပါတယ်။ Website က ပြောင်းလဲသွားတာ၊ Login/Region ကန့်သတ်ချက်၊ CAPTCHA၊ Link ဖျက်ထားတာတွေကြောင့် URL တစ်ခုချင်း အလုပ်လုပ်မယ်လို့ အာမမခံနိုင်ပါဘူး။ DRM သို့မဟုတ် ဝင်ရောက်ခွင့်ကန့်သတ်ချက်တွေကို ကျော်ဖြတ်ဖို့ မရည်ရွယ်ထားပါဘူး။ ကိုယ်ပိုင်ခွင့်ပြုချက်ရှိတဲ့ Video တွေကိုသာ Download လုပ်ပါ။

**English:** Studio uses yt-dlp to download supported public media URLs. It offers format/quality selection, audio-only downloads, playlist and subtitle options where available, authorized cookie-file support, a persistent download queue, retry controls, provider testing, glossary editing and hand-off to Recap. Site support can change; it does not bypass DRM or access controls.

#### 4. Thumbnail — သီးခြား Thumbnail ဖန်တီးတဲ့ Tool

**မြန်မာ:** Thumbnail ကို Recap ပြီးမှသာ ဖန်တီးရတာ မဟုတ်ပါဘူး။ မူရင်း Video တစ်ခုကို ရွေးပြီး ဒီ Tab ထဲမှာ သီးခြား Thumbnail ဖန်တီးနိုင်ပါတယ်။

- **Source Video:** Thumbnail ထုတ်ချင်တဲ့ မူရင်း Video ကို ရွေးပါ။
- **Automatic Frame Selection:** Video ထဲက Frame အများအပြားကို FFmpeg နဲ့ ထုတ်ယူပြီး ပုံရိပ်အရည်အသွေး/ကြည့်လို့ကောင်းမှုကို အခြေခံကာ Thumbnail အတွက် Frame ရွေးပေးပါတယ်။
- **Choose Frame:** ကိုယ်တိုင်ကြိုက်တဲ့ အချိန်က Frame ကို ရွေးချယ်နိုင်ပါတယ်။ မရွေးချင်ရင် Automatic Best Frame ကို ပြန်သုံးနိုင်ပါတယ်။
- **Local Variants:** Local Mode နဲ့ Thumbnail ပုံစံ ၃ မျိုး ထုတ်နိုင်ပါတယ်။ ဒီနည်းလမ်းမှာ AI Image Generation မလိုသလို fal.ai Credit လည်း မသုံးပါဘူး။
- **Myanmar Title / Logo:** မြန်မာခေါင်းစဉ်၊ Title Style နဲ့ ကိုယ်ပိုင် Logo ကို Thumbnail ပေါ်မှာ ထည့်နိုင်ပါတယ်။ Title အကြံပြုချက်တချို့ကို Built-in Template ကနေဖြစ်စေ၊ ချိတ်ဆက်ထားတဲ့ AI Text Provider ကနေဖြစ်စေ ရယူနိုင်ပါတယ်။
- **Aspect Ratio:** 16:9, 9:16 နဲ့ 1:1 အချိုးတွေကို ရွေးနိုင်ပါတယ်။
- **fal.ai AI Background:** Frame-based Thumbnail အစား AI နဲ့ Background ပုံအသစ် ဖန်တီးချင်ရင် fal.ai ကို ရွေးနိုင်ပါတယ်။ ဒီနည်းလမ်းအတွက် \`FAL_KEY\` လိုပြီး Account ရဲ့ Credit/Plan အလိုက် ကုန်ကျစရိတ်ရှိနိုင်ပါတယ်။
- **Auto-thumbnail after Recap:** Default အားဖြင့် ဖွင့်ထားတဲ့ ဒီ Option က Recap ပြီးသွားတဲ့အခါ မူရင်း Source Video ထဲက Frame ကို အသုံးပြုပြီး JPG Thumbnail ကို Final Video ဘေးမှာ သိမ်းပေးပါတယ်။ ထွက်လာတဲ့ Recap Video ထဲက Frame ကိုသာ ယူတာမဟုတ်ပါဘူး။
- **Download ပြီးနောက် Thumbnail:** Download လုပ်ပြီးတဲ့ Video အတွက်လည်း Auto-thumbnail Option သီးခြားရှိပါတယ်။

**English:** Thumbnail is a standalone tool. It can select frames from a local source video, let the user choose a frame, create three local variants, add Burmese titles/logos and export 16:9, 9:16 or square images. Optional fal.ai mode generates a new background and may consume account credits. Automatic Recap thumbnails are extracted from the original source video and saved beside the final output.

#### 5. Subtitles — SRT / VTT တင်သွင်းပြီး ဘာသာပြန်ခြင်း

**မြန်မာ:** မူရင်း Video ကို Whisper နဲ့ ထပ်နားထောင်စရာမလိုဘဲ ရှိပြီးသား Subtitle ဖိုင်ကို တိုက်ရိုက် ဘာသာပြန်ချင်တဲ့အခါ ဒီ Tab ကို သုံးနိုင်ပါတယ်။

1. **Import:** ကိုယ့်မှာရှိပြီးသား \`.srt\` သို့မဟုတ် \`.vtt\` ဖိုင်ကို ထည့်ပါ။
2. **Source / Target Language:** မူရင်း Subtitle ရဲ့ ဘာသာစကားနဲ့ ပြောင်းချင်တဲ့ ဘာသာစကားကို ရွေးပါ။
3. **Translate:** ရွေးထားတဲ့ AI Provider နဲ့ Subtitle စာသားကိုသာ ဘာသာပြန်ပါတယ်။ ဒီအဆင့်မှာ Whisper ကို မခေါ်ပါဘူး။
4. **Glossary:** Recap မှာ သုံးထားတဲ့ Character Names, Terms, Places နဲ့ Style Notes တွေကို ဘာသာပြန်ရာမှာ ထည့်သုံးနိုင်ပါတယ်။ ဒါကြောင့် ဇာတ်ကောင်နာမည်တွေ မတူညီတဲ့ပုံစံနဲ့ ပြန်ဆိုမိတာကို လျှော့ချနိုင်ပါတယ်။
5. **Review / Edit:** AI ပြန်ထားတဲ့ စာကြောင်းတွေကို Export မလုပ်ခင် တစ်ကြောင်းချင်း ပြန်စစ်ပြီး ပြင်နိုင်ပါတယ်။
6. **Export:** ဘာသာပြန်စာတန်းတစ်မျိုးတည်းပါတဲ့ SRT သို့မဟုတ် မူရင်းစာတန်းနဲ့ ဘာသာပြန်စာတန်း နှစ်မျိုးတွဲပါတဲ့ Bilingual SRT ထုတ်နိုင်ပါတယ်။ မူရင်း Subtitle ရဲ့ Timestamp တွေကို ထိန်းထားပေးပါတယ်။

**English:** Subtitle Tools imports SRT/VTT files and translates their text without running Whisper. It can reuse the Recap glossary, supports line-by-line review/editing, and exports translated-only or bilingual SRT while preserving cue timestamps.

#### 6. Project — Project, Audio နဲ့ Storage ကိရိယာများ

**မြန်မာ:** မကြာခဏ သုံးနေတဲ့ Setting တွေကို ပြန်ရွေးစရာမလိုအောင် Project အဖြစ် သိမ်းထားနိုင်ပြီး အသံ၊ Video Quality နဲ့ ဖိုင်သိမ်းဆည်းမှုဆိုင်ရာ Tool တွေကိုလည်း ဒီ Tab မှာ စီမံနိုင်ပါတယ်။

- **Save / Load Project:** Target Language, Narrator, Video Ratio နဲ့ သက်ဆိုင်ရာ Setting/Path တွေကို Project ဖိုင်အဖြစ် သိမ်းပြီး နောက်တစ်ခါ ပြန်ဖွင့်သုံးနိုင်ပါတယ်။ လုံခြုံရေးအတွက် API Secret တန်ဖိုးတွေကို Project JSON ထဲ မကူးသိမ်းပါဘူး။
- **Audio Waveform:** မူရင်းအသံရဲ့ Waveform Overview ကို ပြပေးပါတယ်။ အသံရှိတဲ့နေရာ၊ အသံတိတ်နေတဲ့နေရာတွေကို အကြမ်းဖျဉ်း သိနိုင်ဖို့ဖြစ်ပြီး Multitrack Timeline Editor မဟုတ်ပါဘူး။
- **Pronunciation Editor:** TTS က စာလုံး/နာမည်တချို့ကို မှားဖတ်တတ်ရင် အသံထွက်အစားထိုးစာလုံးကို သတ်မှတ်နိုင်ပါတယ်။ ဒီပြင်ဆင်ချက်က အသံထုတ်တဲ့အခါ အသုံးပြုတာဖြစ်ပြီး Video ပေါ်က Subtitle စာသားကို အလိုအလျောက် မပြောင်းပေးပါဘူး။
- **Intro / Outro:** Channel Name နဲ့ Logo ပါတဲ့ အဖွင့်/အပိတ် Card တွေ ထည့်နိုင်ပါတယ်။ မလိုအပ်ရင် ပိတ်ထားနိုင်ပြီး Default အားဖြင့် ပိတ်ထားပါတယ်။
- **Background Music (BGM):** Narration အောက်မှာ နောက်ခံသီချင်း ထည့်နိုင်ပြီး အသံအတိုးအကျယ်ကို ချိန်နိုင်ပါတယ်။ မူလ Default က ပိတ်ထားပါတယ်။
- **Smart Silence Removal:** Narration ထဲက အသံတိတ်နေချိန်တွေကို လျှော့ချနိုင်ပါတယ်။ အသံတိုးတိုးပြောထားတဲ့ စကားလုံးတွေကို Silence လို့ မှားသတ်မှတ်မိနိုင်တဲ့အတွက် Default ပိတ်ထားပြီး Video အတိုနဲ့ အရင်စမ်းသင့်ပါတယ်။
- **Preflight Check:** Source Video, FFmpeg/FFprobe, Disk Space နဲ့ API Credential ရှိ/မရှိကို အလုပ်မစခင် စစ်ပေးပါတယ်။ Key ရှိနေတာကို စစ်နိုင်ပေမဲ့ Key မှန်/မမှန်၊ Quota ကျန်/မကျန်ကို အာမမခံနိုင်ပါဘူး။
- **Output Quality Check (QC):** ထွက်လာတဲ့ Video ဖိုင် ရှိ/မရှိ၊ Audio/Video Stream, ကြာချိန်, Resolution နဲ့ မျှော်လင့်ထားတဲ့ SRT/Thumbnail ဖိုင်တွေ ရှိ/မရှိကို စစ်ပြီး JSON Report ထုတ်ပေးပါတယ်။ စာသားဘာသာပြန်ကောင်းမကောင်း၊ လူနားထောင်တဲ့အခါ Sync အပြည့်အဝမှန်မမှန်ကိုတော့ အလိုအလျောက် အတည်မပြုနိုင်ပါဘူး။
- **Storage Scan:** Jobs, Downloads, Logs နဲ့ Runtime Folder တွေ ဘယ်လောက်နေရာယူထားလဲ ခန့်မှန်းပြပေးပါတယ်။
- **Safe Cache Cleanup:** မလိုအပ်တော့တဲ့ သတ်မှတ်ထားသော Cache တွေကိုသာ ရှင်းပေးပါတယ်။ Final Video, Download လုပ်ထားတဲ့ဖိုင်နဲ့ Resume အတွက်လိုတဲ့ Checkpoint တွေကို မဖျက်ဖို့ ရည်ရွယ်ထားပါတယ်။
- **Platform Presets:** YouTube 16:9, Shorts/Reels/TikTok 9:16, Square Feed 1:1 နဲ့ 720p အရည်အသွေးနိမ့် Preset တွေကို အဆင်သင့် ရွေးနိုင်ပါတယ်။

**English:** Project Tools save and restore settings/paths without embedding API secrets, show a lightweight waveform overview, manage TTS pronunciation substitutions, optionally add intro/outro cards or background music, reduce narration silence, run preflight and media QC checks, estimate storage use, clean selected cache files safely and apply common platform presets. The waveform is not a full timeline editor, and QC does not judge translation quality.

#### 7. Recap Queue — Video အများအပြားကို တစ်ခုပြီးတစ်ခု လုပ်ခြင်း

**မြန်မာ:** Recap လုပ်စရာ Video အများအပြားရှိတဲ့အခါ တစ်ခုချင်းစီကို လက်နဲ့ ထပ်ရွေးနေစရာမလိုဘဲ Queue ထဲ စုပေါင်းထည့်နိုင်ပါတယ်။

- Local Video ဖိုင်အများအပြားကို Queue ထဲ ထည့်နိုင်ပါတယ်။
- အလုပ်တွေကို တစ်ခုချင်းစီ အစဉ်လိုက် လုပ်ဆောင်ပါတယ်။ တစ်ချိန်တည်းမှာ အလုပ်များစွာကို ပြိုင်တူလုပ်တဲ့စနစ် မဟုတ်ပါဘူး။
- Queue အခြေအနေကို သိမ်းထားတဲ့အတွက် App ပိတ်သွားပြီး ပြန်ဖွင့်တဲ့အခါ မပြီးသေးတဲ့ Job တွေကို ပြန်ရယူနိုင်ပါတယ်။
- App ပိတ်သွားချိန် Processing ဖြစ်နေတဲ့ Job ကို Pending အဖြစ် ပြန်ထားပြီး ဆက်လုပ်နိုင်အောင် စီမံထားပါတယ်။
- မအောင်မြင်တဲ့ Job တွေကို Retry ပြန်လုပ်နိုင်ပါတယ်။ ပြီးသွားတဲ့ Job တွေကိုလည်း Queue ထဲက ရှင်းနိုင်ပါတယ်။

**English:** Recap Queue stores multiple local video jobs, processes them sequentially, restores pending work after restart and allows failed jobs to be retried. It is a sequential queue, not parallel rendering.

### ဘာသာစကား၊ AI Provider နဲ့ Voice ရွေးချယ်မှု / Languages, AI Providers & Voices

#### Target Language များ

**မြန်မာ:** Recap မှာ နောက်ဆုံးထွက်လာမယ့် ဘာသာစကားကို အောက်ပါထဲက ရွေးနိုင်ပါတယ်။ အသုံးပြုတဲ့ TTS Provider က ရွေးထားတဲ့ ဘာသာစကားကို အသံထုတ်ပံ့ပိုးမှု ရှိ/မရှိပေါ် မူတည်ပြီး အသံရွေးချယ်မှု ကွာခြားနိုင်ပါတယ်။

Myanmar (Burmese), English, Chinese, Japanese, Korean, Hindi, Thai, Vietnamese, Indonesian, Malay, Filipino (Tagalog), Spanish, Portuguese, French, German, Italian, Russian, Turkish, Arabic, Bengali, Tamil, Telugu နဲ့ Urdu။

**English:** Recap supports the target languages listed above. Available narration voices depend on the language and capabilities of the selected TTS provider.

#### Text / Translation AI Provider များ

| Provider | မြန်မာလို ရှင်းပြချက် | English |
|---|---|---|
| Gemini | မူလ Default Provider ဖြစ်ပါတယ်။ Story Context, Translation နဲ့ Audit အတွက် သုံးပါတယ်။ Google API Key လိုပါတယ်။ | Default provider for story context, translation and audit; requires a Google API key. |
| Groq | ရွေးချယ်အသုံးပြုနိုင်တဲ့ Cloud AI Provider ဖြစ်ပါတယ်။ Groq API Key နဲ့ အသုံးပြုခွင့်ရှိတဲ့ Model ID လိုပါတယ်။ | Optional cloud provider; requires a Groq API key and an available model ID. |
| OpenRouter | Model အမျိုးမျိုးကို Gateway တစ်ခုကနေ ရွေးသုံးနိုင်ပါတယ်။ ရွေးထားတဲ့ Model အလိုက် ဈေးနှုန်းနဲ့ Quota ကွာခြားနိုင်ပါတယ်။ | Optional model gateway; pricing and limits depend on the selected model. |
| Ollama | ကိုယ့် Computer ထဲမှာ Model ကို Local အနေနဲ့ ထည့်သွင်းပြီး သုံးနိုင်ပါတယ်။ Ollama ကို အရင် Install လုပ်ထားပြီး Model ကို Download လုပ်ထားဖို့ လိုပါတယ်။ | Local provider; Ollama and a suitable local model must already be installed. |

**အရေးကြီး:** Provider တစ်ခုကို ရွေးထားရုံနဲ့ အခမဲ့ဖြစ်မယ်လို့ မဆိုလိုပါဘူး။ Free Quota, Rate Limit, Model Availability နဲ့ Pricing တွေဟာ Provider Account နဲ့ Model ပေါ်မူတည်ပြီး ပြောင်းနိုင်ပါတယ်။ App မှာ ထည့်ထားတဲ့ Provider တစ်ခုချင်းစီအတွက် ကိုယ့် Key နဲ့ Quota ရှိဖို့ လိုပါတယ်။

**English:** Selecting a provider does not guarantee free usage. Free quotas, rate limits, model availability and pricing depend on the provider and selected model.

#### Narrator / TTS Provider များ

| Voice Provider | မြန်မာလို ရှင်းပြချက် | English |
|---|---|---|
| Microsoft Edge TTS | Myanmar အတွက် Thiha (ယောက်ျားသံ) နဲ့ Nilar (မိန်းမသံ) လို Edge Voice တွေ ပါဝင်ပါတယ်။ Online Service ဖြစ်လို့ Internet လိုပါတယ်။ | Includes available Edge voices such as Myanmar Thiha and Nilar; requires internet access. |
| Gemini TTS | Gemini ရဲ့ Prebuilt Voice တွေထဲက ရွေးနိုင်ပါတယ်။ Voice Style အမျိုးမျိုး ရှိပေမဲ့ အားလုံးကို Native Myanmar Voice လို့ မယူဆသင့်ပါဘူး။ | Offers Gemini prebuilt voice choices and styles; these are not all native Burmese voices. |
| Azure Speech | သက်ဆိုင်ရာ Language နဲ့ Voice ကို Azure က ပံ့ပိုးထားရင် သုံးနိုင်ပါတယ်။ API Key နဲ့ Region သတ်မှတ်ချက် လိုပါတယ်။ | Optional Azure voices require a Speech key and region and depend on Azure language/voice support. |
| ElevenLabs | သက်ဆိုင်ရာ Multilingual Model နဲ့ Voice ကို ရွေးသုံးနိုင်ပါတယ်။ API Key, Voice ID နဲ့ Account Quota လိုပါတယ်။ | Optional multilingual TTS requiring an API key, voice ID and account quota. |

### API Key ထည့်သွင်းရမည့်နေရာ / API Keys and Environment Variables

**မြန်မာ:** API Key တွေကို Repository ထဲက \`.env.example\` ကို မူတည်ပြီး ကိုယ့်စက်ထဲမှာရှိတဲ့ \`.env\` ဖိုင်ထဲမှာသာ ထည့်ပါ။ API Key, Cookie File နဲ့ ကိုယ်ပိုင် Project ဖိုင်တွေကို GitHub ပေါ် မတင်ပါနဲ့။ \`.env\` ကို အခြားသူထံ ပို့ပေးဖို့လည်း မလိုပါဘူး။

| Feature / ဝန်ဆောင်မှု | Environment Variable | ဘာအတွက်လဲ |
|---|---|---|
| Gemini | \`GEMINI_API_KEY\` | Story Context, Translation နဲ့ Audit အတွက် Google API Key။ |
| Groq | \`GROQ_API_KEY\`, \`GROQ_MODEL\` | Groq Provider ရွေးသုံးတဲ့အခါ လိုအပ်တဲ့ Key နဲ့ Model။ |
| OpenRouter | \`OPENROUTER_API_KEY\`, \`OPENROUTER_MODEL\` | OpenRouter မှတစ်ဆင့် Model သုံးဖို့။ |
| Ollama | \`OLLAMA_BASE_URL\`, \`OLLAMA_MODEL\` | Local Ollama Server လိပ်စာနဲ့ Install လုပ်ထားတဲ့ Model အမည်။ |
| Azure Speech | \`AZURE_SPEECH_KEY\`, \`AZURE_SPEECH_REGION\` | Azure Speech အသံထုတ်ဖို့ Key နဲ့ Region။ |
| ElevenLabs | \`ELEVENLABS_API_KEY\`, \`ELEVENLABS_VOICE_ID\`, \`ELEVENLABS_MODEL_ID\` | ElevenLabs Voice နဲ့ Model သတ်မှတ်ဖို့။ |
| fal.ai | \`FAL_KEY\`, \`FAL_IMAGE_MODEL\` | AI Thumbnail Background ဖန်တီးဖို့။ Credit ကုန်နိုင်ပါတယ်။ |

**English:** Store credentials only in your local \`.env\` file. The table lists optional provider variables. Never commit API keys, cookies or private project files.

### စမ်းသပ်ရန် အကြံပြုအစီအစဉ် / Recommended Test Order

Feature အားလုံးကို Video အရှည်ကြီးနဲ့ တစ်ခါတည်း မစမ်းပါနဲ့။ အရင်ဆုံး Video အတိုနဲ့ အောက်ပါအစီအစဉ်အတိုင်း တစ်ဆင့်ချင်း စမ်းသပ်ပါ။

1. **Recap အခြေခံစမ်းသပ်မှု:** ၁–၃ မိနစ်ခန့် Video တစ်ခုနဲ့ Recap လုပ်ပါ။ မြန်မာဘာသာပြန်စာ၊ အသံထွက်၊ စာတန်းနဲ့ ရုပ်/အသံ Sync ကို ကိုယ်တိုင် စစ်ပါ။  
   **English:** Run a 1–3 minute recap and inspect the translation, narration, subtitles and audio/video sync.

2. **Thumbnail:** Auto-thumbnail ထွက်လာသလား၊ JPG ဖိုင်က မူရင်း Source Video ထဲက Frame ကို အသုံးပြုထားသလား စစ်ပါ။ Standalone Thumbnail Tab မှာ Frame ကို ကိုယ်တိုင်ရွေးတာနဲ့ Local Variants ၃ မျိုးကိုလည်း စမ်းပါ။  
   **English:** Check the automatically generated JPG and test manual frame selection and local variants.

3. **Stop / Resume နဲ့ Queue:** Video အတိုတစ်ခုကို အလယ်မှာ ရပ်ပြီး ပြန်ဆက်ပါ။ Recap Queue ထဲ Video အများအပြား ထည့်ပြီး App ပြန်ဖွင့်တဲ့အခါ Pending Job ပြန်ရလာသလား စစ်ပါ။  
   **English:** Test safe stopping, resuming, sequential queue processing and recovery after restarting the app.

4. **Downloader:** ကိုယ်တိုင် Download လုပ်ခွင့်ရှိတဲ့ Public URL တစ်ခုနဲ့ အရင်စမ်းပါ။ Video Download, Audio-only, Queue နဲ့ Retry ကို သီးခြားစမ်းပါ။  
   **English:** Test one authorized public URL first, then check video/audio downloads, queue persistence and retry.

5. **Subtitle Tools:** SRT/VTT ဖိုင်တစ်ခု Import လုပ်ပြီး ဘာသာပြန်ပါ။ Timestamp မပြောင်းသွားကြောင်း၊ ပြင်ထားတဲ့စာသားတွေ Export ထဲ ပါကြောင်းနဲ့ Bilingual SRT ပုံစံမှန်ကြောင်း စစ်ပါ။  
   **English:** Import and translate an SRT/VTT file, then verify timestamps, edited text and bilingual export.

6. **Project Tools:** Project Save/Load, Pronunciation Editor, Waveform, Intro/Outro, BGM နဲ့ Smart Silence Removal ကို တစ်ခုချင်းစီ စမ်းပါ။ မလိုအပ်တဲ့ Audio Tool တွေကို Default ပိတ်ထားနိုင်ပါတယ်။  
   **English:** Test project save/load, pronunciation, waveform, branding, music and silence removal separately.

7. **နောက်ဆုံးမှ Video အရှည်ကြီး စမ်းပါ:** အခြေခံအဆင့်တွေ အဆင်ပြေမှသာ Video အရှည်ကြီးနဲ့ စမ်းပါ။ Memory, CPU/GPU အပူချိန်, Disk Space, ပြီးသွားတဲ့ Output နဲ့ ရုပ်/အသံ Sync ကို စောင့်ကြည့်ပါ။  
   **English:** Test long videos only after the short tests pass. Monitor memory, CPU/GPU temperature, disk space, output integrity and sync.

### စစ်ဆေးမှုအခြေအနေနဲ့ သိထားရမယ့် ကန့်သတ်ချက်များ / Validation Status & Limitations

- **မြန်မာ:** GitHub Actions မှာ Python Compile နဲ့ Automated Regression Tests တွေကို စစ်ဆေးပါတယ်။ CI အောင်မြင်တယ်ဆိုတာ Windows GUI အားလုံး၊ Live API Key/Quota၊ Website တစ်ခုချင်းစီ၊ Video အရှည်ကြီးတွေရဲ့ Sync အားလုံး အောင်မြင်ကြောင်း အာမခံတာ မဟုတ်ပါဘူး။  
  **English:** GitHub Actions checks Python compilation and automated regression tests. A green CI result does not prove every Windows GUI interaction, live API account, website URL or long-video sync scenario works.

- **မြန်မာ:** AI Provider တစ်ခုချင်းစီမှာ Quota, Rate Limit, Model ပိတ်သိမ်းမှုနဲ့ ဈေးနှုန်း ပြောင်းလဲမှုတွေ ရှိနိုင်ပါတယ်။ အသုံးမပြုခင် Provider ဘက်က လက်ရှိသတ်မှတ်ချက်တွေကို စစ်ဆေးပါ။  
  **English:** AI providers may change quotas, rate limits, model availability and pricing. Check the provider's current terms before use.

- **မြန်မာ:** Downloader အလုပ်လုပ်မှုဟာ yt-dlp နဲ့ Website ရဲ့ လက်ရှိပံ့ပိုးမှုအပေါ် မူတည်ပါတယ်။ URL တိုင်းကို အာမခံမပေးနိုင်ပါဘူး။ DRM နဲ့ Access Control ကို ကျော်ဖြတ်မပေးပါဘူး။  
  **English:** Downloader support depends on yt-dlp and each site's current behavior. Not every URL is guaranteed to work; DRM/access controls are not bypassed.

- **မြန်မာ:** Preflight နဲ့ Output QC က ဖိုင်/Tool/Metadata ရှိမရှိ စစ်ပေးတဲ့ ကိရိယာတွေဖြစ်ပြီး ဘာသာပြန်အဓိပ္ပာယ်မှန်ကန်မှု၊ အသံအရည်အသွေးနဲ့ လူနားထောင်တဲ့အခါ Sync ခံစားချက်ကို အပြည့်အဝ မဆုံးဖြတ်နိုင်ပါဘူး။  
  **English:** Preflight and output QC check prerequisites and media metadata. They cannot fully judge translation accuracy, listening quality or perceived synchronization.

- **မြန်မာ:** Error ဖြစ်ရင် \`run.log\` နဲ့ Error Message ကို ပို့ပါ။ API Key, Cookie, Password နဲ့ ကိုယ်ရေးကိုယ်တာ အချက်အလက်တွေကို ဖျောက်ပြီးမှ မျှဝေပါ။  
  **English:** When reporting an issue, share the relevant log and error message after removing API keys, cookies, passwords and personal information.

အပြည့်အစုံ Feature စာရင်းနဲ့ နည်းပညာပိုင်း အသေးစိတ်ကို [STUDIO_FEATURES.md](STUDIO_FEATURES.md) မှာလည်း ကြည့်နိုင်ပါတယ်။ ဒီ README ကတော့ အသုံးပြုသူအနေနဲ့ ဘယ် Tab က ဘာလုပ်ပေးလဲ၊ ဘယ်လိုသုံးရမလဲ၊ ဘာတွေသတိထားရမလဲဆိုတာ မြန်မာလို နားလည်လွယ်အောင် ရှင်းပြထားတာပါ။

**English:** See [STUDIO_FEATURES.md](STUDIO_FEATURES.md) for the implementation scope and additional technical details. This README is intended as the user-facing bilingual guide to the available tabs, workflows, setup and limitations.
