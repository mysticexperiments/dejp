# Wie eine Lektion entsteht

Diese Datei ist fuer ein KI-Modell geschrieben, das eine neue Lektion
schreiben soll. Sie sagt, in welcher Reihenfolge was passiert, und vor allem
WARUM die Regeln in `writer.md` so streng sind: weil die App den Text nicht
anzeigt, sondern VORLIEST.

Lies zuerst Teil A. Ohne Teil A wirken die Regeln willkuerlich, und ein
Modell, das sie fuer willkuerlich haelt, bricht sie.

---

# TEIL A — Was die App mit dem Text macht

## A1. Der Text wird gehoert, nicht gelesen

Der Lernende hoert die Lektion. Der Bildschirm zeigt die Zeile zwar an, aber
die App ist zum Zuhoeren gebaut, oft unterwegs. Deshalb gilt:

- "Wie du oben siehst" funktioniert nicht. Es gibt kein Oben.
- Eine Tabelle funktioniert nicht. Man kann eine Tabelle nicht hoeren.
- Was nicht gesagt wird, kommt nicht an.

## A2. Eine Zeile wird in mehrere Sprech-Stuecke zerlegt

Die Sprachausgabe kann die Stimme MITTEN in einem Satz nicht wechseln. Ein
Stueck Text hat genau eine Stimme. Deshalb zerschneidet die App jede Zeile an
den geschweiften Klammern:

    Aoki: Dazwischen gehoert {は|は|wa|Themenpartikel|わ}, und das sagt: darueber rede ich.

    wird zu

    1. "Dazwischen gehoert"        -> deutsche Stimme
    2. "わ"                         -> japanische Stimme
    3. ", und das sagt: darueber rede ich."  -> deutsche Stimme

Drei getrennte Ansagen, nacheinander. Daraus folgt direkt:

- **Zwei Tags nebeneinander klingen falsch.** `{...}{...}` gibt zwei japanische
  Ansagen ohne Pause und ohne deutschen Text dazwischen. Zwischen zwei Tags
  gehoert immer deutscher Text.
- **Sehr viele Tags in einer Zeile zerhacken die Zeile.** Eine Zeile mit sechs
  Tags wird zu dreizehn Ansagen und klingt wie eine Maschine.

## A3. Was ausserhalb der Klammern steht, liest die DEUTSCHE Stimme

Das ist der Grund fuer das Romaji-Verbot, und es ist kein Schoenheitsproblem:

| Du schreibst | Deutsche Stimme sagt |
|---|---|
| `desu`     | "dezu"     |
| `gakusei`  | "gakuzei"  |
| `watashi`  | "vatashi"  |
| `wa`       | "va"       |

Die portugiesische Stimme macht denselben Fehler mit dem s, und schluckt
zusaetzlich das h in `ha`. Der Lernende lernt also eine falsche Aussprache,
und zwar genau bei den Woertern, die die Lektion beibringen will.

**Regel:** willst du ueber ein japanisches Wort reden, steht es im Tag. Immer.
Die einzigen Ausnahmen stehen in `writer.md` und sind eng.

## A4. Welches Feld gesprochen wird

    {Feld1|Feld2|Feld3|Feld4}  oder  {Feld1|Feld2|Feld3|Feld4|Feld5}

| Feld | Inhalt | Wird gesprochen? |
|---|---|---|
| 1 | japanische Schreibung (Kanji) | nein |
| 2 | dasselbe in Hiragana | nur wenn Feld 5 fehlt |
| 3 | Romaji | **nie** |
| 4 | Bedeutung | **nie** |
| 5 | die Aussprache in Hiragana | ja, wenn vorhanden |

Gesprochen wird: **Feld 5, sonst Feld 2.** Nie Feld 1, nie Feld 3.

Feld 1 wird nicht gesprochen, weil eine Sprachausgabe bei Kanji raten muss.
Feld 2 ist eindeutig.

Feld 5 gibt es, weil Schreibung und Aussprache auseinandergehen: das Partikel
は wird `wa` gesprochen, を wird `o` gesprochen. Feld 5 ist immer die
VOLLSTAENDIGE Aussprache des GANZEN Tags, nicht nur das eine abweichende
Zeichen. Steht dort nur `わ` fuer einen ganzen Satz, liest die App den ganzen
Satz als "wa" vor.

## A5. Feld 4 wird NIE vorgelesen — die wichtigste Folge

Feld 4 steht auf dem Bildschirm und sonst nirgends.

Wer nur hoert, bekommt also `watashi wa hatarakimasu` ins Ohr und danach
nichts. Die Bedeutung ist zwar im Tag, aber sie war nie zu hoeren.

**Deshalb muss Aoki oder Jonas die Bedeutung im deutschen Fliesstext SAGEN.**
Nicht bei Partikeln — die haben keine Uebersetzung, da wird gesagt, was das
Zeichen TUT. Aber bei jedem Wort und jedem Satz.

