"""This file contains the CLI function for Langviz"""

import argparse
from typing import List, Optional

import dash_bootstrap_components as dbc
from dash import Dash

from langviz.core import callbacks, layout
from langviz.data_loader import data_loader


def run_app(path: str, column_name: str, doc_id: Optional[str], n_process: int) -> None:
    """Initiates the application"""
    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])
    data = data_loader(path, column_name, doc_id, n_process)
    app.layout = layout.layout(data)
    callbacks.get_callbacks(app)
    app.run(debug=True)


def cli():
    """CLI handler"""
    parser = argparse.ArgumentParser(
        description="CLI command for running the Langviz software"
    )
    parser.add_argument(
        "-p",
        "--path",
        help="Path to input data",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--column_name",
        help="Name of column housing language data to analyze",
        required=True,
    )
    parser.add_argument(
        "-i",
        "--id",
        help="Unique row identifer. Must exist in dataset already",
        required=False,
    )
    parser.add_argument(
        "--n_process",
        help="Number of processes to use for NLP pipeline. Default is 4.",
        default=4,
        required=False,
        type=int
    )
    args = parser.parse_args()
    path = args.path
    column_name = args.column_name
    doc_id = args.id
    n_process = args.n_process

    run_app(path, column_name, doc_id, n_process)
