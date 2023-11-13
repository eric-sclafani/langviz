import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html

from . import callbacks, dataset, layout


def run_app(input_path: str) -> None:
    """Runs the application"""

    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

    data = dataset.load_dataset(input_path)
    app.layout = layout.layout(data)
    callbacks.get_callbacks(app)
    app.run(debug=True)
