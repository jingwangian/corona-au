import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output
from config import Config
from app.components.people_page import get_people_page
from app.components.navbar import nav

body_content = html.Div(children=[
    html.H1(children='Coronavirus in Australia'),

    html.Div(children='''
        A web application help people to get the Corona information.
    '''),

    get_people_page()

    # infect_people_graph(),
])


def get_main_page():
    return dbc.Container(
        dbc.Row(
            [
                dbc.Col(nav,
                        width=2,
                        align='stretch',
                        style={
                            'background': '#edf0f5',
                            'border-style': 'solid',
                            'border-color': 'white',
                            'border-width': '1px',
                        }),
                dbc.Col(body_content),
            ]
        ),
        # body_content,
        fluid=True,
        className="dash-container",
        style={"paddingTop": "20px"})
