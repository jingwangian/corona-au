# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from app.components.series_component import get_graph
from config import Config
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])

# graph = get_graph()

boduy_content = html.Div(children=[
    html.H1(children='Coronavirus in Australia'),

    html.Div(children='''
        A web application help people to get the Corona information.
    '''),
    dcc.Dropdown(
        id='id_select_area',
        options=[{'label': x[0], 'value':x[1]} for x in Config.AUS_STATE],
        value='NSW'
    ),
    # dcc.Dropdown(
    #     id='id_select_status',
    #     options=[{'label': x[0], 'value':x[1]} for x in Config.STATUS],
    #     value='confirmed'
    # ),
    html.Div(id='dd-output-area'),
    html.Div(id='id_graph',
             children=[
                 get_graph('NSW', 'confirmed'),
                 get_graph('NSW', 'death'),
                 get_graph('NSW', 'recover')
             ])
])

app.layout = dbc.Container(
    boduy_content,
    fluid=True,
    className="dash-container",
    style={"paddingTop": "20px"})


@app.callback(
    [Output('dd-output-area', 'children'),
     Output('id_graph', 'children'), ],
    [Input('id_select_area', 'value'),
     ],
)
def update_output(state):
    confirmed = get_graph(state, 'confirmed')
    death = get_graph(state, 'death')
    recover = get_graph(state, 'recover')
    # return [f'You have selected "{state}"', [confirmed]]
    return f'You are looking "{state}" information', [confirmed, death, recover]


if __name__ == '__main__':
    app.run_server(debug=True)
