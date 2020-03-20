# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app
from app.components.series_component import get_graph
from dash.dependencies import Input, Output
from config import Config


def get_people_page():

    content = html.Div(children=[
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                    id='id_select_area',
                    options=[{'label': x[0], 'value':x[1]} for x in Config.AUS_STATE],
                    value='NSW'
                )),
                dbc.Col(dcc.Dropdown(
                    id='id_select_status',
                    options=[{'label': x[0], 'value':x[1]} for x in Config.STATUS],
                    value='confirmed'
                )),
                dbc.Col(width=6)
            ]
        ),
        html.Div(id='dd-output-area'),
        html.Br(),
        # dbc.Row(
        #     [
        #         dbc.Col(html.Div("One of three columns")),
        #         dbc.Col(html.Div("One of three columns")),
        #         dbc.Col(html.Div("One of three columns")),
        #     ]
        # ),
        dbc.Col(html.Div(id='id_infect_people',
                         children=[
                             get_graph('NSW', 'confirmed')
                         ])),
    ])

    return content


@app.callback(
    [Output('dd-output-area', 'children'),
     Output('id_infect_people', 'children'), ],
    [Input('id_select_area', 'value'),
     Input('id_select_status', 'value')
     ],
)
def update_output(state, status):
    # confirmed = get_graph(state, 'confirmed')
    # death = get_graph(state, 'death')
    # recover = get_graph(state, 'recover')
    # rows = dbc.Row(
    #     [
    #         dbc.Col(confirmed),
    #         dbc.Col(death),
    #         dbc.Col(recover),
    #     ]
    # )
    # return [f'You have selected "{state}"', [confirmed]]
    # return f'You are looking "{state}" information', infect_people_graph(state)
    return f'You are looking "{state}" information', get_graph(state, status)
