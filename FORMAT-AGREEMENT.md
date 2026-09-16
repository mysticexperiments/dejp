# Formatvertrag — dejp, Version 1

Dieser aktuelle Vertrag ersetzt die historische Abstimmung mit ihren
zurückgezogenen Regeln. Die frühere Abstimmung bleibt in der Git-Historie.

## Dateien und Manifest

`lektionen/index.json` enthält `formatVersion: 1`, die Sprachzuordnung
`de / pt / ja` und die geordneten Lektionen mit `id`, `number`, `grammar`,
`title`, `titlePt`, `de` und `pt`. Pfade sind relativ zum Repository.
Nur hier registrierte Texte erscheinen in der App.

Jede Fassung ist UTF-8, ein Sprecherbeitrag pro Zeile, ohne Leerzeilen.
Sprecher: Jonas und Aoki, abwechselnd; Aoki hat die letzte Zeile.
Mindestens 80 Zeilen pro Sprache. Keine Hausaufgaben-Pflicht.
Beide Sprachfassungen haben dieselbe Zeilenzahl und dieselben Sprecher.

## Japanische Tags

`{Schreibung|Kana|Romaji|Bedeutung}`
oder `{Schreibung|Kana|Romaji|Bedeutung|Aussprache}`.

- Felder 1–4 sind nicht leer.
- Feld 2 ist die Kana-Lesung der ganzen Einheit.
- Feld 3 dient nur der Anzeige.
- Feld 4 ist deutsch beziehungsweise portugiesisch und wird nicht gesprochen.
- Feld 5 ist optional, bei Vorhandensein nicht leer: die vollständige
  phonetische Kana-Fassung der Einheit, etwa mit わ für die Themenpartikel は.
- Japanische Stimme: Feld 5, sonst Feld 2. Niemals Romaji als Audioersatz.
- Jedes Tag wird gesprochen, auch einzelne Partikeln.
- DE und PT enthalten pro Zeile dieselben Tags in derselben Reihenfolge.
  Alle Felder außer Feld 4 bleiben exakt gleich, einschließlich Leerzeichen.
- Neue Autoren schreiben vier oder fünf Felder. Parser und Validator nehmen
  auch angehängte Felder 6+ an; deren Bedeutung bleibt dieser Version unbekannt.
  Feldreihenfolge oder bestehende Feldbedeutung ändern erfordert eine neue Version.
- Keine Verschachtelung, keine Zeilenumbrüche im Tag. Geschweifte Klammern und
  senkrechte Striche kommen ausschließlich als Tagdelimiter vor.
- Kein ungetaggtes Japanisch oder japanisches Romaji in der gesprochenen
  DE/PT-Prosa; Personennamen in lateinischer Schrift sind erlaubt.
- Zwischen zwei Tags steht erklärender Text, nicht bloß ein Komma.

## Wiedergabe

Pro Zeile DE → PT → DE; die beiden zusätzlichen Durchgänge sind im Player
über Einstellungen steuerbar. Japanische Tags standardmäßig dreimal pro
Durchgang; insgesamt neunmal je Tagvorkommen bei allen Standarddurchgängen.
Der Kurs liefert nur eine DE- und eine PT-Datei.

Kein japanischer Text wird ersatzweise mit einer deutschen/portugiesischen
Stimme gelesen. Ohne erkannte japanische Stimme zeigt die App die Tags und
einen Hinweis, lässt ihre Aussprache aus und spielt die Prosa weiter.
Der Player schützt die Kette mit einem Timeout je Äußerung und einem
idempotenten Fortschritt. Das Repository implementiert keine Sprachausgabe.

## Didaktische Anforderungen

Die Regel ist für die konkrete Situation richtig und verständlich.
Jedes neue Wort oder jeder neue Satz bekommt eine hörbare Bedeutung;
Partikeln bekommen eine hörbare Funktion. Feld 4 ersetzt keine Erklärung.

Bei Austausch eines Satzteils müssen Ausgangssatz, Änderung, vollständiges
Ergebnis und dessen Bedeutung hörbar sein. Keine starre Obergrenze für
fachlich nützliche Beispielwiederholungen. Ein Hauptziel je Text, mit den
dafür ausdrücklich erklärten Hilfsbausteinen.

PT bewahrt dieselben Regeln, Beispiele, Einschränkungen und Vergleichssprachen.
Die Dateien dürfen nicht zwei unterschiedliche Unterrichtsinhalte vermitteln.

## Prüfumfang

`tools/check.py` prüft deterministisch Länge, Sprecher, Delimiter,
Pflichtfelder, Kana-Form, exakte DE/PT-Paarung und Manifestpfade.
Bei einer als `--particle` angegebenen Partikel prüft es außerdem, ob sie
isoliert und in einer längeren Einheit vorkommt. Die längere Einheit muss
redaktionell als sinnvoller vollständiger Satz geprüft werden; die bloße
Zeichenfolge beweist keine syntaktische Funktion.

Romaji-Erkennung und Längenvergleich der Aussprachefelder sind nur Hinweise.
Keine dieser Prüfungen beweist korrekte Grammatik, Übersetzung oder Aussprache.
