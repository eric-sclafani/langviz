"""
This module contains code for the 'About' tab
"""

import dash_bootstrap_components as dbc
from dash import html

from . import description, links, motivation

CARD_COLOR = "#E8E8E8"


def _about_tab_layout():
    return html.Div(
        [
            dbc.Stack(
                [
                    description.description_card(CARD_COLOR),
                    motivation.motivation_card(CARD_COLOR),
                    links.links_card(CARD_COLOR),
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
