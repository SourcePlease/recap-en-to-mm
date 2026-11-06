# Recap Studio — အသုံးပြုနည်း၊ Feature လမ်းညွှန်နှင့် PC Test Checklist

ဤစာတမ်းက Recap Studio ထဲမှာ ဘာတွေပါသလဲ၊ Feature တစ်ခုချင်းစီက ဘာအတွက် အသုံးဝင်သလဲ၊ ဘယ်လိုသုံးရမလဲဆိုတာကို မြန်မာလို အဓိကထားပြီး ရှင်းပြထားပါတယ်။ လိုအပ်တဲ့နေရာတွေမှာ English အမည်နဲ့ Technical အကြောင်းအရာကိုပါ တွဲရေးထားပါတယ်။

ဒီစာတမ်းက SourcePlease/recap-en-to-mm ရဲ့ feature/studio-expansion branch အတွက် ဖြစ်ပါတယ်။ မူရင်း Windows App နဲ့ main branch ကို မထိခိုက်စေဘဲ သီးခြားပြင်ဆင်ထားပါတယ်။

> **အရေးကြီး:** စာတမ်းထဲမှာ “အသုံးပြုနိုင်ပြီ” လို့ ဖော်ပြထားတာက Code ထဲမှာ အကောင်အထည်ဖော်ထားတဲ့အရာကို ဆိုလိုတာပါ။ သင့် PC ပေါ်မှာ Run ပြီး လက်တွေ့စမ်းသပ်ပြီးမှသာ အလုပ်လုပ်ကြောင်း အတည်ပြုနိုင်ပါတယ်။ “စမ်းသပ်ရန် / Planned” လို့ ဖော်ပြထားတဲ့အရာတွေကို လက်ရှိအလုပ်လုပ်နေတဲ့ Feature လို့ မယူဆပါနဲ့။

---

## 1. App ကို ဘယ်လိုအသုံးပြုမလဲ

ဒီ App ကို Video Recap တစ်ခုတည်းလုပ်ဖို့ မဟုတ်ဘဲ Video ကို Download လုပ်ခြင်း၊ စာတန်းထိုးပြင်ခြင်း၊ Thumbnail ဖန်တီးခြင်း၊ Video အပိုင်းခွဲခြင်း၊ Project သိမ်းခြင်းနဲ့ Batch အလုပ်လုပ်ခြင်းတို့အတွက်ပါ စုစည်းထားပါတယ်။

### App ထဲက အဓိက Tab များ

| Tab | ဘာလုပ်ပေးသလဲ | ဘယ်အချိန်မှာ သုံးမလဲ |
|---|---|---|
| Recap | Video ကို နားထောင်၊ စာသားထုတ်၊ ဘာသာပြန်၊ Narrator အသံထုတ်ပြီး Video ပြန်တည်ဆောက် | Anime / Movie / Documentary Recap လုပ်မယ်ဆိုရင် |
| Splitter | Video တစ်ခုကို အချိန်အလိုက် အပိုင်းခွဲ | Episode အရှည်ကြီးကို အပိုင်းငယ်ခွဲချင်ရင် |
| Studio | YouTube၊ Facebook စတဲ့ Supported URL များ Download လုပ်၊ AI Provider စမ်း | Online Video ကို Recap လုပ်ဖို့ အရင် Download လုပ်ချင်ရင် |
| Thumbnail | မူရင်း Video Frame ကနေ Thumbnail ထုတ်၊ Title/Logo တင် | Recap Video အတွက် Cover ပုံလုပ်ချင်ရင် |
| Subtitles | SRT/VTT တင်သွင်း၊ ဘာသာပြန်၊ စာကြောင်းပြင်၊ Export | Whisper ကို ထပ်မသုံးဘဲ Subtitle သီးသန့်ပြင်ချင်ရင် |
| Project | Project Save/Load၊ Audio Waveform၊ Pronunciation၊ BGM၊ Intro/Outro၊ QC | Project ကို နောက်မှဆက်လုပ်ချင်ရင် |
| Recap Queue | Video အများအပြားကို တစ်ခုချင်းစီ အလိုအလျောက်လုပ် | Folder ထဲက Episode အများကြီးကို Batch လုပ်ချင်ရင် |

**English:** Recap Studio combines video recap, splitting, downloading, thumbnail generation, subtitle translation, project tools and a persistent batch queue in one Windows desktop application.

---

## 2. Recap Mode များ — Storytelling တစ်မျိုးတည်း မဟုတ်တော့ပါ

Recap မှာ အဓိကအားဖြင့် “ဘာသာပြန်ပြီး ဘယ်လိုပြောပြမလဲ” ဆိုတာကို ရွေးနိုင်ဖို့ Narration Style များ ထည့်ထားပါတယ်။ အောက်ပါ Style များဟာ Narrator ပြောပုံပြောင်းပေးတာဖြစ်ပြီး မူရင်းဇာတ်လမ်းထဲက အချက်အလက်တွေကို ကိုယ်တိုင်ဖြည့်စွက်ဖန်တီးခွင့် မပေးပါဘူး။

### လက်ရှိ UI မှာ ရွေးနိုင်တဲ့ Narration Style များ

| Style | ဘယ်လိုပြောမလဲ | သင့်တော်တဲ့ Video |
|---|---|---|
| **Storytelling** | ဇာတ်လမ်းကို အစမှအဆုံး သဘာဝကျကျ ဆက်စပ်ပြောပြမယ်။ လက်ရှိ Default Style ဖြစ်တယ်။ | Anime / Movie Recap အများစု |
| **Documentary** | တည်ငြိမ်ပြီး အချက်အလက်ကို ဦးစားပေးပြောမယ်။ အလွန်အကျွံ စိတ်လှုပ်ရှားစေတဲ့ စကားမသုံးဘူး။ | Documentary / History / True Story |
| **Cinematic** | ရုပ်ရှင်ဆန်တဲ့ စကားပြောစီးဆင်းမှုနဲ့ Suspense ကို ထိန်းပြီး ပြောမယ်။ မူရင်းမှာမရှိတဲ့ အန္တရာယ်၊ စိတ်ခံစားချက်ကို မတီထွင်ဘူး။ | Action / Thriller / Mystery |
| **Casual** | ပေါ့ပေါ့ပါးပါး နားလည်လွယ်တဲ့ စကားပြောပုံစံ သုံးမယ်။ Slang နဲ့ အပိုစကားတွေ အလွန်အကျွံ မထည့်ဘူး။ | Comedy / Slice of Life |
| **Character Focus** | ဇာတ်ကောင်တစ်ယောက်ချင်းစီရဲ့ ဆုံးဖြတ်ချက်၊ ဆက်ဆံရေး၊ ရည်ရွယ်ချက်နဲ့ ပြောင်းလဲမှုကို ပိုရှင်းအောင် ပြောမယ်။ | Character Drama / Romance |
| **Anime Recap** | Anime Recap လို တက်ကြွတဲ့ စကားပြောစီးဆင်းမှု သုံးမယ်။ ဂျပန်နာမည်နဲ့ Technique အမည်တွေကို တစ်သမတ်တည်း ထိန်းမယ်။ | Anime / Manga Adaptation |
| **Explainer** | အကြောင်းရင်း၊ အကျိုးဆက်၊ စည်းမျဉ်းနဲ့ ဇာတ်လမ်းထဲက Clue တွေကို အဆင့်လိုက် နားလည်လွယ်အောင် ရှင်းမယ်။ | Sci-fi / Fantasy / Mystery |

**သုံးနည်း**
1. Recap Tab ကိုဖွင့်ပါ။
2. Source Video နဲ့ Source Language ကို ရွေးပါ။
3. Target Language ကို Myanmar (Burmese) ရွေးပါ။
4. Narration Style မှာ ကိုယ်လိုချင်တဲ့ပုံစံကို ရွေးပါ။
5. Narrator Voice နဲ့ Speed ကို ရွေးပါ။
6. Preview စစ်ပြီး START / RESUME ကိုနှိပ်ပါ။

