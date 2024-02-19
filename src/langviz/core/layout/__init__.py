"""This module contains consolidates all four tab modules into one"""

import dash_bootstrap_components as dbc
from dash import html

from langviz.processing import Corpus

from . import corpus_tab, document_tab, start_tab


def layout(config) -> dbc.Container:
    return dbc.Container(
        [
            html.H1("Langviz"),
            dbc.Tabs(
                id="main-tabs",
                active_tab="start-tab",
                children=[
                    start_tab.start_tab(config),
                    # corpus_tab.corpus_tab(corpus),
                    # document_tab.document_tab(),
                ],
            ),
        ],
        fluid=True,
    )
