from typing import Union

import dash_bootstrap_components as dbc
import pandas as pd
from dash import html


# COLUMN_INPUT = html.Div(
#     [
#         dbc.Label("Column", html_for="text-column-input"),
#         dbc.Input(id="text-column-input", placeholder="Enter column name"),
#         dbc.FormText(
#             "This column should contain all the language data you want to analyze",
#             color="secondary",
#         ),
#     ]
# )
#
def maybe_load_dataset(input_path: str) -> Union[pd.DataFrame, None]:
    """Attempts to load data from path into a Dataframe. Returns None if unsuccessful"""
    try:
        if input_path.endswith(".csv"):
            return pd.read_csv(input_path)
        if input_path.endswith(".json"):
            return pd.read_json(input_path, orient="records")
    except FileNotFoundError:
        return None


def data_loading_alert(input_path: str, data_is_loaded: bool) -> dbc.Alert:
    """Returns an Alert component colored by if the data was loaded or not"""
    if data_is_loaded:
        color = "success"
        children = [
            html.B("Success!"),
            f"Data loaded from path:'{input_path}'",
        ]
    else:
        color = "danger"
        children = [
            html.B("Whoops!"),
            f"Data from path: '{input_path}' was not loaded. Please check your path.",
        ]

    return dbc.Alert(children, color=color, id="data-load-alert")


def data_loading_card(input_path: str):
    return dbc.Card(
        [
            dbc.CardHeader(),
        ],
        color="#E8E8E8",
    )
