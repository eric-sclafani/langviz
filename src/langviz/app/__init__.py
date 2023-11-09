import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html

from . import callbacks, layout


def run_app(input_path: str) -> None:
    """Runs the application"""

    # data will be loaded here and passed to all layout components
    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])
    app.layout = html.Div([layout.header])
    callbacks.get_callbacks(app)
    app.run(debug=True)
