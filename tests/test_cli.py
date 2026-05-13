"""Tests for the command-line adapter."""

import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


class CliTest(unittest.TestCase):
    """Covers command-line ticket classification behavior."""

    def test_cli__incident_text__prints_routing_decision(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "harness_demo.cli",
                "Cannot log in to production",
            ],
            check=False,
            cwd=REPO_ROOT,
            env={"PYTHONPATH": str(REPO_ROOT / "src")},
            capture_output=True,
            text=True,
        )

        self.assertEqual(0, result.returncode)
        self.assertIn("queue=incident", result.stdout)
        self.assertIn("priority=high", result.stdout)


if __name__ == "__main__":
    unittest.main()
