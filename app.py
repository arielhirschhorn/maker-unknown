# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


import plotly.express as px
import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
fig = {}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
full_bce_df = pd.read_pickle('./full_bce_df.pkl')
known_bce_df = pd.read_pickle('./known_bce_df.pkl')
unknown_bce_df = pd.read_pickle('./unknown_bce_df.pkl')

full_ce_df = pd.read_pickle('./full_ce_df.pkl')
known_ce_df = pd.read_pickle('./known_ce_df.pkl')
unknown_ce_df = pd.read_pickle('./unknown_ce_df.pkl')

def line_plot(df, plot_title):
    fig = px.line(df, x='Year', y="Object Count",title=plot_title)
    fig.update_yaxes(type='linear')
    return fig
                    
full_bce = line_plot(full_bce_df, 'Full collection')
known_bce = line_plot(known_bce_df, 'Known makers')
unknown_bce = line_plot(unknown_bce_df, 'Unknown makers')

full_ce = line_plot(full_ce_df, 'Full collection')
known_ce = line_plot(known_ce_df, 'Known makers')
unknown_ce = line_plot(unknown_ce_df, 'Unknown makers')

app.layout = html.Div(children=[
    
    html.H1(children='Website in progress'),
    
    
    dbc.Row(html.H3(children='Amount of objects by year, BCE'), justify="center", align="center"),
    dbc.Row(
        [dbc.Col(dcc.Graph(id='bce-full',figure=full_bce), width = 4),
        dbc.Col(dcc.Graph(id='bce-known',figure=known_bce), width = 4),
         dbc.Col(dcc.Graph(id='bce-unknown',figure=unknown_bce), width = 4),
        ],
    
    ),
    
    
    dbc.Row(html.H3(children='Amount of objects by year, CE'), justify="center", align="center"),
    dbc.Row(
        [dbc.Col(dcc.Graph(id='ce-full',figure=full_ce), width = 4),
        dbc.Col(dcc.Graph(id='ce-known',figure=known_ce), width = 4),
         dbc.Col(dcc.Graph(id='ce-unknown',figure=unknown_ce), width = 4),
        ],
        justify="center",
        
        ),
    dbc.Row(html.H3(children='Word Clouds: Description field'), justify="center", align="center"),
    dbc.Row(
        [dbc.Col([html.H4(children='Full collection'), html.Img(src=app.get_asset_url('full_collection_description.png'),style={'height':'25%'})], width = 4),
         dbc.Col([html.H4(children='Known makers'), html.Img(src=app.get_asset_url('known_maker_description.png'),style={'height':'25%'})], width = 4),
         dbc.Col([html.H4(children='Unknown makers'), html.Img(src=app.get_asset_url('unknown_maker_description.png'),style={'height':'25%'})], width = 4),
        ],
    ),
    
    dbc.Row(html.H3(children='Word Clouds: Title field'), justify="center", align="center"),
    dbc.Row(
        [dbc.Col([html.H4(children='Full collection'), html.Img(src=app.get_asset_url('full_collection_title.png'),style={'height':'25%'})], width = 4),
         dbc.Col([html.H4(children='Known makers'), html.Img(src=app.get_asset_url('known_maker_title.png'),style={'height':'25%'})], width = 4),
         dbc.Col([html.H4(children='Unknown makers'), html.Img(src=app.get_asset_url('unknown_maker_title.png'),style={'height':'25%'})], width = 4),
        ],
    ),
        
    
            

    
])

if __name__ == '__main__':
    app.run_server(debug=True)
    app.run_server(debug=True)