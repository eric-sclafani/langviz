import dash_bootstrap_components as dbc


def corpus_tab():
    return dbc.Tab(
        label="Corpus",
        activeTabClassName="fw-bold fst-italic",
        disabled=True,
        id="corpus-tab",
    )
