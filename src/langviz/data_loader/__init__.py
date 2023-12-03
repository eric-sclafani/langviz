from typing import List

import pandas as pd


def load_from_path(path: str) -> pd.DataFrame:
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


def data_loader(path: str, column_name: str) -> List[str]:
    """Loads the user's data from path and extracts text data from provided column"""
    df = load_from_path(path)
    text_data = extract_text_column_data(df, column_name)
    return text_data
