# Vokabular — was erlaubt ist

Diese Liste fuellt den Platzhalter `{{VOKABULAR}}` in `prompts/writer.md`.

**Regel:** eine Lektion benutzt alles aus den Lektionen DAVOR plus die neuen
Woerter IHRER eigenen Zeile. Nichts darueber hinaus. Erfinde kein Japanisch.

Warum so streng: der Text wird vorgelesen. Ein unbekanntes Wort im Ohr, ohne
Seite zum Nachschlagen, bleibt einfach ein Geraeusch. Die Reihe lehrt, wie
Japanisch GEBAUT ist, nicht eine Wortliste — rund 60 Woerter bis Lektion 19
sind Absicht.

Die Bedeutung in Feld 4 muss fuer dieselbe Schreibung IMMER gleich lauten.
`check.py` bricht ab, wenn dasselbe Tag zweimal verschieden uebersetzt wird.
Nimm die Bedeutung unten woertlich.

---

## Nach Lektion 1 — は

| Japanisch | Kana | Romaji | Bedeutung |
|---|---|---|---|
| 私 | わたし | watashi | ich |
| 学生 | がくせい | gakusei | Student |
| です | です | desu | bin, ist |
| は | は | wa | Themenpartikel (gesprochen わ) |
| 日本人 | にほんじん | nihonjin | Japaner, Japanerin |
| ドイツ人 | どいつじん | doitsujin | Deutscher, Deutsche |
| 青木 | あおき | Aoki | Aoki (Name der Lehrerin) |

## Nach Lektion 2 — か

| Japanisch | Kana | Romaji | Bedeutung |
|---|---|---|---|
| か | か | ka | Fragepartikel |
| あなた | あなた | anata | du |
| はい | はい | hai | ja |
| いいえ | いいえ | iie | nein |
| 彼 | かれ | kare | er |
| 先生 | せんせい | sensei | Lehrerin, Lehrer |
| 大阪出身 | おおさかしゅっしん | oosaka shusshin | aus Osaka |

## Nach Lektion 3 — Verb am Satzende

| Japanisch | Kana | Romaji | Bedeutung |
|---|---|---|---|
| 働きます | はたらきます | hatarakimasu | arbeiten |
| 飲みます | のみます | nomimasu | trinken |
| 中村 | なかむら | Nakamura | Nakamura (Name der Kollegin) |
| さん | さん | san | hoefliche Anrede |

## Nach Lektion 4 — を

| Japanisch | Kana | Romaji | Bedeutung |
|---|---|---|---|
| を | を | o | Objektpartikel (gesprochen お) |
| コーヒー | こーひー | koohii | Kaffee |
| お茶 | おちゃ | ocha | Tee |

## Nach Lektion 5 — ません

| Japanisch | Kana | Romaji | Bedeutung |
|---|---|---|---|
| ます | ます | masu | hoefliche Endung |
| ません | ません | masen | hoefliche Verneinung |
| 飲みません | のみません | nomimasen | nicht trinken |
| 働きません | はたらきません | hatarakimasen | nicht arbeiten |

---

## Geplant, noch NICHT erlaubt

Aus `PLAN.md`. Ein Wort wird erst in der Lektion erlaubt, die es einfuehrt.

| Lektion | Neu |
|---|---|
| 8 | 中村さん als Thema, さん als Regel |
| 10 | が, だれ |
| 11 | に, 行きます, 時 |
| 12 | で, 食べます, 会社 |
| 16 | 人, 会社の人 |
| 18 | だ und lockere Endungen, nur zum Wiedererkennen |

Lektionen 6, 9, 13, 14, 15, 17 und 19 bringen KEINE neuen Woerter.

## Namen

Japanische Namen stehen in Kanji: 青木, 中村. Katakana ist nur fuer
auslaendische Namen und Fremdwoerter da: ヨナス fuer Jonas, コーヒー fuer Kaffee.

Bei einem Namen ist Feld 4 der Name selbst. `check.py` erkennt das daran, dass
Feld 4 und Feld 3 gleich sind, und verlangt dann keine Uebersetzung in der
portugiesischen Fassung.

## Hinweis zu 中村

`PLAN.md` fuehrt 中村さん in Lektion 8 ein, aber Lektion 3 benutzt sie bereits
im Satz 中村さんは働きます. Der Plan ist an dieser Stelle noch nicht mit den
Texten abgeglichen. Fuer neue Lektionen gilt der Stand oben: 中村 ist ab
Lektion 3 bekannt.
