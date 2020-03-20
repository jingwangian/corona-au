import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.services.covid_time_series import COVIDTimeSeriesData
from config import Config


ts_data = COVIDTimeSeriesData()

STATUS_FN = {
    'confirmed': ts_data.get_confirmed_data,
    'death': ts_data.get_death_data,
    'recover': ts_data.get_recover_data,
}


def get_state_name(state_abr_name):
    for x in Config.AUS_STATE:
        if x[1] == state_abr_name:
            return x[0]


def get_graph(state, status):
    """
    :param state: The state of the australia
    :status: 'confirmed, death, recovered
    """
    print(STATUS_FN[status])
    df = STATUS_FN[status]()

    state_name = get_state_name(state)

    x = df.index
    y = df[state_name].to_list()

    # print(df)
    id = f'id_{state}_{status}'

    df1 = df.drop(df.columns[0:4], axis=1)
    fig = dcc.Graph(
        id=id,
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'bar', 'name': 'New South Wales'},
                # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': f'The number of people {status}',
                'width': '400px',
            },
        },
        config={
            'responsive': True,
        },
        style={
            'background': '0x123456',
        }
    )

    card = dbc.Card(
        dbc.CardBody(
            [
                fig,
            ]
        ),
    )

    return card
