import dash_bootstrap_components as dbc
from dash import html


def make_link(link_text: str, url: str):
    """Creates an Anchor component"""
    return html.A(
        link_text,
        href=url,
        disable_n_clicks=True,
        target="_blank",
    )


def links_card():
    """Returns the 'Links' card inside the 'About' tab"""
    return dbc.Card(
        [
            dbc.CardHeader(html.H1("Links!")),
            dbc.CardBody(
                [
                    html.Div("Check out these cool links", className="links-subheader"),
                    make_link(
                        "Source code", "https://github.com/eric-sclafani/langviz"
                    ),
                    html.Br(),
                    make_link("My GitHub", "https://github.com/eric-sclafani"),
                ]
            ),
        ]
    )
