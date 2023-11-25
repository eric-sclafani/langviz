"""
This module contains functions for converting raw text into useful objects for the layout components
"""

from dataclasses import dataclass
from typing import List, Set

import pandas as pd
import spacy
from spacy.cli.download import download
from spacy.language import Language
from spacy.tokens import Doc, Span


@dataclass
class Document:
    """"""

    tokens: List[str]
    types: Set[str]
    sentences: List[Span]
    num_tokens: int
    num_types: int
    num_sentences: int
    doc: Doc


def process_documents(data: pd.Series) -> List[Document]:
    """"""

    def load_spacy_model(model: str) -> Language:
        """Attempts to load given spaCy model. Attempts to download if not found"""
        try:
            return spacy.load(model)
        except OSError:
            print(f"spaCy model '{model}' not detected. Downloading...")
            download(model)
            return spacy.load(model)

    def get_token_strings(spacy_doc: Doc) -> List[str]:
        """Returns a list of all token strings"""
        return [token.text for token in spacy_doc]

    def get_type_strings(spacy_doc: Doc) -> Set[str]:
        """Returns a set of all unique token strings"""
        return {token.text for token in spacy_doc}

    nlp = load_spacy_model("en_core_web_lg")
    docs = nlp.pipe(data)