**သတိပြုရန်:** Style ပြောင်းလိုက်ရင် Translation Plan အသစ်တည်ဆောက်ရပါမယ်။ အရင် Style နဲ့ ရေးထားတဲ့ Translation ကို မမှားယွင်းစွာ ပြန်သုံးမိစေဖို့ Style ကို Job Checkpoint ထဲမှာပါ ထည့်သွင်းခွဲထားပါတယ်။ Whisper Transcript ကိုတော့ Source Video မပြောင်းလဲသရွေ့ ပြန်သုံးနိုင်ပါတယ်။

### Production Modes / Production Mode များ

Subbing နဲ့ Dubbing ကို Narration Style တစ်ခုတည်းအဖြစ် မရောဘဲ သီးခြား Workflow အဖြစ်ထားပါတယ်။

#### A. Subbing Mode — မူရင်းအသံမပြောင်းဘဲ စာတန်းထိုးမယ် (Implemented)

လက်ရှိ Subtitle Import / Translate Tab မှာ SRT/VTT ဖိုင်ရှိပြီးသားဆိုရင် အောက်ပါအတိုင်း အလုပ်လုပ်နိုင်ပါတယ်။

- SRT/VTT Import လုပ်ပြီး Timestamp မပျက်အောင် ဘာသာပြန်မယ်။
- Cue တစ်ကြောင်းချင်း ပြင်ဆင်နိုင်မယ်။
- Translated SRT သို့မဟုတ် Bilingual SRT ထုတ်နိုင်မယ်။
- Source Video ရွေးပြီး Subtitle Burn-in MP4 ထုတ်နိုင်မယ်။
- TTS မခေါ်ဘူး။ မူရင်း Audio Content ကို ထိန်းထားပြီး MP4 နဲ့ ကိုက်ညီအောင် AAC အဖြစ် Encode ပြန်လုပ်နိုင်တယ်။
- ဒီ Import workflow က Whisper ကို အလိုအလျောက် မခေါ်သေးဘူး။ SRT/VTT မရှိရင် အရင် Transcript ထုတ်ရမယ်။

**မြန်မာလို:** မူရင်းအသံကို မပြောင်းဘဲ Subtitle ပဲ ဘာသာပြန်ထည့်ချင်ရင် ဒီ Mode ကို သုံးပါ။ SRT/VTT ကို Import လုပ်၊ Translate/Edit လုပ်ပြီး Source Video ကို ရွေးကာ Render လုပ်နိုင်ပါတယ်။

#### B. Original Audio + BGM Control — မူရင်းအသံနဲ့ BGM ကို ထိန်းမယ် (Implemented)

- Original Audio ON — Source Dialogue + Original BGM နှစ်မျိုးလုံးကို Smart Sync Timeline နဲ့ ချိန်ညှိပြီး Narration အောက်ခံအဖြစ် ထားမယ်။
- Original Audio OFF — မူရင်း Source Audio Track တစ်ခုလုံးကို ပိတ်မယ်။
- Source BGM ON — မူရင်း Dialogue + BGM အပြည့်အစုံကို ထားမယ်။
- Source BGM OFF — Demucs နဲ့ Dialogue/Vocals ကို ခွဲထုတ်ပြီး BGM ကို ဖယ်ရှားမယ်။
- Narration ပြောနေချိန် Source Audio ကို Sidechain Ducking နဲ့ လျှော့ပေးမယ်။
- External BGM File ကတော့ Source BGM နဲ့ သီးခြား Control ဖြစ်တယ်။

**သတိ:** Source BGM OFF အတွက် Demucs လိုအပ်တယ်။ Demucs မရှိရင် pip install -U demucs လုပ်ရမယ်။ Separation မအောင်မြင်ရင် Dialogue ကိုပါ ပိတ်မိမယ့်အစား Render ကို Error နဲ့ ရပ်မယ်။ Demucs က CPU/RAM နဲ့ ပထမဆုံး Model Download အချိန် ပိုယူနိုင်တယ်။

#### C. Character Voice Dub — ဇာတ်ကောင်အလိုက် အသံသီးခြားတပ်မယ် (Manual Workflow Implemented)

- Dubbing Tab မှာ Translated SRT/VTT ကို Import လုပ်ပြီး Timestamped Dialogue Row အဖြစ် ပြောင်းနိုင်တယ်။
- Row တစ်ကြောင်းချင်းစီမှာ Start / End / Speaker / Translated Text ကို ကိုယ်တိုင်ပြင်နိုင်တယ်။
- Speaker A/B စတဲ့ Label တစ်ခုစီကို Edge TTS Voice တစ်မျိုးစီနဲ့ ချိတ်နိုင်တယ်။ ဇာတ်ကောင်တစ်ယောက်က Scene အများကြီးမှာ ပြန်ပေါ်လာရင် သတ်မှတ်ထားတဲ့ Voice ကိုပဲ ပြန်သုံးတယ်။
- Dialogue Row နဲ့ Speaker-to-Voice Mapping ကို Dubbing Project JSON အဖြစ် Save/Load လုပ်နိုင်တယ်။
- Cue Timestamp အတိုင်း TTS အသံတွေကို ချိန်ပြီး Video ထဲ ပြန်ပေါင်းတယ်။ Dialogue ကြာချိန် မကိုက်ရင် သတ်မှတ်ထားတဲ့ အကန့်အသတ်အတွင်း အမြန်နှုန်းညှိတယ်။
- Source Audio ကို Mute, Original Dialogue + BGM ထားခြင်း၊ သို့မဟုတ် Demucs နဲ့ Instrumental BGM သီးသန့်ထားခြင်း ရွေးနိုင်တယ်။
- **ကန့်သတ်ချက်:** Automatic Speaker Diarization / Character Identity Detection မပါသေးပါ။ Translated Subtitle ကို အရင်ပြင်ဆင်ထားရမယ်။ Speaker Label နဲ့ Voice ကို User ကိုယ်တိုင် စစ်ပြီး သတ်မှတ်ရမယ်။

**ဒီ Mode မှာ အရေးကြီးတာ:** AI က အသံကြားရုံနဲ့ Character ရဲ့ Gender ကို အမြဲမှန်မှန် မခန့်မှန်းနိုင်ပါဘူး။ Voice ကို AI က အလိုအလျောက် ခန့်မှန်းပေးနိုင်တဲ့အဆင့်ရှိလာရင်တောင် User က Character နဲ့ Voice ကို ပြန်စစ်ပြီး ပြင်နိုင်တဲ့ Manual Voice Casting စနစ် ထည့်သင့်ပါတယ်။ အသံအမျိုးအစားကို လူတစ်ယောက်ရဲ့ Gender နဲ့ တစ်ထပ်တည်း သတ်မှတ်မထားဘဲ Voice Profile အဖြစ်သာ သုံးမယ်။

#### D. Original Dialogue + Translated Subtitle — မူရင်းစကားသံနဲ့ ဘာသာပြန်စာတန်း

- မူရင်းဇာတ်ကောင်အသံကို ထားမယ်။
- စကားသံကို မြန်မာလို Dub မလုပ်ဘူး။
- မူရင်းစကားကို မြန်မာစာတန်းအဖြစ် ပြမယ်။
- မူရင်း Audio Track ကို မပျက်စီးစေဘဲ Video ထဲ Subtitle Burn-in လုပ်မယ်။
- BGM ကို သီးခြားဖယ်/ထိန်းချင်ရင် Source Separation လိုမယ်။

#### E. Scene-by-Scene Recap — ဇာတ်ဝင်ခန်းလိုက် Recap

- Video ကို Scene အလိုက် ခွဲမယ်။
- Scene တစ်ခုချင်းစီမှာ သက်ဆိုင်တဲ့ Subtitle Cue / Transcript ကို ချိတ်မယ်။
- Scene အစ/အဆုံးကို Preview ကြည့်ပြီး ကိုယ်တိုင်ပြင်နိုင်မယ်။
- Narration တစ်ပိုင်းချင်းစီနဲ့ Source Clip ကို တွဲစစ်နိုင်မယ်။

