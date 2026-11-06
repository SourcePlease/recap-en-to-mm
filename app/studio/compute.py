"""GPU-first local compute helpers with safe CPU fallbacks."""
from __future__ import annotations

import subprocess
from typing import Callable, Sequence


def cuda_available() -> bool:
    """Check the installed PyTorch CUDA runtime without making it a hard dependency."""
    try:
        import torch
        return bool(torch.cuda.is_available())
    except Exception:
        return False


def run_demucs(command: Sequence[str], log: Callable[[str], None] | None = None) -> subprocess.CompletedProcess:
    """Run Demucs on CUDA when usable; retry on CPU if the GPU attempt fails."""
    emit = log or (lambda _message: None)
    devices = ["cuda", "cpu"] if cuda_available() else ["cpu"]
    last = None
    for device in devices:
        args = list(command)
        try:
            marker = args.index("demucs")
            args[marker + 1:marker + 1] = ["-d", device]
        except ValueError:
            args.extend(["-d", device])
        emit("⚡ Demucs device: NVIDIA/CUDA GPU" if device == "cuda" else "🖥️ Demucs device: CPU")
        result = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode == 0:
            return result
        last = result
        if device == "cuda":
            detail = (result.stderr or result.stdout or "").lower()
            emit("⚠️ Demucs GPU failed; retrying on CPU (slower).")
            continue
        break
    detail = ((last.stderr or last.stdout or "Demucs failed.") if last else "Demucs could not start.")
    raise RuntimeError("Demucs failed on available compute devices:\n" + detail[-3000:])
