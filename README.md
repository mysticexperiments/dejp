# dejp — Deutsch lernen, Japanisch nebenbei

Lektionen fuer eine Lern-App: eine japanische Lehrerin (Aoki) unterrichtet
einen deutschen Schueler (Jonas) in JAPANISCH, auf DEUTSCH. Portugiesisch
laeuft als Sicherheitsnetz mit, damit die Bedeutung sicher ankommt, auch
wenn das Deutsche nur zur Haelfte verstanden wird.

## Ordner

    lektionen/index.json     Manifest. Was hier nicht steht, sieht die App nicht.
    lektionen/vokabular.md   erlaubtes Vokabular, kumulativ je Lektion
    lektionen/de-pt/     lektion-NN.txt      deutsche Fassung
                         lektion-NN.pt.txt   portugiesische Fassung
    prompts/             WORKFLOW.md   der Ablauf, und warum die Regeln so sind
                         writer.md, translator.md, reviewer.md
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

## Neue Lektion schreiben

Lies `prompts/WORKFLOW.md`. Dort steht der ganze Ablauf in sieben Schritten,
und davor, was die App mit dem Text macht: sie liest ihn VOR. Fast jede Regel
in `prompts/writer.md` folgt daraus. Wer das ueberspringt, haelt die Regeln
fuer Geschmack und bricht sie.

## Herkunft

Lektionen 1 bis 5 sind von Hand geschrieben und durch ein zweites Sprachmodell
(gpt-5.6-luna) gegengelesen. Der Ablauf, der dabei entstand, steht jetzt in
`prompts/WORKFLOW.md`.
