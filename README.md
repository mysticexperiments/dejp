# dejp — Japanisch auf Deutsch, mit portugiesischer Verständnishilfe

Ein fortlaufender Hörkurs für Japanisch-Anfänger. Aoki erklärt auf Deutsch,
Jonas fragt nach und arbeitet vollständige Beispiele durch. Brasilianisches
Portugiesisch vermittelt dieselbe Erklärung.

## Planung und Texte

- [Hauptplan: alle 90 Themen](planung/hauptplan.md)
- [Block 1: vier Klassen und neun Teiltexte](planung/bloecke/block-01.md)
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

Jede Fassung hat 80 Zeilen. Die drei Texte bilden zusammen Klasse 1 des
ersten Blocks. B01-T04 bis B01-T09 sind geplant, noch nicht geschrieben.

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
[Prüfbericht zur ersten Lieferung](planung/pruefung-block-01-texte-01-03.md).

## Veröffentlichung

Die App liest nur die Einträge in `lektionen/index.json`. Die neuen Texte
haben neue IDs, damit alte Lesepositionen und Cacheeinträge nicht unter
denselben IDs als neue Lektionen erscheinen. Das technische Tagformat
bleibt bei `formatVersion: 1`; die längeren Texte benötigen keine Appänderung.

Die alten Dateien sind aus dem aktuellen Kurs entfernt und über die
Git-Historie weiterhin wiederherstellbar. Ein Gerät ohne Netzwerk kann noch
seinen alten Cache anzeigen, bis die App die neue Liste erfolgreich lädt.
