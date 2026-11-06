# Audio Modes & Studio Integration / Audio Mode များနှင့် Studio ချိတ်ဆက်မှု

ဒီစာတမ်းမှာ Recap Studio ရဲ့ မူရင်းအသံထိန်းသိမ်းမှု၊ BGM ခွဲခြားမှုနဲ့ Subbing / Dubbing Mode တွေကို သီးခြားသတ်မှတ်ထားပါတယ်။

This document defines source-audio preservation, optional background-music separation, and the planned boundaries between Subbing and Dubbing.

## 1. Original Audio Controls / မူရင်းအသံထိန်းချုပ်မှု

- **Original Audio ON** — keep the source video's dialogue and original background music.
- **Original Audio OFF** — remove the complete source audio track. Narration and separately selected external music remain independent.
- **Source BGM ON** — keep the complete source mix (dialogue + original BGM).
- **Source BGM OFF** — use Demucs vocal separation to retain dialogue/vocals while removing most accompaniment. This is optional and CPU-intensive.
- **Original Audio Volume** — controls the source track before narration-aware ducking.
- **External Background Music** — remains a separate optional music file and does not replace the source-audio controls.

**မြန်မာလို**
- **Original Audio ON** — မူရင်းဗီဒီယိုထဲက Dialogue နဲ့ မူရင်း BGM နှစ်မျိုးလုံး ထိန်းထားမယ်။
- **Original Audio OFF** — မူရင်း Audio Track တစ်ခုလုံးကို ပိတ်မယ်။ Narration နဲ့ သီးခြားရွေးထားတဲ့ External Music ကတော့ သီးခြားဖြစ်တယ်။
- **Source BGM ON** — မူရင်း Dialogue + BGM အပြည့်အစုံကို ထားမယ်။
- **Source BGM OFF** — Demucs နဲ့ Vocal/Dialogue ကို ခွဲထုတ်ပြီး BGM/Accompaniment ကို အများဆုံးဖယ်ရှားမယ်။ ဒီလုပ်ဆောင်ချက်က CPU အချိန်များနိုင်တယ်။
- **Original Audio Volume** — Narration နဲ့ ရောမယ့်အချိန် မူရင်းအသံရဲ့ အခြေခံအသံအတိုးအကျယ်ကို သတ်မှတ်တယ်။
- **External Background Music** — ကိုယ်တိုင်ရွေးထားတဲ့ သီချင်းဖိုင်ဖြစ်ပြီး မူရင်းအသံထိန်းချုပ်မှုနဲ့ သီးခြားဖြစ်တယ်။

### Important limitation / အရေးကြီးသော ကန့်သတ်ချက်

Dialogue and BGM are commonly mixed into one source audio stream. FFmpeg cannot reliably mute only the BGM in that mixed stream. When Source BGM is OFF, Demucs is required; if it is unavailable or separation fails, rendering stops with an install/error message rather than silently muting dialogue.

မူရင်း Dialogue နဲ့ BGM ဟာ Audio Track တစ်ခုတည်းထဲ ရောနေတတ်တယ်။ FFmpeg တစ်ခုတည်းနဲ့ BGM ကိုသာ ယုံကြည်စိတ်ချရအောင် ဖယ်လို့မရပါ။ Source BGM ကို OFF လုပ်ထားရင် Demucs လိုအပ်တယ်။ Demucs မရှိတာ၊ Separation မအောင်မြင်တာမျိုးမှာ Dialogue ကိုပါ မတော်တဆပိတ်မိမယ့်အစား Error ပြပြီး ရပ်မယ်။

## 2. Smart Sync Alignment / Smart Sync အချိန်ညှိမှု

Original audio is processed per timestamp segment using the same Smart Sync speed factor as the corresponding video segment. Each audio part is padded or trimmed to the narration segment duration, then concatenated in timeline order. This avoids simply laying the untouched source track under a video whose segments have been sped up, slowed down, trimmed, or frozen.

