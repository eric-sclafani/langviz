"""
This file contains the function that gets called from the command line
"""
import argparse

from langviz.app import run_app


def is_valid_path(path: str) -> bool:
    """Checks if provided path is an accepted formed"""
    if path.endswith(".csv") or path.endswith(".json") or path.endswith(".jsonl"):
        return True
    return False


def langviz():
    """CLI handler"""
    parser = argparse.ArgumentParser(
        description="CLI command for running the Langviz software"
    )
    parser.add_argument(
        "-i",
        "--input_path",
        help="Path to input data. Currently supported formats: .csv, .json, .jsonl",
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

    if not is_valid_path(path):
        raise RuntimeError(
            f"Unsupported format in path '{path}'. Currently supported formats: .csv, .json, .jsonl"
        )

    run_app(path)
