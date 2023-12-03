"""This file contains the CLI function for Langviz"""

import argparse
from typing import List

import dash_bootstrap_components as dbc
from dash import Dash

from langviz.core import callbacks, layout
from langviz.data_loader import data_loader
from langviz.processing import process_documents


def run_app(data: List[str]) -> None:
    """Initiates the application"""

    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

    processed_documents = process_documents(data)
    app.layout = layout.layout(processed_documents)
    callbacks.get_callbacks(app)
    app.run(debug=True)


def cli():
    """CLI handler"""
    parser = argparse.ArgumentParser(
        description="CLI command for running the Langviz software"
    )
    parser.add_argument(
        "-i",
        "--input_path",
        help="Path to input data",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--column_name",
        help="Name of column housing language data to analyze",
        required=True,
    )
    args = parser.parse_args()
    path = args.input_path
    column_name = args.column_name

    text_data = data_loader(path, column_name)

    run_app(text_data)
