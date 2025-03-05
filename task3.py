from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

my_app = Dash('Pink Morsel Sales')

df = pd.read_csv('pink_morsel_sales.csv')
graph = px.line(df, x='date', y='sales', color='region')

dcc.Graph(figure=graph)

my_app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales', style={'textAlign': 'center'}),
    dcc.Graph(figure=graph)
])

my_app.run()