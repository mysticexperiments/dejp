#!/usr/bin/env python3
"""Baut den Rueckblick fuer die naechste Lektion aus allen bisherigen Lektionen.
Aufruf:  python3 recap.py lessons/lektion-01.txt lessons/lektion-02.txt ...
Ausgabe: der fertige RUECKBLICK-Block auf stdout."""
import sys, re

zeilen = ["RUECKBLICK: WAS JONAS SCHON GELERNT HAT"]
letzte_hausaufgabe = None

for n, path in enumerate(sys.argv[1:], start=1):
    raw = open(path, encoding="utf-8").read().strip()
    L = [l for l in raw.split("\n") if l.strip()]
    tags = re.findall(r"\{([^}]*)\}", raw)
    einzel, saetze = [], []
    for t in tags:
        f = t.split("|")
        if len(f) < 4: continue
        romaji, de = f[2].strip(), f[3].strip()
        ziel = (romaji, de)
        if len(f[0]) <= 2:
            if ziel not in einzel: einzel.append(ziel)
        else:
            if romaji not in saetze: saetze.append(romaji)
    teile = ", ".join(f"{r} ({d})" for r, d in einzel[:4]) or "-"
    bsp = saetze[0] if saetze else "-"
    zeilen.append(f"Tag {n}: {teile}. Beispielsatz, den Jonas kann: {bsp}.")
    for l in L:
        if l.startswith("Aoki: Deine Hausaufgabe ist"):
            h = l.split("ist", 1)[1].strip().rstrip(".")
            h = re.sub(r"\bdu\b", "er", h)
            h = re.sub(r"\bdein(e|en|em|er)?\b", lambda m: "sein" + (m.group(1) or ""), h)
            h = re.sub(r"\bdich\b", "sich", h)
            h = re.sub(r"\bdir\b", "sich", h)
            letzte_hausaufgabe = h

if letzte_hausaufgabe:
    zeilen.append(f"Seine letzte Hausaufgabe war{letzte_hausaufgabe}.")
zeilen.append(f"Heute ist Tag {len(sys.argv)}. Die Geschichte geht weiter. Erklaere NICHTS davon noch einmal, aber benutze es.")
zeilen.append("Die Lektion beginnt damit, dass Jonas seine Hausaufgabe mitbringt.")
print("\n".join(zeilen))
