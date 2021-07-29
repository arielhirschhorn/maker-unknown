# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
fig = {}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
full_bce_df = pd.read_pickle('./full_bce_df.pkl')
known_bce_df = pd.read_pickle('./known_bce_df.pkl')
unknown_bce_df = pd.read_pickle('./unknown_bce_df.pkl')

def line_plot(df, plot_title):
    fig = px.line(df, x='Year', y="Object Count",title=plot_title)
    fig.update_yaxes(type='linear')
    return fig
                    
full_bce = line_plot(full_bce_df, 'Full collection')
known_bce = line_plot(known_bce_df, 'Known makers')
unknown_bce = line_plot(unknown_bce_df, 'Unknown makers')

app.layout = html.Div(children=[
    
    html.H1(children='Website in progress'),
    html.H3(children='Amount of objects by year, BCE'),
    
    dbc.Row(
        [dbc.Col(dcc.Graph(id='bce-full',figure=full_bce)),
        dbc.Col(dcc.Graph(id='bce-known',figure=known_bce)),
         dbc.Col(dcc.Graph(id='bce-unknown',figure=unknown_bce))
        ],
    
    ),
            

    
])

if __name__ == '__main__':
    app.run_server(debug=True)
    app.run_server(debug=True)