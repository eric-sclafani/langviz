"""This module contains consolidates all four tab modules into one"""

import dash_bootstrap_components as dbc
from dash import html

from langviz.processing import Corpus

from . import about_tab, corpus_tab, document_tab


def layout(corpus: Corpus) -> dbc.Container:
    return dbc.Container(
        [
            html.H1("Langviz"),
            dbc.Tabs(
                id="main-tabs",
                active_tab="corpus-tab",  # for testing purposes
                children=[
                    about_tab.about_tab(),
                    corpus_tab.corpus_tab(corpus),
                    document_tab.document_tab(),
                ],
            ),
        ],
        fluid=True,
    )
