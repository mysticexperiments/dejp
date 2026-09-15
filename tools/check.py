#!/usr/bin/env python3
"""Tier 1: deterministisches Zaehlen. Zaehlt nur, urteilt nicht ueber Bedeutung.
Aufruf:  python3 check.py lessons/lektion-04.txt
Ausgabe: JSON auf stdout. Exit 0 = bestanden, 1 = HARTE Fehler."""
import sys, re, json, collections

HARD, SOFT = [], []
path = sys.argv[1]
raw = open(path, encoding="utf-8").read().strip()
L = [l for l in raw.split("\n") if l.strip()]

# --- Form ---
bad = [i+1 for i, l in enumerate(L) if not re.match(r"^(Aoki|Jonas):", l)]
if bad: HARD.append(f"Zeilen ohne Sprecher-Praefix: {bad}")
if len(L) != 22: HARD.append(f"{len(L)} Zeilen statt 22")

# Sprecherwechsel, letzte Zeile ausgenommen
dbl = [i+1 for i in range(1, len(L)) if L[i].split(":")[0] == L[i-1].split(":")[0] and i+1 != len(L)]
if dbl: HARD.append(f"Zwei gleiche Sprecher hintereinander in Zeile {dbl}")

if not L or not L[-1].startswith("Aoki: Deine Hausaufgabe ist"):
    HARD.append("Letzte Zeile ist keine Hausaufgabe im vorgegebenen Format")

# --- Tags ---
tags = re.findall(r"\{([^}]*)\}", raw)
fld = [t for t in tags if len(t.split("|")) not in (4, 5)]
if fld: HARD.append(f"Tags mit falscher Feldzahl: {fld}")

leer = [t for t in tags if any(f.strip() == "" for f in t.split("|")[:4])]
if leer: HARD.append(f"Tags mit leerem Pflichtfeld: {leer}")

cnt = collections.Counter(t.split("|")[0] for t in tags)
ziel = sys.argv[2] if len(sys.argv) > 2 else None
for form, n in cnt.items():
    if form == ziel: continue
    if n > 3: HARD.append(f"Tag '{form}' kommt {n}x vor, erlaubt sind 3")
if ziel:
    z = cnt.get(ziel, 0)
    if not 3 <= z <= 5: HARD.append(f"Ziel '{ziel}' kommt {z}x vor, noetig sind 3 bis 5")

# Japanisch ausserhalb der Klammern
outside = re.sub(r"\{[^}]*\}", "", raw)
jp = sorted(set(re.findall(r"[぀-ヿ一-鿿]", outside)))
if jp: HARD.append(f"Japanische Zeichen ausserhalb der Tags: {jp}")

# Uneinheitliche Uebersetzung
tr = collections.defaultdict(set)
for t in tags:
    f = t.split("|")
    if len(f) >= 4: tr[f[0]].add(f[3].strip())
inc = {k: sorted(v) for k, v in tr.items() if len(v) > 1}
if inc: HARD.append(f"Uneinheitliche Uebersetzung: {inc}")

# Ein Tag darf nicht direkt neben einem anderen stehen
if re.search(r"\}\s*\{", raw): HARD.append("Zwei Tags stehen direkt nebeneinander")


# Mindestzahl Tags
if len(tags) < 10: HARD.append(f"nur {len(tags)} Tags, noetig sind mindestens 10")

# Feld 5 muss die VOLLE gesprochene Form sein, nicht nur ein Zeichen
KANA = re.compile(r"^[぀-ゟ゠-ヿー]+$")
for t in tags:
    f = t.split("|")
    if len(f) < 5 or not f[4].strip(): continue
    kana, speak = f[1].strip(), f[4].strip()
    if not KANA.match(speak):
        HARD.append(f"Feld 5 ist kein reines Kana: {f[0]} -> {speak}")
    elif abs(len(speak) - len(kana)) > 1:
        HARD.append(f"Feld 5 passt nicht zu Feld 2 ({len(speak)} vs {len(kana)} Zeichen): {f[0]} -> {speak}")

# Romaji im Fliesstext
ROMAJI = re.compile(r"\b(watashi|gakusei|desu|sensei|nihonjin|doitsujin|yonasu)\b", re.I)
for i, l in enumerate(L):
    ohne = re.sub(r"\{[^}]*\}", "", l)
    hits = [h for h in ROMAJI.findall(ohne) if h.lower() not in ("wa", "ha")]
    if hits: HARD.append(f"Zeile {i+1}: Romaji im Fliesstext {sorted(set(hits))} -> deutsche Stimme spricht das falsch")

