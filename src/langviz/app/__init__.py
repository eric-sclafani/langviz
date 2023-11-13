import dash_bootstrap_components as dbc
from dash import Dash, html

from . import callbacks, data_loader, layout


def run_app(input_path: str) -> None:
    """Runs the application"""

    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

    data = data_loader.load_dataset(input_path)
    app.layout = layout.layout(data)
    callbacks.get_callbacks(app)
    app.run(debug=True)
