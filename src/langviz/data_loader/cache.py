"""
This modules contains code for caching user data calculations
"""

import pickle
from pathlib import Path


def create_cache_dir(path_name=".langviz_cache") -> None:
    path = Path(path_name)
    if not path.exists():
        print(f"{path_name} not found. Creating...")
        print(
            f"Note: you must run 'langviz' from the same directory as the cache, which is: '{Path.cwd()}'"
        )
        path.mkdir()
