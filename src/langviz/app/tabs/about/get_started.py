import dash_bootstrap_components as dbc
from dash import html

GET_STARTED_TEXT = """
To begin, if your data was loaded correctly, you should see some shit, blah blah, click button or 
apply optional text cleaning, yada yada yada...
"""


def get_started_card():
    """Returns the 'Get started' card inside the 'About' tab"""
    return dbc.Card(
        [
            dbc.CardHeader(html.H1("Get started")),
            dbc.CardBody(
                [GET_STARTED_TEXT],
            ),
        ],
        color="#E8E8E8",
    )
