"""
This module contains code for the 'About' tab
"""

import dash_bootstrap_components as dbc
from dash import dcc, html

from . import description, get_started, links, motivation

layout = html.Div(
    [
        dbc.Stack(
            [
                description.description_card(),
                motivation.motivation_card(),
                links.links_card(),
            ],
        ),
        dbc.Stack(
            [
                get_started.get_started_card(),
            ]
        ),
    ],
    className="d-flex flex-direction-column",
)


def about_tab():
    """Returns the 'About' tab"""
    return dbc.Tab(
        layout,
        label="About",
        active_tab_class_name="fw-bold fst-italic",
        id="about-tab",
    )