#### F. Highlights / Trailer Mode — အဓိကအခန်းများကို ရွေးထုတ်မယ်

- ဇာတ်လမ်းထဲက အရေးကြီးတဲ့ Scene တွေကို ရွေးထုတ်မယ်။
- Spoiler Level နဲ့ Target Duration ကို User က သတ်မှတ်နိုင်ရမယ်။
- Original Ending ကို ဖော်ပြမလား၊ မဖော်ပြဘူးလား ရွေးနိုင်ရမယ်။
- ဒီ Mode က ဇာတ်လမ်းအချက်အလက်ကို ချန်လှပ်နိုင်တဲ့ Summary Task ဖြစ်တဲ့အတွက် ပုံမှန် Storytelling ရဲ့ “အချက်အလက်မချန်ရ” စည်းမျဉ်းနဲ့ သီးခြား Planner Logic လိုအပ်တယ်။

---

## 3. AI Text Provider — အခမဲ့ Provider ကို ဦးစားပေးပြီး အလိုအလျောက်ရွေးမယ်

Text AI Provider တွေကို အဓိကအားဖြင့် Story Context, Translation နဲ့ Translation Audit အတွက် သုံးပါတယ်။ Whisper က Audio ကို စာသားပြောင်းပေးတာဖြစ်ပြီး Text AI Provider နဲ့ မတူပါဘူး။

### Auto / Free-first Rotation

လက်ရှိပြင်ဆင်ထားတဲ့ Auto Mode ရဲ့ အလုပ်လုပ်ပုံက ဒီလိုပါ။

1. RECAP_AI_PROVIDER ကို auto ထားမယ်။
2. App က RECAP_AI_AUTO_ORDER ထဲက Provider တွေကို အစဉ်လိုက် စစ်မယ်။
3. API Key လိုတဲ့ Provider ဆိုရင် Key ရှိရမယ်။ Model ID လည်း သတ်မှတ်ထားရမယ်။
4. ပထမဆုံး ပြည့်စုံတဲ့ Provider ကို အသုံးပြုမယ်။
5. Request မအောင်မြင်ရင် RECAP_AI_FALLBACKS ထဲမှာ ပါပြီး Key/Model ပြည့်စုံတဲ့ Provider နောက်တစ်ခုကို စမ်းမယ်။
6. Hosted Free Provider တစ်ခုမှ မပြည့်စုံရင် Gemini ကို Default အဖြစ် သုံးမယ်။

**သိထားရန်:** Auto Rotation ဆိုတာ Model အားလုံးကို အလိုအလျောက် Download လုပ်ပေးတာ မဟုတ်ပါဘူး။ API Key နဲ့ Model ID ထည့်ထားတဲ့ Provider တွေကြားမှာသာ ပြောင်းသုံးနိုင်ပါတယ်။ OpenRouter ရဲ့ openrouter/free ကို သုံးရင် Free Model ရနိုင်တဲ့အထဲက တစ်ခုကို OpenRouter ဘက်က ရွေးပေးနိုင်ပါတယ်။

### Free-first Provider အစီအစဉ်

| အစဉ် | Provider | အသုံးပြုပုံ | Free သုံးရာမှာ သတိထားရန် |
|---:|---|---|---|
| 1 | Groq | မြန်ဆန်တဲ့ Text Generation / Translation | Model အလိုက် RPM, RPD, TPM, TPD ကန့်သတ်ချက်ရှိတယ်။ |
| 2 | OpenRouter | Model မျိုးစုံကို API တစ်ခုနဲ့ သုံးနိုင်တယ် | openrouter/free သို့မဟုတ် :free Model ကို ရွေးပါ။ Free Variant တွေမှာ Rate Limit ရှိတယ်။ |
| 3 | Cloudflare Workers AI | Text Generation / Translation | Free Daily Neurons ရှိပေမဲ့ Model တိုင်း Free မဟုတ်ဘူး။ |
| 4 | NVIDIA NIM | Hosted Open Model များ စမ်းသပ်ရန် | Developer API Catalog မှာ Model Access နဲ့ Limit ပြောင်းနိုင်တယ်။ |
| 5 | Mistral AI | Translation / Text Generation | Free Mode က Evaluation/Prototyping အတွက်ဖြစ်ပြီး Limit နည်းတယ်။ Data Terms ကိုဖတ်ပါ။ |
| 6 | Cohere | Text Generation / Translation | Trial Key က Free ဖြစ်ပေမဲ့ Call Limit နဲ့ Model Limit ရှိတယ်။ |
| 7 | Ollama | Local AI Model | API Bill မရှိဘူး။ ဒါပေမဲ့ PC ရဲ့ RAM/CPU/GPU ကို အသုံးပြုမယ်။ |
| Fallback | Gemini | Story Context, Translation, Audit | Selected Models မှာ Free Tier ရှိတယ်။ Quota က Account အလိုက် ကွာတယ်။ |

**လက်တွေ့အကြံပြုချက်**
- Free Model ကို ရွေးချင်ရင် OpenRouter Model ID ကို openrouter/free ထားနိုင်တယ်။
- Groq Model ID ကို ရွေးတဲ့အခါ Groq Console ရဲ့ လက်ရှိ Model Catalog နဲ့ Free Developer Limit ကို စစ်ပါ။
- Cloudflare / NVIDIA / Mistral / Cohere တို့မှာလည်း ကိုယ့် Account မှာ ရရှိနိုင်တဲ့ Model ID ကိုပဲ သုံးပါ။
- Free Tier ရှိတယ်ဆိုတာ အကန့်အသတ်မရှိ သုံးလို့ရတယ်လို့ မဆိုလိုပါဘူး။
- Provider တစ်ခုချင်းစီရဲ့ Quota ပြည့်သွားရင် နောက် Provider ကို ပြောင်းစမ်းနိုင်ပေမဲ့ အားလုံး Limit ပြည့်နေရင် Job ရပ်နိုင်တယ်။

### Paid / Usage-based Provider များ

အောက်ပါ Provider တွေကို လက်ရှိ Free-first Default Rotation ထဲ မထည့်ထားပါဘူး။ လိုအပ်မှသာ သီးခြားထည့်သွင်းစဉ်းစားသင့်ပါတယ်။

| Provider / Model Family | ဘာအတွက် အသုံးဝင်လဲ | ကုန်ကျစရိတ်သတိပြုရန် |
|---|---|---|
| # OpenAI GPT API | အရည်အသွေးမြင့် Translation / Reasoning | Token အလိုက် ပေးချေရတယ်။ |
| # Anthropic Claude API | Long Context / Natural Writing | Token အလိုက် ပေးချေရတယ်။ |
| # DeepSeek API | Reasoning / Translation | API က Usage-based ဖြစ်ပြီး အမြဲတမ်း Free မဟုတ်ဘူး။ |
| # Paid Gemini Models | Context / Translation / Audit | Free Tier ကျော်ရင် Billing သက်ရောက်နိုင်တယ်။ |
| # Paid OpenRouter Models | Model အမျိုးမျိုး ရွေးချယ်သုံးရန် | Model တစ်ခုချင်းစီ ဈေးနှုန်းမတူဘူး။ |
| # fal.ai | AI Thumbnail Background / Image Generation | Image တစ်ပုံချင်းစီအလိုက် Credits ကုန်နိုင်တယ်။ |
| # ElevenLabs | Premium TTS | Free Credits ကန့်သတ်ထားပြီး Burmese Support ကို Model အလိုက် စစ်ရမယ်။ |
| # Azure Speech | Burmese TTS | Free Quota ကျော်ရင် Paid ဖြစ်နိုင်တယ်။ |

# နဲ့ စထားတဲ့အရာတွေကို Paid / Usage-based အဖြစ် သတ်မှတ်ထားတာပါ။ လက်ရှိ Free-first Rotation ထဲ အလိုအလျောက် မထည့်ထားပါဘူး။

