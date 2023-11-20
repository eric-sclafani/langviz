"""This module contains consolidates all four tab modules into one"""

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

from . import about, corpus, document, sentence


def layout(data: pd.Series) -> dbc.Container:
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
