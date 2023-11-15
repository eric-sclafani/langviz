"""
This module contains code for the 'About' tab
"""

import dash_bootstrap_components as dbc
from dash import dcc, html

from . import description, links, motivation


def _about_tab_layout():
    return html.Div(
        [
            dbc.Stack(
                [
                    description.description_card(),
                    motivation.motivation_card(),
                    links.links_card(),
                ],
            )
        ],
        className="d-flex flex-direction-column",
    )


def about_tab():
    """Returns the 'About' tab"""
    return dbc.Tab(
        _about_tab_layout(),
        label="About",
        active_tab_class_name="fw-bold fst-italic",
        id="about-tab",
    )