### API Key ထည့်နည်း

1. App Folder ထဲက .env.example ကို Copy လုပ်ပြီး .env အမည်နဲ့ သိမ်းပါ။
2. ကိုယ်သုံးမယ့် Provider ရဲ့ API Key ကို သက်ဆိုင်ရာ Variable ထဲ ထည့်ပါ။
3. Model ID ကိုလည်း သတ်မှတ်ပါ။
4. .env ကို GitHub ပေါ် မတင်ပါနဲ့။
5. Studio Tab ထဲက Provider Test ကို အသုံးပြုပြီး Key/Model အလုပ်လုပ်မလုပ် စမ်းပါ။
6. Recap ကို START မလုပ်ခင် Provider နဲ့ Model ရွေးချယ်မှုကို စစ်ပါ။

ဥပမာ — OpenRouter Free Router:

~~~dotenv
RECAP_AI_PROVIDER=auto
RECAP_AI_AUTO_ORDER=groq,openrouter,cloudflare,nvidia,mistral,cohere,ollama
RECAP_AI_FALLBACKS=groq,openrouter,cloudflare,nvidia,mistral,cohere,ollama

OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL=openrouter/free
~~~

---

## 4. TTS — အသံထုတ်ပေးတဲ့ Provider များ

TTS ဆိုတာ Text-to-Speech ဖြစ်ပြီး ဘာသာပြန်ထားတဲ့ စာသားကို အသံဖိုင်အဖြစ် ပြောင်းပေးတာပါ။

| Provider | အသုံးပြုပုံ | အခမဲ့အခြေအနေ |
|---|---|---|
| Microsoft Edge TTS | Myanmar Thiha / Nilar အသံထုတ်နိုင်တယ် | API Key မလိုဘဲ သုံးနိုင်ပေမဲ့ Network / Service ကန့်သတ်ချက်ရှိတယ်။ |
| Gemini TTS | Voice Style / Natural Speech | Account / Model / Billing အလိုက် ကွာတယ်။ |
| Azure Speech | my-MM-ThihaNeural / my-MM-NilarNeural | F0 Free Quota ကန့်သတ်ချက်ရှိတယ်။ |
| ElevenLabs | Premium Multilingual Voice | Free Credit ရှိပေမဲ့ Default Multilingual v2 မှာ Burmese ပါမပါကို အရင်စစ်ရမယ်။ |

**အကြံပြုချက်:** မြန်မာအသံကို အဓိကသုံးမယ်ဆိုရင် Edge TTS ရဲ့ Thiha / Nilar ကို ပထမဆုံးစမ်းပါ။ Voice ရွေးချယ်မှုက Output Language နဲ့ ကိုက်ညီရပါမယ်။

### Character Voice Dub အတွက် နောက်ထပ်လိုအပ်မယ့်အရာ

Narrator Voice တစ်မျိုးတည်းနဲ့ ဇာတ်ကောင်အားလုံးကို ပြောစေတာနဲ့ Character Voice Dub က မတူပါဘူး။ Character Voice Dub အတွက် အောက်ပါအဆင့်တွေ လိုပါတယ်။

1. Speaker Diarization — ဘယ်အချိန်မှာ ဘယ်သူပြောသလဲ ခွဲခြားခြင်း။
2. Speaker Review — Speaker A / B ကို Character အမည်နဲ့ User က ချိတ်ပေးခြင်း။
3. Voice Casting — Character တစ်ယောက်စီအတွက် အသံရွေးပေးခြင်း။
4. Dialogue Translation — Character ရဲ့ စကားပြောပုံနဲ့ ကိုက်ညီအောင် ဘာသာပြန်ခြင်း။
5. Audio Separation — မူရင်းစကားသံနဲ့ BGM ကို ခွဲထုတ်ခြင်း။
6. Voice Mixing — Dub အသံကို မူရင်း BGM နဲ့ အချိန်ညှိပေါင်းခြင်း။

Speaker Diarization နဲ့ Source Separation ကို Free Local Model တွေနဲ့ လုပ်နိုင်တဲ့နည်းလမ်းတွေရှိပေမဲ့ Model Download, RAM/VRAM နဲ့ Processing Time လိုအပ်ပါတယ်။ Optional Feature အဖြစ် ထည့်ပြီး Default မှာ မဖွင့်ထားတာ ပိုကောင်းပါတယ်။

---

## 5. Recap — Video ကို ဘာသာပြန်အသံနဲ့ ပြန်တည်ဆောက်ခြင်း

### အလုပ်လုပ်ပုံ

1. Source Video ကို ရွေးတယ်။
2. Whisper က မူရင်းအသံကို နားထောင်ပြီး Timestamp ပါတဲ့ Transcript ထုတ်တယ်။
3. AI က Story Context တည်ဆောက်ပြီး Character Name, Relationship, Place နဲ့ Term တွေကို မှတ်ထားတယ်။
4. Transcript ကို Target Language သို့ ပြန်ဆိုတယ်။
5. Translation Audit က အဓိပ္ပာယ်မပျောက်၊ စာကြောင်းမထပ်၊ သဘာဝကျမကျ စစ်တယ်။
6. TTS က Narration Audio ထုတ်တယ်။
7. Smart Sync က Narration နဲ့ Video Clip ကို အချိန်ညှိတယ်။
8. FFmpeg က Final Video, Subtitle နဲ့ Audio ကို ပေါင်းစပ်တယ်။

### Recap ထဲမှာ ပါဝင်တဲ့ Tools

- Source Language / Target Language ကို သီးခြားရွေးနိုင်တယ်။
- Myanmar Native Narration Style ကို အသုံးပြုတယ်။
- Story Context / Glossary နဲ့ Character Name တစ်သမတ်တည်း ထိန်းတယ်။
- Narrator Voice / Speed ကို ရွေးနိုင်တယ်။
- Smart Sync နဲ့ Segment တစ်ခုချင်းစီကို Video အချိန်နဲ့ ချိန်တယ်။
- Stop / Resume လုပ်နိုင်တယ်။
- TTS Segment Cache ကို ပြန်သုံးနိုင်တယ်။
- Folder Batch Processing နဲ့ Video အများအပြား လုပ်နိုင်တယ်။
- Preview Frame ကို ရွှေ့ကြည့်နိုင်တယ်။
- Title / Logo / Extra Text ကို Drag လုပ်နိုင်တယ်။
- Blur Box ကို Preview ပေါ်မှာ ဆွဲသတ်မှတ်နိုင်တယ်။
- Zoom / Mirror / Ratio / Fill / Output Quality ကို ချိန်နိုင်တယ်။
- Subtitle Burn-in နဲ့ SRT Export ကို အသုံးပြုနိုင်တယ်။

### Myanmar Narration အရည်အသွေး

မြန်မာစာကို English ဝါကျအစီအစဉ်အတိုင်း တိုက်ရိုက်ပြန်တာမျိုး မလုပ်ဖို့ သတ်မှတ်ထားပါတယ်။ မြန်မာလူတစ်ယောက်က ပရိသတ်ကို ပြောပြနေသလို နားလည်လွယ်ပြီး သဘာဝကျတဲ့ စကားပြောပုံစံကို ဦးစားပေးပါတယ်။

- “သည် / ၏ / ၌ / ပြုလုပ်ခဲ့သည်” လို စာပေသုံးပုံစံကို မလိုအပ်ဘဲ မသုံးဘူး။
- “သူက” ကို စာကြောင်းတိုင်းမှာ ထပ်မသုံးဘူး။
- “နော် / ဗျာ / ပေါ့” လို ဖြည့်စွက်စကားကို မလိုအပ်ဘဲ မထည့်ဘူး။
- ဇာတ်ကောင်အမည်၊ နေရာအမည်၊ Technique အမည်ကို တစ်သမတ်တည်း သုံးတယ်။
- အဓိပ္ပာယ်၊ အဖြစ်အပျက်နဲ့ အချက်အလက်ကို မပြောင်းဘူး။

