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
def create_cache_dir(path_name=".langviz_cache") -> None:
    """Creates the .langviz_cache directory if not found"""
    cache_path = Path(path_name)
    cwd = Path.cwd()
    if not cache_path.exists():
        print(
            f"Cache not found in current working directory. Saving as {cwd}/{path_name}"
        )
        print(
            f"Note: you must run 'langviz' from the same directory as the cache, which is: '{cwd}'"
        )

        cache_path.mkdir()


# TODO: eventually support loading a directory of files (ex: a dir of .json or .csv files with the same fields)
def get_file_name(path: str) -> str:
    """Extracts the dataset filename from given path"""
    file = path.split("/")[-1]
    file_name = re.sub(r"\..+", "", file)  # remove file extension
    return file_name


def pickle_corpus(cache_path: str, corpus: Corpus) -> None:
    """Saves the given Corpus to cache"""
    with open(cache_path, "wb") as fout:
        pickle.dump(corpus, fout)


def cache_handler(corpus: Corpus):
    pass
