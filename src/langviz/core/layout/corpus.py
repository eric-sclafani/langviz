"""This module contains the code for the 'Corpus' tab"""
import os
from dataclasses import dataclass
from typing import List, Set

import dash_bootstrap_components as dbc
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

    @property
    def named_entities_df(self) -> pd.DataFrame:
        entities = [
            {"text": ent.text, "label": ent.label_}
            for document in self.documents
            for ent in document.doc.ents
        ]
        return pd.DataFrame(entities)


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


# eventually: add a note saying umap is stochastic, so topics will
# change for each code run (not drastically though)
# also: maybe dont use sentencetransformers, use spacy vectors for this
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


# replace Div with dcc.Store??
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


def stats_tables(corpus: Corpus) -> dbc.Stack:
    return dbc.Stack(
        [
            corpus_stats_per_doc_table(corpus),
            corpus_stats_total_table(corpus),
        ],
        class_name="stats-tables",
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
            ),
            dbc.Row(
                [
                    dbc.Col(named_entity_histogram(corpus)),
                    named_entity_json_storage(corpus),
                    dbc.Col(named_entity_list()),
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
