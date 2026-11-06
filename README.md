# Recap → Myanmar (+ Splitter)

**English၊ တရုတ်၊ ဟိန္ဒီ၊ ကိုရီးယား … ဘယ်ဘာသာနဲ့ ပြောထားတဲ့ recap / ဇာတ်လမ်းပြော video ကိုမဆို မြန်မာအသံနဲ့ ပြန်ထုတ်ပေးတဲ့ Windows tool**
Selectable narration styles · Free-first AI auto selection · Whisper + Gemini · Edge TTS · Smart Sync
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
   - **FFmpeg** — စက်ထဲမှာ မရှိရင် (~100 MB) download လုပ်ပြီး ဒီ folder ထဲက `ffmpeg` ထဲ ထည့်ပေးပါမယ်။ PATH ထဲ (သို့) `C:\ffmpeg\bin` မှာ ရှိပြီးသားဆိုရင် အဲ့ဒါကိုပဲ သုံးပါတယ်။
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
| **Save to** | ဗလာထားရင် video ဘေးက `<video နာမည်>_parts` ထဲ သိမ်းပါတယ်။ Folder ရွေးထားရင် `<ရွေးထားတဲ့ folder>\<video နာမည်>_parts` ထဲ။ ဖိုင်နာမည် `<video နာမည်>_part_01.mp4`, `_part_02.mp4` … |
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
- SRT ဖိုင်ကိုလည်း ထုတ်ပေးပါတယ် — `SRT_for_upload` folder ထဲမှာ (video ဘေးမှာ မထားပါ၊ နာမည်တူ .srt ရှိရင် VLC / PotPlayer က
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
| `[WinError 2] The system cannot find the file specified` (သို့) `ffmpeg.exe မတွေ့ပါ` (Preview မှာ `00:00 / 00:00`) | FFmpeg မရှိလို့ပါ။ `INSTALL_REQUIREMENTS.bat` ကို ပြန် run ပါ (FFmpeg ကို `ffmpeg` ထဲ ထည့်ပေးပါမယ်)။ (သို့) gyan.dev ကနေ download လုပ်ပြီး `ffmpeg.exe`၊ `ffprobe.exe` ကို `RUN.bat` ဘေးက `ffmpeg` folder ထဲ ထည့်ပါ။ |
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
  subtitle_tools_tab.py    Imported SRT/VTT translation and Subbing render
  dubbing_tab.py           Manual character dialogue / voice assignment UI
  studio/dubbing.py       Timestamped Edge TTS character dubbing renderer
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
   FFmpeg: when it is not on PATH or in `C:\ffmpeg\bin`, about 100 MB is downloaded into `ffmpeg`).
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
- **+ Videos / + Folder**, **Save to** (empty = `<video folder>\<name>_parts`; files `<name>_part_01.mp4` …).
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
always written to `SRT_for_upload` (not next to the video, where players would show it twice).

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

**အရေးကြီး / Branch အခြေအနေ:** ဒီ Feature တွေဟာ `feature/studio-expansion` branch မှာပဲ ရှိပါသေးတယ်။ `main` branch ထဲကို မပေါင်းရသေးသလို မူရင်း upstream repository ကိုလည်း မပြောင်းထားပါဘူး။ စမ်းသပ်ပြီးမှ Merge လုပ်ဖို့ သီးခြားထားတာပါ။

**English:** The new Studio features described below are available on `feature/studio-expansion`. They have not been merged into this fork's `main` branch, and the original upstream repository remains separate.

### Recap Narration Styles / ဇာတ်ကြောင်းပြောပုံစံများ

Recap မှာ Storytelling တစ်မျိုးတည်း မဟုတ်တော့ပါဘူး။ လက်ရှိ UI မှာ Storytelling, Documentary, Cinematic, Casual, Character Focus, Anime Recap နဲ့ Explainer Style တွေကို ရွေးနိုင်ပါတယ်။ ဒီ Style တွေက Narration စကားပြောပုံကို ပြောင်းပေးတာဖြစ်ပြီး မူရင်းအချက်အလက်ကို မတီထွင်ပါဘူး။ Style တစ်ခု ပြောင်းလိုက်ရင် Translation Plan အသစ်တည်ဆောက်ပါတယ်။

**Free-first AI Auto:** .env ထဲမှာ RECAP_AI_PROVIDER=auto ထားရင် API Key နဲ့ Model ID ပြည့်စုံတဲ့ Free-first Provider ကို အစဉ်လိုက်ရွေးပါတယ်။ OpenRouter အတွက် OPENROUTER_MODEL=openrouter/free ထားနိုင်ပါတယ်။ Hosted Free Provider တစ်ခုမှ မပြည့်စုံရင် Gemini ကို သုံးပါတယ်။ Provider Rotation က Configured Provider တွေကြားမှာသာ လုပ်နိုင်ပြီး Quota မရှိတဲ့ အကန့်အသတ်မဲ့ Service မဟုတ်ပါဘူး။

**Audio controls / မူရင်းအသံထိန်းချုပ်မှု:** Project Tools → Audio, Music & Intro / Outro ထဲမှာ Original Audio ON/OFF နဲ့ Source BGM ON/OFF ကို သီးခြားရွေးနိုင်ပါတယ်။ Original Audio ON က မူရင်း Dialogue + BGM ကို Smart Sync Timeline နဲ့ ချိန်ညှိပြီး Narration အောက်ခံအဖြစ် ထားပေးပါတယ်။ Source BGM OFF လုပ်ပြီး Dialogue ကိုသာ ထားချင်ရင် Demucs လိုအပ်ပြီး CPU အချိန် ပိုယူနိုင်ပါတယ်။ Demucs မရနိုင်တဲ့အခါ Dialogue ကိုပါ မှားပိတ်မယ့်အစား Error ပြပါမယ်။

**Subbing Mode / စာတန်းထိုး Video:** Subtitle Import / Translate Tab မှာ SRT/VTT ကို Import လုပ်၊ Timestamp မပျက်အောင် ဘာသာပြန်၊ Cue တစ်ကြောင်းချင်း ပြင်ပြီး Translated သို့မဟုတ် Bilingual SRT ထုတ်နိုင်ပါတယ်။ Source Video ကို ရွေးပြီး TTS မသုံးဘဲ Subtitle Burn-in MP4 ထုတ်နိုင်တယ်။ မူရင်း Audio Content ကို ထိန်းထားပြီး MP4 နဲ့ ကိုက်ညီဖို့ AAC အဖြစ် Encode ပြန်လုပ်နိုင်ပါတယ်။

