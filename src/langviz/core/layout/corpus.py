"""This module contains the code for the 'Corpus' tab"""
from dataclasses import dataclass
from typing import List, Set

import dash_bootstrap_components as dbc
import pandas as pd
from dash.dash_table import DataTable

from langviz.processing import Document


@dataclass
class Corpus:
    _documents: List[Document]

    @property
    def documents(self) -> List[str]:
        """Returns a list of all document strings"""
        return [document.doc.text for document in self._documents]

    @property
    def tokens(self) -> List[str]:
        """Returns a list of all token strings in corpus"""
        all_tokens = []
        for document in self._documents:
            all_tokens.extend(document.tokens)
        return all_tokens

    @property
    def document_count(self):
        return len(self._documents)

    @property
    def total_sentence_count(self):
        return sum(document.num_sentences for document in self._documents)

    @property
    def total_token_count(self):
        return sum(document.num_tokens for document in self._documents)


def corpus_stats_table(corpus: Corpus) -> DataTable:
    data = pd.DataFrame(
        {
            "Total # of documents": [corpus.document_count],
            "Total # sentences": [corpus.total_sentence_count],
            "Total # of tokens": [corpus.total_token_count],
        },
    )
    columns = [{"name": col_name, "id": col_name} for col_name in data.columns]
    return DataTable(
        id="corpus-stats-table",
        columns=columns,
        data=data.to_dict("records"),
    )


def layout(data: List[Document]):
    corpus = Corpus(data)
    return dbc.Stack(
        [
            corpus_stats_table(corpus),
        ]
    )


def corpus_tab(data: List[Document]):
    return dbc.Tab(
        layout(data),
        label="Corpus",
        activeTabClassName="fw-bold fst-italic",
        id="corpus-tab",
        tab_id="corpus-tab",
    )
