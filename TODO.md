# TODO

---

# Higher priority

## Optimization

- Experiment with spaCy model sizes, processing time VS accuracy
- Bertopic: instead of using sentence transformers, maybe use spaCy vectors since they're already generated
-

# Lower priority

## Debugging

- Debug document frequency issues (<10 documents, bertopic acts up)
- Make it so if a components fails to complete, it will just show an error in that region of the app, instead of throwing an exception
