from typing import Union

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

from .components.tabs.about import about_tab

ACTIVE_TAB_CLASS_NAME = "fw-bold fst-italic"
ABOUT_PAGE_CARD_COLOR = "#E8E8E8"

# will be added to components.tabs.__init__.py
tabs = dbc.Tabs(
    [
        about_tab,
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
        ),
    ],
    className="main-tabs",
)


def layout(data: Union[pd.DataFrame, None]):
    return dbc.Container(
        [
            html.H1("Langviz"),
            tabs,
        ],
        fluid=True,
    )
