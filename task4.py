from dash import Dash, dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px

my_app = Dash('Pink Morsel Sales')

df = pd.read_csv('pink_morsel_sales.csv')

my_app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales', style={'textAlign': 'center'}),

    html.Div(children=[
        dcc.Graph(id='line-graph'),
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'left'}),

    html.Div(children=[
        html.H2(children='Region'),

        dcc.RadioItems(
            ['north', 'east', 'south', 'west', 'all'],
            'all',
            id='region',
            inline=True
        )
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
])

@callback(
    Output('line-graph', 'figure'),
    Input('region', 'value')
)
def update_graph(region):
    if region == 'all':
        df_filtered = df
    else:
        df_filtered = df[df.region == region]

    graph = px.line(df_filtered, x='date', y='sales', color='region')
    graph.update_layout()
    return graph

my_app.run()