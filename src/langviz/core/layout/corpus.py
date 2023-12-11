"""This module contains the code for the 'Corpus' tab"""
import os
from dataclasses import dataclass
from typing import List, Set
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import umap
from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from bertopic.vectorizers import ClassTfidfTransformer
from dash import dcc, html
from dash.dash_table import DataTable
from sentence_transformers import SentenceTransformer

from langviz.processing import Document

os.environ["TOKENIZERS_PARALLELISM"] = "false"


@dataclass
class Corpus:
    documents: List[Document]

    @property
    def sentences(self) -> list[str]:
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


### COMPONENT FUNCTIONS ###


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
            "width": "650px",
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
            "width": "500px",
        },
    )


def document_scatter_plot(corpus: Corpus) -> dcc.Graph:
    """"""

    def get_document_vectors() -> np.ndarray:
        """Returns a 2D array of all document word2vec vectors"""
        return np.vstack(
            [np.array(document.doc.vector) for document in corpus.documents]
        )

    def get_doc_ids() -> List[str]:
        return [document.doc_id for document in corpus.documents]

    def reduce_to_2d(matrix: np.ndarray) -> np.ndarray:
        reducer = umap.UMAP()
        return reducer.fit_transform(matrix)  # type: ignore

    doc_matrix = get_document_vectors()
    doc_ids = get_doc_ids()
    reduced_matrix = reduce_to_2d(doc_matrix)

    fig = go.Figure(
        go.Scatter(
            mode="markers",
            x=reduced_matrix[:, 0],
            y=reduced_matrix[:, 1],
            text=doc_ids,
        )
    )
    fig.update_layout(
        title="Document Vectors in 2D Space",
        title_x=0.5,
        title_y=0.85,
        xaxis=go.layout.XAxis(showticklabels=False),
        yaxis=go.layout.YAxis(showticklabels=False),
    )

    return dcc.Graph(figure=fig, className="doc-scatter-plot")


def corpus_topics(corpus: Corpus):
    all_text_documents = [document.doc.text for document in corpus.documents]

    representation_model = KeyBERTInspired()
    ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)

    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = sentence_model.encode(all_text_documents, show_progress_bar=False)

    topic_model = BERTopic(
        ctfidf_model=ctfidf_model, representation_model=representation_model
    )
    topics, topic_probs = topic_model.fit_transform(all_text_documents)

    fig = topic_model.visualize_documents(
        docs=all_text_documents,
        embeddings=embeddings,  # type: ignore
        width=700,
        height=400,
    )

    fig.update_traces(hovertext=[document.doc_id for document in corpus.documents])

    return dcc.Graph(figure=fig)


### LAYOUT FUNCTIONS ###


def stats_tables(corpus: Corpus) -> dbc.Stack:
    return dbc.Stack(
        [
            corpus_stats_per_doc_table(corpus),
            corpus_stats_total_table(corpus),
        ],
        class_name="top-row-stack",
    )


def layout(data: List[Document]):
    corpus = Corpus(data)
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(stats_tables(corpus)),
                    dbc.Col(corpus_topics(corpus)),
                ],
                class_name="d-flex flex-nowrap",
            ),
            dbc.Row([]),
        ],
    )


def corpus_tab(data: List[Document]):
    return dbc.Tab(
        layout(data),
        label="Corpus",
        activeTabClassName="fw-bold fst-italic",
        id="corpus-tab",
        tab_id="corpus-tab",
    )
