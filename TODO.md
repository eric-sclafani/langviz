# TODO

This document contains items on the immediate horizon. Check the README for a list of implemented and planned features.

---

## General

- Add status update terminal messages

## Optimization

- Caching: for each given path, Langviz will cache all calculations, so when the use provides a path langiz has seen already, it will
  just load the cached data. This means the first load of any medium to large sized dataset will take longer, but after that, it SHOULD
  take significantly less time to load that data. If the user provides the same path but the data has been changed (i.e. documents added, subtracted),
  they will have to use a "--reset_cache" flag to recalculate

- Experiment with spaCy model sizes, processing time VS accuracy

- Bertopic: instead of using sentence transformers, maybe use spaCy vectors since they're already generated
-
- Make each component non-blocking: the application shouldn't have to wait for each component to finish,
  it will instead show a loading bar for each. `dcc.Loading` may take care of this, otherwise will need to use asynchronous functions

## Debugging

- Debug document frequency issues (<10 documents, bertopic acts up. Below idea will solve this issue)
- Make it so if a components fails to complete, it will just show an error in that region of the app, instead of throwing an exception