Dieser Fehler ist mir in Lektion 4 passiert und wurde erst beim Gegenlesen
gefunden. Er sieht auf dem Bildschirm vollkommen richtig aus.

## A6. Deutsch, Portugiesisch, Deutsch — pro ZEILE

Die App durchlaeuft jede Zeile dreimal, bevor sie zur naechsten geht:

    Zeile 1: deutsch -> portugiesisch -> deutsch
    Zeile 2: deutsch -> portugiesisch -> deutsch
    ...

Nicht die ganze Lektion dreimal. **Zeile fuer Zeile.** Beides ist im Code
abschaltbar: ohne Portugiesisch bleibt deutsch, deutsch; ohne Wiederholung
bleibt deutsch, portugiesisch. Voreingestellt ist beides an.

Portugiesisch ist das Sicherheitsnetz: wer die deutsche Erklaerung nur halb
verstanden hat, bekommt sie sofort einfacher, und hoert dieselbe deutsche
Zeile dann noch einmal mit dem Wissen, was gemeint war.

Das hat eine Folge fuers Schreiben: **die portugiesische Zeile muss allein
stehen koennen.** Sie steht zwischen zwei deutschen Durchgaengen derselben
Zeile, nicht am Ende einer ganzen Lektion. Ein Rueckverweis wie "wie vorhin
gesagt" geht dort ins Leere.

## A6b. Japanische Stuecke werden mehrfach gesprochen

Die App spricht jedes japanische Tag standardmaessig DREIMAL hintereinander,
einstellbar zwischen ein- und mehrmals. Der deutsche Text daneben nur einmal.

Deshalb ist die Obergrenze fuer Tags nicht nur Geschmack: eine Zeile mit sechs
Tags wird zu achtzehn japanischen Ansagen plus dem deutschen Text, mal drei
Durchgaenge. Das ist keine Zeile mehr, das ist eine Uebung.

Deshalb muessen beide Fassungen Zeile fuer Zeile und Tag fuer Tag
uebereinstimmen. Die App zaehlt mit. Und deshalb ist die portugiesische
Fassung ABSICHTLICH einfacher formuliert als die deutsche.

**Wiederhole keine Zeile selbst.** Die Wiederholung macht die App.

## A7. Die japanische Stimme kann fehlen

Hat das Geraet keine japanische Stimme installiert, zeigt die App einen
Hinweis, stellt die Tags dar und spricht das Japanische einfach nicht. Die
Lektion laeuft trotzdem bis zum Ende durch.

Das heisst: der deutsche Text muss auch dann noch etwas erklaeren, wenn das
Japanische stumm bleibt. Ein Satz wie "Hoerst du den Unterschied?" ohne jede
weitere Erklaerung ist in diesem Fall wertlos.

## A8. Einzelne Kana werden gesprochen

Frueher stand hier die Regel, dass einzelne Kana wie `わ` nicht gesprochen
werden und deshalb zu vermeiden sind. **Diese Regel war falsch.** Sie wurde
gemessen und zurueckgezogen; siehe AMENDMENT 1 in `FORMAT-AGREEMENT.md`.

Ein einzelnes `わ` wird sauber gesprochen, rund 0,8 Sekunden. Partikel duerfen
also allein in einem Tag stehen. Genau so werden sie ja gelehrt.

---

# TEIL B — Der Ablauf, Schritt fuer Schritt

Sieben Schritte. Kein Schritt wird uebersprungen.

## Schritt 1 — Ziel und Vokabular festlegen

Schlage die Lektionsnummer in `PLAN.md` nach. Dort stehen das Grammatik-Ziel,
der konkrete Anlass ("Jonas braucht das heute, weil...") und die neuen Woerter.

Genau EIN neues Grammatik-Ziel pro Lektion.

## Schritt 2 — Den Rueckblick bauen

    python3 tools/recap.py lektionen/de-pt/lektion-04.txt > /tmp/recap-05.md

**Nur die unmittelbar vorhergehende Lektion uebergeben, nicht alle.**

Das ist hart erarbeitet: als alle bisherigen Lektionen uebergeben wurden,
listete der Rueckblick Stoff als "schon gelernt", der in der neuen Lektion
gerade erst drankam. Der Pruefer meldete daraufhin einen Fehler, den die
Lektion gar nicht hatte. Der Fehler lag im Rueckblick, nicht im Text.

## Schritt 3 — Die deutsche Fassung schreiben

Nimm `prompts/writer.md` und setze die drei Platzhalter ein:

| Platzhalter | Woher |
|---|---|
| `{{ZIEL}}`       | aus `PLAN.md`, Spalte Grammar |
| `{{RUECKBLICK}}` | die Ausgabe aus Schritt 2 |
| `{{VOKABULAR}}`  | aus `lektionen/vokabular.md`: alles Bisherige plus die neuen Woerter dieser Lektion |

