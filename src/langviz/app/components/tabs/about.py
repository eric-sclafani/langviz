"""
This module contains code for the 'About' tab
"""
from typing import List

import dash_bootstrap_components as dbc
from dash import html


def make_card(header_text: str, body: List, header_classname="", body_classname=""):
    return dbc.Card(
        [
            dbc.CardHeader(html.H1(header_text), className=header_classname),
            dbc.CardBody(body, className=body_classname),
        ],
        color="#E8E8E8",
    )


def make_link(link_text: str, url: str):
    return html.A(
        link_text,
        href=url,
        disable_n_clicks=True,
        target="_blank",
    )


DESCRIPTION_TEXT = """
Langviz is a corpus analysis toolkit for observing useful statistics and linguistic information 
from text data. Designed to be used in the beginning of the NLP pipeline, this tool provides 

"""

MOTIVATION_TEXT = """
Data EDA is an essential part of the machine learning pipeline because what data you feed into a machine
directly corresponds to the quality of the output (garbage in, garbage out). 
"""

DESCRIPTION_CARD = make_card(
    "What is Langviz",
    [DESCRIPTION_TEXT],
)

MOTIVATION_CARD = make_card(
    "Motivation",
    [MOTIVATION_TEXT],
)

LINKS_CARD = make_card(
    "Links!",
    [
        html.Div("Check out these cool links", className="links-subheader"),
        make_link("Source code", "https://www.google.com/"),
        html.Br(),
        make_link("My GitHub", "https://github.com/eric-sclafani"),
    ],
)


_layout = html.Div(
    [
        dbc.Stack(
            [
                DESCRIPTION_CARD,
                MOTIVATION_CARD,
                LINKS_CARD,
            ],
        ),
    ]
)


about_tab = dbc.Tab(
    _layout, label="About", active_tab_class_name="fw-bold fst-italic", id="about-tab"
)
