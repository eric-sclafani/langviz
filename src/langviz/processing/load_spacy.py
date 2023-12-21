"""
This module contains code for creating the spaCy NLP object with custom extentions
"""

from typing import Callable, Dict, List, Set

import spacy
from spacy.cli.download import download
from spacy.language import Language
from spacy.tokens import Doc

### GETTERS


def _get_tokens(doc: Doc) -> List[str]:
    return [token.text for token in doc]


def _get_types(doc: Doc) -> Set[str]:
    return set(token.text for token in doc)


def _get_entities(doc: Doc) -> List[Dict[str, str]]:
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]


# EXTENSIONS

CUSTOM_EXTENSIONS = {
    ("tokens", _get_tokens),
    ("types", _get_types),
    ("entities", _get_entities),
}


def _set_spacy_extension(name: str, function: Callable) -> None:
    """
    Turns a given function into a spaCy extenstion accessed via a given name.
    Updates the global state of the spaCy Doc object
    """
    if not Doc.has_extension(name):
        Doc.set_extension(name, getter=function)


def _apply_custom_extensions() -> None:
    """Adds new extentions to the spaCy Doc object"""

    for name, function in CUSTOM_EXTENSIONS:
        _set_spacy_extension(name, function)


# TODO: add support for custom models
def load_spacy_model(model: str) -> Language:
    """
    Attempts to load given spaCy model and apply custom extentions.
    Will try to download model if possible and not found on system
    """
    try:
        nlp = spacy.load(model)
    except OSError:
        print(f"spaCy model '{model}' not detected. Downloading...")
        download(model)
        nlp = spacy.load(model)
    nlp.max_length = 10000000
    _apply_custom_extensions()
    return nlp
