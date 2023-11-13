"""This module loads the dataset from the provided path"""
from typing import Union

import pandas as pd


def load_dataset(path: str) -> Union[pd.DataFrame, None]:
    """Attempts to load data from path into a Dataframe. Returns None if unsuccessful"""
    try:
        if path.endswith(".csv"):
            return pd.read_csv(path)
        if path.endswith(".json"):
            return pd.read_json(path, orient="records")
    except FileNotFoundError:
        return None
