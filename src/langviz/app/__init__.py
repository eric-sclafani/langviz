import dash_bootstrap_components as dbc
from dash import Dash, html

from . import callbacks


def run_app(input_path: str) -> None:
    """Runs the application"""

    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

    app.layout = layout.layout(input_path)
    callbacks.get_callbacks(app)
    app.run(debug=True)