မူရင်းအသံကို Video Segment တစ်ခုချင်းစီရဲ့ Timestamp နဲ့ Smart Sync သုံးထားတဲ့ Speed Factor အတိုင်း ပြန်ညှိတယ်။ Narration Segment ကြာချိန်နဲ့ တူအောင် Audio ကို Pad/Trim လုပ်ပြီး အစဉ်လိုက် ပြန်ပေါင်းတယ်။ ဒါကြောင့် Video ကို မြန်/နှေး၊ ဖြတ်တောက်၊ Freeze လုပ်ထားတဲ့အခါ မူရင်းအသံက Timeline နောက်ကျ/ရှေ့ကျတာကို လျှော့ချနိုင်တယ်။

Narration is kept primary. Source audio is mixed underneath and ducked while narration is active. The source audio is not discarded by the visual overlay pass.

Narration ကို အဓိကထားပြီး မူရင်းအသံကို အောက်ခံအဖြစ် ရောမယ်။ Narration ပြောနေချိန်မှာ မူရင်းအသံကို အလိုအလျောက် လျှော့ပေးမယ်။ Visual Overlay လုပ်တဲ့အဆင့်မှာ Source Audio ကို မပယ်ဖျက်ရပါ။

## 3. Subbing vs Dubbing / စာတန်းထိုးနှင့် အသံပြန်သွင်းခြင်း

These are separate workflows and should not be implemented as one overloaded toggle.

ဒီနှစ်ခုကို Toggle တစ်ခုတည်းထဲ မရောဘဲ သီးခြား Workflow အဖြစ်ထားမယ်။

### Subbing Mode / Subtitle-only

- Import existing SRT/VTT; this path does not invoke Whisper.
- Translate subtitle cues while preserving timestamps.
- Review/edit each translated cue, use the shared glossary, and export translated or bilingual SRT.
- Select the source video and render a subtitle-burned MP4.
- Skip TTS generation entirely and retain the source audio content without TTS; MP4 output may re-encode it to AAC for container compatibility.

**မြန်မာလို:** SRT/VTT ဖိုင်ကို Import လုပ်မယ်။ ဒီနည်းလမ်းမှာ Whisper ကို ထပ်မခေါ်ဘူး။ Timestamp မပျက်အောင် ဘာသာပြန်ပြီး စာကြောင်းတစ်ကြောင်းချင်း ပြင်နိုင်မယ်။ Glossary ကို အသုံးပြုနိုင်ပြီး Translated/Bilingual SRT ထုတ်နိုင်မယ်။ Source Video ရွေးပြီး Subtitle Burn-in MP4 ထုတ်နိုင်တယ်။ TTS မခေါ်ဘဲ မူရင်း Audio Content ကို ထိန်းထားမယ်။ MP4 နဲ့ ကိုက်ညီဖို့ AAC အဖြစ် Encode ပြန်လုပ်နိုင်တယ်။

### Narrated Dubbing / Recap narration

- Translate and rewrite the story into narration segments.
- Generate one narrator voice.
- Smart Sync video to narration duration.
- Optionally retain and duck the source dialogue/audio under narration.
- Generate narration subtitles and SRT.

**မြန်မာလို:** ဇာတ်လမ်းကို Narration အဖြစ် ပြန်ရေးပြီး Narrator Voice တစ်မျိုးနဲ့ အသံထုတ်မယ်။ Smart Sync နဲ့ Video အချိန်ညှိမယ်။ လိုအပ်ရင် မူရင်းအသံကို အောက်ခံအဖြစ် ထားမယ်။ Narration Subtitle နဲ့ SRT ထုတ်မယ်။

### Character Voice Dubbing / ဇာတ်ကောင်အလိုက် အသံပြန်သွင်းခြင်း (Manual workflow implemented)

- Import translated SRT/VTT and convert it into timestamped dialogue rows.
- Edit start/end, speaker label, and translated dialogue text in the Dubbing tab.
- Map each speaker label to a stable Edge TTS voice; save/load the dialogue and voice map as a project.
- Render each dialogue line at its cue timestamp and mix the generated voices into the final video.
- Choose to mute source audio, retain the full original mix, or keep the Demucs instrumental stem.
- Automatic speaker diarization and character identity detection are not included; the user reviews and assigns speakers/voices.

