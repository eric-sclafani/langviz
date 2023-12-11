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

## Planned starting features

These are the planned features for the first usable version of this software, organized by level:

**CORPUS**

- \# of documents, sentences, tokens, types, lemmas, etc...
- Token-type ratio
- Mean, median, range # of tokens per doc
- Tfidf word cloud over whole corpus
- Topic modeling
- Part of speech information

**DOCUMENT**

- Named Entity Recognition
- Morphological parsing
- Sentiment analysis
- Part of speech information
- Sentence analysis (dependency parse knowledge graphs, sentence-specific information)

## Possible future implementations

- Possibly support multiple languages
- Corpus word search
- Bias detection
- More complex statistics
- Use co-occurrence matrices to create a graph-based interactive visualization
- User can search for specific terms across all docs?
- User can point it to a directory and can select which dataset to use
- Right now, an exception is raised when a UnicodeDecodeError happens which tells the user to preprocess their data before loading. I want to eventually improve this system to make it more user friendly
