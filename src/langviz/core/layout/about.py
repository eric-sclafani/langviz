"""
This module contains code for the 'About' tab
"""

import dash_bootstrap_components as dbc
from dash import html


def description_card(card_color: str):
    """Returns the 'Description' card inside the 'About' tab"""

    text = """
    Langviz is a corpus analysis toolkit for observing useful statistics and linguistic information 
    from text data... """

    return dbc.Card(
        [
            dbc.CardHeader(html.H1("What is Langviz?")),
            dbc.CardBody(
                [text],
            ),
        ],
        color=card_color,
    )


def links_card(card_color: str):
    """Returns the 'Links' card inside the 'About' tab"""

    def make_link(link_text: str, url: str):
        """Creates an Anchor component"""
        return html.A(
            link_text,
            href=url,
            disable_n_clicks=True,
            target="_blank",
        )

    return dbc.Card(
        [
            dbc.CardHeader(html.H1("Links!")),
            dbc.CardBody(
                [
                    html.Div("Check out these cool links", className="links-subheader"),
                    make_link(
                        "Source code", "https://github.com/eric-sclafani/langviz"
                    ),
                    html.Br(),
                    make_link("My GitHub", "https://github.com/eric-sclafani"),
                ]
            ),
        ],
        color=card_color,
    )


def motivation_card(card_color: str) -> dbc.Card:
    """Returns the 'Motivation' card inside the 'About' tab"""

    text = """
    Data EDA is an essential part of the machine learning pipeline because what data you feed into a machine
    directly corresponds to the quality of the output (garbage in, garbage out)... 
    """

    return dbc.Card(
        [
            dbc.CardHeader(html.H1("Motivation")),
            dbc.CardBody(
                [text],
            ),
        ],
        color=card_color,
    )


def layout():
    card_color = "#E8E8E8"
    return html.Div(
        [
            dbc.Stack(
                [
                    description_card(card_color),
                    motivation_card(card_color),
                    links_card(card_color),
                ],
            )
        ],
        className="d-flex flex-direction-column",
    )


def about_tab():
    """Returns the 'About' tab"""
    return dbc.Tab(
        layout(),
        label="About",
        active_tab_class_name="fw-bold fst-italic",
        id="about-tab",
        tab_id="about-tab",
    )
