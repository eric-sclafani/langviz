"""
This file contains the function that gets called from the command line
"""

import argparse

import pandas as pd

from langviz.app import run_app


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


def extract_text_column_data(data: pd.DataFrame, column_name: str) -> pd.Series:
    """
    Extracts the text column from given data

    Raises RuntimeError if column doesn't exist
    """

    if column_name in data.columns:
        return data[column_name]
    raise RuntimeError(f"Column '{column_name}' not found in provided data")


def langviz():
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

    # print(f"Loading data from path: '{path}'")
    df = data_loader(path)
    text_data = extract_text_column_data(df, column_name)

    run_app(text_data)
