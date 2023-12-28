"""
This modules contains code for caching user data calculations
"""

import pickle
import re
from pathlib import Path

from langviz.processing import Corpus

# Create cache dir if not exists inside user's home directory
# Create cache path for current dataset if not exists
# After processing documents into a Corpus object, pickle it
# Save metadata in an "info.json" file (date created, full given path, how large the processed corpus is, dataset name, etc...)

# On startup with given path, check if cache for that dataset exists
# if so, load the pickle. If user uses the --reset_cache command, will recalculate the cached Corpus
# if not, create the Corpus object and save to dataset cache directory


# TODO: experiment with saving cache to user's home dir (using https://github.com/platformdirs/platformdirs)
# Maybe langviz will present the cached options to user and they can select which one to show?
def create_langviz_cache_dir(path=".langviz_cache") -> None:
    """Creates the .langviz_cache if not found"""
    cache_path = Path(path)
    cwd = Path.cwd()
    if not cache_path.exists():
        print(
            f"Langviz cache not found in current working directory. Saving as {cwd}/{path}"
        )
        print(
            f"Note: you must run 'langviz' from the same directory as the cache, which is: '{cwd}'"
        )

        cache_path.mkdir()


# TODO: eventually support loading a directory of files (ex: a dir of .json or .csv files with the same fields)
def get_file_name(dataset_path: str) -> str:
    """Extracts the dataset filename from given path"""
    file = dataset_path.split("/")[-1]
    file_name = re.sub(r"\..+", "", file)  # remove file extension
    return file_name


def create_dataset_cache_dir(dataset_path: str) -> None:
    """Creates a cache for given dataset if not found"""
    dataset_cache_path = Path(f".langviz_cache/{get_file_name(dataset_path)}/")
    if not dataset_cache_path.exists():
        print(f"Dataset cache not found. Saving as {dataset_cache_path}")
        dataset_cache_path.mkdir()
    else:
        print(f"Cached data detected at '{dataset_cache_path}'")


def pickle_corpus(cache_path: str, corpus: Corpus) -> None:
    """Saves the given Corpus to cache"""
    with open(cache_path, "wb") as fout:
        pickle.dump(corpus, fout)


def cache_handler(data_path: str):
    create_langviz_cache_dir()
    create_dataset_cache_dir(data_path)
