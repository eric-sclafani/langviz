import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table


def corpus_tab():
    return dbc.Tab(
        label="Corpus",
        activeTabClassName="fw-bold fst-italic",
        id="corpus-tab",
        tab_id="corpus-tab",
    )
