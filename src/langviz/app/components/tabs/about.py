"""
This module contains code for the 'About' tab
"""
from typing import List

import dash_bootstrap_components as dbc
from dash import dcc, html


def make_card(header_text: str, body: List, header_classname="", body_classname=""):
    """Creates a Card component"""
    return dbc.Card(
        [
            dbc.CardHeader(html.H1(header_text), className=header_classname),
            dbc.CardBody(body, className=body_classname),
        ],
        color="#E8E8E8",
    )


def make_link(link_text: str, url: str):
    """Creates an Anchor component"""
    return html.A(
        link_text,
        href=url,
        disable_n_clicks=True,
        target="_blank",
    )


### ~~~ DESCRIPTION ~~~
DESCRIPTION_TEXT = """
Langviz is a corpus analysis toolkit for observing useful statistics and linguistic information 
from text data. Designed to be used in the beginning of the NLP pipeline, this tool provides 

"""

DESCRIPTION_CARD = make_card(
    "What is Langviz",
    [DESCRIPTION_TEXT],
)

### ~~~ MOTIVATION ~~~
MOTIVATION_TEXT = """
Data EDA is an essential part of the machine learning pipeline because what data you feed into a machine
directly corresponds to the quality of the output (garbage in, garbage out). 
"""

MOTIVATION_CARD = make_card(
    "Motivation",
    [MOTIVATION_TEXT],
)


### ~~~ LINKS ~~~

LINKS_BODY = [
    html.Div("Check out these cool links", className="links-subheader"),
    make_link("Source code", "https://www.google.com/"),
    html.Br(),
    make_link("My GitHub", "https://github.com/eric-sclafani"),
]

LINKS_CARD = make_card(
    "Links!",
    LINKS_BODY,
)

### ~~~ GET STARTED ~~~
GET_STARTED_TEXT = """
To begin, if your data was loaded correctly, you should see some shit, blah blah, click button or 
apply optional text cleaning, yada yada yada...
"""

GET_STARTED_CARD = make_card(
    "Get started",
    [GET_STARTED_TEXT],
)

### TEXT CLEANING


TEXT_CLEANING_CARD = make_card(
    "Text cleaning (optional)",
    [],
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
        dbc.Stack(
            [
                GET_STARTED_CARD,
            ]
        ),
    ],
    className="d-flex flex-direction-column",
)


about_tab = dbc.Tab(
    _layout, label="About", active_tab_class_name="fw-bold fst-italic", id="about-tab"
)
