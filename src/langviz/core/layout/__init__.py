"""This module contains consolidates all four tab modules into one"""

from typing import List

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

from langviz.processing import Document

from . import about, corpus, document


def layout(data: List[Document]) -> dbc.Container:
    return dbc.Container(
        [
            html.H1("Langviz"),
            dbc.Tabs(
                id="main-tabs",
                active_tab="corpus-tab",  # for testing purposes
                children=[
                    about.about_tab(),
                    corpus.corpus_tab(),
                    document.document_tab(),
                ],
            ),
        ],
        fluid=True,
    )
