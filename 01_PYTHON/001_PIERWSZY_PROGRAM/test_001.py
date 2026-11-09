"""Testy pierwszego programu."""

import subprocess
import sys
import unittest
from pathlib import Path


class FirstProgramTests(unittest.TestCase):
    def test_program_prints_expected_messages(self):
        lesson_path = Path(__file__).with_name("lekcja_001.py")
        result = subprocess.run(
            [sys.executable, str(lesson_path)],
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual(
            result.stdout.splitlines(),
            [
                "Witaj, META-GENIUSZ!",
                "Rozpoczynam naukę informatyki.",
                "Moim celem jest stworzenie META-GENIUSZ CITY.",
            ],
        )
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
