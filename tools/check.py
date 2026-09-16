#!/usr/bin/env python3
"""Structural checks, not linguistic certification.

python3 -B tools/check.py --all
python3 -B tools/check.py DE_FILE --pt PT_FILE [--particle は]
"""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
TAG = re.compile(r"\{([^{}\n]*)\}")
JAPANESE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uff66-\uff9f]")
KANA = re.compile(r"[ぁ-ゖゝゞァ-ヺー・ 　]+")
ROMAJI = re.compile(
    r"\b(watashi|gakusei|desu|sensei|nihonjin|doitsujin|nomimasu|nomimasen|"
    r"hatarakimasu|tabemasu|koohii|ocha|mizu|anata|masu|masen|wa|ha)\b", re.I
)


def inspect_text(raw, language, minimum_lines=80):
    """Keep blank lines so structural errors cannot disappear through filtering."""
    lines = raw.splitlines()
    hard, soft, parsed, all_tags = [], [], [], []
    meanings = defaultdict(set)
    if len(lines) < minimum_lines:
        hard.append(f"{language}: {len(lines)} Zeilen; mindestens {minimum_lines} erforderlich")
    for number, line in enumerate(lines, 1):
        label = f"{language} Zeile {number}"
        expected = "Jonas" if number % 2 else "Aoki"
        if not line.startswith(expected + ": ") or not line[len(expected) + 2:].strip():
            hard.append(f"{label}: erwartet {expected}: mit nichtleerem Text")
        matches = list(TAG.finditer(line))
        outside = TAG.sub("", line)
        if any(char in outside for char in "{}|"):
            hard.append(f"{label}: ungültige, verschachtelte oder freie Tagdelimiter")
        if JAPANESE.search(outside):
            hard.append(f"{label}: Japanisch außerhalb der Tags")
        bare = sorted(set(ROMAJI.findall(outside)))
        if bare:
            soft.append(f"{label}: mögliches Romaji in Prosa: {bare}; manuell prüfen")
        for first, second in zip(matches, matches[1:]):
            if not re.search(r"[^\W\d_]", line[first.end():second.start()], re.UNICODE):
                hard.append(f"{label}: zwischen Tags fehlt erklärende Prosa")
        fields_in_line = []
        for match in matches:
            fields = match.group(1).split("|")
            fields_in_line.append(fields)
            if len(fields) < 4:
                hard.append(f"{label}: Tag braucht mindestens vier Felder")
                continue
            if any(not field.strip() for field in fields[:4]):
                hard.append(f"{label}: leeres Pflichtfeld")
            if not KANA.fullmatch(fields[1]):
                hard.append(f"{label}: Feld 2 ist keine Kana-Lesung")
            if JAPANESE.search(fields[2]):
                hard.append(f"{label}: japanische Zeichen im Romaji-Feld")
            if len(fields) >= 5:
                if not fields[4].strip() or not KANA.fullmatch(fields[4]):
                    hard.append(f"{label}: Feld 5 muss eine nichtleere Kana-Aussprache sein")
                elif abs(len(fields[4]) - len(fields[1])) > 1:
                    soft.append(f"{label}: Länge von Aussprache und Lesung weicht ab; ganze Einheit prüfen")
            all_tags.append(fields)
            meanings[fields[0]].add(fields[3])
        parsed.append(fields_in_line)
    if not lines or not lines[-1].startswith("Aoki: "):
        hard.append(f"{language}: Aoki muss den Text abschließen")
    if len(all_tags) < 10:
        hard.append(f"{language}: {len(all_tags)} gültige Tags; mindestens zehn erforderlich")
    for written, values in meanings.items():
        if len(values) > 1:
            soft.append(f"{language}: mehrere Bedeutungen für {written}: {sorted(values)}; Kontext prüfen")
    return lines, parsed, all_tags, hard, soft