**Character Voice Dubbing / ဇာတ်ကောင်အလိုက် အသံပြန်သွင်းခြင်း:** Dubbing Tab မှာ Translated SRT/VTT ကို Import လုပ်ပြီး Timestamped Dialogue Row တစ်ကြောင်းချင်းစီကို Speaker Label နဲ့ သတ်မှတ်နိုင်ပါတယ်။ Speaker တစ်ယောက်စီကို Edge TTS Voice တစ်မျိုးစီ ချိတ်ပြီး Project Save/Load လုပ်ကာ Dialogue ကို Cue အချိန်အတိုင်း Render လုပ်နိုင်ပါတယ်။ Source Audio ကို Mute / Original Mix / Demucs Instrumental ရွေးနိုင်ပါတယ်။ Automatic Speaker Diarization မပါသေးတဲ့အတွက် Speaker နဲ့ Voice ကို User ကိုယ်တိုင် သတ်မှတ်ရပါမယ်။

**English:** Character Dubbing imports translated SRT/VTT, lets users edit timestamped dialogue rows, assign stable speaker-to-Edge-TTS voice mappings, save/load dubbing projects, and render timed dialogue. Source audio can be muted, retained as a full mix, or separated to an instrumental bed with optional Demucs. Automatic diarization is not included.

အသေးစိတ်: [Audio Modes & Studio Integration / Audio Mode များ](STUDIO_AUDIO_MODES.md)။

### Feature Branch ကို ဘယ်လိုရယူမလဲ / How to Get This Branch

