import dash_bootstrap_components as dbc
from dash import html

DESCRIPTION_TEXT = """
Langviz is a corpus analysis toolkit for observing useful statistics and linguistic information 
from text data... 


"""


def description_card(card_color: str):
    """Returns the 'Description' card inside the 'About' tab"""
    return dbc.Card(
        [
            dbc.CardHeader(html.H1("What is Langviz?")),
            dbc.CardBody(
                [DESCRIPTION_TEXT],
            ),
        ],
        color=card_color,
    )
