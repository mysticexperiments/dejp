# Prüfung — Block 1, Texte 01–03

Stand: 2026-09-16. Neue Kursfassung, keine Fortsetzung der alten fünf Kurztexte.

## Lieferung

- Hauptplan mit allen 90 Nummern der gelieferten Grammatiklandkarte.
- Block 1 mit vier Klassen und neun Teiltexten; T01–T03 ausgearbeitet.
- Drei deutsche und drei portugiesische Dateien mit jeweils 80 Zeilen.
- Neues Manifest mit eigenen IDs und unverändertem technischen Format 1.
- Aktuelle Autoren-, Übersetzer- und Prüfanweisungen sowie kumulatives Vokabular.

## Durchgeführte Prüfungen

| Prüfung | Ergebnis |
|---|---|
| `python3 -B tools/check.py --all` | alle drei Paare bestanden |
| Sprecher, Zeilenzahl, Tagfolge, exakte nicht übersetzte Felder | bestanden |
| `python3 -B -m unittest discover -s tests` | 12 Tests bestanden |
| Parser der konsumierenden App mit allen sechs Dateien | 80 zugeordnete Zeilen pro Paar |
| Daraus erzeugte Sprachsegmente | japanische Segmente benutzen Kana und ja-JP |
| `git diff --check` | bestanden |
| Eigene redaktionelle DE/PT-Durchsicht | durchgeführt; kein unabhängiges Modellurteil |

Ein Hinweis bleibt absichtlich sichtbar: In T01 Zeile 30 ist der Name Jonas
in beiden Bedeutungsfeldern gleich, obwohl seine Romaji-Lautform Yonasu lautet.
Das ist eine geprüfte Namensausnahme, keine fehlende Übersetzung.

Die Regressionstests decken insbesondere kaputte/verschachtelte/mehrzeilige
Tags, leere Aussprachefelder, Leerzeilen, ungetaggtes Japanisch in PT, exakte
Paarung ohne Normalisierung, angehängte unbekannte Felder, Partikelbeispiele
und die CLI-Paarprüfung ohne erfundenes Zielargument ab.

## Inhaltliche Durchsicht

- Jede neue Form bekommt eine Bedeutung oder Funktion im gesprochenen Text.
- T01 entwickelt Student → eigener Name → Nationalität und erklärt, warum
  das Wort ich bei Aoki eine andere Person meint.
- T02 entwickelt Kaffee → Tee → Wasser mit jeweils vollständigem Ergebnis.
  Die Nominalaussage wird vom Handlungssatz getrennt; kein zusätzliches です
  nach dem höflichen Verb. Gewohnheit/Wahl wird nicht als laufende Handlung
  ausgegeben.
- T03 führt Namen und さん vor dem Austausch ein. Aus Ich trinke Tee wird
  Frau Nakamura trinkt Tee; anschließend ändern sich Getränk und Person in
  getrennten, vollständig erklärten Schritten.
- Beide Sprachen behalten dieselben Personen, Situationen, Vergleiche und
  Einschränkungen. Deutsch bleibt dort die Vergleichssprache, wo es erklärt wird.
- Aussagen über das Weglassen des Themas sind kontextbezogen, kein pauschales
  Verbot kurzer Sätze. Früh erwähnte Auslassung wird später systematisch vertieft.

Fachlicher Gegencheck an ausgewählten Primärquellen:

- [Japan Foundation: Irodori Starter, Lektion 3](https://www.irodori.jpf.go.jp/assets/data/starter/pdf/X_L03.pdf),
  Grammatiknotizen S. 14 und 16: Nominalsätze, Thema, Auslassung und Namen.
- [Japan Foundation: Irodori-Grammatiknotizen](https://www.irodori.jpf.go.jp/assets/data/Grammar_all.pdf),
  Starter L5-26: Objektmarker, Stellung vor dem Verb und Verwendung höflicher Formen.
- [University of Cambridge: Introduction to Modern Japanese, Lesson 7](https://www.ames.cam.ac.uk/files/IMJ_1_8/Lesson%207.pdf),
  Einführung: Verbformen ohne Personen-/Numerusflexion.

Diese Referenzen prüfen grundlegende Konstruktionen. Sie sind keine externe
Abnahme sämtlicher neu geschriebener Dialogzeilen oder Übersetzungen.

## Rechnerische Wiedergabeprüfung

Aus den tatsächlichen Parserfunktionen der App, mit allen drei Phasen und
dreifacher japanischer Wiederholung:

| Text | Zeilen pro Sprache | Tags pro Fassung | Äußerungen insgesamt | Davon japanisch |
|---|---|---|---|---|
| B01-T01 | 80 | 23 | 510 | 207 |
| B01-T02 | 80 | 22 | 492 | 198 |
| B01-T03 | 80 | 24 | 513 | 216 |

Die Zahlen sind erzeugte Segmentzahlen, keine Audioaufzeichnung. Keine
Minutenangabe wird daraus als gemessen ausgegeben. Die japanische Wiederholung
ist ausdrücklich gewünscht und wurde beibehalten.

## Noch nicht verifiziert

- Keine Wiedergabe dieser neuen Texte auf dem tatsächlichen Telefon.
- Kein gemessener Durchlauf mit realen Stimmen, Pausen oder Gerätewechseln.
- Keine unabhängige Prüfung durch einen zweiten Sprachprüfer oder einen
  fachkundigen menschlichen Japanisch-/Portugiesischsprecher.
- Kein Nachweis, dass der Lernende nach einmaligem Hören alles verstanden hat.
- Die 90-Themen-Karte ist ein Arbeitsplan, keine offizielle A1-Zertifizierung.

Nächste sinnvolle Abnahme: T01 in der App vollständig anhören und konkrete
unverständliche Stellen markieren. Dieses Feedback kann die Erklärungstiefe
der Folgetexte verbessern, ohne den gespeicherten Hauptplan zu verwerfen.
