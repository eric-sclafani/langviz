"""
This file contains the function that gets called from the command line
"""
import argparse

from langviz.app import run_app


def langviz():
    """CLI handler"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_path",
        help="Path to input data",
        required=True,
    )

    args = parser.parse_args()
    run_app(args.input_path)
