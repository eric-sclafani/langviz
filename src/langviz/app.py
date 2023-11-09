#!/usr/bin/env python3
"""
This file contains the main application code
"""

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, Input, Output, State, dcc, html

from .components.tabs.about import about_tab
from .components.tabs.get_started import get_started_tab

ACTIVE_TAB_CLASS_NAME = "fw-bold fst-italic"
ABOUT_PAGE_CARD_COLOR = "#E8E8E8"


tabs = dbc.Tabs(
    [
        about_tab,
        get_started_tab,
        dbc.Tab(
            label="Corpus",
            activeTabClassName=ACTIVE_TAB_CLASS_NAME,
            disabled=True,
            id="corpus-tab",
        ),
        dbc.Tab(
            label="Document",
            activeTabClassName=ACTIVE_TAB_CLASS_NAME,
            disabled=True,
            id="document-tab",
        ),
        dbc.Tab(
            label="Sentence",
            activeTabClassName=ACTIVE_TAB_CLASS_NAME,
            disabled=True,
            id="sentence-tab",
        ),
    ],
    className="main-tabs",
)


header = dbc.Container(
    [
        html.H1("Langviz"),
        tabs,
    ],
    fluid=True,
)


def run_app(input_path: str):
    """Runs the application"""
    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH], title="Langviz")
    app.layout = html.Div([header])
    print(input_path)
    app.run(debug=True)
