from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from studio.compute import run_demucs


class ComputeFallbackTests(unittest.TestCase):
    def test_demucs_uses_cuda_first_and_retries_cpu_after_gpu_failure(self):
        failed = Mock(returncode=1, stdout="", stderr="CUDA out of memory")
        passed = Mock(returncode=0, stdout="", stderr="")
        with patch("studio.compute.cuda_available", return_value=True), patch(
            "studio.compute.subprocess.run", side_effect=[failed, passed]
        ) as run:
            messages = []
            result = run_demucs([sys.executable, "-m", "demucs", "-n", "htdemucs", "source.mp4"], messages.append)
        self.assertIs(result, passed)
        self.assertEqual(run.call_count, 2)
        self.assertEqual(run.call_args_list[0].args[0][run.call_args_list[0].args[0].index("-d") + 1], "cuda")
        self.assertEqual(run.call_args_list[1].args[0][run.call_args_list[1].args[0].index("-d") + 1], "cpu")
        self.assertTrue(any("retrying on CPU" in message for message in messages))

    def test_demucs_uses_cpu_when_cuda_is_unavailable(self):
        passed = Mock(returncode=0, stdout="", stderr="")
        with patch("studio.compute.cuda_available", return_value=False), patch(
            "studio.compute.subprocess.run", return_value=passed
        ) as run:
            run_demucs([sys.executable, "-m", "demucs", "source.mp4"])
        self.assertEqual(run.call_count, 1)
        self.assertEqual(run.call_args.args[0][run.call_args.args[0].index("-d") + 1], "cpu")


if __name__ == "__main__":
    unittest.main()