---

## 6. Splitter — Video အပိုင်းခွဲခြင်း

Splitter က Video တစ်ခုတည်းကို အပိုင်းငယ်တွေ ခွဲပေးတယ်။

- Split Duration သတ်မှတ်နိုင်တယ်။
- Video အများအပြားကို Batch Split လုပ်နိုင်တယ်။
- Output Ratio / Fill / Text / Part Number ကို သတ်မှတ်နိုင်တယ်။
- Smart Cut က စကားပြောနေတဲ့အချိန်ကို ဖြတ်မိတာ လျှော့ချဖို့ Speech Pause ကို ရှာနိုင်တယ်။
- Output ဖိုင်တစ်ခုချင်းစီကို Preview စစ်နိုင်တယ်။

**သုံးနည်း**
1. Splitter Tab ကို ဖွင့်ပါ။
2. Video တစ်ခု သို့မဟုတ် Folder ထဲက Video များကို ရွေးပါ။
3. အပိုင်းတစ်ခုစီ ကြာချိန် သတ်မှတ်ပါ။
4. Ratio / Fill / Part Number ကို ရွေးပါ။
5. Smart Cut ကို လိုအပ်မှ ဖွင့်ပါ။
6. Output Folder ကို သတ်မှတ်ပြီး Split လုပ်ပါ။

---

## 7. Studio Downloader — Online Video Download

yt-dlp ကို အသုံးပြုပြီး Supported Website တွေက Video / Audio ကို Download လုပ်နိုင်ပါတယ်။

- Best Available / 1080p / 720p / 480p Quality။
- Audio Only (MP3)။
- Playlist Download။
- ရနိုင်တဲ့ Subtitle Download။
- Authorized cookies.txt ကို အသုံးပြုနိုင်တယ်။
- Download Progress ကို ကြည့်နိုင်တယ်။
- URL အများကြီးကို Persistent Queue ထဲ ထည့်နိုင်တယ်။
- Stop after current / Retry Failed / Clear Finished။
- Download ပြီးတဲ့ Video ကို Recap Queue ထဲ အလိုအလျောက် ထည့်နိုင်တယ်။
- Download ပြီးရင် Thumbnail ကို အလိုအလျောက် ဖန်တီးနိုင်တယ်။

**Supported Site သတိပြုရန်:** YouTube, Facebook, TikTok, Instagram, Reddit, X/Twitter စတာတွေကို yt-dlp Extractor ရှိသလောက် အသုံးပြုနိုင်ပါတယ်။ RedNote / Xiaohongshu အတွက် Generic Extractor က အမြဲအလုပ်လုပ်မယ်လို့ မအာမခံနိုင်ပါဘူး။ Login, Region Restriction, CAPTCHA, Website Update နဲ့ Removed URL ကြောင့် Download မရနိုင်ပါ။ DRM / Access Control ကို ကျော်ဖြတ်ဖို့ မရည်ရွယ်ထားပါဘူး။

---

## 8. Thumbnail Studio — Thumbnail သီးသန့်ဖန်တီးခြင်း

Thumbnail ကို Recap ပြီးမှသာ ဖန်တီးရတာ မဟုတ်ပါဘူး။ Thumbnail Tab ကို သီးခြားဖွင့်ပြီး မူရင်း Video ကနေ Cover ပုံ ထုတ်နိုင်ပါတယ်။

- FFmpeg နဲ့ Video Frame အများအပြား ထုတ်တယ်။
- Contrast / Detail ကို အခြေခံပြီး Best Frame ရွေးတယ်။
- Choose Frame နဲ့ ကိုယ်ကြိုက်တဲ့ Frame ကို ရွေးနိုင်တယ်။
- Local Variant ၃ မျိုး ထုတ်နိုင်တယ်။
- မြန်မာ Title Style တွေ ထည့်နိုင်တယ်။
- Logo / Channel Name ကို ထည့်နိုင်တယ်။
- 16:9 / 9:16 / 1:1 Ratio ကို ရွေးနိုင်တယ်။
- Auto-thumbnail after Recap နဲ့ Final Video ထွက်ပြီးနောက် Original Source Video က Frame ကို အသုံးပြုပြီး JPG ထုတ်နိုင်တယ်။
- Optional fal.ai AI Background ကို အသုံးပြုနိုင်တယ်။

**Local Mode** က PC ပေါ်မှာပဲ Frame / Text / Logo ကို ပေါင်းစပ်တာဖြစ်လို့ AI Image API Credits မလိုပါဘူး။ **fal.ai Mode** က AI Background Generate လုပ်တာဖြစ်ပြီး Account Credit ကုန်နိုင်ပါတယ်။

---

## 9. Subtitle Tools — SRT / VTT တင်သွင်းပြီး ဘာသာပြန်ခြင်း

Whisper ကို ထပ်မသုံးချင်တဲ့အခါ ဒီ Tab ကို သုံးပါ။

1. Subtitle Tab ကို ဖွင့်ပါ။
2. SRT သို့မဟုတ် VTT ဖိုင်ကို Import လုပ်ပါ။
3. Source / Target Language ကို ရွေးပါ။
4. Glossary ကို သုံးချင်ရင် ထည့်ပါ။
5. Translate ကို နှိပ်ပါ။
6. Cue တစ်ကြောင်းချင်းစီကို စစ်ပြီး လိုအပ်ရင် ပြင်ပါ။
7. Translated-only သို့မဟုတ် Bilingual SRT ကို Export လုပ်ပါ။

Timestamp တွေကို ထိန်းထားပြီး Subtitle Text ကိုပဲ ဘာသာပြန်ပေးပါတယ်။ Bilingual SRT မှာ Original နဲ့ Translation ကို တွဲထုတ်နိုင်ပါတယ်။

---

## 10. Project & Audio Tools

### Project Save / Load
- Project Settings နဲ့ File Path တွေကို သိမ်းထားနိုင်တယ်။
- နောက်မှ Project ကို ပြန်ဖွင့်ပြီး ဆက်လုပ်နိုင်တယ်။
- API Key / Secret ကို Project File ထဲ မကူးဘူး။

### Audio Waveform
- Audio ကို အပိုင်းငယ်စီ ဖတ်ပြီး RMS Waveform ဆွဲပြတယ်။
- RAM အများကြီး မသုံးအောင် Block အလိုက် စစ်တယ်။
- ဒီ Feature က Full Multitrack Timeline Editor မဟုတ်ဘူး။

### Pronunciation Dictionary
- TTS က နာမည်၊ ဂျပန်စကား၊ English Abbreviation တွေကို မှားဖတ်တဲ့အခါ အသံထွက်ကို ပြင်ပေးတယ်။
- ဥပမာ Source Term တစ်ခုကို ဘယ်လိုဖတ်စေချင်တယ်ဆိုတာ Mapping လုပ်နိုင်တယ်။
- ဒီ Dictionary က TTS အသံထွက်ကိုသာ ပြင်တယ်။ Subtitle စာသားကို မပြောင်းဘူး။

### Intro / Outro
- Channel Name / Logo ပါတဲ့ Intro / Outro Card ထည့်နိုင်တယ်။
- Intro / Outro Duration ကို သတ်မှတ်နိုင်တယ်။
- Default အနေနဲ့ ပိတ်ထားတယ်။

### Background Music (BGM)
- Narration အောက်မှာ Music File ကို Loop လုပ်ပြီး ထည့်နိုင်တယ်။
- Volume ကို 0–50% အတွင်း ချိန်နိုင်တယ်။
- Default ပိတ်ထားတယ်။
- ကိုယ်ပိုင်အသုံးပြုခွင့်ရှိတဲ့ Music ကိုသာ သုံးပါ။

