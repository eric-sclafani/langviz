"""
This module contains text processing 
"""

from dataclasses import dataclass
from typing import Iterator, List, Set

import numpy as np
import pandas as pd
from spacy.tokens import Doc, Span

from langviz.processing.load_spacy import load_spacy_model
from langviz.utils import timer


@dataclass
class Document:
    doc_id: str
    text: str
    vector: np.ndarray
    tokens: Iterator[str]
    types: Set[str]
    sentences: Iterator[Span]
    named_entities: pd.DataFrame

    def __repr__(self):
        return self.text

    @property
    def token_count(self) -> int:
        return len(list(self.tokens))

    @property
    def type_count(self) -> int:
        return len(self.types)

    @property
    def sentence_count(self) -> int:
        return len(list(self.sentences))

    @classmethod
    def from_spacy_document(cls, doc: Doc, doc_id: str):
        text = doc.text
        vector = np.array(doc.vector)
        tokens = doc._.tokens
        types = doc._.types
        sentences = doc.sents
        named_entities = doc._.entities_df
        return cls(doc_id, text, vector, tokens, types, sentences, named_entities)


@dataclass
class Corpus:
    _documents: List[Document]

    @property
    def documents(self):
        return self._documents


# TODO: break into smaller functions
@timer
def process_documents(
    data: List[str], doc_ids: List[str], n_process: int
) -> List[Document]:
    """Converts each text document into Document object containing useful information"""

    nlp = load_spacy_model("en_core_web_lg")
    docs = nlp.pipe(data, n_process=n_process)

    all_documents = []
    for doc, doc_id in zip(docs, doc_ids):
        all_documents.append(Document.from_spacy_document(doc, doc_id))

    return all_documents
