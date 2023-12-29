"""
This modules contains code for caching user data calculations
"""

import datetime
import os
import pickle
from pathlib import Path
from typing import Dict

from langviz.processing import Corpus


# TODO: eventually support loading a directory of files (ex: a dir of .json or .csv files with the same fields)
def get_dataset_cache_path(dataset_path: str) -> Path:
    """Extracts the dataset filename from given path"""
    file = os.path.split(dataset_path)[1]
    file_name = os.path.splitext(file)[0]
    return Path(f".langviz_cache/{file_name}/")


def dataset_cache_exists(path: str) -> bool:
    cache_path = get_dataset_cache_path(path)
    return cache_path.exists()


# TODO: experiment with spacy DocBin https://spacy.io/usage/saving-loading
def load_cached_corpus(path: str) -> Corpus:
    cache_path = get_dataset_cache_path(path)
    with open(f"{cache_path}/corpus.pkl", "rb") as fin:
        return pickle.load(fin)


# TODO: experiment with saving cache to user's home dir (using https://github.com/platformdirs/platformdirs)
# Maybe langviz will present the cached options to user and they can select which one to show?
def create_langviz_cache_dir() -> None:
    """Creates the .langviz_cache if not found"""
    cwd = Path.cwd()
    cache_path = Path(".langviz_cache/")
    if not cache_path.exists():
        print(f"Langviz cache not found. Saving as {cwd}/{cache_path}")
        print(
            f"Note: for this dataset, run 'langviz' from the same directory as the cache, which is: '{cwd}'"
        )
        cache_path.mkdir()


def create_dataset_cache_dir(cache_dir: Path) -> None:
    """Creates a cache for given dataset"""
    print(f"Dataset cache not found. Saving as '{cache_dir}'")
    cache_dir.mkdir()


def pickle_corpus(cache_path: Path, corpus: Corpus) -> None:
    """Saves the given Corpus to cache"""
    with open(f"{cache_path}/corpus.pkl", "wb") as fout:
        pickle.dump(corpus, fout)


def save_cache(corpus: Corpus, path: str) -> None:
    create_langviz_cache_dir()

    dataset_cache_path = get_dataset_cache_path(path)
    create_dataset_cache_dir(dataset_cache_path)
    pickle_corpus(dataset_cache_path, corpus)
