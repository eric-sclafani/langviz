import dash_bootstrap_components as dbc


def document_tab():
    return dbc.Tab(
        label="Document",
        activeTabClassName="fw-bold fst-italic",
        disabled=True,
        id="document-tab",
        tab_id="document-tab",
    )
