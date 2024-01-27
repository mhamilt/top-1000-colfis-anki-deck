# Top 1000 CoLFIS AnkiDeck
Top 1000 most common Italian words from the [CoLFIS corpus](https://linguistica.sns.it/CoLFIS/Download_eng.htm) as an AnkiDeck

## About

This was constructed as the readily available lists of "Top 1000 words" were without citation.

There is the [Wiktionary:Frequency lists/Italian1000](https://en.m.wiktionary.org/wiki/Wiktionary:Frequency_lists/Italian1000) but that topped out at 1000 and included a few duplicates and non-italian words.

The deck was constructed using the [Genanki](https://github.com/kerrickstaley/genanki) package from a filtered version of the first 1000 words in the CoLFIS corpus
with a few filters placed on it.

The Python script to filter the corpus, a `.tsv` version of which is also in the repository.

The source of the corpus [Scuola Normal Superiore](https://linguistica.sns.it/CoLFIS/Lemmario.htm) use the following grammatical categories

```
B	Avverbio				C	Congiunzione
E	Nome proprio				G	Aggettivo
I	Interiezione				K	Punteggiatura
N	Pronome					NU	Numerale
P	Preposizione				R	Articolo
S	Sostantivo				TC	Tempo composto di un verbo
V	Verbo					VA	Verbo ausiliare
X	Lingua non ben identificata		Z	Simbolo
@	Parola sintagmatica
```

### Filtering Process

The corpus was ingested as a `pandas` data frame, ordered by rank (_Rango_) and filtered for any punctuation `K`. Symbols containing hyphens (`-`) were also excluded as these were typically incomplete contractions of preposition and articles.
