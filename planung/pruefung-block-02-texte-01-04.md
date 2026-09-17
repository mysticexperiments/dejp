# Lieferung und Prüfung — Block 2, Texte 1 bis 4

Stand: 2026-09-17. Vier neue deutsche Hörtexte und ihre zeilengleichen
brasilianisch-portugiesischen Fassungen, nach dem [Blockplan](bloecke/block-02.md).

## Lieferumfang

| Text | Thema | Zeilen je Sprache | Japanische Tags je Fassung | Davon bei Jonas |
|---|---|---:|---:|---:|
| [B02-T01](../lektionen/de-pt/block-02-text-01.txt) | Eine falsche nominale Zuordnung verneinen | 82 | 31 | 12 |
| [B02-T02](../lektionen/de-pt/block-02-text-02.txt) | Kürzere höfliche Negativvariante | 82 | 36 | 13 |
| [B02-T03](../lektionen/de-pt/block-02-text-03.txt) | Aussage in Frage umwandeln und antworten | 80 | 26 | 6 |
| [B02-T04](../lektionen/de-pt/block-02-text-04.txt) | Antwortbezug, Bestätigung und Richtigstellung | 86 | 26 | 11 |

Das sind 330 Dialogzeilen je Sprache, 660 gespeicherte Zeilen insgesamt.
Die deutsche Wiederholung wird nicht zusätzlich gespeichert. Die vier
Einträge stehen unter neuen IDs an Position 10–13 im Lektionsmanifest.
Block 2, Texte 5–8 bleiben geplant und sind nicht registriert.

Weitere aktualisierte Dateien: README, Planungsindex, Lieferstand im
Blockplan und kumulative Vokabularübersicht. Bestehende Block-1-Textdateien
wurden für diese Lieferung nicht verändert; ihre Dateihashes wurden vor
und nach der Arbeit verglichen. App-Code, Formatvertrag und Prüfcode bleiben
unverändert. Die zuvor vorhandenen lokalen Änderungen bleiben erhalten.

## Lehrweg und redaktionelle Durchsicht

Die Texte sind eigene Dialoge, keine Übersetzung eines fremden Lehrwerks.
Die Durchsicht wurde vom schreibenden Agenten selbst durchgeführt, nicht
von einem unabhängigen Modell oder einem menschlichen Sprachprüfer.

- T01: neues Inhaltswort nur ノート. Bekannte Getränke, Namen und Rollen
  erlauben unterschiedliche Anwendungen der neuen Verneinung ohne einen
  gleichzeitigen großen Wortschatzsprung. Eine negative Zuordnung ist weder
  die Behauptung fehlender Existenz noch schon die positive Richtigstellung.
- T02: Kontraktion では → じゃ und Weglassen eines klaren Personenbezugs
  werden getrennt erklärt. Die kürzere Negativvariante bleibt höflich.
  Andere korrekte Formen werden nicht als Fehler ausgeschlossen.
- T03: か, はい und いいえ werden vor ihren Anwendungen erklärt.
  Fragen und Antworten werden tatsächlich ausgesprochen, nicht nur
  besprochen. Positive Fragen mit negativen Antworten sind von noch nicht
  gelehrten negativen Fragen abgegrenzt.
- T04: Bestätigung mit そうです ist auf die behandelten nominalen Fragen
  begrenzt. Die Antwort kann auf Jonas, Aoki oder ein Getränk verweisen.
  Eine alternative Korrektur mit いいえ、学生です zeigt ausdrücklich,
  dass nach nein auch die richtige positive Information folgen kann.

Bei jeder neuen Satzform stehen Bedeutungen in der gesprochenen Prosa;
das stumme Bedeutungsfeld allein reicht nicht. Umformungen liefern das
ganze Ergebnis. Jonas spricht selbst Beispiele und erklärt Veränderungen.
Fragen werden im Dialog beantwortet; es gibt keine verpflichtende Eingabe,
Lernkontrolle oder Hausaufgabe für den Hörer.

Die deutschen Dialoge üben unter anderem kein/nicht, Fragewortstellung,
sondern, Begründungen und Perspektivwechsel mit ich/du. Portugiesisch
bewahrt diese deutschen Vergleiche und ersetzt sie nicht durch andere
portugiesische Grammatiklektionen.

Szenenwechsel, Gegenstände und Wissensstände werden hörbar angekündigt.
Fragen mit これ betreffen Dinge beim Fragenden; die Antworten verwenden
kurze nominale Formen, statt beim Sprecherwechsel versehentlich auf ein
anderes Ding zu zeigen. Die Frage über Aoki mit ihrem Namen wird als
weitergegebene Frage erklärt, nicht als pauschale Empfehlung für ihre Anrede.

### Während der Durchsicht korrigiert

- Eine unnatürliche portugiesische Formulierung zur Namensverwechslung
  durch eine klare Aussage über das Verwechseln zweier Personen ersetzt.
- Die Beschreibung des Einbands in T03 präzisiert.
- Einen künstlichen Irrtum in T04 durch eine sinnvolle alternative
  Antwortform mit vollständiger Bedeutung ersetzt.