### Smart Silence Removal
- Narration ထဲက တိတ်ဆိတ်နေတဲ့အချိန်တွေကို လျှော့ပေးနိုင်တယ်။
- အသံတိုးတိုးပြောထားတဲ့ စကားလုံးတွေကို မှားဖယ်နိုင်တဲ့အတွက် Default ပိတ်ထားတယ်။
- Video အတိုနဲ့ အရင်စမ်းပါ။

### Preflight / Output Quality Check
- Source File / FFmpeg / FFprobe / Disk Space ကို စစ်တယ်။
- API Credential ရှိမရှိကို စစ်နိုင်ပေမဲ့ Key မှန်မမှန်ကို Preflight တစ်ခုတည်းနဲ့ အာမမခံနိုင်ဘူး။
- Final Video ရှိမရှိ၊ Audio/Video Stream, Duration, Resolution, SRT နဲ့ Thumbnail ကို စစ်နိုင်တယ်။
- Quality Report ကို JSON အဖြစ် သိမ်းနိုင်တယ်။

### Storage / Safe Cache Cleanup
- Jobs / Downloads / Logs / Runtime Folder အရွယ်အစားကို ကြည့်နိုင်တယ်။
- Safe Cleanup က သတ်မှတ်ထားတဲ့ Cache File တွေကိုသာ ဖယ်ရှားတယ်။
- Final Video, Download, Job Checkpoint တွေကို မဖျက်ဘူး။

---

## 11. Recap Queue — Video အများကြီးကို တစ်ခုပြီးတစ်ခုလုပ်ခြင်း

- Local Video အများအပြားကို Queue ထဲ ထည့်နိုင်တယ်။
- Queue ကို Disk ပေါ်မှာ သိမ်းထားတယ်။
- App ပိတ်သွားရင် Pending Job တွေကို ပြန်ရယူနိုင်တယ်။
- Failed Job ကို Retry လုပ်နိုင်တယ်။
- Job တစ်ခုချင်းစီရဲ့ Progress / Status ကို ကြည့်နိုင်တယ်။
- Job တစ်ခုရဲ့ Result ကို နောက် Job နဲ့ မရောအောင် သီးခြား Folder ခွဲထားတယ်။

**အကြံပြုချက်:** ပထမဆုံး ၁–၃ မိနစ် Video နဲ့ စမ်းပါ။ Queue အလုပ်လုပ်ကြောင်း သေချာမှ Episode အများကြီး ထည့်ပါ။

---

## 12. PC မှာ Run ပြီးမှ စစ်ရန် — Test Checklist

အောက်က Checklist တွေကို PC မှာ App ကို Run ပြီးမှသာ Check လုပ်ပါ။ GitHub Actions အောင်မြင်တာနဲ့ PC မှာ GUI / API / Video အားလုံး အလုပ်လုပ်တယ်လို့ မဆိုလိုပါဘူး။

### A. Install & Startup

- [ ] Windows မှာ INSTALL_REQUIREMENTS.bat အောင်မြင်စွာ ပြီးသွားတယ်။
- [ ] RUN.bat နဲ့ App ဖွင့်လို့ရတယ်။
- [ ] App ဖွင့်ချိန်မှာ Python Error မတက်ဘူး။
- [ ] FFmpeg နဲ့ FFprobe ကို App က ရှာတွေ့တယ်။
- [ ] Myanmar Font ကို Preview / Subtitle မှာ မှန်မှန်ပြတယ်။
- [ ] App ပိတ်ပြီး ပြန်ဖွင့်တဲ့အခါ Config မပျောက်ဘူး။

### B. AI Provider & Free Rotation

- [ ] .env ကို ဖတ်နိုင်တယ်။
- [ ] Provider မရွေးထားဘဲ Auto Mode နဲ့ Gemini Fallback အလုပ်လုပ်တယ်။
- [ ] Groq Key + Model ထည့်ပြီး Auto Mode က Groq ကို ရွေးတယ်။
- [ ] OpenRouter Key + openrouter/free ထည့်ပြီး Free Router ကို စမ်းလို့ရတယ်။
- [ ] Groq ကို မရနိုင်အောင်လုပ်ပြီး နောက် Free Provider ကို Fallback လုပ်တယ်။
- [ ] Model ID မရှိတဲ့ Provider ကို Auto Mode က ကျော်သွားတယ်။
- [ ] API Key မမှန်ရင် Error Message က ဘယ် Provider မှာ ပြဿနာဖြစ်တယ်ဆိုတာ ဖော်ပြတယ်။
- [ ] Key ကို Log ထဲမှာ အပြည့်အစုံ မဖော်ပြဘူး။
- [ ] Provider တစ်ခု Quota ပြည့်ရင် အခြား Provider ကို ပြောင်းသုံးနိုင်တယ်။

### C. Recap Narration Styles

- [ ] Storytelling Style နဲ့ ၁–၃ မိနစ် Video စမ်းပြီး အလုပ်လုပ်တယ်။
- [ ] Documentary Style နဲ့ စမ်းပြီး စကားပြောပုံ တည်ငြိမ်လာတယ်။
- [ ] Cinematic Style နဲ့ စမ်းပြီး မူရင်းမှာမရှိတဲ့ အဖြစ်အပျက် မတီထွင်ဘူး။
- [ ] Casual Style နဲ့ စမ်းပြီး မြန်မာစကားပြောပုံ သဘာဝကျတယ်။
- [ ] Character Focus Style နဲ့ စမ်းပြီး ဇာတ်ကောင်အမည် / ဆက်ဆံရေး မလွဲဘူး။
- [ ] Anime Recap Style နဲ့ စမ်းပြီး Japanese Name / Technique တွေ တစ်သမတ်တည်း ရှိတယ်။
- [ ] Explainer Style နဲ့ စမ်းပြီး Cause / Effect ကို နားလည်လွယ်တယ်။
- [ ] Style ပြောင်းပြီး Resume လုပ်တဲ့အခါ အရင် Style ရဲ့ Translation ကို မမှားဘဲ ပြန်မသုံးဘူး။
- [ ] Whisper Transcript ကို မလိုအပ်ဘဲ ထပ်မလုပ်ဘူး။

### D. Voice / TTS / Audio

- [ ] Myanmar Thiha Voice နဲ့ အသံထွက်တယ်။
- [ ] Myanmar Nilar Voice နဲ့ အသံထွက်တယ်။
- [ ] Narrator Speed ကို ပြောင်းလို့ရတယ်။
- [ ] TTS Segment Cache ကို ပြန်သုံးနိုင်တယ်။
- [ ] Edge TTS 403 / Network Error ဖြစ်ရင် Log မှာ အကြောင်းရင်းပြတယ်။
- [ ] Narration နဲ့ Video Sync မလွဲဘူး။
- [ ] Background Music ပိတ်ထားရင် မထည့်ဘူး။
- [ ] Background Music ဖွင့်ထားရင် Voice ကို မဖုံးဘူး။
- [ ] Intro / Outro ဖွင့်ထားရင် Duration မှန်တယ်။
- [ ] Smart Silence Removal ပိတ်/ဖွင့် နှိုင်းယှဉ်ပြီး စကားလုံး မပျောက်ဘူး။

### E. Subtitle / Preview / Editor

- [ ] SRT Import လုပ်လို့ရတယ်။
- [ ] VTT Import လုပ်လို့ရတယ်။
- [ ] Subtitle Translation က Timestamp မပြောင်းဘူး။
- [ ] Bilingual SRT မှာ Original + Myanmar စာသား နှစ်မျိုးပါလာတယ်။
- [ ] Subtitle Text ကို ကိုယ်တိုင်ပြင်လို့ရတယ်။
- [ ] Preview Frame ရွှေ့ကြည့်လို့ရတယ်။
- [ ] Title ကို Drag လုပ်ရွှေ့လို့ရတယ်။
- [ ] Logo ကို Drag လုပ်ရွှေ့လို့ရတယ်။
- [ ] Blur Box ကို ဆွဲသတ်မှတ်လို့ရတယ်။
- [ ] Myanmar Font / Outline / Shadow မှန်တယ်။

