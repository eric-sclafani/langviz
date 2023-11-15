"""This module contains consolidates all four tab modules into one"""

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

from . import about, corpus, document, sentence

# def maybe_load_dataset(input_path: str) -> Union[pd.DataFrame, None]:
#     """Attempts to load data from path into a Dataframe. Returns None if unsuccessful"""
#     try:
#         if input_path.endswith(".csv"):
#             return pd.read_csv(input_path)
#         if input_path.endswith(".json") or input_path.endswith(".jsonl"):
#             return pd.read_json(input_path, orient="records")
#     except FileNotFoundError:
#         return None


def layout(data: pd.DataFrame) -> dbc.Container:
    return dbc.Container(
        [
            html.H1("Langviz"),
            dbc.Tabs(
                [
                    about.about_tab(),
                    corpus.corpus_tab(),
                    document.document_tab(),
                    sentence.sentence_tab(),
                ]
            ),
        ],
        fluid=True,
    )
