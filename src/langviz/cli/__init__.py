"""This file contains the CLI function for Langviz"""

import argparse
from typing import Dict

import dash_bootstrap_components as dbc
from dash import Dash

from langviz.core import callbacks, layout
from langviz.data_loader import data_loader


def run_app(args: Dict) -> None:
    """Initiates the application"""
    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])
    data = data_loader(args)
    app.layout = layout.layout(data)
    callbacks.get_callbacks(app)
    app.run()


def cli():
    """Handles the CLI args and passes them into the application."""
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
        help="Unique row identifer. Must exist in dataset already. Generated otherwise",
        required=False,
    )
    parser.add_argument(
        "--n_process",
        help="Number of processes to use for NLP pipeline. Default is 4.",
        default=4,
        required=False,
        type=int,
    )
    parser.add_argument(
        "--reset_cache",
        help="Option to reset cache for given dataset path",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "-s",
        "--spacy_model",
        help="Which pretrained spaCy model to use",
        choices=["en_core_web_sm", "en_core_web_md", "en_core_web_lg"],
        default="en_core_web_sm",
    )

    config = vars(parser.parse_args())
    run_app(config)