# --- Soft ---
ad = raw.count("Auf Deutsch:")
if ad > 5: SOFT.append(f"'Auf Deutsch:' {ad}x, erlaubt sind 5")

# "Auf Deutsch:" direkt nach einem Partikel-Tag (Feld 4 enthaelt 'partikel')
for m in re.finditer(r"\{([^}]*)\}\.?\s*Auf Deutsch:", raw):
    f = m.group(1).split("|")
    if len(f) >= 4 and "partikel" in f[3].lower():
        SOFT.append(f"Partikel-Tag mit 'Auf Deutsch:': {f[0]}")

# Wortgleich wiederholte japanische Saetze
sent = [t.split("|")[0] for t in tags if len(t.split("|")[0]) > 3]
for s, n in collections.Counter(sent).items():
    if n > 1: SOFT.append(f"Japanischer Satz '{s}' steht {n}x wortgleich drin")

# Ueberstrenge Formulierungen
for i, l in enumerate(L):
    if re.search(r"\b(nie|niemals|immer|geht nicht|darf man nicht)\b", l, re.I):
        SOFT.append(f"Zeile {i+1}: moeglicherweise ueberstrenge Regel -> {l[:80]}")

# Fehlende Kommas vor haeufigen Nebensatz-Einleitungen
for i, l in enumerate(L):
    if re.search(r"[a-zäöüß]\s+(dass|weil|obwohl|wenn)\b", l) and not re.search(r",\s*(dass|weil|obwohl|wenn)\b", l):
        SOFT.append(f"Zeile {i+1}: Komma vor Nebensatz fehlt")


# --- Optional: portugiesische Fassung gegenpruefen ---
PT_HARD = []
pt_path = None
for a in sys.argv[2:]:
    if a.startswith("--pt="): pt_path = a[5:]
if pt_path:
    praw = open(pt_path, encoding="utf-8").read().strip()
    PL = [l for l in praw.split("\n") if l.strip()]
    if len(PL) != len(L):
        PT_HARD.append(f"pt hat {len(PL)} Zeilen, de hat {len(L)}")
    for i, (d, p) in enumerate(zip(L, PL), start=1):
        if d.split(":")[0] != p.split(":")[0]:
            PT_HARD.append(f"Zeile {i}: Sprecher verschieden ({d.split(':')[0]} vs {p.split(':')[0]})")
        dt = re.findall(r"\{([^}]*)\}", d)
        pt = re.findall(r"\{([^}]*)\}", p)
        if len(dt) != len(pt):
            PT_HARD.append(f"Zeile {i}: {len(dt)} Tags in de, {len(pt)} in pt")
            continue
        for a, b in zip(dt, pt):
            fa, fb = a.split("|"), b.split("|")
            for k, name in ((0, "Japanisch"), (1, "Kana"), (2, "Romaji")):
                if fa[k].strip() != fb[k].strip():
                    PT_HARD.append(f"Zeile {i}: Feld {k+1} ({name}) weicht ab: '{fa[k]}' vs '{fb[k]}'")
            if (len(fa) > 4) != (len(fb) > 4):
                PT_HARD.append(f"Zeile {i}: Feld 5 fehlt auf einer Seite: {fa[0]}")
            elif len(fa) > 4 and fa[4].strip() != fb[4].strip():
                PT_HARD.append(f"Zeile {i}: Feld 5 weicht ab: '{fa[4]}' vs '{fb[4]}'")
            # Eigennamen werden nicht uebersetzt: Feld 4 gleich Feld 3 heisst Name
            ist_name = fa[3].strip() == fa[2].strip()
            if not ist_name and len(fb) > 3 and fa[3].strip() == fb[3].strip() and len(fa[3].strip()) > 3:
                PT_HARD.append(f"Zeile {i}: Feld 4 wurde nicht uebersetzt: '{fa[3]}'")
    # Romaji im portugiesischen Fliesstext
    PTR = re.compile(r"\b(watashi|gakusei|desu|sensei|nihonjin|doitsujin|yonasu)\b", re.I)
    for i, p in enumerate(PL, start=1):
        ohne = re.sub(r"\{[^}]*\}", "", p)
        hits = PTR.findall(ohne)
        if hits: PT_HARD.append(f"pt Zeile {i}: Romaji im Fliesstext {sorted(set(hits))} -> pt-BR spricht das falsch")
    HARD.extend(PT_HARD)

res = {"datei": path, "zeilen": len(L), "tags": len(tags),
       "tag_haeufigkeit": dict(cnt.most_common()), "hart": HARD, "weich": SOFT,
       "pt_geprueft": bool(pt_path), "bestanden": not HARD}
print(json.dumps(res, ensure_ascii=False, indent=2))
sys.exit(0 if not HARD else 1)
