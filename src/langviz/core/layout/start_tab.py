"""
This module contains code for the 'About' tab
"""

import dash_bootstrap_components as dbc
from dash import html


def config_item(label_text, display_text):
    return html.Div(
        [
            html.Strong(f"{label_text}:", className="text-black"),
            html.Div(str(display_text)),
        ],
        className="d-flex gap-1",
    )


def display_config(config):
    return html.Div(
        [
            config_item("Path", config["path"]),
            config_item("Data Column", config["column_name"]),
            config_item("Unique ID Column", config["id"] or "None"),
            config_item("Number of Processes", config["n_process"]),
            config_item("Reset Cache?", config["reset_cache"]),
            config_item("spaCy Model", config["spacy_model"]),
        ],
        className="border border-5 border-dark p-3",
    )


def visualize_button():
    return dbc.Button(
        "Visualize!", id="initialize-components", className="bg-primary text-white"
    )


def layout(config):
    """Returns the layout for the 'About' tab"""
    return dbc.Stack(
        [
            display_config(config),
            visualize_button(),
        ],
        className="d-flex flex-direction-column m-5",
    )


def start_tab(config):
    """Returns the 'Getting started' tab"""
    return dbc.Tab(
        layout(config),
        label="Getting started",
        id="start-tab",
        tab_id="start-tab",
        active_tab_class_name="fw-bold fst-italic",
    )