- Die Grenze der Bestätigung mit そうです ausdrücklich ergänzt, damit
  aus nominalen Beispielen kein universelles Antwortrezept entsteht.
- Klarer formuliert, dass der Inhalt einer Frage bestätigt wird, nicht
  die Frage selbst.
- Die Aussage über zwei Negativvarianten auf deren Verwendung im echten
  Gespräch bezogen; die gewünschte App-Wiederholung bleibt davon unberührt.

## Fachliche Gegenprüfung

Die Quellen wurden für die grammatischen Muster konsultiert, nicht als
Beweis einer vollständigen sprachlichen Zertifizierung aller Dialogzeilen.

- [TUFS: Nです / Nではありません](https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/001.html):
  nominale Verneinung, höflicher Stil und gesprochene Variante じゃありません.
- [TUFS: Nですか](https://www.coelang.tufs.ac.jp/mt/ja/gmod/contents/explanation/003.html):
  Fragepartikel, Frageintonation und Bezug von ja/nein. Die dort ebenfalls
  behandelten negativen Fragen werden hier nicht vorweggenommen.
- [TUFS: Wortschatzmodul そう](https://www.coelang.tufs.ac.jp/modules/ja/vmod/v_search_detail.php?id=45&ls=%E3%81%9D&rf=3):
  Bestätigungsform はい、そうです. Im Dialog wird sie an ausdrücklich
  eingeführten nominalen Fragen erklärt.

## Ausgeführte technische Prüfungen

### Repository

```sh
python3 -B tools/check.py --all
python3 -B -m unittest discover -s tests
git diff --check
```

- Alle 13 registrierten DE/PT-Paare bestehen die Strukturprüfung.
- Die vier neuen Paare haben weder harte Fehler noch weiche Hinweise.
- Vorhandene weiche Hinweise in Block 1 betreffen dort bereits dokumentierte
  Kontextübersetzungen und einen Eigennamen; sie sind keine neuen Befunde.
- Alle zwölf vorhandenen Unit-Tests bestehen.
- Keine Whitespace-Fehler im Diff.
- Lokale Verweise der aktualisierten Dokumentation und des Lieferberichts geprüft.

### Reader-Kompatibilität

Ein zusätzlicher einmaliger Node-Prüflauf verwendete das aktuelle
App-Modul `src/lessons/lesson-format.js` mit `buildLessonRows`,
`speechSegmentsFor` und `repeatJapaneseUtterances`, ohne die App zu ändern.

Geprüft wurden:

- vollständige Zeilenpaarung und unveränderte Sprecherfolge;
- gleiche japanische Tagfelder in DE und PT, abgesehen vom Bedeutungsfeld;
- japanischer Sprechtext aus Feld fünf, sonst Feld zwei;
- korrekte Sprachzuordnung, keine japanischen Schriftzeichen oder
  Tag-Trennzeichen in den DE/PT-Sprechsegmenten;
- PT an/aus, deutsche Wiederholung an/aus, japanische Äußerungen
  enthalten/herausgefiltert und japanische Wiederholungszahl eins bis fünf.

Alle **520 Kombinationen** für 13 Texte bestanden, darunter **160** für die
vier neuen Texte. Das ist ein Parser-/Segmenttest, kein Browser- oder
Audio-End-to-End-Test. Die Variante ohne japanische Stimme simuliert nur
das Filtern japanischer Äußerungen; sie prüft nicht die Geräte-Stimmenerkennung.
Der Zusatzlauf wurde direkt ausgeführt und nicht als neuer dauerhafter Test
installiert. Die vorhandenen Repository-Tests bleiben unverändert.

Bei DE → PT → DE und drei japanischen Wiederholungen pro Phase entstehen:

| Text | Berechnete TTS-Äußerungen insgesamt |
|---|---:|
| B02-T01 | 597 |
| B02-T02 | 657 |
| B02-T03 | 525 |
| B02-T04 | 552 |

Eine Äußerung ist ein erzeugtes Sprachsegment, keine gemessene Audiodauer.
Die neunfache japanische Wiederholung je Tagvorkommen bleibt erhalten.

## Offene Prüfungen und Veröffentlichung

Nicht durchgeführt: vollständige Hörprobe auf dem Zielgerät,
Zeitmessung, unabhängige menschliche DE/PT/JP-Sprachprüfung und Lernerfeedback.
Insbesondere die langen negativen Abschlüsse, die kurzen Antwortwörter und
die Intonation der Fragen müssen am Gerät gehört werden. Ein Fragezeichen
im Bedeutungsfeld wird nicht gesprochen und garantiert keine Frageintonation.

Dieses Protokoll dokumentiert den lokalen Prüfstand vor der Veröffentlichung.
Die Texte sind im Manifest registriert. Nach dem Push muss die App die
aktualisierte Liste und die Texte aus dem Remote-Repository laden; ein
älterer Offline-Cache wird durch den lokalen Prüfstand allein nicht aktualisiert.
