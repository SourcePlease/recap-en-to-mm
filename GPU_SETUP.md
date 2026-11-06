# GPU Setup — GPU Acceleration / CPU Fallback

ဤလမ်းညွှန်သည် Windows 10/11, Python 3.12 (64-bit) အတွက် ဖြစ်ပါတယ်။ NVIDIA GPU မရှိလည်း App ကို CPU နဲ့ ဆက်သုံးနိုင်ပါတယ်။

## 1. ဘယ်အလုပ်တွေ GPU သုံးနိုင်သလဲ

| Feature | GPU အသုံးပြုပုံ | GPU မရလျှင် |
|---|---|---|
| Whisper transcription | NVIDIA CUDA + faster-whisper (float16) | CPU / int8 |
| Demucs source separation | PyTorch CUDA | CPU |
| Video encoding | FFmpeg h264_nvenc | FFmpeg libx264 |
| AI translation / hosted TTS | Cloud provider ရဲ့ server | Local GPU မသုံးပါ |
| Subtitle editor / UI / အများစုသော FFmpeg filter | CPU | CPU ပဲသုံးပါတယ် |

**English:** GPU acceleration is available for local Whisper, Demucs and NVIDIA NVENC encoding. Hosted AI/TTS services run remotely. UI, subtitle editing and most FFmpeg filters remain CPU tasks.

## 2. NVIDIA GPU Driver စစ်ရန်

Command Prompt မှာ run ပါ။

~~~bat
nvidia-smi
~~~

GPU name, driver version နဲ့ VRAM ပေါ်လာရပါမယ်။ Command မတွေ့ရင် NVIDIA driver ကို update/install လုပ်ပါ။ AMD/Intel GPU တွေကို ဒီ CUDA/NVENC path က မသုံးနိုင်ပါ။

## 3. Whisper CUDA လိုအပ်ချက်

လက်ရှိ faster-whisper / CTranslate2 GPU path အတွက် CUDA 12 အတွက် cuBLAS နဲ့ cuDNN 9 လိုအပ်ပါတယ်။ NVIDIA Driver တစ်ခုတည်း install လုပ်ထားရုံနဲ့ မလုံလောက်နိုင်ပါ။

- Install လုပ်မယ့် CUDA/cuDNN version ကို faster-whisper official README နဲ့ ကိုက်ညီအောင်ရွေးပါ။
- Windows မှာ လိုအပ်တဲ့ NVIDIA DLL folder တွေကို PATH ထဲမှာ မြင်ရအောင်ထားပါ။
- Official reference: https://github.com/SYSTRAN/faster-whisper

## 4. Demucs CUDA လိုအပ်ချက်

Demucs က PyTorch ကို သုံးပါတယ်။ PyTorch official installer မှာ Windows + Pip + Python + သင့် NVIDIA driver နဲ့ကိုက်တဲ့ CUDA version ကိုရွေးပြီး ပြထားတဲ့ command ကို run ပါ။ ပြီးမှ—

~~~bat
python -m pip install -U demucs
~~~

PyTorch GPU ရ/မရ စစ်ရန်—

~~~bat
python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('Torch CUDA:', torch.version.cuda)"
~~~

CUDA available: True ဖြစ်ရပါမယ်။ Demucs htdemucs model က VRAM များစွာလိုနိုင်ပါတယ်။ GPU memory မလုံလောက်ရင် App က CPU ကို ပြန်စမ်းပါတယ်။

Official PyTorch installer: https://pytorch.org/get-started/locally/

## 5. NVENC စစ်ရန်

~~~bat
ffmpeg -hide_banner -encoders | findstr /i nvenc
~~~

h264_nvenc ပေါ်လာရင် FFmpeg build မှာ encoder ပါပါတယ်။ App က long render မစခင် smoke test တစ်ခါလုပ်ပြီး အမှန်တကယ် အလုပ်လုပ်မှ NVENC သုံးပါတယ်။ Driver/device မရရင် libx264 CPU ကို အလိုအလျောက်ရွေးပါတယ်။

## 6. App ထဲက အလိုအလျောက် Fallback

- Whisper CUDA error ဖြစ်ရင် CPU/int8 နဲ့ ပြန်စမ်းတယ်။
- Demucs GPU error / VRAM error ဖြစ်ရင် CPU နဲ့ ပြန်စမ်းတယ်။
- NVENC preflight မအောင်မြင်ရင် libx264 CPU နဲ့ စတယ်။
- CPU fallback ဖြစ်တာက ပိုနှေးနိုင်ပေမယ့် GPU မရလို့ အလုပ်တစ်ခုလုံး ရပ်သွားတာကို လျှော့ချပေးပါတယ်။

**သတိ:** GPU ရှိတာနဲ့ Feature အားလုံး GPU သုံးတာ မဟုတ်ပါ။ Driver, CUDA runtime, cuBLAS/cuDNN, PyTorch build နဲ့ FFmpeg encoder တို့ အဆင်သင့်ဖြစ်မှ သက်ဆိုင်ရာ Feature က GPU သုံးနိုင်ပါတယ်။

**English:** A detected GPU does not mean every feature runs on it. The matching driver, CUDA runtime, cuBLAS/cuDNN, CUDA-enabled PyTorch and an NVENC-capable FFmpeg build must be available. CPU fallback remains enabled for supported local tasks.
