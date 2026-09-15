# dejp — Deutsch lernen, Japanisch nebenbei

Lektionen fuer eine Lern-App: eine japanische Lehrerin (Aoki) unterrichtet
einen deutschen Schueler (Jonas) in JAPANISCH, auf DEUTSCH. Portugiesisch
laeuft als Sicherheitsnetz mit, damit die Bedeutung sicher ankommt, auch
wenn das Deutsche nur zur Haelfte verstanden wird.

## Ordner

    lektionen/de-pt/     lektion-NN.txt      deutsche Fassung
                         lektion-NN.pt.txt   portugiesische Fassung
    prompts/             writer.md, translator.md, reviewer.md
    tools/               check.py  (Tier 1, deterministisch)
                         recap.py  (baut den Rueckblick aus alten Lektionen)

## Format

Jede Zeile: `Aoki: ...` oder `Jonas: ...`.
Japanisches Stueck: `{Kanji|Kana|Romaji|Bedeutung}` oder mit Aussprachefeld
`{Kanji|Kana|Romaji|Bedeutung|was gesprochen wird}`.
Feld 4 ist sprachlokal: in der deutschen Zeile deutsch, in der
portugiesischen Zeile portugiesisch. Felder 1, 2, 3, 5 sind in beiden
Fassungen zeichengenau identisch.

## Pruefen

    python3 tools/check.py lektionen/de-pt/lektion-01.txt は
    python3 tools/check.py lektionen/de-pt/lektion-02.txt か \
      --pt=lektionen/de-pt/lektion-02.pt.txt

## Herkunft

Entwickelt und geprueft in /tmp/jptest (siehe dortiges README.md fuer den
vollen Ablauf: Schreiben, Tier-1-Zaehlung, Tier-2-Pruefung durch ein
Sprachmodell). Lektionen 1 und 2 sind von Hand geschrieben und durch
gpt-5.6-luna als Pruefer gegengelesen.
