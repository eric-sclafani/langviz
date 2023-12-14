from typing import Dict

from dash import Dash, Input, Output, dcc, html
import pandas as pd


def get_callbacks(app: Dash):
    """Houses all callbacks under one function"""

    @app.callback(
        Output("named-entity-list", "children"),
        Input("named-entity-json-storage", "data"),
        Input("ner-histogram", "clickData"),
    )
    def update_named_entity_list(json_string: str, click_data: Dict):
        if json_string is None or click_data is None:
            return dcc.Textarea(
                value="Click on a labeled bar in the\nhistogram to display a full list of that entity's texts",
                readOnly=True,
                draggable=False,
                style={"height": "450px"},
            )

        selected_named_entity = click_data["points"][0]["x"]
        entities_df = pd.read_json(json_string, orient="records")

        selected_entity_texts = entities_df[entities_df.label == selected_named_entity][
            "text"
        ]
        joined_texts_to_display = "\n".join(selected_entity_texts.to_list())
        return dcc.Textarea(
            value=joined_texts_to_display,
            readOnly=True,
            draggable=False,
            style={"height": "450px"},
        )
