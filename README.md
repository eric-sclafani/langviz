# Langviz

## What is Langviz?

Langviz is an open-source corpus visualization tool designed to assist with EDA with language data. Given a corpus, the application
will generate interactive visualizations that users can interact with and draw insights from.

Langiz is currently in a very early stage of development, so this README is subject to change.

## Motivation

Data EDA exists at the beginning of any machine learning pipeline. It is an essential step that grants insight into their data and highlights
notable characteristics. This process also enables people to determine if a dataset meets certain criteria and consequently whether to continue
using it in the pipeline.

Text data specifically can be more difficult to analyze because language data is not as straightforward
as a spreadsheet of numbers. Sentences often relate to other sentences in some way, sometimes spanning
long distances within a single document. Words depend on other words, again, spanning long distances.
Words can have different meanings depending on the context (word-sense disambiguation).

Tldr, in my opinion, NLP datasets need more care and consideration when exploring them.
This EDA process, however, can be tedious and time-consuming. That is where this project comes in.
It would be nice to have a one-stop shop for attaining useful statistics such as # of documents, tokens, types, sentences, etc.,
and visualizing more advanced features like named entities and dependency parses.

## Features

After providing a dataset path, the user can observe useful statistics and visualizations both
on the corpus and document levels.

**Checked features (`[x]`) are already implemented**, empty ones are not

### General

- [ ] More configuration options:
  - [ ] spacy model, can specify a certain model including custom ones
  - [ ] only use first X documents
- [ ] Multiple languages
- [ ] User can provide labels and additional visualizations will be made
- [ ] Implement more knowledge graphs because knowledge graphs are cool
- [ ]

### Corpus

- [x] Topic modeling with BERTopic
- [x] Corpus level statistics
  - [x] document/sentence/token/type counts per document
  - [x] total document/sentence/token/type count over corpus
  - [ ] mean/median/range num of tokens/sentences per document
- [x] Named entity histogram + list of all texts extracted per label

### Document

- [ ] Named entities
- [ ] Morphological information
- [ ] Sentiment
- [ ] Sentences: users can observe information about each individual sentence
  - [ ] Dependency parse knowledge graph
  - [ ] ...
- [ ] User can filter for documents that meet a condition or group of conditions
