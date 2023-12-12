from dash import Dash, Input, Output
from typing import Dict


def get_callbacks(app: Dash):
    """Houses all callbacks under one function"""

    @app.callback(
        Output("named-entity-list", "children"),
        Input("named-entity-json", "children"),
        Input("ner-histogram", "clickData"),
    )
    def update_named_entity_list(json_data, clickData: Dict):
        if clickData is not None:
            named_entity = clickData["points"][0]["x"]
            print(named_entity)
        if json_data is not None:
            print(json_data)
