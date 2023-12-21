import sys
from typing import List, Optional

import pandas as pd

from langviz.processing import Corpus, process_documents


# TODO: improve decoding error handling, maybe cycle through different decoding options before raising error?
def load_from_path(path: str) -> pd.DataFrame:
    """
    Loads the user's tabular data into a Pandas dataframe.

    Raises RuntimeError if unsupported format is given

    Raises UnicodeDecodeError if any decoding errors occur
    """

    try:
        if path.endswith(".csv"):
            return pd.read_csv(path)
        if path.endswith(".json") or path.endswith(".jsonl"):
            return pd.read_json(path, lines=True)
        if path.endswith(".xlsx"):
            return pd.read_excel(path)
    except UnicodeDecodeError:
        print("Unable to decode file. Please check and preprocess your data")
        sys.exit()

    raise RuntimeError(f"Unsupported format in path '{path}'")


def get_text_column_data(data: pd.DataFrame, column_name: str) -> List[str]:
    """
    Extracts the text column from given data

    Raises RuntimeError if provided column holds no documents or column does not exist
    """
    if column_name in data.columns:
        text_data = data[column_name].values.tolist()
        if not text_data:
            raise RuntimeError(
                f"Provided dataset has no documents in column '{column_name}'"
            )
        return text_data

    raise RuntimeError(
        f"Column '{column_name}' not found in provided data. Existing columns: {list(data.columns)}"
    )


def get_doc_ids(data: pd.DataFrame, doc_id: Optional[str]) -> List[str]:
    """
    Returns a list of unique document IDs. If user provides a column name for this,
    attempts to use that column's values. Else, generates new IDs for each document

    Raises RuntimeError if provided column is not found
    """
    if doc_id is None:
        return [f"Doc-{i+1}" for i in range(len(data))]
    if doc_id in data:
        return data[doc_id].astype(str).values.tolist()

    raise RuntimeError(
        f"Column '{doc_id}' not found in provided data. Existing columns: {list(data.columns)}"
    )


# TODO: improve CLI argument handling
def data_loader(
    path: str, column_name: str, doc_id: Optional[str], n_process: int
) -> Corpus:
    """Loads the user's data from path and extracts text data from provided column"""
    df = load_from_path(path)
    text_data = get_text_column_data(df, column_name)
    doc_ids = get_doc_ids(df, doc_id)
    processed_documents = process_documents(text_data, doc_ids, n_process)
    return processed_documents
