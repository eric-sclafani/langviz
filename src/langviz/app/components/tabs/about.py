"""
This module contains code for the 'About' tab
"""
import dash_bootstrap_components as dbc
from dash import html

ABOUT_PAGE_CARD_COLOR = "#E8E8E8"
ACTIVE_TAB_CLASS_NAME = "fw-bold fst-italic"


_description_text = """
Langviz is an open-source corpus visualization tool 
"""


#
# _layout = html.Div(
#     [
#         dbc.Stack(
#             [
#                 html.H2("To get started, upload your data below"),
#                 html.Div(id="test-div"),
#             ]
#         )
#     ]
# )
#

_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card("This is card one", color=ABOUT_PAGE_CARD_COLOR)),
                dbc.Col(dbc.Card("This is card two", color=ABOUT_PAGE_CARD_COLOR)),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card("This is card one", color=ABOUT_PAGE_CARD_COLOR)),
                dbc.Col(dbc.Card("This is card two", color=ABOUT_PAGE_CARD_COLOR)),
            ]
        ),
    ]
)


about_tab = dbc.Tab(
    _layout, label="About", active_tab_class_name=ACTIVE_TAB_CLASS_NAME, id="about-tab"
)
