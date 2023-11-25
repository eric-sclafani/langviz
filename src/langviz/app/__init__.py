"""This file houses the main application execution function"""

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash

from . import callbacks
from .layout import layout


def run_app(data: pd.Series) -> None:
    """Runs the application and passes the data into it"""

    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])
    app.layout = layout(data)
    callbacks.get_callbacks(app)
    app.run(debug=True)
