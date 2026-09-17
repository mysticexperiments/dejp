# Lieferung und Prüfung — Block 2, Texte 5 und 6

Stand: 2026-09-17. Fortsetzung der [Texte 1–4](pruefung-block-02-texte-01-04.md)
nach dem [Blockplan](bloecke/block-02.md). Zwei eigene deutsche Dialoge mit
zeilengleichen brasilianisch-portugiesischen Fassungen.

## Lieferumfang

| Text | Neues Hauptziel | Zeilen je Sprache | Tags je Fassung | Tags bei Jonas |
|---|---|---:|---:|---:|
| [B02-T05](../lektionen/de-pt/block-02-text-05.txt) / [PT](../lektionen/de-pt/block-02-text-05.pt.txt) | Bejahte nominale Vergangenheit mit でした | 84 | 27 | 6 |
| [B02-T06](../lektionen/de-pt/block-02-text-06.txt) / [PT](../lektionen/de-pt/block-02-text-06.pt.txt) | Verneinte nominale Vergangenheit mit beiden höflichen Varianten | 90 | 34 | 6 |

Zusammen 174 neue Zeilen je Sprache, 348 gespeicherte Dialogzeilen.
Neue Manifestpositionen 14 und 15 mit eigenen IDs. Block 2 umfasst damit
sechs von acht geplanten Texten und 504 Zeilen je Sprache. T07 und T08
sind weiterhin nur geplant; keine leeren Einträge oder Platzhalterdateien.

Aktualisiert: Manifest, README, Planungsindex, Block-2-Lieferstand und
kumulatives Vokabular. Bestehende Lektionsdateien, App-Code, Formatvertrag,
Validator und Unit-Tests wurden nicht verändert. Die gewünschte Wiedergabe
DE → PT → DE und die standardmäßig neun japanischen Wiederholungen je
Tagvorkommen bleiben unverändert.

## Redaktionelle Prüfung und Kontinuität

Die Durchsicht erfolgte durch den schreibenden Agenten selbst. Sie ist
keine unabhängige Modellprüfung oder menschliche sprachliche Abnahme.

- T05 setzt direkt beim angekündigten Bericht über Aokis Studienzeit an.
  Aoki bleibt heute Lehrerin. Ihre Aussage Ich bin Studentin gehört
  ausdrücklich zur vorgestellten damaligen Gegenwart; der heutige Rückblick
  lautet Ich war Studentin. Person und Nomen bleiben im Zeitvergleich gleich.
- Die Form wird isoliert erklärt, im ganzen Satz verwendet, gekürzt und
  von Jonas als Bericht über Aoki wiedergegeben. Kaffee, Wasser und das
  bekannte Notizheft liefern weitere vollständige Anwendungen ohne neue
  lexikalische Grundwörter. Nominale Beschreibung und Handlung werden getrennt.
- T06 verneint Aokis Lehrerrolle für genau diese frühere Studienzeit.
  Eine positive Vergleichsaussage über eine frühere Lehrerin gehört ausdrücklich
  zu einer anderen Sprecherin, nicht plötzlich zu Aokis Biografie.
- Vergangenheit und Verneinung werden zunächst einzeln verglichen. Erst danach
  folgt die kürzere höfliche Variante, getrennt von der Personenauslassung.
  Beide negativen Formen erhalten ganze Ergebnissätze mit hörbarer Bedeutung.
- Die Teepause in T06 ist ausdrücklich eine andere frühere Pause als die
  Kaffeepause in T05. Die Büroszene mit dem Notizheft wird dagegen bewusst
  wiederaufgenommen. Innerhalb einer Korrektur bleiben Sache und Zeitraum gleich.
- Keine vorausgesetzten Vergangenheitsfragen, keine neue Verbkonjugation und
  keine japanischen Zeitwörter. Der Übergang zu T07 kündigt erst die Verbindung
  von Vergangenheit und Frage an. Keine Eingabe oder Hausaufgabe verlangt.
- Deutsche Sprachpraxis: bin/war, kein/nicht, innerhalb einer Szene gegenüber
  rückblickend, obwohl, deshalb, weder/noch und die Korrektur mit sondern.
  Portugiesisch bewahrt diese deutschen Vergleiche und alle Szenenbedingungen.
