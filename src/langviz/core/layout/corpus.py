from dataclasses import dataclass
from typing import List

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table

from langviz.processing import Document


@dataclass
class Corpus:
    _documents: List[Document]

    def documents(self) -> List[str]:
        """Returns a list of all document strings"""
        return [document.doc.text for document in self._documents]

    def tokens(self) -> List[str]:
        """Returns a list of all token strings in corpus"""
        all_tokens = []
        for document in self._documents:
            all_tokens.extend(document.tokens)
        return all_tokens

    def document_count(self):
        return len(self._documents)

    def sentence_count(self):
        return sum(document.num_sentences for document in self._documents)

    def token_count(self):
        return sum(document.num_tokens for document in self._documents)


def corpus_tab():
    return dbc.Tab(
        label="Corpus",
        activeTabClassName="fw-bold fst-italic",
        id="corpus-tab",
        tab_id="corpus-tab",
    )
