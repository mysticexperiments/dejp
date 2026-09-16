# Prüfung — Block 1, Texte 04–09

Stand: 2026-09-16. Ergänzung der neuen Kursreihe; keine Wiederverwendung der
alten fünf Kurzlektionen. [Erste Lieferung](pruefung-block-01-texte-01-03.md).

## Lieferung und Kontinuität

Sechs neue Texte, jeweils 80 deutsche und 80 portugiesische Sprecherzeilen.
Zusammen mit den unveränderten T01–T03 ist Block 1 mit neun Texten vollständig
geschrieben: 720 Zeilen je Sprache, 18 Textdateien. Die deutsche Wiederholung
erzeugt die App; es gibt keine dritte Kopie der Dateien.

| Text | Neue Einsicht | Anschluss und vollständige Beispielketten |
|---|---|---|
| T04 | Thema ist nicht automatisch handelnde Person | Nakamura trinkt Tee → Gegenstand als Thema → Kaffee als Thema, ich als Subjekt; Umstellung und beide Marker erklärt |
| T05 | Person kann aus dem Kontext verstanden werden | voller Teesatz → kurze eigene Antwort → dieselbe Form über Nakamura → ausdrücklicher Wechsel zu Aoki |
| T06 | Marker zeigen Beziehungen zum vorangehenden Ausdruck | Thema gegenüber Antwort auf Wer trinkt?; Person und Getränk wechseln; Sache ist nicht automatisch Objekt |
| T07 | Existenzort und Handlungsort sind verschiedene Beziehungen | Wasser vorhanden → Buch/Tee/Kaffee vorhanden → Wasser im Zimmer trinken → Person/Getränk wechseln → bekannten Ort auslassen |
| T08 | Artikel, Genus und Zahl sind keine übertragenen deutschen Pflichtformen | neues Buch gegenüber gesuchtem bekannten Buch → Lehrerin/Lehrer → ein Buch/mehrere Bücher → einzelner Student/Gruppe |
| T09 | höflich und schlicht bei gleicher Grundinformation | Student, Buch, Kaffee, Wasser, Nakamura jeweils im ganzen Satz vergleichen; selbst beim höflichen Stil bleiben |

T08 enthält zusätzlich zum ursprünglichen Pflichtpaar einen durchgehend
erklärten Satz über das bekannte Buch: 本は部屋にあります. Er verbindet
bereits eingeführte Bausteine und macht hörbar, dass は kein bestimmter
Artikel ist. Der Blockplan und das kumulative Vokabular dokumentieren das.

## Tatsächlich durchgeführte Prüfungen

- `python3 -B tools/check.py --all`: alle neun DE/PT-Paare bestanden.
- Mindestlänge, Sprecherwechsel, Taggrenzen, Kana, identische nicht übersetzte
  Tagfelder und isolierte Partikeln mit ganzen Beispielen: bestanden.
- `python3 -B -m unittest discover -s tests`: alle 12 bestehenden Tests bestanden.
- Tatsächlicher App-Parser, Funktionen `buildLessonRows`, `speechSegmentsFor`
  und `repeatJapaneseUtterances`: alle neun Paare ergeben je 80 zugeordnete Zeilen.
- Alle drei Phasen je Zeile geprüft: DE, PT, DE-Wiederholung; je japanischem
  Tag drei Wiederholungen pro Phase. Japanische Ausgabe besteht aus Kana
  und benutzt `ja-JP`, Prosa aus der jeweils richtigen DE/PT-Sprachzuordnung.
- Japanische Tags/Klammern gelangen nicht in die erzeugten Prosa-Segmente.
- T01–T03 beider Sprachen byteweise mit dem vorherigen Commit verglichen:
  unverändert.
- Eigene redaktionelle Durchsicht der DE/PT-Paare und ihres Lernanschlusses.
  Keine unabhängige Zweitprüfung und keine menschliche Sprachabnahme.

Die Formattests beweisen nicht die Qualität der Erklärung oder ihre sprachliche
Richtigkeit. Sie wurden nicht geändert, um die neuen Texte bestehen zu lassen.
Die App selbst wurde nicht verändert.

## Geprüfte Hinweise, nicht unterdrückte Warnungen

- T01: bereits bekannte Eigenname-Ausnahme Jonas in beiden Bedeutungsfeldern.
- T05: dieselben Kurzsätze über Tee und Wasser bekommen je nach ausdrücklich
  eingeführter Person die Bedeutung Ich trinke oder Sie trinkt. Genau diese
  Kontextabhängigkeit ist der Unterrichtsgegenstand.
