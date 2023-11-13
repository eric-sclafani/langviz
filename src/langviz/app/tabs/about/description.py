import dash_bootstrap_components as dbc
from dash import html

DESCRIPTION_TEXT = """
Langviz is a corpus analysis toolkit for observing useful statistics and linguistic information 
from text data. Designed to be used in the beginning of the NLP pipeline, this tool provides 

"""


def description_card():
    """Returns the 'Description' card inside the 'About' tab"""
    return dbc.Card(
        [
            dbc.CardHeader(html.H1("What is Langviz?")),
            dbc.CardBody(
                [DESCRIPTION_TEXT],
            ),
        ],
        color="#E8E8E8",
    )
