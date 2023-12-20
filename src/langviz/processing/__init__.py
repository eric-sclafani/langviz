"""
This module contains text processing 
"""

from dataclasses import dataclass
from typing import List, Set

import spacy
from spacy.cli.download import download
from spacy.language import Language
from spacy.tokens import Doc, Span

from langviz.utils import timer


@dataclass
class Document:
    """Contains attributes to be used in visualization components"""

    doc_id: str
    tokens: List[str]
    types: Set[str]
    sentences: List[Span]
    doc: Doc

    def __repr__(self):
        return self.doc.text


# TODO: break into smaller functions


@timer
def process_documents(
    data: List[str], doc_ids: List[str], n_process: int
) -> List[Document]:
    """Converts each text document into Document object containing useful information"""

    @timer
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

    # TODO: experiment with medium and large model time
    nlp = load_spacy_model("en_core_web_lg")
    nlp.max_length = 10000000
    docs = nlp.pipe(data, n_process=n_process)

    all_documents = []
    for doc, doc_id in zip(docs, doc_ids):
        tokens = get_token_strings(doc)
        types = set(token.lower() for token in tokens)
        sentences = get_sentences(doc)

        document = Document(
            doc_id,
            tokens,
            types,
            sentences,
            doc,
        )
        all_documents.append(document)

    return all_documents
