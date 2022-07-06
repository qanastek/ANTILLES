**People Involved**

* LABRAK Yanis (1)
* DUFOUR Richard (2)

**Affiliations**

1. LIA, Avignon University, Avignon, France.
2. LS2N, Nantes University, Nantes, France.

# ANTILLES : An Open French Linguistically Enriched Part-of-Speech Corpus

`ANTILLES` is a part-of-speech tagging corpus based on [UD_French-GSD](https://universaldependencies.org/treebanks/fr_gsd/index.html) which was originally created in 2015 and is based on the [universal dependency treebank v2.0](https://github.com/ryanmcd/uni-dep-tb).

Originally, the corpus consists of 400,399 words (16,341 sentences) and had 17 different classes. Now, after applying our tags augmentation script `transform.py`, we obtain 60 different classes which add semantic information such as: the gender, number, mood, person, tense or verb form given in the different CoNLL-03 fields from the original corpus.

We based our tags on the level of details given by the [LIA_TAGG](http://pageperso.lif.univ-mrs.fr/frederic.bechet/download.html) statistical POS tagger written by [Frédéric Béchet](http://pageperso.lif.univ-mrs.fr/frederic.bechet/index-english.html) in 2001.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## Demo: How to use in Flair

```python
from flair.datasets import UniversalDependenciesCorpus

corpus: Corpus = UniversalDependenciesCorpus(
    data_folder='ANTILLES',
    train_file="train.conllu",
    test_file="test.conllu",
    dev_file="dev.conllu"
)
```

## Statistics

|                    | Train  |  Dev   | Test  |
|:------------------:|:------:|:------:|:-----:|
|       # Docs       | 14 449 | 1 476  |  416  |
| Avg # Tokens / Doc | 24.54  | 24.19  | 24.08 |

## Original Tags from UD_FRENCH-GSD

```plain
PRON VERB SCONJ ADP CCONJ DET NOUN ADJ AUX ADV PUNCT PROPN NUM SYM PART X INTJ
```

## New Tags based on LIA_TAGG

| Abbreviation | Description | Examples | # tokens |
|:--------:|:--------:|:--------:|:--------:|
| PREP | Preposition | de | 63 738 |
| AUX | Auxiliary Verb | est | 12 886 |
| ADV | Adverb | toujours | 14 969 |
| COSUB | Subordinating conjunction | que | 3 007 |
| COCO | Coordinating Conjunction | et | 10 102 |
| PART | Demonstrative particle | -t | 93 |
| PRON | Pronoun | qui ce quoi | 667 |
| PDEMMS | Singular Masculine Demonstrative Pronoun | ce | 1 950 |
| PDEMMP | Plurial Masculine Demonstrative Pronoun | ceux | 108 |
| PDEMFS | Singular Feminine Demonstrative Pronoun | cette | 1 004 |
| PDEMFP | Plurial Feminine Demonstrative Pronoun | celles | 53 |
| PINDMS | Singular Masculine Indefinite Pronoun | tout | 961 |
| PINDMP | Plurial Masculine Indefinite Pronoun | autres | 89 |
| PINDFS | Singular Feminine Indefinite Pronoun | chacune | 136 |
| PINDFP | Plurial Feminine Indefinite Pronoun | certaines | 31 |
| PROPN | Proper noun | houston | 22 135 |
| XFAMIL | Last name | levy | 6 449 |
| NUM | Numerical Adjectives | trentaine vingtaine | 67 |
| DINTMS | Masculine Numerical Adjectives | un | 4 254 |
| DINTFS | Feminine Numerical Adjectives | une | 3 543 |
| PPOBJMS | Singular Masculine Pronoun complements of objects | le lui | 1 425 |
| PPOBJMP | Plurial Masculine Pronoun complements of objects | eux y | 212 |
| PPOBJFS | Singular Feminine Pronoun complements of objects | moi la | 358 |
| PPOBJFP | Plurial Feminine Pronoun complements of objects | en y | 70 |
| PPER1S | Personal Pronoun First Person Singular | je | 571 |
| PPER2S | Personal Pronoun Second Person Singular | tu | 19 |
| PPER3MS | Personal Pronoun Third Person Masculine Singular | il | 3 938 |
| PPER3MP | Personal Pronoun Third Person Masculine Plurial | ils | 513 |
| PPER3FS | Personal Pronoun Third Person Feminine Singular | elle | 992 |
| PPER3FP | Personal Pronoun Third Person Feminine Plurial | elles | 121 |
| PREFS | Reflexive Pronouns First Person of Singular | me m' | 120 |
| PREF | Reflexive Pronouns Third Person of Singular | se s' | 2 337 |
| PREFP | Reflexive Pronouns First / Second Person of Plurial | nous vous | 686 |
| VERB | Verb | obtient | 21 131 |
| VPPMS | Singular Masculine Past Participle Verb | formulé | 6 275 |
| VPPMP | Plurial Masculine Past Participle Verb | classés | 1 352 |
| VPPFS | Singular Feminine Past Participle Verb | appelée | 2 434 |
| VPPFP | Plurial Feminine Past Participle Verb | sanctionnées | 813 |
| VPPRE | Present participle | étant | 2 |
| DET | Determinant | les l' | 25 206 |
| DETMS | Singular Masculine Determinant | les | 15 444 |
| DETFS | Singular Feminine Determinant | la | 10 978 |
| ADJ | Adjective | capable sérieux | 1 075 |
| ADJMS | Singular Masculine Adjective | grand important | 8 338 |
| ADJMP | Plurial Masculine Adjective | grands petits | 3 274 |
| ADJFS | Singular Feminine Adjective | française petite | 8 004 |
| ADJFP | Plurial Feminine Adjective | légères petites | 3 041 |
| NOUN | Noun | temps | 1 389 |
| NMS | Singular Masculine Noun | drapeau | 29 698 |
| NMP | Plurial Masculine Noun | journalistes | 10 882 |
| NFS | Singular Feminine Noun | tête | 25 414 |
| NFP | Plurial Feminine Noun | ondes | 7 448 |
| PREL | Relative Pronoun | qui dont | 2 976 |
| PRELMS | Singular Masculine Relative Pronoun | lequel | 94 |
| PRELMP | Plurial Masculine Relative Pronoun | lesquels | 29 |
| PRELFS | Singular Feminine Relative Pronoun | laquelle | 70 |
| PRELFP | Plurial Feminine Relative Pronoun | lesquelles | 25 |
| PINTFS | Singular Feminine Interrogative Pronoun | laquelle | 3 |
| INTJ | Interjection | merci bref | 75 |
| CHIF | Numbers | 1979 10 | 10 417 |
| SYM | Symbol | € % | 705 |
| YPFOR | Endpoint | . | 15 088 |
| PUNCT | Ponctuation | : , | 28 918 |
| MOTINC | Unknown words | Technology Lady | 2 022 |
| X | Typos & others | sfeir 3D statu | 175 |

## BibTeX Citations

Please cite the following paper when using this model.

ANTILLES extended corpus:

```latex
@inproceedings{labrak:hal-03696042,
  TITLE = {{ANTILLES: An Open French Linguistically Enriched Part-of-Speech Corpus}},
  AUTHOR = {Labrak, Yanis and Dufour, Richard},
  URL = {https://hal.archives-ouvertes.fr/hal-03696042},
  BOOKTITLE = {{25th International Conference on Text, Speech and Dialogue (TSD)}},
  ADDRESS = {Brno, Czech Republic},
  PUBLISHER = {{Springer}},
  YEAR = {2022},
  MONTH = Sep,
  KEYWORDS = {Part-of-speech corpus ; POS tagging ; Open tools ; Word embeddings ; Bi-LSTM ; CRF ; Transformers},
  PDF = {https://hal.archives-ouvertes.fr/hal-03696042/file/ANTILLES_A_freNch_linguisTIcaLLy_Enriched_part_of_Speech_corpus.pdf},
  HAL_ID = {hal-03696042},
  HAL_VERSION = {v1},
}
```

UD_French-GSD corpus:

```latex
@misc{
    universaldependencies,
    title={UniversalDependencies/UD_French-GSD},
    url={https://github.com/UniversalDependencies/UD_French-GSD}, journal={GitHub},
    author={UniversalDependencies}
}
```

LIA TAGG:

```latex
@techreport{LIA_TAGG,
  author = {Frédéric Béchet},
  title = {LIA_TAGG: a statistical POS tagger + syntactic bracketer},
  institution = {Aix-Marseille University & CNRS},
  year = {2001}
}
```
