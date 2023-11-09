"""
This module contains code for the 'Getting started' tab
"""

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table, dcc, html

ABOUT_PAGE_CARD_COLOR = "#E8E8E8"
ACTIVE_TAB_CLASS_NAME = "fw-bold fst-italic"


_layout = html.Div(
    [
        dbc.Stack(
            [
                html.H2("To get started, upload your data below"),
                html.Div(id="test-div"),
            ]
        )
    ]
)


get_started_tab = dbc.Tab(
    _layout,
    label="Get started",
    active_tab_class_name=ACTIVE_TAB_CLASS_NAME,
    id="get-started-tab",
)