- T08: dieselben Formen werden als Lehrer/Lehrerin, ein Buch/Bücher und
  Student/Studierende übersetzt. Jede Variante hat eine ausdrücklich erklärte
  Szene; die abweichenden Bedeutungsfelder sind beabsichtigt.

Die zehn neuen weichen Hinweise betreffen diese fünf Kontextunterschiede,
jeweils in DE und PT. Keine anderen neuen Validatorhinweise bleiben offen.

## Erzeugte Sprachsegmente

Konfiguration: portugiesische Phase an, deutsche Wiederholung an,
japanische Wiederholung drei. Diese Zahlen stammen aus der Segmenterzeugung,
nicht aus einer Audioaufnahme oder einer gemessenen Wiedergabedauer.

| Text | Zeilen je Sprache | Tags je Fassung | Äußerungen gesamt | Japanische Äußerungen |
|---|---|---|---|---|
| T01 | 80 | 23 | 510 | 207 |
| T02 | 80 | 22 | 492 | 198 |
| T03 | 80 | 24 | 513 | 216 |
| T04 | 80 | 23 | 504 | 207 |
| T05 | 80 | 23 | 492 | 207 |
| T06 | 80 | 21 | 477 | 189 |
| T07 | 80 | 26 | 528 | 234 |
| T08 | 80 | 21 | 486 | 189 |
| T09 | 80 | 31 | 594 | 279 |

Der Node-Aufruf meldete die bestehende Modulart-Warnung der App und lud die
Datei erfolgreich als ES-Modul. Keine Paketkonfiguration wurde dafür geändert.

## Fachliche Gegenprüfung

Eigene Dialoge und Beispiele, keine Übernahme von Lehrbuchdialogen.
Folgende Primärquellen wurden für ausgewählte Grundregeln herangezogen:

- [Japan Foundation, は: Funktionen und Kombination mit anderen Partikeln](https://www.kyozai.jpf.go.jp/kyozai/material/BTS00038/ja/render.do):
  Thema und begrenzter Austausch von が/を durch は.
- [Irodori Starter, Lektion 7, Grammatiknotizen S. 24](https://www.irodori.jpf.go.jp/assets/data/starter/pdf/X_L07.pdf):
  Existenzmuster mit Ort und vorhandenem Gegenstand.
- [Japan Foundation, で als Handlungsort](https://www.kyozai.jpf.go.jp/kyozai/material/BTS00050/en/render.do):
  Handlungsort mit で.
- [Irodori Elementary 1, Lektion 1, S. 15 und 18](https://www.irodori.jpf.go.jp/assets/data/elementary01/pdf/Y_L01.pdf):
  höflicher/schlichter Stil und ganze Verbformen; schlichte Sprache zunächst verstehen.
- [University of Cambridge, Introduction to Modern Japanese, Introduction, S. 3–4](https://www.ames.cam.ac.uk/files/IMJ_1_8/4.%20Introduction.pdf):
  Personen-/Numerusunabhängigkeit der Verbform und nicht nach Genus/Zahl flektierte Nomen.

Diese Gegenprüfung zertifiziert nicht jede neue Zeile. Portugiesisch wurde
bei der eigenen Paardurchsicht inhaltlich abgeglichen: dieselben Situationen,
Personen, Einschränkungen und ausdrücklich deutschen Vergleiche bleiben erhalten.

## Offen und nächster sinnvoller Schritt

- Kein vollständiger Audiolauf auf Telefon oder Browser mit diesen neuen Texten.
- Keine gemessene Dauer; keine Prüfung tatsächlicher japanischer Prosodie,
  Pausen, Stimmwechsel, Abbrüche oder Wiedereinstieg auf dem Zielgerät.
- Kein Lernernachweis und keine unabhängige fachkundige JP/PT-Abnahme.
- Keine Änderung der bewusst gewünschten neunfachen japanischen Wiederholung.

Als Nächstes die Texte in Reihenfolge anhören und konkrete unverständliche
Stellen markieren. Besonders T04 mit dem Themenwechsel und T07 mit zwei
verschiedenen Ortsbeziehungen sollten praktisch erprobt werden. Die Reihe
bleibt ein Hörkurs ohne verpflichtende Eingabe oder bewertete Hausaufgabe.