### F. Thumbnail / Downloader

- [ ] Local Thumbnail ကို API Key မပါဘဲ ထုတ်လို့ရတယ်။
- [ ] Choose Frame နဲ့ ကိုယ်ကြိုက်တဲ့ Frame ရွေးလို့ရတယ်။
- [ ] Local Variant ၃ မျိုး ထွက်တယ်။
- [ ] Burmese Title / Logo မှန်တယ်။
- [ ] Auto-thumbnail after Recap အလုပ်လုပ်တယ်။
- [ ] YouTube URL တစ်ခု Download လုပ်လို့ရတယ်။
- [ ] Facebook / TikTok URL တစ်ခုချင်းစီ စမ်းတယ်။
- [ ] RedNote URL ကို သီးခြားစမ်းပြီး Support ရှိမရှိ မှတ်တမ်းတင်တယ်။
- [ ] Playlist Download စမ်းတယ်။
- [ ] MP3-only Download စမ်းတယ်။
- [ ] Download Queue ပိတ်ပြီးပြန်ဖွင့်ရင် Pending Item မပျောက်ဘူး။
- [ ] Failed Download ကို Retry လုပ်လို့ရတယ်။

### G. Splitter / Project / Queue

- [ ] Splitter က Video ကို သတ်မှတ်ထားတဲ့ Duration အတိုင်း ခွဲတယ်။
- [ ] Smart Cut က Speech Pause ကို သင့်တော်တဲ့နေရာမှာ ရွေးတယ်။
- [ ] Project Save လုပ်လို့ရတယ်။
- [ ] Project Load လုပ်ပြီး Setting ပြန်ရတယ်။
- [ ] Project JSON ထဲ API Key မပါဘူး။
- [ ] Audio Waveform ထွက်တယ်။
- [ ] Pronunciation Dictionary Save / Load လုပ်လို့ရတယ်။
- [ ] Preflight Report မှန်တယ်။
- [ ] Output Quality Report မှန်တယ်။
- [ ] Safe Cache Cleanup က Final Video / Checkpoint မဖျက်ဘူး။
- [ ] Recap Queue ထဲ Video အတို ၂ ခု ထည့်ပြီး တစ်ခုပြီးတစ်ခု လုပ်တယ်။
- [ ] Job တစ်ခု Fail ဖြစ်ရင် နောက် Job ကို မပျက်စီးစေဘူး။
- [ ] Stop / Resume လုပ်ပြီး အရင်ပြီးထားတဲ့အပိုင်းတွေကို ပြန်သုံးတယ်။

### H. Long Video / Final Quality

- [ ] ၁၀ မိနစ် Video တစ်ခု အစအဆုံး စမ်းပြီးတယ်။
- [ ] ၃၀ မိနစ် Video တစ်ခု စမ်းပြီးတယ်။
- [ ] Video အရှည်ကြီးမှာ RAM / CPU / Disk Usage ကို စစ်တယ်။
- [ ] Final Video မှာ Audio / Video Sync မလွဲဘူး။
- [ ] Subtitle အချိန်မရွေ့ဘူး။
- [ ] Video အဆုံးထိ Audio မဖြတ်သွားဘူး။
- [ ] Output Resolution / Ratio မှန်တယ်။
- [ ] Final Video ကို Windows Media Player / VLC မှာ ဖွင့်လို့ရတယ်။

### Test လုပ်တဲ့အခါ မှတ်တမ်းတင်ရန်

- [ ] App Version / Commit SHA ကို မှတ်ထားတယ်။
- [ ] ဘယ် Tab / ဘယ် Feature မှာ Error ဖြစ်တယ်ဆိုတာ ရေးထားတယ်။
- [ ] Error Log / Traceback ကို သိမ်းထားတယ်။
- [ ] Source Video ရဲ့ Format / Duration ကို မှတ်ထားတယ်။
- [ ] API Key / Cookies / Private Path တွေကို မျှဝေမိအောင် ဖယ်ထားတယ်။

---

## 13. Reference Repositories — ကိုးကားစစ်ဆေးထားတဲ့ Repo ၃ ခု

ဒီအပိုင်းက Feature အသစ်နံပါတ် 13 မဟုတ်ပါဘူး။ User ပေးထားတဲ့ Reference Repo ၃ ခုကနေ ဘယ် Feature တွေ အသုံးဝင်လဲ၊ ဘယ်အရာတွေကို တိုက်ရိုက်ကူးမသုံးသင့်လဲဆိုတာ နှိုင်းယှဉ်ထားတဲ့ စာတမ်းအပိုင်းပါ။ လက်ရှိ Project ဖြစ်တဲ့ `SourcePlease/recap-en-to-mm` ကိုလည်း အခြေခံ Repo အဖြစ် ထည့်တွက်ထားပါတယ်။

### 13.1 recap_studio_mm

Reference: https://github.com/htinkyawzaw2017-maker/recap_studio_mm

အသုံးဝင်တဲ့ အယူအဆများ —
- Recap နဲ့ Dialogue Dubbing ကို Workflow သီးခြားထားခြင်း။
- Original Audio ကို Narration အောက်ခံအဖြစ် Ducking လုပ်ခြင်း။
- Subtitle Timing / Coverage ကို စစ်ဆေးခြင်း။
- Thumbnail နဲ့ Branding ထည့်ခြင်း။

သတိပြုရန် — ဒီ Repo ရဲ့ Dialogue Dubbing ရှိတာနဲ့ Character တစ်ယောက်ချင်းစီကို အလိုအလျောက် မှန်ကန်စွာ ခွဲခြားပေးတဲ့ Diarization အပြည့်အစုံ ရှိတယ်လို့ မယူဆရပါ။

### 13.2 recap-studio-streamlit

Reference: https://github.com/htinkyawzaw2017-maker/recap-studio-streamlit

အသုံးဝင်တဲ့ အယူအဆများ —
- Render မလုပ်ခင် Script ကို User က Approve လုပ်နိုင်ခြင်း။
- API Key Pool / Failover နည်းလမ်း။
- Progress ကို သိမ်းဆည်းပြီး ပြန်ဆက်လုပ်နိုင်ခြင်း။
- Splitter ကနေ Recap Workflow သို့ ဆက်သွားနိုင်ခြင်း။

သတိပြုရန် — `recap_studio_mm` နဲ့ Engine အစိတ်အပိုင်းများ ဆက်စပ်နေတဲ့အတွက် Feature တူတာတွေကို Code အပြည့်အစုံ ထပ်ကူးမထည့်ဘဲ လိုအပ်တဲ့ Logic ကို လက်ရှိ Architecture နဲ့ ပေါင်းစပ်ရပါမယ်။

### 13.3 mmnext-movie-recap-pro

Reference: https://github.com/thihakyaw-leo/mmnext-movie-recap-pro

အသုံးဝင်တဲ့ အယူအဆများ —
- Narrator Segment နဲ့ Exact Dialogue Row ကို Data Model သီးခြားထားခြင်း။
- Speaker တစ်ယောက်ချင်းစီအတွက် Voice Mapping ပြုလုပ်ခြင်း။
- Local Whisper / FFmpeg Splitter အသုံးပြုခြင်း။
- Output Validation ထည့်သွင်းခြင်း။

သတိပြုရန် — Repo ထဲမှာ License ဖိုင် မတွေ့ခဲ့တဲ့အတွက် Source Code ကို တိုက်ရိုက်ကူးယူမသုံးဘဲ Architecture Idea အဖြစ်သာ ကိုးကားရပါမယ်။ UI ထဲမှာ ဖော်ပြထားတဲ့ Feature တိုင်းကို အလုပ်လုပ်ပြီးသားလို့လည်း မယူဆရပါ။

### 13.4 လက်ရှိ Project — recap-en-to-mm

Current branch: `feature/studio-expansion`