Ergebnis: genau 22 Zeilen, sonst nichts.

## Schritt 4 — Tier 1, zaehlen

    python3 tools/check.py lektionen/de-pt/lektion-05.txt 飲みません

Das zweite Argument ist das Ziel-Tag, und zwar als Argument 2, nicht als
Option. `check.py` gibt JSON aus. `"hart": []` und `"bestanden": true` muessen
erfuellt sein. Punkte unter `"weich"` sind Hinweise, kein Ausschluss, aber lies
sie.

`check.py` zaehlt nur. Es urteilt nicht ueber Bedeutung. Ein Text kann
bestehen und trotzdem sachlich falsch sein.

## Schritt 5 — Tier 2, gegenlesen lassen

Nimm `prompts/reviewer.md`, setze denselben `{{RUECKBLICK}}` ein, haenge die
Lektion an und gib das einem ANDEREN Sprachmodell. Nicht demselben, das
geschrieben hat: ein Modell findet seine eigenen Fehler schlecht.

Bisher benutzt: `gpt-5.6-luna` ueber `codex exec`. Zwei Fallstricke:

- `codex exec` braucht `< /dev/null`, sonst wartet es auf Eingabe und haengt.
- Die Antwort in eine Datei schreiben und das Urteil aus der LETZTEN Zeile
  lesen, die mit `URTEIL:` beginnt. Der Prompt selbst enthaelt die Zeichenkette
  `URTEIL: BRAUCHBAR oder NICHT BRAUCHBAR` als Vorlage, und ein einfaches
  `grep` findet diese Vorlage statt der Antwort.

**Der Pruefer schreibt nicht um. Er meldet.** Ueber jeden Befund entscheidet
der Schreiber. Ein Befund kann falsch sein — dann liegt der Fehler oft in der
Eingabe, wie in Schritt 2 beschrieben, und der Text bleibt, wie er ist.

Bei `NICHT BRAUCHBAR`: ueberarbeiten und zurueck zu Schritt 4. Lektionen 3 bis
5 brauchten vier Durchgaenge.

## Schritt 6 — Portugiesisch uebersetzen und paaren

Nimm `prompts/translator.md`, haenge die fertige deutsche Fassung an, speichere
das Ergebnis als `lektion-NN.pt.txt`. Dann beide zusammen pruefen:

    python3 tools/check.py lektionen/de-pt/lektion-05.txt 飲みません \
      --pt=lektionen/de-pt/lektion-05.pt.txt

Das prueft Zeilenzahl, Sprecher, Tag-Zahl je Zeile, und dass die Felder 1, 2,
3 und 5 zeichengenau gleich sind, waehrend Feld 4 tatsaechlich uebersetzt
wurde.

## Schritt 7 — In `index.json` eintragen

**Dieser Schritt wird am leichtesten vergessen, und dann zeigt die App die
Lektion nie an.** Die App liest ausschliesslich `lektionen/index.json`. Eine
Datei, die dort nicht steht, existiert fuer die App nicht.

Ein neuer Eintrag am Ende von `lessons`:

    {
      "id": "lektion-06",
      "number": 6,
      "grammar": "Rueckblick",
      "title": "Rueckblick — die vier Bausteine zusammen",
      "titlePt": "Revisao — as quatro pecas juntas",
      "de": "lektionen/de-pt/lektion-06.txt",
      "pt": "lektionen/de-pt/lektion-06.pt.txt"
    }

`formatVersion` bleibt bei 1, solange sich das Tag-Format nicht aendert. Aeltere
App-Versionen weigern sich, eine hoehere Version zu lesen.

Zuletzt `lektionen/vokabular.md` um die neuen Woerter ergaenzen, sonst fehlen
sie beim naechsten `{{VOKABULAR}}`.

---

# Die Abnahme in einer Liste

Eine Lektion ist fertig, wenn alles davon stimmt:

- [ ] 22 Zeilen, `Aoki:` / `Jonas:`, abwechselnd, letzte Zeile Hausaufgabe von Aoki
- [ ] ein einziges neues Grammatik-Ziel, 3- bis 5-mal als eigener Tag
- [ ] mindestens 10 Tags, kein anderer Tag oefter als 3-mal
- [ ] kein nacktes Romaji, kein Japanisch ausserhalb der Klammern
- [ ] nach jedem Wort und jedem Satz wird die Bedeutung GESAGT, nicht nur im Tag
- [ ] bei Partikeln wird gesagt, was sie TUN, und kein "Auf Deutsch:" dahinter
- [ ] nur Vokabular aus `vokabular.md` plus die neuen Woerter dieser Lektion
- [ ] `check.py` ohne `--pt`: `"hart": []`
- [ ] Pruefer-Urteil: `BRAUCHBAR`
- [ ] `check.py` mit `--pt=`: `"hart": []`
- [ ] Eintrag in `lektionen/index.json`
- [ ] `vokabular.md` ergaenzt
