# Neue Hörtexte schreiben

Zuerst den Hauptplan und den betreffenden Blockplan lesen. Entscheidungen
des Lernenden gehen älteren Texten und früheren Modellurteilen vor.

## 1. Ziel und Voraussetzungen bestimmen

Hauptplan: `planung/hauptplan.md`. Detailpläne: `planung/bloecke/`.
Jeder Text hat ein verständliches Hauptziel. Erkläre Hilfsbausteine, die zum
Verstehen nötig sind, bevor du sie voraussetzt. Die erste Satzklasse darf
nicht stillschweigend eine spätere Partikelklasse verlangen.

Geschichtsstand und Kenntnisstand getrennt festhalten:
- Geschichte: wer spricht mit wem, was möchten die Figuren sagen?
- Kenntnisse: welche Wörter, Formen und Funktionen wurden tatsächlich erklärt?

Nur frühere Texte zählen zum Vorwissen. Der Text unter Prüfung darf nicht
seine eigenen neuen Inhalte als schon bekannt deklarieren.
`tools/recap.py` ist ein älterer, verlustbehafteter Extraktor, keine
kumulative Wissensquelle; sein automatisch ermittelter Tag ist kein Kursindex.
Für den neuen Kurs den Blockplan und das kumulative Vokabular verwenden.

## 2. Die Erklärung vor dem Dialog planen

Für jeden neuen Bestandteil festlegen:
- Ausgangssituation und verständlicher Ausgangssatz;
- neue Form mit hörbarer Bedeutung/Funktion;
- vollständig gesprochenes Beispiel mit vollständiger Übersetzung;
- begründete Änderung, vollständiges Ergebnis und neue Bedeutung;
- typische Anfängerfrage und deren konkrete Antwort;
- Grenze der Regel und Anschluss an den nächsten Text.

Keine Tabelle im Hörtext, keine reine Auswechselanweisung ohne Ergebnis.
Kein künstlicher Irrtum und keine Folge bloßer Zustimmungen zum Auffüllen.

## 3. Deutsch schreiben

`prompts/writer.md` mit Ziel, Vorwissen, Geschichte und erlaubtem Vokabular
füllen. Mindestens 80 Zeilen. Mehr ist erlaubt; ein zu großer Lernschritt
wird auf mehrere Texte verteilt.

Der Text muss ohne Bildschirm funktionieren. Feld 4 eines Tags wird nie
gesprochen. Die App spricht japanisch aus Feld 5, sonst Feld 2. Einzelne
Partikeln sind hörbar. Japanische Wörter gehören auch bei Aussprachefragen
in Tags. Deutsche und portugiesische Stimmen sind kein Ausspracheersatz.

Wiederholung: pro Zeile DE → PT → DE, japanische Tags standardmäßig je
dreimal. Diese bewusste Wiederholung nicht aus Effizienzgründen entfernen.
Keine zusätzliche deutsche Wiederholungsdatei anlegen.

## 4. Inhalt und Hörbarkeit prüfen

`prompts/reviewer.md` verwenden. Die vollständigen Ergebnisse jeder
Substitution nachverfolgen, nicht nur die Ausgangssätze.
Grammatische Aussagen anhand geeigneter Fachquellen überprüfen.
Eine Strukturprüfung bestätigt keine japanische Richtigkeit.

Eine zusätzliche unabhängige Sprachprüfung ist hilfreich, aber ein Modellurteil
ist kein fachlicher Beweis. Nur tatsächlich durchgeführte Prüfungen behaupten.
Ein separates Modell oder ein menschlicher Prüfer muss als solcher benannt
werden; die eigene Durchsicht nicht als unabhängige Prüfung ausgeben.

## 5. Portugiesisch übertragen

`prompts/translator.md` verwenden. Pro deutscher Zeile genau eine
portugiesische Zeile, mit denselben Tags und demselben Sprecher.
Derselbe Inhalt, gegebenenfalls einfacherer Satzbau. Wenn Deutsch mit Deutsch
verglichen wird, nicht stillschweigend Portugiesisch zum Vergleich machen.
Bekannter Kontext darf aufgegriffen werden; der Bezug muss hörbar klar bleiben.

## 6. Struktur prüfen und Manifest ergänzen

```sh
python3 -B tools/check.py lektionen/de-pt/block-01-text-01.txt \
  --pt=lektionen/de-pt/block-01-text-01.pt.txt --particle は
python3 -B tools/check.py --all
python3 -B -m unittest discover -s tests
```

Keine starre Zielhäufigkeit oder Höchstzahl von Tags. Mindestens zehn Tags
bleiben als strukturelles Mindestmaß erhalten. Wichtiger ist, ob das Japanische
im Text wirklich erklärt und angewendet wird.

Neue Einträge in `lektionen/index.json` eintragen, sonst sieht die App sie
nicht. Bei vollständigem Ersatz alter Texte neue IDs vergeben. Formatversion
nur bei einer technischen, inkompatiblen Formatänderung erhöhen.

## 7. Vokabular und Prüfprotokoll aktualisieren

Die neuen Wörter/Funktionen in `lektionen/vokabular.md` ergänzen. Bereits
bekannte Figuren behalten ihre Rollen.
Unter `planung/` ein nachvollziehbares Protokoll speichern:
- welche Texte und welche Prüfungen;
- fachliche Referenzen und korrigierte Befunde;
- offene Grenzen, insbesondere reale Gerätewiedergabe und Lernerfeedback.

Vor Veröffentlichung Diff und persönliche Daten prüfen. Keine lokalen
Benutzernamen, privaten Dateipfade, Zugangsdaten oder Gesprächsprotokolle
veröffentlichen. Die persönliche Git-Identität aus den übergeordneten
Repository-Anweisungen verwenden.
