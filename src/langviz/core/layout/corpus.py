"""This module contains the code for the 'Corpus' tab"""
import os
from dataclasses import dataclass
from typing import List

import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
import umap
from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from bertopic.vectorizers import ClassTfidfTransformer
from dash import dcc, html
from dash.dash_table import DataTable
from sentence_transformers import SentenceTransformer

from langviz.processing import Document
from langviz.utils import timer

os.environ["TOKENIZERS_PARALLELISM"] = "false"


@dataclass
class Corpus:
    documents: List[Document]

    @property
    def sentence_counts(self) -> List[int]:
        return [len(document.sentences) for document in self.documents]

    @property
    def token_counts(self) -> List[int]:
        return [len(document.tokens) for document in self.documents]

    @property
    def type_counts(self) -> List[int]:
        return [len(document.types) for document in self.documents]

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
        entities = [
            {"text": ent.text, "label": ent.label_}
            for document in self.documents
            for ent in document.doc.ents
        ]
        return pd.DataFrame(entities)


### COMPONENT FUNCTIONS ###


@timer
def document_stats_overview_table(corpus: Corpus) -> DataTable:
    """Returns a table showing the per-document corpus stats"""
    data = pd.DataFrame(
        {
            "Document ID": corpus.document_ids,
            "Sentences": corpus.sentence_counts,
            "Tokens": corpus.token_counts,
            "Types": corpus.type_counts,
        },
    )
    columns = [{"name": col_name, "id": col_name} for col_name in data.columns]
    return DataTable(
        id="document-stats-overview-table",
        data=data.to_dict("records"),
        columns=columns,
        page_size=100,
        fixed_rows={"headers": True},
        style_cell={"textAlign": "left"},
        style_table={
            "width": "650px",
            "height": "300px",
            "overflowY": "auto",
        },
    )


@timer
def corpus_stats_list(corpus: Corpus) -> dbc.ListGroup:
    def make_list_item(text: str, calculation) -> dbc.ListGroupItem:
        return dbc.ListGroupItem(
            [
                html.B(text),
                f": {calculation}",
            ],
            class_name="p-0",
        )

    return dbc.ListGroup(
        [
            make_list_item("Total documents", len(corpus.documents)),
            make_list_item("Total sentences", sum(corpus.sentence_counts)),
            make_list_item("Total tokens", sum(corpus.token_counts)),
            make_list_item("Total types", corpus.total_types),
            make_list_item("Mean sentence count", int(np.mean(corpus.sentence_counts))),
            make_list_item(
                "Median sentence count", int(np.median(corpus.sentence_counts))
            ),
            make_list_item(
                "Range of sentence counts",
                (np.min(corpus.sentence_counts), np.max(corpus.sentence_counts)),
            ),
            make_list_item("Mean token count", int(np.mean(corpus.token_counts))),
            make_list_item("Median token count", int(np.median(corpus.token_counts))),
            make_list_item(
                "Range of token counts",
                (np.min(corpus.token_counts), np.max(corpus.token_counts)),
            ),
        ],
    )


# eventually: add a note saying umap is stochastic, so topics will
# change for each code run (not drastically though)
# also: maybe dont use sentencetransformers, use spacy vectors for this
@timer
def corpus_topics(corpus: Corpus) -> dcc.Graph:
    """
    **Heavy WIP**

    Performs topic modeling over corpus and returns a
    scatterplot where documents are clustered by their topic
    """
    all_text_documents = [document.doc.text for document in corpus.documents]

    representation_model = KeyBERTInspired()
    ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)

    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = sentence_model.encode(all_text_documents, show_progress_bar=False)

    topic_model = BERTopic(
        ctfidf_model=ctfidf_model,
        representation_model=representation_model,
        embedding_model=sentence_model,
        calculate_probabilities=False,
    )

    topic_model.fit(documents=all_text_documents, embeddings=embeddings)  # type:ignore
    reduced_embeddings = umap.UMAP(
        n_neighbors=10, min_dist=0.0, metric="cosine"
    ).fit_transform(embeddings)

    fig = topic_model.visualize_documents(
        docs=all_text_documents,
        reduced_embeddings=reduced_embeddings,  # type: ignore
        # width=700,
        height=400,
    )

    return dcc.Graph(figure=fig)


@timer
def named_entity_histogram(corpus: Corpus) -> dcc.Graph:
    fig = px.histogram(
        corpus.named_entities_df,
        x="label",
        color="label",
        title="Named Entity Frequencies",
    )
    fig.update_layout(
        xaxis={"categoryorder": "total descending"},
        xaxis_title="Named Entity Labels",
        yaxis_title="Frequency",
        showlegend=False,
        title_x=0.5,
    )
    return dcc.Graph(figure=fig, id="ner-histogram")


def named_entity_json_storage(corpus: Corpus):
    """
    Retrieves the jsonified named entity dataframe and stores it in
    a dcc.Store component to be used by the named entity list callback.
    """
    json_data = corpus.named_entities_df.to_json(orient="records")
    return dcc.Store(
        data=json_data,
        id="named-entity-json-storage",
        storage_type="session",
    )


def named_entity_list():
    """
    Returns the named entity table div for the named entity table callback
    to insert either a placeholder component or the table of named entity texts
    """
    return html.Div(id="named-entity-list")


### LAYOUT FUNCTIONS ###


def layout(data: List[Document]):
    corpus = Corpus(data)
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(document_stats_overview_table(corpus)),
                    dbc.Col(corpus_stats_list(corpus)),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(named_entity_histogram(corpus)),
                    named_entity_json_storage(corpus),
                    dbc.Col(named_entity_list()),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(corpus_topics(corpus)),
                ]
            ),
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
