"""Regression checks for malformed content and the longer bilingual format."""
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from tools.check import ROOT, check_manifest, check_texts


DE_TAG = "{私は学生です|わたしはがくせいです|watashi wa gakusei desu|Ich bin Student|わたしわがくせいです}"
PT_TAG = "{私は学生です|わたしはがくせいです|watashi wa gakusei desu|Eu sou estudante|わたしわがくせいです}"


def fixture(tag, length=80):
    return "\n".join(f"{'Jonas' if i % 2 == 0 else 'Aoki'}: {tag}. Erklärung." for i in range(length)) + "\n"


class CheckTests(unittest.TestCase):
    def test_long_text_and_repetition_are_allowed(self):
        for length in (80, 82, 120):
            with self.subTest(length=length):
                self.assertTrue(check_texts(fixture(DE_TAG, length), fixture(PT_TAG, length))["bestanden"])

    def test_old_short_format_fails(self):
        self.assertFalse(check_texts(fixture(DE_TAG, 22))["bestanden"])

    def test_blank_lines_not_discarded(self):
        text = fixture(DE_TAG).replace("Jonas: ", "\nJonas: ", 1)
        self.assertFalse(check_texts(text)["bestanden"])

    def test_malformed_delimiters_and_short_tags_do_not_crash(self):
        for bad in ("{私}", "{私|わたし}", "{私|わたし|watashi|ich", "{x" + DE_TAG + "}",
                    DE_TAG + " | prose", "{私|\nわたし|watashi|ich}"):
            with self.subTest(bad=bad):
                result = check_texts(fixture(DE_TAG), fixture(PT_TAG).replace(PT_TAG, bad, 1))
                self.assertFalse(result["bestanden"])

    def test_empty_pronunciation_rejected(self):
        self.assertFalse(check_texts(fixture("{私|わたし|watashi|ich|}"))["bestanden"])

    def test_pairing_requires_exact_fields(self):
        for bad in (PT_TAG.replace("watashi wa", "watashi  wa"), PT_TAG.replace("わたしわ", "わたしは")):
            with self.subTest(bad=bad):
                self.assertFalse(check_texts(fixture(DE_TAG), fixture(bad))["bestanden"])

    def test_unknown_appended_fields_are_supported_and_paired(self):
        de = fixture(DE_TAG[:-1] + "|future}")
        pt = fixture(PT_TAG[:-1] + "|future}")
        self.assertTrue(check_texts(de, pt)["bestanden"])
        self.assertFalse(check_texts(de, pt.replace("future", "different"))["bestanden"])

    def test_japanese_outside_tags_in_portuguese_rejected(self):
        self.assertFalse(check_texts(fixture(DE_TAG), fixture(PT_TAG).replace("Erklärung", "私", 1))["bestanden"])

    def test_punctuation_does_not_count_as_explanation_between_tags(self):
        bad = fixture(DE_TAG).replace(DE_TAG, DE_TAG + ", " + DE_TAG, 1)
        self.assertFalse(check_texts(bad)["bestanden"])

    def test_particle_needs_standalone_and_larger_example(self):
        particle = "{は|は|wa|Themenpartikel|わ}"
        self.assertFalse(check_texts(fixture(particle), particles=["は"])["bestanden"])
        self.assertFalse(check_texts(fixture(DE_TAG), particles=["は"])["bestanden"])
        good = fixture(DE_TAG).replace(DE_TAG, particle + " markiert das Thema in " + DE_TAG, 1)
        self.assertTrue(check_texts(good, particles=["は"])["bestanden"])

    def test_manifest_rejects_incompatible_format_and_escaping_path(self):
        manifest = json.loads((ROOT / "lektionen/index.json").read_text(encoding="utf-8"))
        manifest["formatVersion"] = 2
        with patch.object(Path, "read_text", return_value=json.dumps(manifest)):
            self.assertFalse(check_manifest(ROOT / "lektionen/index.json")["bestanden"])
        manifest["formatVersion"] = 1
        manifest["lessons"][0]["de"] = "../outside.txt"
        with patch.object(Path, "read_text", return_value=json.dumps(manifest)):
            self.assertFalse(check_manifest(ROOT / "lektionen/index.json")["bestanden"])

    def test_pt_option_needs_no_positional_target(self):
        process = subprocess.run([
            sys.executable, "-B", str(ROOT / "tools/check.py"),
            str(ROOT / "lektionen/de-pt/block-01-text-01.txt"),
            "--pt", str(ROOT / "lektionen/de-pt/block-01-text-01.pt.txt"),
        ], capture_output=True, text=True, check=False)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertTrue(json.loads(process.stdout)["pt_geprueft"])


if __name__ == "__main__":
    unittest.main()
