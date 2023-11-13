from typing import Union

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

ACTIVE_TAB_CLASS_NAME = "fw-bold fst-italic"
ABOUT_PAGE_CARD_COLOR = "#E8E8E8"


def maybe_load_dataset(input_path: str) -> Union[pd.DataFrame, None]:
    """Attempts to load data from path into a Dataframe. Returns None if unsuccessful"""
    try:
        if input_path.endswith(".csv"):
            return pd.read_csv(input_path)
        if input_path.endswith(".json"):
            return pd.read_json(input_path, orient="records")
    except FileNotFoundError:
        return None


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


def layout(input_path: str):
    return dbc.Container(
        [
            html.H1("Langviz"),
            tabs,
        ],
        fluid=True,
    )
