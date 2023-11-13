"""This module contains consolidates all four tab modules into one"""

import dash_bootstrap_components as dbc
import tabs
from dash import dcc, html

ACTIVE_TAB_CLASS_NAME = "fw-bold fst-italic"
ABOUT_PAGE_CARD_COLOR = "#E8E8E8"

from .tabs import about


def layout(input_path: str) -> dbc.Container:
    return dbc.Container(
        [
            html.H1("Langviz"),
            dbc.Tabs(
                [
                    about.about_tab(),
                ]
            ),
        ],
        fluid=True,
    )
