from dash import Dash, Input, Output


def get_callbacks(app: Dash):
    """Houses all callbacks under one function"""

    @app.callback(
        Output("test-div", "children"),
        Input("test-button", "n_clicks"),
    )
    def update_test(n_clicks):
        if n_clicks is not None:
            return "Helloo"
