"""
This file contains the function that gets called from the command line
"""

import argparse
from typing import List

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash

from langviz.processing import process_documents

from . import callbacks, layout


def data_loader(path: str) -> pd.DataFrame:
    """
    Loads the user's tabular data into a Pandas dataframe.

    Raises RuntimeError if unsupported format is given
    """
    if path.endswith(".csv"):
        return pd.read_csv(path, engine="c")

    if path.endswith(".json") or path.endswith(".jsonl"):
        return pd.read_json(path, lines=True)

    if path.endswith(".xlsx"):
        return pd.read_excel(path)

    raise RuntimeError(f"Unsupported format in path '{path}'")


def extract_text_column_data(data: pd.DataFrame, column_name: str) -> List[str]:
    """
    Extracts the text column from given data

    Raises RuntimeError if column doesn't exist
    """

    if column_name in data.columns:
        return data[column_name].values.tolist()
    raise RuntimeError(
        f"Column '{column_name}' not found in provided data. Existing columns: {list(data.columns)}"
    )


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

    df = data_loader(path)
    text_data = extract_text_column_data(df, column_name)

    run_app(text_data)
