# Revision — Block 1, Texte 1 bis 9

Stand: 2026-09-17. Redaktionelle Überarbeitung der neun deutschen Texte und
ihrer neun portugiesischen Paralleltexte. Dieser Bericht beschreibt den
aktuellen Stand; ältere Prüfberichte bleiben historische Momentaufnahmen.

## Ziel und Umfang

Japanisch durch verständliche, ausführliche deutsche Hördialoge lernen und
dabei Deutsch üben. Portugiesisch vermittelt dieselbe Erklärung als
Verständnishilfe, einschließlich der Vergleiche mit dem Deutschen.

Geändert wurden die 18 Textdateien sowie der Blockplan und die abgeleitete
Vokabularübersicht. App, Manifest und Formatvertrag bleiben unverändert.
Es wurden keine Texte gelöscht und keine zusätzlichen Lektionen angelegt.

Die Figuren bleiben beim gegenseitigen du. Jonas spricht häufiger selbst
japanische Beispiele, prüft deren Bedeutung und bekommt konkrete Antworten.
Neue Erklärungen ergänzen den Text dort, wo hörbare Zwischenschritte fehlen;
80 Zeilen sind keine Obergrenze.

## Änderungen je Text

Die Zeilenzahl gilt jeweils für Deutsch und Portugiesisch. Eine Zeile ist
ein Dialogbeitrag, keine einzelne TTS-Äußerung.

| Text | Zeilen je Sprache | Schwerpunkt der Überarbeitung |
|---|---:|---|
| 01 | 84 | Eigene Berufsangabe mit 教師; begrenzte Abgrenzung zu 先生; Jonas spricht eigene Vorstellungsbeispiele; eindeutiger Sprecherbezug. |
| 02 | 80 | Natürliches Deutsch statt irreführender Wort-für-Wort-Satzstellung; Getränk und Partikel als hörbare Einheit; vollständige Änderungen der Getränkewahl. |
| 03 | 80 | Jonas spricht selbst über Nakamura; Bedeutung und Ergebnis eines Personenwechsels werden überprüft; Aussage über eine Person von einer Bestellung unterschieden. |
| 04 | 86 | Thema und Subjekt anhand einer konkreten übrigen Tasse; Satz in hörbare Bausteine zerlegt; vollständiges Beispiel mit Nakamura als neuer trinkender Person. |
| 05 | 84 | Fragen und kurze Antworten tatsächlich durchgespielt; gleicher japanischer Satz mit verschiedenen Personenbezügen; unklarer Wechsel zu Aoki ausdrücklich repariert. |
| 06 | 84 | Eigener Hörschwerpunkt: Wortgruppe und zugehörige Partikel; unterschiedliche Gesprächsfragen führen zu unterschiedlichen Markern; Szenenwechsel ausdrücklich angekündigt. |
| 07 | 88 | Ortsangabe, vorhandene Sache und Verb einzeln hörbar; Existenz und Handlung vollständig gegenübergestellt; portugiesische Raumbezeichnung passend zur Büroszene. |
| 08 | 82 | Klarere deutsche Erklärung zu Genus; Beispiele mit konkretem Personenbezug; hörbare Szenen für Einzahl und Mehrzahl, einschließlich der Grenzen ohne Kontext. |
| 09 | 82 | Schlichte Formen als belauschte Beispiele zwischen vertrauten Personen; Jonas verwendet selbst weiter höfliche Formen; Satzstil und respektvolle Personenbezeichnung getrennt. |

## Fachliche Abgrenzungen

