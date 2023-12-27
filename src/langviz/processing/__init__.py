"""
This module contains functions and classes for text processing 
"""

from dataclasses import dataclass
from typing import Dict, Iterator, List, Set

import numpy as np
import pandas as pd
from spacy.tokens import Doc, Span

from langviz.utils import timer

from .load_spacy import load_spacy_model


@dataclass
class Document:
    """Class representing extracted informaton from spaCy docs"""

    doc_id: str
    text: str
    vector: np.ndarray
    tokens: List[str]
    types: Set[str]
    sentences: List[Span]
    named_entities: List[Dict[str, str]]

    def __repr__(self):
        return self.text

    @property
    def token_count(self) -> int:
        """Returns the document token count"""
        return len(self.tokens)

    @property
    def type_count(self) -> int:
        """Returns the document type count"""
        return len(self.types)

    @property
    def sentence_count(self) -> int:
        """Returns the document sentence count"""
        return len(self.sentences)

    @classmethod
    def from_spacy_document(cls, doc: Doc, doc_id: str):
        """Constructs a Document object given a spaCy Doc object"""
        text = doc.text
        vector = np.array(doc.vector)
        tokens = doc._.tokens
        types = doc._.types
        sentences = list(doc.sents)
        named_entities = doc._.entities
        return cls(doc_id, text, vector, tokens, types, sentences, named_entities)


@dataclass
class Corpus:

    """
    Encapsulates all processed documents under one class
    and exposes functions for getting corpus-level information
    """

    documents: List[Document]

    @property
    def sentence_counts(self) -> List[int]:
        return [document.sentence_count for document in self.documents]

    @property
    def token_counts(self) -> List[int]:
        return [document.token_count for document in self.documents]

    @property
    def type_counts(self) -> List[int]:
        return [document.type_count for document in self.documents]

    @property
    def total_types(self) -> int:
        all_types = {
            token_type for document in self.documents for token_type in document.types
        }
        return len(all_types)

    @property
    def document_ids(self) -> List[str]:
        return [document.doc_id for document in self.documents]

    @property
    def named_entities_df(self) -> pd.DataFrame:
        all_entities = []
        for doc in self.documents:
            all_entities.extend(doc.named_entities)

        return pd.DataFrame(all_entities)


@timer
def process_documents(data: List[str], doc_ids: List[str], n_process: int) -> Corpus:
    """Processes all documents into a Corpus object"""

    nlp = load_spacy_model("en_core_web_lg")
    docs = nlp.pipe(data, n_process=n_process)

    all_documents = []
    for doc, doc_id in zip(docs, doc_ids):
        all_documents.append(Document.from_spacy_document(doc, doc_id))

    corpus = Corpus(all_documents)
    return corpus