1. [ဒီ Repository ကိုဖွင့်ပါ](https://github.com/SourcePlease/recap-en-to-mm)။
2. GitHub ရဲ့ **Branch** ရွေးတဲ့နေရာမှာ `main` အစား **`feature/studio-expansion`** ကို ရွေးပါ။
3. **Code → Download ZIP** ကိုနှိပ်ပြီး ZIP ဖိုင်ကို ဖြည်ပါ။
4. အောက်က မူလ Install လုပ်နည်းအတိုင်း လိုအပ်တဲ့ Python, FFmpeg နဲ့ API Key တွေ ပြင်ဆင်ပြီး `INSTALL_REQUIREMENTS.bat` ကို အရင်ဖွင့်ပါ။ ပြီးရင် `RUN.bat` နဲ့ App ကို စတင်နိုင်ပါတယ်။

**English:** Open the repository, switch the branch selector to `feature/studio-expansion`, then choose **Code → Download ZIP**. Extract it and follow the installation instructions above before launching `RUN.bat`.

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
- **fal.ai AI Background:** Frame-based Thumbnail အစား AI နဲ့ Background ပုံအသစ် ဖန်တီးချင်ရင် fal.ai ကို ရွေးနိုင်ပါတယ်။ ဒီနည်းလမ်းအတွက် `FAL_KEY` လိုပြီး Account ရဲ့ Credit/Plan အလိုက် ကုန်ကျစရိတ်ရှိနိုင်ပါတယ်။
- **Auto-thumbnail after Recap:** Default အားဖြင့် ဖွင့်ထားတဲ့ ဒီ Option က Recap ပြီးသွားတဲ့အခါ မူရင်း Source Video ထဲက Frame ကို အသုံးပြုပြီး JPG Thumbnail ကို Final Video ဘေးမှာ သိမ်းပေးပါတယ်။ ထွက်လာတဲ့ Recap Video ထဲက Frame ကိုသာ ယူတာမဟုတ်ပါဘူး။
- **Download ပြီးနောက် Thumbnail:** Download လုပ်ပြီးတဲ့ Video အတွက်လည်း Auto-thumbnail Option သီးခြားရှိပါတယ်။

**English:** Thumbnail is a standalone tool. It can select frames from a local source video, let the user choose a frame, create three local variants, add Burmese titles/logos and export 16:9, 9:16 or square images. Optional fal.ai mode generates a new background and may consume account credits. Automatic Recap thumbnails are extracted from the original source video and saved beside the final output.

#### 5. Subtitles — SRT / VTT တင်သွင်းပြီး ဘာသာပြန်ခြင်း

**မြန်မာ:** မူရင်း Video ကို Whisper နဲ့ ထပ်နားထောင်စရာမလိုဘဲ ရှိပြီးသား Subtitle ဖိုင်ကို တိုက်ရိုက် ဘာသာပြန်ချင်တဲ့အခါ ဒီ Tab ကို သုံးနိုင်ပါတယ်။

1. **Import:** ကိုယ့်မှာရှိပြီးသား `.srt` သို့မဟုတ် `.vtt` ဖိုင်ကို ထည့်ပါ။
2. **Source / Target Language:** မူရင်း Subtitle ရဲ့ ဘာသာစကားနဲ့ ပြောင်းချင်တဲ့ ဘာသာစကားကို ရွေးပါ။
3. **Translate:** ရွေးထားတဲ့ AI Provider နဲ့ Subtitle စာသားကိုသာ ဘာသာပြန်ပါတယ်။ ဒီအဆင့်မှာ Whisper ကို မခေါ်ပါဘူး။
4. **Glossary:** Recap မှာ သုံးထားတဲ့ Character Names, Terms, Places နဲ့ Style Notes တွေကို ဘာသာပြန်ရာမှာ ထည့်သုံးနိုင်ပါတယ်။ ဒါကြောင့် ဇာတ်ကောင်နာမည်တွေ မတူညီတဲ့ပုံစံနဲ့ ပြန်ဆိုမိတာကို လျှော့ချနိုင်ပါတယ်။
5. **Review / Edit:** AI ပြန်ထားတဲ့ စာကြောင်းတွေကို Export မလုပ်ခင် တစ်ကြောင်းချင်း ပြန်စစ်ပြီး ပြင်နိုင်ပါတယ်။
6. **Export:** ဘာသာပြန်စာတန်းတစ်မျိုးတည်းပါတဲ့ SRT သို့မဟုတ် မူရင်းစာတန်းနဲ့ ဘာသာပြန်စာတန်း နှစ်မျိုးတွဲပါတဲ့ Bilingual SRT ထုတ်နိုင်ပါတယ်။ မူရင်း Subtitle ရဲ့ Timestamp တွေကို ထိန်းထားပေးပါတယ်။

**English:** Subtitle Tools imports SRT/VTT files and translates their text without running Whisper. It can reuse the Recap glossary, supports line-by-line review/editing, and exports translated-only or bilingual SRT while preserving cue timestamps.

#### 6. Dubbing — Character Voice Dubbing / ဇာတ်ကောင်အလိုက် အသံပြန်သွင်းခြင်း

**မြန်မာ:** ဒီ Tab က Narrator တစ်ယောက်တည်းနဲ့ Recap ပြောတာမဟုတ်ဘဲ ဇာတ်ကောင်တစ်ယောက်ချင်းစီအတွက် အသံသီးခြားတပ်ဖို့ ဖြစ်ပါတယ်။ အရင်ဆုံး Subtitles Tab မှာ Translated SRT/VTT ပြင်ဆင်ပြီး Export လုပ်ပါ။ ပြီးရင် Dubbing Tab မှာ အဲဒီဖိုင်ကို Import လုပ်ပါ။

- **Dialogue Rows:** Start / End Timestamp, Speaker Label နဲ့ ဘာသာပြန်ထားတဲ့ စာသားကို တစ်ကြောင်းချင်း ပြင်နိုင်ပါတယ်။ Row Format က Tab-separated ဖြစ်ပါတယ်။
- **Speaker Voice Mapping:** ဥပမာ `Speaker A=my-MM-ThihaNeural` လို့ သတ်မှတ်ပါ။ Speaker တစ်ယောက် ပြန်ပေါ်လာတိုင်း အဲဒီ Voice ကိုပဲ အသုံးပြုပါတယ်။
- **Project Save/Load:** Dialogue Row နဲ့ Voice Mapping ကို Dubbing Project JSON အဖြစ် သိမ်းပြီး ပြန်ဖွင့်နိုင်ပါတယ်။
- **Source Audio:** Mute, Original Dialogue + BGM အပြည့်ထားခြင်း၊ သို့မဟုတ် Demucs နဲ့ Instrumental BGM ပဲထားခြင်း ရွေးနိုင်ပါတယ်။
- **Render:** Dialogue တစ်ကြောင်းစီကို Cue Timestamp နဲ့ ချိန်ပြီး Edge TTS အသံထုတ်ကာ Video နဲ့ ပြန်ပေါင်းပါတယ်။ အချိန်မလောက်တဲ့ Dialogue ကို အများဆုံး 1.5x အထိ မြန်စေပြီး မလုံလောက်ရင် Trim ဖြစ်နိုင်ပါတယ်။

**ကန့်သတ်ချက်:** Automatic Speaker Diarization နဲ့ Character Identity Detection မပါသေးပါ။ Translated Subtitle ကို အရင်ပြင်ဆင်ထားရပြီး Speaker Label နဲ့ Voice ကို User ကိုယ်တိုင် စစ်ဆေးသတ်မှတ်ရပါမယ်။ Instrumental BGM ရွေးထားရင် Demucs ကို သီးခြား Install လုပ်ရနိုင်ပြီး CPU/RAM ပိုသုံးနိုင်ပါတယ်။

**English:** The Dubbing tab supports manually reviewed timestamped dialogue rows, stable Edge TTS voice assignment per speaker, project save/load, and final video rendering. It does not automatically diarize speakers or identify characters.

#### 7. Project — Project, Audio နဲ့ Storage ကိရိယာများ

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

#### 8. Recap Queue — Video အများအပြားကို တစ်ခုပြီးတစ်ခု လုပ်ခြင်း

**မြန်မာ:** Recap လုပ်စရာ Video အများအပြားရှိတဲ့အခါ တစ်ခုချင်းစီကို လက်နဲ့ ထပ်ရွေးနေစရာမလိုဘဲ Queue ထဲ စုပေါင်းထည့်နိုင်ပါတယ်။

- Local Video ဖိုင်အများအပြားကို Queue ထဲ ထည့်နိုင်ပါတယ်။
- အလုပ်တွေကို တစ်ခုချင်းစီ အစဉ်လိုက် လုပ်ဆောင်ပါတယ်။ တစ်ချိန်တည်းမှာ အလုပ်များစွာကို ပြိုင်တူလုပ်တဲ့စနစ် မဟုတ်ပါဘူး။
- Queue အခြေအနေကို သိမ်းထားတဲ့အတွက် App ပိတ်သွားပြီး ပြန်ဖွင့်တဲ့အခါ မပြီးသေးတဲ့ Job တွေကို ပြန်ရယူနိုင်ပါတယ်။
- App ပိတ်သွားချိန် Processing ဖြစ်နေတဲ့ Job ကို Pending အဖြစ် ပြန်ထားပြီး ဆက်လုပ်နိုင်အောင် စီမံထားပါတယ်။
- မအောင်မြင်တဲ့ Job တွေကို Retry ပြန်လုပ်နိုင်ပါတယ်။ ပြီးသွားတဲ့ Job တွေကိုလည်း Queue ထဲက ရှင်းနိုင်ပါတယ်။

**English:** Recap Queue stores multiple local video jobs, processes them sequentially, restores pending work after restart and allows failed jobs to be retried. It is a sequential queue, not parallel rendering.

### ဘာသာစကား၊ AI Provider နဲ့ Voice ရွေးချယ်မှု / Languages, AI Providers & Voices

#### Text AI / Translation Provider — ဘယ်ဟာကို ဘယ်နေရာမှာ သုံးရမလဲ

**မြန်မာ:** ဒီ Provider တွေကို Video ထဲက ဇာတ်လမ်းအကြောင်းအရာကို နားလည်မှတ်သားခြင်း (Story Context)၊ ဘာသာပြန်ခြင်း (Translation)၊ ဘာသာပြန်စာကို ပြန်စစ်ခြင်း (Audit) နဲ့ Thumbnail ခေါင်းစဉ်အကြံပြုခြင်းတို့အတွက် သုံးပါတယ်။ Provider တစ်ခုနဲ့တစ်ခု Free Quota, Model, အမြန်နှုန်းနဲ့ ဘာသာစကားနားလည်နိုင်မှု မတူပါဘူး။

| Provider | အခမဲ့အသုံးပြုနိုင်မှု / ကန့်သတ်ချက် | ဘာအတွက်အသုံးဝင်လဲ | လက်ရှိ App အခြေအနေ |
|---|---|---|---|
| **[Gemini API](https://ai.google.dev/gemini-api/docs/pricing)** | Google AI Studio မှာ Free Tier ရှိပါတယ်။ ဒါပေမဲ့ Free Tier မှာ Model အချို့ကိုသာ သုံးခွင့်ရှိပြီး Request/Token Limit က Model နဲ့ Account ပေါ်မူတည်ပါတယ်။ | Story Context, Translation, Audit အတွက် မူလ Default Provider ဖြစ်ပါတယ်။ | **ပါပြီးသား / Default** |
| **[Groq](https://console.groq.com/docs/rate-limits)** | Free Plan ရှိပါတယ်။ Model တစ်ခုချင်းစီအလိုက် RPM, RPD, TPM, TPD ကွာပါတယ်။ အတိအကျကို ကိုယ့် Groq Console ရဲ့ Limits မှာ စစ်ပါ။ | တုံ့ပြန်မှုမြန်တဲ့ Text AI Provider တစ်ခုဖြစ်ပြီး Translation/Audit အတွက် စမ်းသုံးနိုင်ပါတယ်။ | **ပါပြီးသား** |
| **[OpenRouter](https://openrouter.ai/collections/free-models)** | Free Model တွေရှိပြီး Free Variant တစ်ခုချင်းရဲ့ Model ID အဆုံးမှာ `:free` ပါပါတယ်။ ၂၀၂၆-၁၁-၀၆ စစ်ဆေးချိန်တွင် `:free` Variant များအတွက် 20 requests/minute နဲ့ 50 requests/day ကန့်သတ်ချက် ဖော်ပြထားပါတယ်။ အခြား $0 Model တွေမှာ Provider-specific Limit သီးခြား ရှိနိုင်ပါတယ်။ | Provider မျိုးစုံက Free Model တွေကို API တစ်ခုတည်းကနေ ရွေးသုံးနိုင်ပါတယ်။ Free Model ပြောင်းစမ်းဖို့ အဆင်ပြေပါတယ်။ | **ပါပြီးသား** |
| **[Mistral AI](https://help.mistral.ai/en/articles/698531-why-am-i-hitting-api-rate-limits-and-how-do-i-increase-them)** | La Plateforme ရဲ့ Free mode ကို Evaluation/Prototype အတွက် အခမဲ့စမ်းနိုင်ပါတယ်။ Free mode က Limit အနိမ့်ဆုံးဖြစ်ပြီး RPS/Token ကန့်သတ်ချက်က Organization ပေါ်မူတည်ပါတယ်။ Free mode မှာ Prompt/Output ကို Model Training အတွက် အသုံးပြုနိုင်ပါတယ်။ | Text Translation/Context/Audit အတွက် OpenAI-compatible endpoint နဲ့ သုံးနိုင်ပါတယ်။ | **အသစ်ထည့်ထားပြီး** |
| **[Cohere](https://docs.cohere.com/v2/docs/rate-limits)** | Trial API Key က အခမဲ့ဖြစ်ပြီး လက်ရှိ Docs အရ တစ်လ 1,000 API Calls အထိသာ အသုံးပြုနိုင်ပါတယ်။ Chat Model အချို့မှာ 20 requests/minute Limit ရှိပါတယ်။ | Command Model တွေကို Translation/Context/Audit အတွက် စမ်းနိုင်ပါတယ်။ OpenAI-compatible API လည်း ရှိပါတယ်။ | **အသစ်ထည့်ထားပြီး** |
| **[Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/platform/pricing/)** | Free Workers Plan မှာ တစ်နေ့လျှင် 10,000 Neurons အထိ အခမဲ့အသုံးပြုနိုင်ပါတယ်။ နေ့စဉ် 00:00 UTC မှာ ပြန်စတင်တွက်ချက်ပါတယ်။ Model အချို့က Paid Plan / Billing လိုနိုင်ပါတယ်။ | OpenAI-compatible API ဖြစ်လို့ Recap ရဲ့ Story Context, Translation, Audit နဲ့ Studio ရဲ့ AI Title Suggestion မှာ သုံးနိုင်ပါတယ်။ | **အသစ်ထည့်ထားပြီး** |
| **[NVIDIA NIM](https://build.nvidia.com/explore/discover)** | NVIDIA Developer Program မှာ API Catalog ကို Prototype/Development အတွက် သုံးနိုင်ပါတယ်။ Model တစ်ခုချင်းစီရဲ့ Access နဲ့ Rate Limit ကို Account/Catalog ထဲမှာ စစ်ရပါမယ်။ | Open-weight Model များကို NVIDIA ရဲ့ Hosted API ကနေ စမ်းသုံးနိုင်ပါတယ်။ | **အသစ်ထည့်ထားပြီး** |
| **[Ollama (Local)](https://ollama.com/download)** | Cloud API အသုံးခ မရှိပါ။ ဒါပေမဲ့ ကိုယ့် PC ထဲမှာ Model Download လုပ်ပြီး CPU/GPU/RAM/Storage ကို ကိုယ်တိုင် သုံးရပါတယ်။ | Internet မလိုဘဲ Local Model နဲ့ Translation/Context စမ်းချင်တဲ့အခါ အသုံးဝင်ပါတယ်။ စက်စွမ်းဆောင်ရည်ပေါ်မူတည်ပြီး နှေးနိုင်ပါတယ်။ | **ပါပြီးသား** |

**Free API နဲ့ပတ်သက်ပြီး သိထားရန်**

- **အခမဲ့ဆိုတာ အကန့်အသတ်မရှိတာ မဟုတ်ပါ။** Quota ပြည့်သွားရင် 429/Rate Limit Error ရနိုင်ပြီး နောက်နေ့ပြန်စောင့်ရတာ၊ Model ပြောင်းရတာ ဖြစ်နိုင်ပါတယ်။
- Mistral Free mode က Evaluation/Prototype အတွက်သာ ရည်ရွယ်ထားပြီး Limit အနိမ့်ဆုံးဖြစ်ပါတယ်။ Mistral Free mode မှာ Prompt နဲ့ Output ကို Model Training အတွက် အသုံးပြုနိုင်တဲ့အတွက် ကိုယ်ရေးကိုယ်တာ/လျှို့ဝှက် Video Transcript တွေကို မပို့ခင် Privacy Setting ကို စစ်ပါ။
- Cohere Trial Key က တစ်လ 1,000 API Calls အထိသာ ရပြီး Model အလိုက် Request/Minute Limit သီးခြားရှိပါတယ်။ အမြဲတမ်း unlimited Free API မဟုတ်ပါ။
- OpenRouter မှာ Model ID အဆုံးမှာ `:free` ပါတဲ့ Free Variant တွေကို ရွေးနိုင်ပါတယ်။ ၂၀၂၆-၁၁-၀၆ စစ်ဆေးချိန်တွင် အဲဒီ `:free` Variant တွေအတွက် 20 requests/minute နဲ့ 50 requests/day Limit ရှိပါတယ်။ `openrouter/free` က Free Model တစ်ခုကို အလိုအလျောက်ရွေးပေးတဲ့ Router ဖြစ်ပေမဲ့ ရလာတဲ့ Model/အရည်အသွေး မတူနိုင်ပါဘူး။
- Cloudflare ကို သုံးမယ်ဆိုရင် Free Workers Plan မှာ ခွင့်ပြုထားတဲ့ Model ကို ရွေးပါ။ ဥပမာ Model Catalog မှာ Free Plan အတွက် ဖော်ပြထားတဲ့ Gemma/GLM/Nemotron Model များထဲက ကိုယ့်အကောင့်မှာ ရနိုင်တာကို ရွေးပါ။ Model တစ်ခုချင်းစီရဲ့ နောက်ဆုံးအခြေအနေကို Cloudflare Dashboard မှာ စစ်ပါ။
- NVIDIA NIM မှာ Model ID ကို ခန့်မှန်းပြီး မထည့်ပါနဲ့။ NVIDIA API Catalog ထဲမှာ ကိုယ့် Key နဲ့ အသုံးပြုခွင့်ရတဲ့ Model ရဲ့ ID အတိအကျကို Copy ကူးထည့်ပါ။
- Hugging Face Inference Providers မှာ Free User အတွက် လစဉ် $0.10 Credit ရှိတယ်လို့ Pricing စာတမ်းမှာ ဖော်ပြထားပါတယ် (ပြောင်းလဲနိုင်ပါတယ်)။ စမ်းသပ်ဖို့ကောင်းပေမဲ့ Video အရှည်ကြီးတစ်ခုလုံး Recap လုပ်ဖို့ များသောအားဖြင့် မလုံလောက်ပါ။ လက်ရှိ App မှာ သီးခြား Provider အဖြစ် မချိတ်ထားသေးပါ။
- Cerebras က စမ်းသပ်ဖို့ $5 Promo Credit တစ်ကြိမ် ရနိုင်ပေမဲ့ Verified Payment Method ထည့်ရပြီး Credit က 30 ရက်အတွင်း သက်တမ်းကုန်ပါတယ်။ အမြဲတမ်း Free Tier မဟုတ်လို့ ဒီ App ရဲ့ ပုံမှန် Free Provider စာရင်းထဲ မထည့်ထားပါ။
- DeepSeek API က Token အလိုက် Billing လုပ်တဲ့ Paid API ဖြစ်ပါတယ်။ အခမဲ့အသုံးပြုနိုင်တဲ့ Model Gateway တချို့မှာ တစ်ခါတစ်ရံ Free Model ရှိနိုင်ပေမဲ့ DeepSeek API ကိုယ်တိုင်ကို Free လို့ မယူဆပါနဲ့။

**English:** These providers power story context, translation, translation audits and AI-assisted thumbnail title ideas. Gemini, Groq, OpenRouter and Ollama were already supported. Cloudflare Workers AI, NVIDIA NIM, Mistral and Cohere are now added to the application. Free quotas and available models can change; check each provider's current account dashboard before long jobs.

#### Studio ထဲက API ကို ဘယ်လိုချိတ်မလဲ / How to Configure an AI Provider

1. **Studio Tab** ကိုဖွင့်ပြီး အောက်ပိုင်းရှိ **Optional AI Provider** အပိုင်းကို ရှာပါ။
2. **Provider** မှာ Groq, OpenRouter, Mistral AI, Cohere, Cloudflare Workers AI, NVIDIA NIM သို့မဟုတ် Ollama တစ်ခုကို ရွေးပါ။
3. **Model ID** အကွက်ထဲမှာ Provider Dashboard မှာ ရတဲ့ Model ID အတိအကျကို ထည့်ပါ။ Free သုံးချင်ရင် Free Plan မှာ အသုံးပြုခွင့်ရှိတဲ့ Model ကိုသာ ရွေးပါ။
4. **API Key** အကွက်မှာ သက်ဆိုင်ရာ Key ကို ထည့်ပါ။ Ollama Local အတွက်တော့ API Key မလိုပါ။
5. **Test AI** ကိုနှိပ်ပြီး စမ်းသပ်ပါ။ ဒီအဆင့်က Prompt အသေးတစ်ခု ပို့တာဖြစ်လို့ Provider Quota ကို အနည်းငယ် သုံးနိုင်ပါတယ်။
6. အလုပ်လုပ်ကြောင်း သေချာမှ **Use for Recap** ကိုနှိပ်ပါ။ နောက်တစ်ကြိမ် **START / RESUME** စတဲ့အခါမှ ရွေးထားတဲ့ Provider/Model ကို Story Context, Translation နဲ့ Audit မှာ သုံးပါမယ်။

**Mistral AI သီးသန့်ပြင်ဆင်ရန်**

- [Mistral La Plateforme](https://console.mistral.ai/) မှာ Account ဖွင့်ပြီး API Key ထုတ်ပါ။
- `MISTRAL_API_KEY` ထဲ Key ထည့်ပါ။
- `MISTRAL_MODEL` အတွက် Model Catalog မှာ ရတဲ့ Model ID ကို ရွေးပါ။ Free mode မှာ Rate Limit အနိမ့်ဆုံးဖြစ်ပြီး Evaluation/Prototype အတွက်သာ သင့်တော်ပါတယ်။ Free mode က Prompt/Output ကို Training အတွက် အသုံးပြုနိုင်ပါတယ်။

**Cohere သီးသန့်ပြင်ဆင်ရန်**

- [Cohere Dashboard](https://dashboard.cohere.com/api-keys) မှာ Trial API Key ထုတ်ပါ။
- `COHERE_API_KEY` ထဲ Key ထည့်ပါ။
- `COHERE_MODEL` ထဲ Dashboard မှာ Trial Key နဲ့ ခေါ်ခွင့်ရှိတဲ့ Chat Model ID ကို ထည့်ပါ။ Cohere Trial က တစ်လ 1,000 API Calls အထိသာ ရပါတယ်။

**Cloudflare သီးသန့်ပြင်ဆင်ရန်**

- `CF_API_TOKEN` = Cloudflare Dashboard က API Token။
- `CF_ACCOUNT_ID` = Cloudflare Account ID။ ဒီတန်ဖိုးကို Studio ထဲက Model/API Key အကွက်မှာ မထည့်ရပါ။ Local `.env` ထဲမှာ ကိုယ်တိုင် ထည့်ပါ။
- `CF_MODEL` = Workers AI မှာ လက်ရှိရနိုင်တဲ့ Model ID။
- ဥပမာ Model ID ပုံစံက `@cf/google/gemma-4-26b-a4b-it` လို ဖြစ်နိုင်ပေမဲ့ ကိုယ့် Free Plan မှာ ရ/မရ Dashboard မှာ စစ်ပါ။

**NVIDIA NIM သီးသန့်ပြင်ဆင်ရန်**

- NVIDIA Developer Program ကို ဝင်ပြီး NVIDIA API Catalog ကနေ API Key ထုတ်ပါ။
- Studio ထဲမှာ **NVIDIA NIM** ကိုရွေးပြီး ကိုယ့် Account မှာ Access ရတဲ့ Model ID ကိုထည့်ပါ။ ဥပမာ `openai/gpt-oss-120b` က NIM Catalog မှာရှိတဲ့ Model ID ပုံစံတစ်ခုဖြစ်ပါတယ်။ Catalog ပြောင်းလဲနိုင်တဲ့အတွက် ကိုယ့် Dashboard မှာ ပြန်စစ်ပါ။

**Fallback Provider သုံးရန်**

Provider တစ်ခု Quota ပြည့်တာ၊ 429 Error ဖြစ်တာမျိုးရှိရင် ကိုယ်တိုင်ပြင်ဆင်ထားတဲ့ အခြား Provider တွေကို အစဉ်လိုက် စမ်းနိုင်ပါတယ်။ Local `.env` ထဲမှာ ဥပမာ—

```ini
RECAP_AI_PROVIDER=groq
RECAP_AI_FALLBACKS=cloudflare,nvidia,mistral,cohere,openrouter
```

ဒီဥပမာမှာ Groq ကို အရင်သုံးပြီး မအောင်မြင်မှ Cloudflare၊ NVIDIA၊ Mistral၊ Cohere နဲ့ OpenRouter တို့ကို အစဉ်လိုက် စမ်းပါမယ်။ Fallback ထဲမှာ ရေးထားတဲ့ Provider တွေကို အရင် Key/Model ပြင်ဆင်ထားဖို့ လိုပါတယ်။ Provider တစ်ခုက Error ပြန်ပေးတိုင်း နောက် Provider ကို အလိုအလျောက် စမ်းနိုင်ပေမဲ့ Paid Model သို့ အလိုအလျောက် ပြောင်းသုံးတာ မဟုတ်ပါ။ ရွေးထားတဲ့ Model ID တွေရဲ့ Pricing ကို ကိုယ်တိုင် စစ်ထားပါ။

**English:** In Studio, select a provider, enter the exact model ID and API key, then press **Test AI**. When the test succeeds, press **Use for Recap**. The next Recap START/RESUME uses that provider for story context, translation and audit. Cloudflare also requires `CF_ACCOUNT_ID` in the local `.env`. Optional fallback providers are tried only when listed explicitly in `RECAP_AI_FALLBACKS`.

#### Thumbnail / Image API — fal.ai ကို ဘယ်လိုသဘောထားရမလဲ

**မြန်မာ:** `fal.ai` ကို Groq လို Text Translation Provider နဲ့ မရောပါနဲ့။ ဒီ App မှာ fal.ai ကို **Thumbnail Background ပုံအသစ် ဖန်တီးဖို့** သုံးတာဖြစ်ပါတယ်။ မူရင်း Video ထဲက Frame ကို ရွေးပြီး မြန်မာခေါင်းစဉ်/Logo တင်တဲ့ Local Thumbnail Mode နဲ့တော့ API Key မလိုပါ။

- **Local Frame Thumbnail:** FFmpeg က မူရင်း Video ထဲက Frame တွေကို ထုတ်ယူပြီး Thumbnail အဖြစ် ပြင်ဆင်ပေးပါတယ်။ AI Credit မလိုပါ။
- **AI Background (fal.ai):** AI က Background ပုံအသစ် ဖန်တီးပေးပြီး App က မြန်မာ Title/Logo ကို Local မှာ ထပ်တင်ပေးပါတယ်။ `FAL_KEY` လိုပါတယ်။
- fal.ai Model API တွေက အောင်မြင်စွာ ထုတ်ပေးတဲ့ Output အလိုက် Credit ကောက်ခံပါတယ်။ လက်ရှိ Pricing ကို စစ်ပြီးမှ သုံးပါ။ `FAL_KEY` ရှိတာနဲ့ Free ဖြစ်သွားတာ မဟုတ်ပါဘူး။
- Thumbnail ပုံ ၃ မျိုးလိုရင် **Create 3 Local Variants** ကို သုံးပါ။ ဒီ Feature က Local အနေနဲ့ ထုတ်ပေးတာဖြစ်လို့ fal.ai Credit မသုံးပါ။

**English:** fal.ai is an image-generation service in this app, not a translation provider. Local frame-based thumbnails and local variants do not need API credits. AI-generated backgrounds require `FAL_KEY` and can consume prepaid fal credits per successful output.

#### Narrator / TTS Voice Provider — ဘယ်အသံက မြန်မာအတွက် အဆင်ပြေလဲ

| Voice Provider | မြန်မာအတွက် အသုံးပြုနိုင်မှု | အခမဲ့ / ကန့်သတ်ချက် | App ထဲက အသုံးပြုပုံ |
|---|---|---|---|
| **Microsoft Edge TTS** | `my-MM-ThihaNeural` (ယောက်ျား)၊ `my-MM-NilarNeural` (မိန်းမ) | သီးခြား API Key မလိုပါ။ Online Service ဖြစ်ပြီး Service/Network ကန့်သတ်ချက် ရှိနိုင်ပါတယ်။ | **အလွယ်ဆုံး Free Myanmar Voice**။ Narrator Voice မှာ ရွေးပါ။ |
| **Azure Speech** | Myanmar Standard Voice နှစ်မျိုးအတွက် Azure ရဲ့ `my-MM` Voice Support ရှိပါတယ်။ | Free F0 Resource မှာ Request Limit ရှိပါတယ် (လက်ရှိ Docs အရ 20 transactions/60 seconds၊ Request တစ်ခုအတွက် Audio အများဆုံး 10 minutes)။ Region/Quota ကို စစ်ပါ။ | `AZURE_SPEECH_KEY` နဲ့ `AZURE_SPEECH_REGION` ထည့်ပြီး Narrator Voice မှာ Azure Voice ကို ရွေးပါ။ |
| **ElevenLabs** | App ရဲ့ မူလ `eleven_multilingual_v2` Model က ပံ့ပိုးတဲ့ ဘာသာစကား 29 မျိုးစာရင်းထဲ Myanmar မပါပါ။ | Free Plan မှာ 10,000 Credits/Month ရှိပြီး API သုံးနိုင်သော်လည်း သုံးသမျှ Credit လျော့ပါတယ်။ | Myanmar Voice အတွက် မူလ Model ကို တိုက်ရိုက်မအကြံပြုပါ။ အခြားဘာသာစကားအတွက်သာ သုံးမယ်ဆိုရင် သက်ဆိုင်ရာ Model/Voice ကို အရင်စမ်းပါ။ |
| **Gemini TTS** | Voice Style အမျိုးမျိုး ရှိပါတယ်။ ဒါတွေကို Native Myanmar Voice 30 မျိုးလို့ မယူဆရပါ။ | Google ရဲ့ TTS Pricing/Model အလိုက် အခမဲ့အသုံးပြုခွင့် မရှိနိုင်ပါ။ | Gemini TTS ကို ရွေးမယ်ဆိုရင် Voice Style ကို စမ်းပြီး Quota/Pricing ကို စစ်ပါ။ |
| **Google Cloud Gemini TTS (Preview)** | Google Cloud ရဲ့ Gemini TTS Language List မှာ Burmese (my-MM) ပါဝင်ပါတယ်။ | လက်ရှိ Pricing မှာ Gemini TTS အတွက် Free usage မရှိကြောင်း ဖော်ပြထားပါတယ်။ | **လက်ရှိ App ထဲ မချိတ်ထားသေးပါ။** အခမဲ့ API လိုအပ်ချက်နဲ့ မကိုက်ညီလို့ နောက်ထပ် Paid TTS Option အဖြစ်သာ စဉ်းစားနိုင်ပါတယ်။ |

**အရေးကြီး:** Myanmar Recap အတွက် ပထမဆုံး စမ်းသင့်တာက Edge TTS ဖြစ်ပါတယ်။ အသံအရည်အသွေး/သတ်မှတ်ချက် ပိုလိုရင် Azure F0 ကို စမ်းနိုင်ပါတယ်။ ElevenLabs Free Plan ရှိတာနဲ့ Myanmar ဘာသာကို လက်ရှိရွေးထားတဲ့ TTS Model က ပံ့ပိုးတယ်လို့ မဆိုလိုပါဘူး။

**English:** Edge TTS is the simplest no-key Burmese narrator option. Azure Speech supports the `my-MM` Nilar and Thiha standard voices and has an F0 free resource with strict request limits. The app's current ElevenLabs default model, `eleven_multilingual_v2`, does not list Burmese among its 29 supported languages; verify a different model before using it for Myanmar narration.

#### Target Language များ / Supported Target Languages

**မြန်မာ:** Recap မှာ နောက်ဆုံးထွက်လာမယ့် ဘာသာစကားကို အောက်ပါထဲက ရွေးနိုင်ပါတယ်။ TTS Provider တစ်ခုချင်းစီရဲ့ Voice ရနိုင်မှုကတော့ မတူပါဘူး။

Myanmar (Burmese), English, Chinese, Japanese, Korean, Hindi, Thai, Vietnamese, Indonesian, Malay, Filipino (Tagalog), Spanish, Portuguese, French, German, Italian, Russian, Turkish, Arabic, Bengali, Tamil, Telugu နဲ့ Urdu။

**English:** The app can translate to the target languages listed above. Narrator voice availability depends on the selected TTS provider and its language support.


### API Key ထည့်သွင်းရမည့်နေရာ / API Keys and Environment Variables

**မြန်မာ:** API Key တွေကို Repository ထဲက `.env.example` ကို မူတည်ပြီး ကိုယ့်စက်ထဲမှာရှိတဲ့ `.env` ဖိုင်ထဲမှာသာ ထည့်ပါ။ API Key, Cookie File နဲ့ ကိုယ်ပိုင် Project ဖိုင်တွေကို GitHub ပေါ် မတင်ပါနဲ့။ `.env` ကို အခြားသူထံ ပို့ပေးဖို့လည်း မလိုပါဘူး။

| Feature / ဝန်ဆောင်မှု | Environment Variable | ဘာအတွက်လဲ |
|---|---|---|
| Gemini | `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/apikey) က API Key။ Story Context, Translation နဲ့ Audit အတွက်။ |
| Groq | `GROQ_API_KEY`, `GROQ_MODEL` | [Groq Console](https://console.groq.com/keys) က Key နဲ့ Model ID။ |
| OpenRouter | `OPENROUTER_API_KEY`, `OPENROUTER_MODEL` | [OpenRouter Keys](https://openrouter.ai/keys) က Key နဲ့ လက်ရှိ Free Model ID။ |
| Mistral AI | `MISTRAL_API_KEY`, `MISTRAL_MODEL` | [Mistral La Plateforme](https://console.mistral.ai/) က Key နဲ့ Free mode Model ID။ |
| Cohere | `COHERE_API_KEY`, `COHERE_MODEL` | [Cohere API Keys](https://dashboard.cohere.com/api-keys) က Trial Key နဲ့ Model ID။ |
| Cloudflare Workers AI | `CF_API_TOKEN`, `CF_ACCOUNT_ID`, `CF_MODEL` | [Cloudflare Dashboard](https://dash.cloudflare.com/) က Token, Account ID နဲ့ Free Plan မှာရနိုင်တဲ့ Model။ |
| NVIDIA NIM | `NVIDIA_API_KEY`, `NVIDIA_MODEL` | [NVIDIA API Catalog](https://build.nvidia.com/) က Developer Key နဲ့ ကိုယ့် Account မှာရတဲ့ Model ID။ |
| Ollama | `OLLAMA_BASE_URL`, `OLLAMA_MODEL` | [Ollama](https://ollama.com/download) ကို စက်ထဲ Install လုပ်ပြီး Local Model Download လုပ်ပါ။ API Key မလိုပါ။ |
| Azure Speech | `AZURE_SPEECH_KEY`, `AZURE_SPEECH_REGION` | Azure Speech Resource ရဲ့ Key နဲ့ Region။ Myanmar Voice အတွက် F0 Quota/Region ကို စစ်ပါ။ |
| ElevenLabs | `ELEVENLABS_API_KEY`, `ELEVENLABS_VOICE_ID`, `ELEVENLABS_MODEL_ID` | [ElevenLabs](https://elevenlabs.io/app/settings/api-keys) ရဲ့ Key နဲ့ Voice/Model ID။ Myanmar ကို လက်ရှိရွေးထားတဲ့ Model က ပံ့ပိုး/မပံ့ပိုး စစ်ပါ။ |
| fal.ai | `FAL_KEY`, `FAL_IMAGE_MODEL` | [fal.ai](https://fal.ai/dashboard/keys) က Key။ AI Thumbnail Background အတွက်ဖြစ်ပြီး Credit ကုန်နိုင်ပါတယ်။ |

**English:** Store credentials only in your local `.env` file. The table lists optional provider variables. Never commit API keys, cookies or private project files.

### လုပ်ငန်းစဉ်အလိုက် အသုံးပြုပုံ / Practical Workflows

#### Workflow A — မူရင်း Video ကို မြန်မာ Recap ထုတ်ခြင်း

1. `RUN.bat` ကိုဖွင့်ပြီး **Source Video → Browse** မှ Video ရွေးပါ။
2. **Source Language** ကို Auto-detect သို့မဟုတ် မူရင်းအသံရဲ့ ဘာသာစကားအတိုင်း ရွေးပါ။ Whisper က မူရင်းအသံကို Local မှာ စာသားပြောင်းပေးပါတယ်။ ပထမဆုံးအကြိမ်မှာ Whisper Model Download လုပ်ရနိုင်ပါတယ်။
3. **Target Language** ကို Myanmar (Burmese) ရွေးပါ။
4. Studio Tab မှာ AI Provider/Model ကို စမ်းပြီး **Use for Recap** လုပ်ထားပါ။ မပြောင်းထားရင် Gemini က Default ဖြစ်ပါတယ်။
5. Narrator Voice မှာ မြန်မာအသံအတွက် **Microsoft Edge Thiha / Nilar** ကို ရွေးပါ။ Voice Speed နဲ့ Production Tools တွေကို လိုအပ်သလို ချိန်ပါ။
6. **Preview** မှာ Title/Logo/Blur Box/Extra Text နေရာချပါ။ Video Ratio, Fill, Quality နဲ့ Narration Subtitle ကိုလည်း စစ်ပါ။
7. **START / RESUME** နှိပ်ပြီး လုပ်ဆောင်ပါ။ မပြီးသေးရင် Safe Stop လုပ်ပြီး နောက်မှ Resume ပြန်လုပ်နိုင်ပါတယ်။
8. ပြီးသွားရင် Output Video, SRT, Thumbnail နဲ့ Quality Report တွေကို Job Folder မှာ စစ်ပါ။ စာကြောင်းတချို့ မသဘာဝကျရင် **Edit Text** မှာ ပြင်ပြီး ပြင်ထားတဲ့ Line တွေကိုပဲ Voice အသစ်ထုတ်ပါ။

**English:** Choose a source video and source language, set Myanmar as the target, select a text provider and Burmese narrator, configure overlays/subtitles/ratio/quality, then press START/RESUME. Review the final video, SRT, thumbnail and report. Use Edit Text to correct individual lines and re-voice only the edits.

#### Workflow B — Video Download လုပ်ပြီး Recap Queue သို့ ပို့ခြင်း

1. Studio Tab ထဲက URL အကွက်မှာ ကိုယ်ပိုင်ခွင့်ပြုချက်ရှိတဲ့ Public Video URL ထည့်ပါ။
2. Video Quality, Audio-only/Video, Playlist နဲ့ Subtitle Download Option တွေကို လိုအပ်သလို ရွေးပါ။
3. **Add to Queue** / Download ကိုနှိပ်ပြီး Queue Status ကို စောင့်ကြည့်ပါ။
4. Download ပြီး Video ကို Recap Input သို့ တိုက်ရိုက်ပို့နိုင်ပါတယ်။ Auto Enqueue/Auto Start ဖွင့်ထားရင် Download ပြီးနောက် Recap Queue ကိုလည်း အလိုအလျောက် လွှဲပို့နိုင်ပါတယ်။
5. Failed ဖြစ်ရင် Retry လုပ်ပါ။ Website/URL တိုင်း အလုပ်လုပ်မယ်လို့ အာမမခံနိုင်တာကို သတိပြုပါ။

**English:** Add an authorized public URL in Studio, choose the download options, and add it to the persistent queue. Send completed downloads to Recap manually or enable the optional automatic enqueue/start settings. Retry failed downloads when appropriate.

#### Workflow C — Thumbnail သီးသန့် ဖန်တီးခြင်း

1. **Thumbnail Tab** ကိုဖွင့်ပြီး Local Video ရွေးပါ။
2. Auto Best Frame သုံးမလား၊ **Choose Frame** နဲ့ ကိုယ်တိုင်ရွေးမလား ဆုံးဖြတ်ပါ။
3. မြန်မာ Title, Title Style, Logo နဲ့ Aspect Ratio ကို သတ်မှတ်ပါ။
4. **Generate Thumbnail** သို့မဟုတ် **Create 3 Local Variants** ကိုနှိပ်ပါ။ Local Mode မှာ API Credit မလိုပါ။
5. Background အသစ်ကို AI နဲ့ဖန်တီးချင်မှသာ fal.ai ကို ရွေးပြီး `FAL_KEY` ထည့်ပါ။ အဲဒီ Mode က Credit ကုန်နိုင်ပါတယ်။

**English:** Choose a local source video, select an automatic or manual frame, add a Burmese title/logo, choose the aspect ratio, and generate a local thumbnail or three variants. Use fal.ai only when you want a newly generated AI background and accept its credit cost.

#### Workflow D — ရှိပြီးသား Subtitle ကိုပဲ ဘာသာပြန်ခြင်း

1. **Subtitles Tab** မှာ SRT/VTT ဖိုင် Import လုပ်ပါ။
2. Source/Target Language, AI Provider နဲ့ Model ကို ရွေးပါ။
3. Translate လုပ်ပါ။ ဒီအလုပ်က Whisper ကို ပြန်မခေါ်ပါ။
4. ဘာသာပြန်စာကို တစ်ကြောင်းချင်း Review/Edit လုပ်ပါ။
5. Translated-only သို့မဟုတ် Bilingual SRT Export လုပ်ပါ။ မူရင်း Timestamp တွေကို ထိန်းထားပါတယ်။

**English:** Import an existing SRT/VTT file, choose languages and a provider, translate without running Whisper, review/edit the cues, then export translated-only or bilingual SRT.

#### Workflow E — Video အရှည်ကို Social Platform အတွက် အပိုင်းခွဲခြင်း

1. **Splitter Tab** မှာ Video တစ်ခု သို့မဟုတ် Folder ရွေးပါ။
2. Each Part ကြာချိန်၊ Smart Cut စောင့်ချိန်၊ Ratio/Fill နဲ့ Quality ကို သတ်မှတ်ပါ။
3. လိုရင် Text Box နဲ့ Part Number ထည့်ပါ။
4. **Check Cuts** နဲ့ ဖြတ်မယ့်နေရာတွေ ကြိုစစ်ပြီး **START SPLIT** နှိပ်ပါ။
5. STOP လုပ်ထားရင် နောက်တစ်ကြိမ် START လုပ်တဲ့အခါ မပြီးသေးတဲ့ အပိုင်းကနေ ဆက်နိုင်ပါတယ်။

**English:** Add one or more videos, set part duration and Smart Cut, choose layout/quality, add text and part numbers, preview cut positions, then start splitting. Interrupted jobs can resume from unfinished parts.

#### Workflow F — Project Setting နဲ့ Batch Processing

- **Project Tab** မှာ မကြာခဏသုံးတဲ့ Setting/Path တွေကို Project အဖြစ် Save/Load လုပ်ပါ။
- **Pronunciation Editor** မှာ ဇာတ်ကောင်အမည်/စကားလုံးတွေကို TTS မှန်ကန်စွာ ဖတ်စေဖို့ အသံထွက် အစားထိုးစာလုံး သတ်မှတ်ပါ။
- **Waveform** မှာ အသံရှိ/မရှိကို အကြမ်းဖျဉ်းကြည့်ပါ။
- Intro/Outro, BGM, Smart Silence Removal ကို လိုအပ်မှသာ ဖွင့်ပါ။ Default ပိတ်ထားတာတွေကို Video အတိုနဲ့ အရင်စမ်းပါ။
- Preflight/QC နဲ့ Disk/Storage ကို စစ်ပါ။
- Video အများကြီး Recap လုပ်ဖို့ **Recap Queue** ထဲထည့်ပါ။ Queue က အလုပ်တွေကို တစ်ခုချင်းစီ လုပ်ဆောင်ပြီး Failed Job ကို Retry လုပ်နိုင်ပါတယ်။

**English:** Save reusable settings in Project, adjust pronunciations, inspect the waveform, optionally add branding/music or reduce silence, run preflight/QC and monitor storage. Add multiple files to Recap Queue for sequential processing and retry failures as needed.

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

- **မြန်မာ:** Error ဖြစ်ရင် `run.log` နဲ့ Error Message ကို ပို့ပါ။ API Key, Cookie, Password နဲ့ ကိုယ်ရေးကိုယ်တာ အချက်အလက်တွေကို ဖျောက်ပြီးမှ မျှဝေပါ။  
  **English:** When reporting an issue, share the relevant log and error message after removing API keys, cookies, passwords and personal information.

အပြည့်အစုံ Feature စာရင်းနဲ့ နည်းပညာပိုင်း အသေးစိတ်ကို [STUDIO_FEATURES.md](STUDIO_FEATURES.md) မှာလည်း ကြည့်နိုင်ပါတယ်။ ဒီ README ကတော့ အသုံးပြုသူအနေနဲ့ ဘယ် Tab က ဘာလုပ်ပေးလဲ၊ ဘယ်လိုသုံးရမလဲ၊ ဘာတွေသတိထားရမလဲဆိုတာ မြန်မာလို နားလည်လွယ်အောင် ရှင်းပြထားတာပါ။

**English:** See [STUDIO_FEATURES.md](STUDIO_FEATURES.md) for the implementation scope and additional technical details. This README is intended as the user-facing bilingual guide to the available tabs, workflows, setup and limitations.