def check_texts(german, portuguese=None, particles=(), minimum_lines=80):
    lines, parsed, tags, hard, soft = inspect_text(german, "de", minimum_lines)
    for particle in particles:
        if not any(fields[0] == particle for fields in tags):
            hard.append(f"de: isoliertes Partikel-Tag fehlt: {particle}")
        if not any(particle in fields[0] and len(fields[0]) > len(particle) + 1 for fields in tags):
            hard.append(f"de: Partikel fehlt in längerer Einheit: {particle}")
    if portuguese is not None:
        pt_lines, pt_parsed, _, pt_hard, pt_soft = inspect_text(portuguese, "pt", minimum_lines)
        hard.extend(pt_hard)
        soft.extend(pt_soft)
        if len(lines) != len(pt_lines):
            hard.append(f"Paarung: de hat {len(lines)}, pt hat {len(pt_lines)} Zeilen")
        for number, (de_line, pt_line, de_tags, pt_tags) in enumerate(
                zip(lines, pt_lines, parsed, pt_parsed), 1):
            if de_line.split(":", 1)[0] != pt_line.split(":", 1)[0]:
                hard.append(f"Paarung Zeile {number}: Sprecher verschieden")
            if len(de_tags) != len(pt_tags):
                hard.append(f"Paarung Zeile {number}: Tagzahl verschieden")
            for de_fields, pt_fields in zip(de_tags, pt_tags):
                # No strip(): pairing is exact, not whitespace-normalized.
                if de_fields[:3] + de_fields[4:] != pt_fields[:3] + pt_fields[4:]:
                    hard.append(f"Paarung Zeile {number}: Tagfelder außer Bedeutung nicht identisch")
                if len(de_fields) >= 4 and len(pt_fields) >= 4:
                    if de_fields[3] == pt_fields[3] and de_fields[3] != de_fields[2]:
                        soft.append(f"Paarung Zeile {number}: gleiche Bedeutung; Eigenname oder fehlende Übersetzung prüfen")
    return {
        "zeilen": len(lines), "tags": len(tags),
        "tag_haeufigkeit": dict(Counter(fields[0] for fields in tags)),
        "hart": hard, "weich": soft, "pt_geprueft": portuguese is not None,
        "bestanden": not hard,
    }


def check_files(de_path, pt_path=None, particles=()):
    try:
        report = check_texts(
            de_path.read_text(encoding="utf-8"),
            pt_path.read_text(encoding="utf-8") if pt_path else None,
            particles,
        )
    except (OSError, UnicodeError) as error:
        report = {"hart": [str(error)], "weich": [], "bestanden": False}
    return {"datei": str(de_path), **report}


def check_manifest(path, root=ROOT):
    hard, reports = [], []
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict) or manifest.get("formatVersion") != 1:
            raise ValueError("Manifest braucht formatVersion 1")
        if manifest.get("language") != {"main": "de", "support": "pt", "target": "ja"}:
            raise ValueError("Sprachzuordnung muss de / pt / ja sein")
        entries = manifest.get("lessons")
        if not isinstance(entries, list) or not entries:
            raise ValueError("Manifest braucht eine nichtleere Lektionsliste")
        ids, paths = set(), set()
        for expected, entry in enumerate(entries, 1):
            if not isinstance(entry, dict):
                raise ValueError("Lektion muss ein Objekt sein")
            for key in ("id", "grammar", "title", "titlePt", "de", "pt"):
                if not isinstance(entry.get(key), str) or not entry[key].strip():
                    raise ValueError(f"Lektion {expected}: Feld {key} fehlt")
            if entry["id"] in ids or entry.get("number") != expected:
                raise ValueError("IDs müssen eindeutig und Nummern fortlaufend sein")
            ids.add(entry["id"])
            resolved = []
            for key in ("de", "pt"):
                relative = Path(entry[key])
                target = (root / relative).resolve()
                if relative.is_absolute() or root.resolve() not in target.parents:
                    raise ValueError("Lektionspfad liegt außerhalb des Repositorys")
                if target in paths:
                    raise ValueError("Lektionspfade müssen eindeutig sein")
                paths.add(target)
                resolved.append(target)
            particles = entry.get("particles", [])
            if not isinstance(particles, list) or not all(isinstance(p, str) and p for p in particles):
                raise ValueError("particles muss eine Liste nichtleerer Zeichenfolgen sein")
            reports.append(check_files(*resolved, particles))
    except (OSError, UnicodeError, ValueError) as error:
        hard.append(str(error))
    return {"manifest": str(path), "lektionen": reports, "hart": hard,
            "bestanden": not hard and bool(reports) and all(r["bestanden"] for r in reports)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("de", nargs="?", type=Path)
    parser.add_argument("--pt", type=Path)
    parser.add_argument("--particle", action="append", default=[])
    parser.add_argument("--all", action="store_true", help="alle Manifest-Einträge prüfen")
    args = parser.parse_args()
    if args.all:
        if args.de or args.pt or args.particle:
            parser.error("--all nicht mit Einzeldateien kombinieren")
        report = check_manifest(ROOT / "lektionen/index.json")
    else:
        if not args.de:
            parser.error("DE-Datei oder --all erforderlich")
        report = check_files(args.de, args.pt, args.particle)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["bestanden"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
