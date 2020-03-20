import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.components.series_component import get_graph


def infect_people_graph(state):
    width = {"size": 4}
    rows = dbc.Row(
        [
            dbc.Col(children=[dbc.Container(get_graph(state, 'confirmed'))],
                    width=width),
            dbc.Col(dbc.Container(get_graph(state, 'death')), width=width),
            dbc.Col(dbc.Container(get_graph(state, 'recover')), width=width),
        ]
    )
    return rows