**မြန်မာလို:** Translated SRT/VTT ကို Import လုပ်ပြီး Dialogue တစ်ကြောင်းချင်းစီရဲ့ Start/End Timestamp, Speaker Label နဲ့ ဘာသာပြန်စာသားကို ပြင်နိုင်တယ်။ Speaker တစ်ယောက်စီကို Edge TTS Voice တစ်မျိုးစီ ချိတ်ပြီး Project အဖြစ် Save/Load လုပ်နိုင်တယ်။ Cue အချိန်အတိုင်း အသံထုတ်ပြီး Video နဲ့ ပြန်ပေါင်းတယ်။ မူရင်းအသံကို Mute လုပ်မလား၊ Dialogue+BGM အပြည့်ထားမလား၊ Demucs နဲ့ Instrumental BGM ပဲထားမလား ရွေးနိုင်တယ်။ Automatic Diarization မပါသေးလို့ Speaker နဲ့ Voice ကို User ကိုယ်တိုင် စစ်ပြီး သတ်မှတ်ရမယ်။

## 4. Cross-tool Integration / Tool အချင်းချင်း ချိတ်ဆက်မှု

Subbing and Dubbing modes should share project metadata, media probing, subtitle editor, glossary, pronunciation dictionary, waveform/preview, queue, checkpoint/resume, output validation, and export settings. They should keep their own processing pipelines so subtitle-only jobs never call TTS and character dubbing never gets flattened into a single narrator.

Subbing နဲ့ Dubbing နှစ်ခုလုံးက Project Save/Load, Media Probe, Subtitle Editor, Glossary, Pronunciation Dictionary, Waveform/Preview, Queue, Checkpoint/Resume, Output Validation နဲ့ Export Setting တွေကို မျှဝေသုံးမယ်။ ဒါပေမဲ့ Processing Pipeline ကို သီးခြားထားမယ်။ Subtitle-only Job က TTS မခေါ်ရဘူး။ Character Dubbing က Narrator တစ်ယောက်တည်းအဖြစ် မပြောင်းသွားရဘူး။

## 5. Reference repository feature selection / ကိုးကား Repo များမှ ယူမည့်အချက်များ

| Reference | Useful design to adopt | Caution |
|---|---|---|
| recap_studio_mm | Recap vs Dialogue Dubbing separation, source-audio ducking, subtitle timing | Do not assume full automatic character diarization exists |
| recap-studio-streamlit | Script approval, key rotation/fallback, progress persistence | Shares an engine lineage with the first repo; avoid duplicate engines |
| mmnext-movie-recap-pro | Separate narrator and exact-dialogue row models, speaker-to-voice mapping | No license file was identified during review; use architecture ideas, do not copy source code |
| recap-en-to-mm | Existing Windows desktop pipeline, Smart Sync, queue, subtitle/project tools, thumbnails | Preserve current features and backwards-compatible project settings |

## 6. Verification checklist / စမ်းသပ်ရန်

- [ ] Original Audio ON + Source BGM ON: dialogue and source BGM both audible.
- [ ] Original Audio OFF: source audio fully muted; narration still audible.
- [ ] Original Audio ON + Source BGM OFF: Demucs vocals/dialogue retained without source BGM.
- [ ] Missing source audio stream: render continues and reports that source audio is absent.
- [ ] Smart Sync fast/slow/freeze segments: source audio follows segment timing without cumulative drift.
- [ ] Narration active: source audio ducks but is not accidentally removed.
- [ ] External BGM remains independently controllable.
- [ ] Project Save/Load restores all audio controls.
- [x] Imported-subtitle Subbing render skips TTS and retains the source audio content (AAC re-encode for MP4 compatibility).
- [ ] Character Voice Dubbing UI, speaker rows, per-speaker voice mapping, TTS generation and final audio mix are implemented and tested.
- [ ] Output QC confirms expected audio/video streams and duration.
