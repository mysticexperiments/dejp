# dejp — Japanisch auf Deutsch, mit portugiesischer Verständnishilfe

Ein fortlaufender Hörkurs für Japanisch-Anfänger. Aoki erklärt auf Deutsch,
Jonas fragt nach und arbeitet vollständige Beispiele durch. Brasilianisches
Portugiesisch vermittelt dieselbe Erklärung.

## Planung und Texte

- [Hauptplan: alle 90 Themen](planung/hauptplan.md)
- [Block 1: vier Klassen und neun Teiltexte](planung/bloecke/block-01.md)
- [Block 2: Kopula, vier Klassen und acht geplante Teiltexte](planung/bloecke/block-02.md)
- [Lektionsmanifest](lektionen/index.json)
- [Kumulatives Vokabular](lektionen/vokabular.md)
- [Autorablauf](prompts/WORKFLOW.md)
- [Formatvertrag](FORMAT-AGREEMENT.md)

Die neue Reihe ersetzt die fünf alten Kurzlektionen. Aktuell ausgearbeitet:

| Text | Thema | DE / PT |
|---|---|---|
| B01-T01 | Erst das Thema, dann die Aussage | [Deutsch](lektionen/de-pt/block-01-text-01.txt) / [Português](lektionen/de-pt/block-01-text-01.pt.txt) |
| B01-T02 | Was ich trinke — die Handlung am Ende | [Deutsch](lektionen/de-pt/block-01-text-02.txt) / [Português](lektionen/de-pt/block-01-text-02.pt.txt) |
| B01-T03 | Eine andere Person, derselbe Satzbau | [Deutsch](lektionen/de-pt/block-01-text-03.txt) / [Português](lektionen/de-pt/block-01-text-03.pt.txt) |
| B01-T04 | Thema und Subjekt auseinanderhalten | [Deutsch](lektionen/de-pt/block-01-text-04.txt) / [Português](lektionen/de-pt/block-01-text-04.pt.txt) |
| B01-T05 | Was aus dem Zusammenhang klar ist | [Deutsch](lektionen/de-pt/block-01-text-05.txt) / [Português](lektionen/de-pt/block-01-text-05.pt.txt) |
| B01-T06 | Partikeln als Rollenmarker | [Deutsch](lektionen/de-pt/block-01-text-06.txt) / [Português](lektionen/de-pt/block-01-text-06.pt.txt) |
| B01-T07 | Existenzort und Handlungsort | [Deutsch](lektionen/de-pt/block-01-text-07.txt) / [Português](lektionen/de-pt/block-01-text-07.pt.txt) |
| B01-T08 | Artikel, Genus und Zahl | [Deutsch](lektionen/de-pt/block-01-text-08.txt) / [Português](lektionen/de-pt/block-01-text-08.pt.txt) |
| B01-T09 | Höflicher und schlichter Stil | [Deutsch](lektionen/de-pt/block-01-text-09.txt) / [Português](lektionen/de-pt/block-01-text-09.pt.txt) |
| B02-T01 | Das ist kein Buch | [Deutsch](lektionen/de-pt/block-02-text-01.txt) / [Português](lektionen/de-pt/block-02-text-01.pt.txt) |
| B02-T02 | Kürzer gesprochen, weiterhin höflich | [Deutsch](lektionen/de-pt/block-02-text-02.txt) / [Português](lektionen/de-pt/block-02-text-02.pt.txt) |
| B02-T03 | Ist das ein Buch? | [Deutsch](lektionen/de-pt/block-02-text-03.txt) / [Português](lektionen/de-pt/block-02-text-03.pt.txt) |
| B02-T04 | Kurz antworten, den Bezug behalten | [Deutsch](lektionen/de-pt/block-02-text-04.txt) / [Português](lektionen/de-pt/block-02-text-04.pt.txt) |
| B02-T05 | Was damals zutraf | [Deutsch](lektionen/de-pt/block-02-text-05.txt) / [Português](lektionen/de-pt/block-02-text-05.pt.txt) |
| B02-T06 | Was damals nicht zutraf | [Deutsch](lektionen/de-pt/block-02-text-06.txt) / [Português](lektionen/de-pt/block-02-text-06.pt.txt) |

Block 1 ist vollständig ausgearbeitet: neun Texte in vier Klassen mit
80–88 Dialogzeilen je Sprache nach der redaktionellen Überarbeitung.
Von Block 2 sind die ersten sechs der acht geplanten Texte geschrieben:
82, 82, 80, 86, 84 und 90 Zeilen je Sprache, zusammen 504 je Sprache.
Sie bauen Verneinung, Fragen, passende Antworten und die bejahte sowie
verneinte nominale Vergangenheit auf. Texte 7–8 sind
weiterhin geplant, nicht geschrieben oder im Manifest registriert.

## Hören und Dateiformat

Eine Zeile ist ein Sprecherbeitrag, beginnend mit `Jonas:` oder `Aoki:`.
Japanisch steht in `{Schreibung|Kana|Romaji|Bedeutung|Aussprache}`; das fünfte
Feld ist optional. Nur die Bedeutung wird in PT übersetzt.

Die App spielt **pro Zeile** Deutsch → Portugiesisch → Deutsch. Japanische
Tags werden standardmäßig dreimal je Durchgang gesprochen, also neunmal pro
Tagvorkommen über die drei Durchgänge. Diese Wiederholung ist beabsichtigt.

Mindestens 80 Zeilen pro Text und Sprache; keine Obergrenze von 22 Zeilen,
keine künstliche Höchstzahl wiederholter Beispielsätze. Es gibt keine
verpflichtende Hausaufgabe oder Eingabe. Ein Text endet mit einem inhaltlichen
Anschluss. Die deutsche Wiederholung wird nicht nochmals als Datei gespeichert.

## Prüfen

Python 3, nur Standardbibliothek:

```sh
python3 -B tools/check.py --all
python3 -B tools/check.py lektionen/de-pt/block-01-text-01.txt \
  --pt=lektionen/de-pt/block-01-text-01.pt.txt
python3 -B -m unittest discover -s tests
```

Die Prüfung kontrolliert Format, Länge, Tagstruktur und Parallelität.
Sie beweist weder sprachliche Richtigkeit noch Lernerfolg.
[Prüfbericht zur ersten Lieferung](planung/pruefung-block-01-texte-01-03.md)
und [Prüfbericht zur Vervollständigung](planung/pruefung-block-01-texte-04-09.md).
Für den neuen Abschnitt: [Prüfbericht Block 2, Texte 1–4](planung/pruefung-block-02-texte-01-04.md).
Die Fortsetzung dokumentiert der [Prüfbericht Block 2, Texte 5–6](planung/pruefung-block-02-texte-05-06.md).
Struktur und erzeugte Sprachsegmente sind geprüft; eine reale Hörprobe auf
dem Zielgerät und eine unabhängige sprachliche Abnahme stehen noch aus.

## Veröffentlichung

Die App liest nur die Einträge in `lektionen/index.json`. Die neuen Texte
haben neue IDs, damit alte Lesepositionen und Cacheeinträge nicht unter
denselben IDs als neue Lektionen erscheinen. Das technische Tagformat
bleibt bei `formatVersion: 1`; die längeren Texte benötigen keine Appänderung.

Die alten Dateien sind aus dem aktuellen Kurs entfernt und über die
Git-Historie weiterhin wiederherstellbar. Ein Gerät ohne Netzwerk kann noch
seinen alten Cache anzeigen, bis die App die neue Liste erfolgreich lädt.