- 教師 wird als neutrale eigene Berufsangabe eingeführt; 先生 als respektvolle
  Bezeichnung beziehungsweise Anrede einer Lehrperson. Das ist eine
  begrenzte Gebrauchserklärung, kein absolutes Verbot für alle denkbaren
  Situationen. Abgleich: [Step Up Japanese — Sensei und Kyoushi](https://www.stepupjapanese.com/blog/2019/02/whats-difference-between-sensei-kyoshi).
- は ist kein deutsches Übersetzungswort und nicht automatisch der handelnde
  Mensch. Das konkrete Beispiel zeigt auch seine Verwendung anstelle von を.
  Abgleich: [Japan Foundation — は](https://www.kyozai.jpf.go.jp/kyozai/material/BTS00038/ja/render.do).
- に und で werden für die konkreten Existenz- und Handlungssätze erklärt,
  nicht als erschöpfende Regeln für diese Partikeln. Abgleich der
  Existenzmuster: [TUFS — Existenz und Ort](https://www.coelang.tufs.ac.jp/mt/ja/gmod/courses/c01/lesson02/step2/explanation/006.html).

Diese Quellenabgleiche und die redaktionelle Durchsicht ersetzen keine
unabhängige fachkundige Prüfung jeder japanischen, deutschen und
portugiesischen Zeile.

## Ausgeführte Prüfungen

1. `python3 -B tools/check.py --all`: alle neun DE/PT-Paare bestanden,
   keine harten Fehler.
2. `python3 -B -m unittest discover -s tests`: alle zwölf bestehenden Tests
   bestanden.
3. `git diff --check`: keine Whitespace-Fehler.
4. Zusätzlicher einmaliger Node-Prüflauf mit dem tatsächlich vorhandenen
   App-Modul `src/lessons/lesson-format.js`, ohne Änderungen an der App:
   `buildLessonRows`, `speechSegmentsFor` und `repeatJapaneseUtterances`.
   Alle 360 Kombinationen bestanden: neun Texte, PT an/aus, deutsche
   Wiederholung an/aus, japanische Äußerungen enthalten/herausgefiltert und
   japanische Wiederholungszahl eins bis fünf.

Der Zusatzlauf prüfte vollständige Zeilenpaarung, Sprecherwechsel,
übereinstimmende japanische Tagfelder, Sprachzuordnung, japanischen Sprechtext
aus Feld fünf beziehungsweise zwei sowie Wiederholungszahlen. In den
deutschen und portugiesischen Sprechsegmenten wurden keine japanischen
Schriftzeichen oder Tag-Trennzeichen gefunden. Romaji und Bedeutungsfeld
werden nicht als japanischer Sprechtext verwendet.

Der Zusatzlauf war ein einmaliger In-Memory-Test, kein neues gespeichertes
Testskript und kein Browser-End-to-End-Test. Die Variante ohne japanische
Stimme simulierte das Herausfiltern japanischer Äußerungen; sie prüfte weder
die Geräte-Stimmenerkennung noch den Playback-Watchdog.

### Berechnete Äußerungen bei den gewünschten Standardeinstellungen

DE → PT → DE pro Zeile, jede japanische Tag-Äußerung dreimal pro Phase.
Damit bleibt die gewünschte neunfache japanische Wiederholung erhalten.
Die Zahlen stammen aus der Segmenterzeugung, nicht aus einem Audiomitschnitt.

| Text | Japanische Tags im deutschen Text | Davon bei Jonas | TTS-Äußerungen insgesamt |
|---|---:|---:|---:|
| 01 | 26 | 5 | 558 |
| 02 | 29 | 4 | 573 |
| 03 | 27 | 5 | 549 |
| 04 | 30 | 6 | 606 |
| 05 | 27 | 7 | 543 |
| 06 | 28 | 5 | 567 |
| 07 | 34 | 6 | 642 |
| 08 | 23 | 4 | 516 |
| 09 | 34 | 3 | 639 |

### Verbleibende weiche Hinweise des Validators

- Text 01: Jonas ist als Eigenname in beiden Sprachen gleich.
- Text 05: Dieselbe kurze japanische Form bedeutet je nach ausdrücklich
  erklärter Situation ich trinke oder sie trinkt. Das ist der Lerninhalt.
- Text 07: Die Bedeutungsfelder für あります enthalten passende Varianten
  von es gibt beziehungsweise ist vorhanden.
- Text 08: Personenbezug, Geschlecht der beschriebenen Person und Anzahl
  wechseln in ausdrücklich eingeführten Situationen, ohne dass die
  japanische Form selbst jeweils wechseln muss. Auch das ist Lerninhalt.

Diese Hinweise wurden kontextuell geprüft, nicht als Fehler unterdrückt.

## Grenzen und nächster sinnvoller Test

Nicht durchgeführt: vollständiges Anhören der überarbeiteten Texte auf dem
Zielgerät, Messung ihrer Dauer, unabhängige menschliche Sprachprüfung und
ein Lerntest. Strukturprüfung beweist weder natürlichen Geräteklang noch
Lernerfolg und rechtfertigt keine Behauptung fehlerfreier Perfektion.

Als nächster Test eignet sich ein vollständiger Hörlauf von Text 04 mit
den gewünschten Einstellungen: Sind Kaffee als Thema, die trinkende Person
und die Satzbausteine ohne Blick auf den Bildschirm verständlich? Die
tatsächliche Dauer und störende Übergänge sollten dabei erfasst werden.

Die Änderungen wurden lokal vorbereitet; ein Commit oder Push gehört nicht
zu dieser Revision.