ဆက်လက်ထိန်းသိမ်းရမည့် အခြေခံများ —
- လက်ရှိ Windows Desktop App နဲ့ ရှိပြီးသား Recap / Splitter / Editor Workflow များ။
- Smart Sync, AI Provider, TTS Provider နဲ့ Queue။
- Downloader, Thumbnail, Subtitle Tools နဲ့ Project Tools။
- ရှိပြီးသား User Config နဲ့ Project Compatibility။

### 13.5 Repo ၄ ခုလုံးမှ ယူမည့် Feature Mapping

| Feature / အင်္ဂါရပ် | အဓိက Reference | လက်ရှိ Project ထဲ ပေါင်းစပ်မည့်ပုံ |
|---|---|---|
| Recap vs Character Dubbing | recap_studio_mm + mmnext-movie-recap-pro | သီးခြား Processing Mode နှစ်ခု |
| Original Audio Ducking | recap_studio_mm + recap-studio-streamlit | Smart Sync Timeline နဲ့ တွဲဖက် |
| Script Approval / Review Gate | recap-studio-streamlit + mmnext-recap design ideas | Render မလုပ်ခင် Review |
| API Key Pool / Failover | recap-studio-streamlit | လက်ရှိ AI Provider Selector နဲ့ ချိတ် |
| Speaker-to-Voice Mapping | mmnext-movie-recap-pro | Manual Mapping အရင်၊ Diarization ကို Optional ထား |
| Subtitle Timing / Scene Mapping | mmnext-recap design ideas + လက်ရှိ Subtitle Tools | Cue / Scene Editor |
| Proxy Preview / Project Metadata | mmnext-recap design ideas | ပေါ့ပါးတဲ့ Preview နဲ့ Local Project Save |
| Output Validation | mmnext-movie-recap-pro + လက်ရှိ Render Pipeline | Final Output QC |
| Existing Windows Features | လက်ရှိ recap-en-to-mm | မဖျက်၊ မပြောင်းလဲစေဘဲ တိုးချဲ့ |

**အရေးကြီးချက်:** Reference Repo ၃ ခုလုံးရဲ့ Feature တွေကို အကုန်လုံး တစ်ပုံစံတည်း ကူးထည့်မှာ မဟုတ်ပါ။ အသုံးဝင်တဲ့ Workflow နဲ့ Logic ကို လက်ရှိ Project ထဲ ပေါင်းစပ်မယ်။ License မသေချာတဲ့ Repo က Code ကို တိုက်ရိုက်မကူးဘူး။ Feature တစ်ခုချင်းစီကို Implemented / Planned / Optional လို့ ခွဲပြီး Test ပြီးမှ Implemented လို့ ပြောင်းမယ်။

---

## 14. နောက်ထပ် ထည့်သင့်တဲ့ Feature အကြံပြုချက်များ

ဒီအပိုင်းက လက်ရှိ Feature လို့ မဆိုလိုပါဘူး။ အရင်ဆုံး Free / Local ကို ဦးစားပေးပြီး အောက်ပါအတိုင်း အဆင့်လိုက် တိုးချဲ့သင့်ပါတယ်။

### Priority 1 — Free / Local နဲ့ အကျိုးရှိဆုံး

1. **Subtitle Timing Editor** — Cue အချိန်ကို Preview နဲ့ တိုက်စစ်ပြီး ပြင်ခြင်း။
2. **Scene Marker / Clip Mapping** — ဇာတ်ဝင်ခန်းအလိုက် Script နဲ့ Clip ချိတ်ခြင်း။
3. **Proxy Preview** — Video အရှည်ကြီး Preview ကို ပေါ့ပါးစေခြင်း။
4. **Manual Speaker / Character Voice Assignment** — Character နဲ့ Voice ကို User က ကိုယ်တိုင်ချိတ်ခြင်း။
5. **Project Library** — Project အများကြီးကို ရှာဖွေပြီး ပြန်ဖွင့်နိုင်ခြင်း။
6. **Subbing auto-transcription** — Subtitle ဖိုင်မရှိရင် Whisper ကနေ တိုက်ရိုက် Subbing Workflow စတင်နိုင်ခြင်း။

### Priority 2 — Optional Local AI

1. **Speaker Diarization** — Speaker တစ်ယောက်ချင်းစီကို ခွဲခြားခြင်း။
2. **Demucs / UVR Source Separation** — Dialogue နဲ့ BGM ခွဲခြင်း။
3. **Scene Detection** — Scene Change ကို အလိုအလျောက်ရှာခြင်း။
4. **Face / Character Tracking** — Scene ထဲက Character ကို လိုက်ကြည့်ခြင်း။
5. **Auto Reframe** — 16:9 ကနေ 9:16 ပြောင်းတဲ့အခါ Subject ကို အလယ်မှာ ထိန်းခြင်း။

### Priority 3 — Optional Cloud / Paid

1. Premium TTS Voice များ။
2. AI Thumbnail Image Generation။
3. Premium Long-context Translation Model များ။
4. Cloud Storage / Team Project Sync။
5. Social Platform Upload Integration။

**အကြံပြုချက်:** Default မှာ Local / Free Mode ကိုပဲ ဖွင့်ထားပါ။ Cloud / Paid Feature တွေကို User က ကိုယ်တိုင်ဖွင့်မှသာ API Request ပို့ပါ။ Paid Model ကို Free Rotation ထဲ မတော်တဆ မထည့်မိစေဖို့ Allowlist သီးခြားထားသင့်ပါတယ်။

---

## 15. Known Limitations / လက်ရှိသိထားရမယ့် ကန့်သတ်ချက်များ

- Free API Provider တစ်ခုချင်းစီရဲ့ Quota / Model Availability က အချိန်နဲ့အမျှ ပြောင်းနိုင်တယ်။
- Auto Provider က Key နဲ့ Model ID ပြည့်စုံတဲ့ Provider ကိုသာ ရွေးနိုင်တယ်။
- OpenRouter Free Model Router သုံးရင်လည်း Rate Limit ရှိတယ်။
- Whisper Model ကို ပထမဆုံးသုံးတဲ့အခါ Download လုပ်ရနိုင်တယ်။
- Video အရှည်ကြီးကို Processing လုပ်တဲ့အခါ CPU / RAM / Disk Space လိုတယ်။
- yt-dlp Website Support က Website ပြောင်းလဲမှုအပေါ် မူတည်တယ်။
- fal.ai Image Generation က Free Local Thumbnail နဲ့ မတူဘဲ Credits သုံးနိုင်တယ်။
- Edge TTS က Network / VPN / Proxy ကြောင့် 403 ဖြစ်နိုင်တယ်။
- Character Voice Dub အတွက် Speaker Diarization နဲ့ Audio Separation မရှိသေးရင် Gender အလိုက် အသံကို အလိုအလျောက် မှန်မှန်ခွဲမပေးနိုင်ဘူး။
- Original BGM ကို Dialogue ကနေ ခွဲထိန်းဖို့ Source Separation လိုတယ်။
- mmnext-recap ထဲက Timeline / AI / Render UI ကို အလုပ်လုပ်ပြီးသား Code လို့ မယူဆရဘူး။

---

## 16. Bug Report ပို့နည်း

Test လုပ်ပြီး Error ဖြစ်ရင် အောက်ပါအချက်တွေကို ပို့ပေးပါ။

1. ဘယ် Tab / Feature မှာ ဖြစ်တာလဲ။
2. ဘယ်အဆင့်မှာ Error ဖြစ်တာလဲ။
3. Error Message / Log / Traceback။
4. Source Video Format နဲ့ Duration။
5. သုံးထားတဲ့ AI Provider / TTS Provider အမည် (API Key မပါစေရ)။
6. မျှော်လင့်ထားတဲ့ Result နဲ့ တကယ်ထွက်လာတဲ့ Result။

**API Key, cookies.txt, Password, Private Token နဲ့ ကိုယ်ရေးကိုယ်တာ File Path တွေကို မပို့ပါနဲ့။**

**English:** When reporting a bug, include the feature, exact step, error log, source format/duration and provider name. Never share credentials or cookies.
