"""This module contains the code for the 'Corpus' tab"""
from dataclasses import dataclass
from typing import List, Set

import dash_bootstrap_components as dbc
import pandas as pd
from dash import html
from dash.dash_table import DataTable

from langviz.processing import Document


@dataclass
class Corpus:
    documents: List[Document]

    @property
    def sentences(self) -> List[str]:
        all_sentences = []
        for document in self.documents:
            all_sentences.extend([sentence.text for sentence in document.sentences])
        return all_sentences

    @property
    def tokens(self) -> List[str]:
        """Returns a list of all token strings in corpus"""
        all_tokens = []
        for document in self.documents:
            all_tokens.extend(document.tokens)
        return all_tokens

    @property
    def types(self) -> Set[str]:
        all_types = {
            token_type for document in self.documents for token_type in document.types
        }
        return all_types

    @property
    def document_ids(self) -> List[str]:
        return [document.doc_id for document in self.documents]


def corpus_stats_per_doc_table(corpus: Corpus) -> DataTable:
    """Returns a table showing the per-document corpus stats"""
    data = pd.DataFrame(
        {
            "Document ID": corpus.document_ids,
            "Sentences": [len(document.sentences) for document in corpus.documents],
            "Tokens": [len(document.tokens) for document in corpus.documents],
            "Types": [len(document.types) for document in corpus.documents],
        },
    )
    columns = [{"name": col_name, "id": col_name} for col_name in data.columns]
    return DataTable(
        id="corpus-stats-per-doc-table",
        data=data.to_dict("records"),
        columns=columns,
        page_action="none",
        fixed_rows={"headers": True},
        style_cell={"textAlign": "left"},
        style_table={
            "width": "auto",
            "height": "300px",
            "overflowY": "auto",
        },
    )


def corpus_stats_total_table(corpus: Corpus) -> DataTable:
    """Returns a table showing the corpus stats totals"""
    data = pd.DataFrame(
        {
            "Total documents": len(corpus.documents),
            "Total sentences": len(corpus.sentences),
            "Total tokens": len(corpus.tokens),
            "Total types": len(corpus.types),
        },
        index=[0],
    )
    columns = [{"name": col_name, "id": col_name} for col_name in data.columns]
    return DataTable(
        id="corpus-stats-total-table",
        data=data.to_dict("records"),
        columns=columns,
        style_cell={"textAlign": "left"},
        style_table={
            "width": "300px",
        },
    )


def stats_tables(corpus: Corpus) -> dbc.Stack:
    return dbc.Stack(
        [
            corpus_stats_per_doc_table(corpus),
            corpus_stats_total_table(corpus),
        ],
    )


def layout(data: List[Document]):
    corpus = Corpus(data)
    return html.Div(
        [
            stats_tables(corpus),
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
