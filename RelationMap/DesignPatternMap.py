import pandas as pd
from dash import Dash, html, dcc, Input, Output
import dash_cytoscape as cyto
import plotly.express as px

patterns = pd.read_csv("DesignPattern.csv")
relations = pd.read_csv("PatternRelation.csv")
elements = [
    {"data": {"id": row["name"], "label": row["name"], "description": row["description"]}} \
        for _, row in patterns.iterrows()
] +\
[
    {"data": {"source": row["source"], "target": row["target"], "annotation": row["annotation"]}}
        for _, row in relations.iterrows()
]

layout_options = [
    "random", "circle", "concentric", "grid", "breadthfirst", "cose",
]

app = Dash(__name__)

app.layout = html.Div([
    html.H1(id="title", children="デザインパターン間の関連"),
    html.P(id="node-data"),
    html.Div([dcc.Dropdown(
        options=[
            {"label": name.capitalize(), "value": name} for name in layout_options
        ], 
        value=layout_options[0], 
        id="layout-option",
        style={"width": "200px"}
    )]),
    cyto.Cytoscape(
        id = "relation",
        elements = elements,
        layout = {"name": layout_options[0]},
        style = {"width": "1000px", "height": "600px", "background-color": "gray"},
        stylesheet = [
            {
                "selector": "edge",
                "style": {
                    "line-color": "white",
                    "label": "data(annotation)"
                }
            },
            {
                "selector": "node",
                "style": {
                    "label": "data(label)",
                    "background-color": "black"
                }
            }
        ]
    )
])

@app.callback(
    Output("relation", "layout"),
    Input("layout-option", "value")
)
def update_cytoscape(layout):
    if layout is None:
        layout = "random"
    return {
        "name": layout,
        "animate": True
    }

@app.callback(
    Output("node-data", "children"),
    Input("relation", "mouseoverNodeData")
)
def display_hover_node_data(data):
    if data:
        return f'{data["label"]}:{data["description"]}'

app.run_server(debug=True)