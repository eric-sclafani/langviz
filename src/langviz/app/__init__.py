"""This file houses the main application execution function"""

import dash_bootstrap_components as dbc
from dash import Dash, html

from . import callbacks
from .tabs import layout


def run_app(input_path: str) -> None:
    """Runs the application"""

    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

    app.layout = layout("data")
    callbacks.get_callbacks(app)
    app.run(debug=True)
