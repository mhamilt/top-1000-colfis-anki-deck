# Top 1000 CoLFIS AnkiDeck
Top 1000 most common Italian words from the [CoLFIS corpus](https://linguistica.sns.it/CoLFIS/Download_eng.htm) as an AnkiDeck

## About

This was constructed as the readily available lists of "Top 1000 words" were without citation.

Two sources were used for generating lists.

- [CoLFIS](https://www.istc.cnr.it/en/grouppage/colfis)
- [Wiktionary:Frequency lists/Italian1000](https://en.m.wiktionary.org/wiki/Wiktionary:Frequency_lists/Italian1000)

The deck was constructed using the [Genanki](https://github.com/kerrickstaley/genanki) package from a filtered version of the first 1000 words in the CoLFIS corpus and the Wiktionary list with a few filters placed on it.

Given the source of CoLFIS is periodicals, literature and newspapers the vocabulary skews to more formal language. The Wiktionary list on the other hand skews towards the informal with subtitle data used as a source. As such, the Wiktionary sourced deck perhaps better reflects common spoken italian while the CoLFIS decks reflect written italian.

The output is three Anki Decks:

- _Top 1000 Italian words by CoLFIS Freq_
- _Top 1000 Italian words by CoLFIS Rank_
- _Wiktionary Top '1000' Italian Words_

The audio is generated using the internal macOS voice assistant (Premium version of italian "Emma").

### ColFIS

The ColFIS set has two useful measurements of frequency

- *Frequency*: total absolute frequency of the form or lemma in the corpus.
- *Rango*: usage rank of the form or lemma compared to usage in the total corpus.

A different deck was generated for each, though the crossover is fairly large.

The Python script to filter the corpus, a `.tsv` version of which is also in the repository.

The source of the corpus [Scuola Normal Superiore](https://linguistica.sns.it/CoLFIS/Lemmario.htm) use the following grammatical categories

```
B	Avverbio						C	Congiunzione
E	Nome proprio					G	Aggettivo
I	Interiezione					K	Punteggiatura
N	Pronome							NU	Numerale
P	Preposizione					R	Articolo
S	Sostantivo						TC	Tempo composto di un verbo
V	Verbo							VA	Verbo ausiliare
X	Lingua non ben identificata		Z	Simbolo
@	Parola sintagmatica
```

#### Filtering Process

The corpus was ingested as a `pandas` data frame, ordered by rank (_Rango_) and filtered for any: 
- punctuation `K`
- Proper nouns `E`
- Symbols `Z`
- Numerals (i.e. regex `\d+`)

Symbols containing hyphens (`-`) were also excluded as these were typically incomplete contractions of preposition and articles.

Some contracted infinitives† were removed (e.g. poter, ander &c.) I felt they duplicated a little too much.

### Wiktionary

The Wiktionary set has had a few entries removed, namely

- interjections
- non-italian words
- duplicates

The set also contains some anomalies, for instance the entry:

```csv
cosi	252	coso
```

It is unlikely that the plural for the seldom usage masculine for thing (_coso_) appeared but the _così_ did not. This entry was changed to _così_ by hand.

† _ not the correct term, come at me linguists!