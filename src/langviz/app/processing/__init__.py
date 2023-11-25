"""

"""

from dataclasses import dataclass
from typing import List

import spacy
from spacy.language import Language


@dataclass
class Document:
    tokens: List[str]
    num_tokens: int
    num_types: int
    raw_text: str


def load_spacy_model(model:str) -> Language:
    """Attempts to load the given spaCy model. Will attempt to download if not found"""
    try:
        return spacy.load(model)
    except OSError:
        print(f"spaCy model '{model}' not detected. Downloading...")
        from spacy.cli.download import download
        download(model)
        return spacy.load(model)

def process_documents(data:pd.Series) -> List[Documents]:

