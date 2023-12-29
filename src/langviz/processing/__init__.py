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

    spacy_doc: Doc
    doc_id: str

    def __str__(self):
        return self.spacy_doc.text

    @property
    def tokens(self) -> List[str]:
        return self.spacy_doc._.tokens

    @property
    def types(self) -> Set[str]:
        return self.spacy_doc._.types

    @property
    def vector(self) -> np.ndarray:
        return np.array(self.spacy_doc.vector)

    @property
    def sentences(self) -> List[Span]:
        return list(self.spacy_doc.sents)

    @property
    def named_entities(self) -> List[Dict[str, str]]:
        return self.spacy_doc._.entities


@dataclass
class Corpus:

    """
    Encapsulates all processed documents under one class
    and exposes functions for getting corpus-level information
    """

    documents: List[Document]

    @property
    def sentence_counts(self) -> List[int]:
        return [len(doc.sentences) for doc in self.documents]

    @property
    def token_counts(self) -> List[int]:
        return [len(doc.tokens) for doc in self.documents]

    @property
    def type_counts(self) -> List[int]:
        return [len(doc.types) for doc in self.documents]

    @property
    def total_types(self) -> int:
        all_types = {token_type for doc in self.documents for token_type in doc.types}
        return len(all_types)

    @property
    def document_ids(self) -> List[str]:
        return [doc.doc_id for doc in self.documents]

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
        all_documents.append(Document(doc, doc_id))

    corpus = Corpus(all_documents)
    return corpus
