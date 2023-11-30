"""
This module contains text processing 
"""

from dataclasses import dataclass
from typing import List, Set

import spacy
from spacy.cli.download import download
from spacy.language import Language
from spacy.tokens import Doc, Span


@dataclass
class Document:
    """Contains attributes to be used in visualization components"""

    tokens: List[str]
    types: Set[str]
    sentences: List[Span]
    num_tokens: int
    num_types: int
    num_sentences: int
    doc: Doc

    def __repr__(self):
        return self.doc.text


def process_documents(data: List[str]) -> List[Document]:
    """Converts each text document into Document object containing useful information"""

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

    def get_sentences(spacy_doc: Doc) -> List[Span]:
        """Returns a list of all sentence objects"""
        return list(spacy_doc.sents)

    nlp = load_spacy_model("en_core_web_lg")
    nlp.max_length = 10000000
    docs = nlp.pipe(data)

    all_documents = []
    for doc in docs:
        tokens = get_token_strings(doc)
        types = set(tokens)
        sentences = get_sentences(doc)
        num_tokens = len(tokens)
        num_types = len(types)
        num_sentences = len(sentences)

        document = Document(
            tokens, types, sentences, num_tokens, num_types, num_sentences, doc
        )

        all_documents.append(document)

    return all_documents