- Bedeutung und Funktion stehen in der gesprochenen Prosa. Das ungesprochene
  Bedeutungsfeld ist keine versteckte Voraussetzung. Aussprachefelder enthalten
  die ganze Einheit, einschließlich Themen-は und は innerhalb von では.

Bei der Durchsicht wurde eine mehrdeutige Rückverweisung auf eine schon
negative Aussage durch Deine Vermutung zurückweisen ersetzt. Eine abstrakte
Erklärung über das Nichtzutreffen einer Berufsangabe wurde in beiden Sprachen
direkter formuliert. Außerdem ist ausdrücklich erklärt, dass Studentsein
eine Berufstätigkeit nicht grundsätzlich ausschließt: Aokis damaliger Status
ist eine gesetzte Szenentatsache, kein Schluss allein aus dem Nomen Studentin.

## Fachliche Referenz

[Tokyo University of Foreign Studies: Nでした / Nではありませんでした](https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/004.html),
am 2026-09-17 konsultiert: vergangene nominale Beschreibungen, Austausch
des Abschlusses, negative Vergangenheit, Weglassen eines bekannten Bezugs
und gesprochene Variante mit じゃ. Die Quelle belegt diese Grundmuster,
nicht die Qualität jeder eigenen Dialogzeile oder ihre TTS-Aussprache.
Die Beispiele, Figurenhandlungen und deutsche Erklärungskette sind eigene
Ausarbeitungen. Weitere korrekte Negativvarianten werden nicht ausgeschlossen.

## Ausgeführte technische Prüfungen

```sh
python3 -B tools/check.py lektionen/de-pt/block-02-text-05.txt --pt lektionen/de-pt/block-02-text-05.pt.txt
python3 -B tools/check.py lektionen/de-pt/block-02-text-06.txt --pt lektionen/de-pt/block-02-text-06.pt.txt
python3 -B tools/check.py --all
python3 -B -m unittest discover -s tests
git diff --check
```

- Beide neuen Paare: keine harten Fehler und keine weichen Hinweise.
- Alle 15 registrierten Paare bestehen die Strukturprüfung. Frühere weiche
  Hinweise in Block 1 bleiben unverändert und sind keine neuen Befunde.
- Alle zwölf bestehenden Unit-Tests bestehen.

Zusätzlich wurde das aktuelle Reader-Modul `src/lessons/lesson-format.js`
direkt in einem einmaligen Node-Lauf verwendet, ohne App-Dateien zu ändern.
Geprüft: vollständige Zeilenpaarung, Sprecherfolge, identische Tagfelder
außer der Bedeutung, Japanisch aus Feld fünf beziehungsweise zwei und
keine japanischen Schriftzeichen oder Tagdelimiter in DE/PT-Sprachsegmenten.

Für alle 15 Paare bestanden **600 Einstellungskombinationen**, darunter
**80 für diese beiden neuen Texte**: PT an/aus, DE-Wiederholung an/aus,
Japanisch enthalten/herausgefiltert und japanische Wiederholungszahl eins
bis fünf. Pro Kombination wurden Segmentzahlen und japanische Wiederholungen
kontrolliert. Das simulierte Filtern prüft keine Geräte-Stimmenerkennung.
Der Zusatzlauf wurde direkt ausgeführt und nicht als dauerhafter Test gespeichert.

Bei den Standardeinstellungen ergeben sich 558 Sprachsegmente für T05
und 672 für T06. Das sind berechnete Äußerungen, keine gemessene Dauer.

## Offene Grenzen

Nicht durchgeführt: echte Wiedergabe auf dem Zielgerät, Hörprobe der langen
Abschlüsse, Zeitmessung, unabhängige menschliche DE/PT/JP-Prüfung oder ein
Nachweis des Lernerfolgs. Die Struktur- und Segmentprüfungen ersetzen diese
Prüfungen nicht. Besonders die langen Negativformen sollten mit der tatsächlich
gewählten japanischen Stimme angehört werden.

Dieses Protokoll hält den Prüfstand vor der Veröffentlichung fest. Nach
dem Push muss die App Manifest und Texte neu laden; ein alter Offline-Cache
wird durch das Schreiben oder Prüfen der Dateien nicht automatisch ersetzt.
