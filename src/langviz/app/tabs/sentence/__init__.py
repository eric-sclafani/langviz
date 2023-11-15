import dash_bootstrap_components as dbc


def sentence_tab():
    return dbc.Tab(
        label="Sentence",
        activeTabClassName="fw-bold fst-italic",
        disabled=True,
        id="sentence-tab",
    )
