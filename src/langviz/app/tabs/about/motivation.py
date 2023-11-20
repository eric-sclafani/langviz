import dash_bootstrap_components as dbc
from dash import html

MOTIVATION_TEXT = """
Data EDA is an essential part of the machine learning pipeline because what data you feed into a machine
directly corresponds to the quality of the output (garbage in, garbage out)... 
"""


def motivation_card(card_color: str) -> dbc.Card:
    """Returns the 'Motivation' card inside the 'About' tab"""
    return dbc.Card(
        [
            dbc.CardHeader(html.H1("Motivation")),
            dbc.CardBody(
                [MOTIVATION_TEXT],
            ),
        ],
        color=card_color,
    )
