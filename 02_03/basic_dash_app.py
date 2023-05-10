import dash
import pandas as pd
from dash import html, dcc
import plotly.express as px


data = pd.read_csv('precious_metals_prices_2018_2021.csv', usecols=['DateTime', 'Gold'])

fig = px.line(data, x='DateTime', y='Gold', title='Gold Prices')

app = dash.Dash(__name__)
app.title = 'Gold Prices'
app.layout = html.Div(
    id='app-container',
    children=[
        html.H1(app.title),
        html.P('Results in USD/oz'),
        dcc.Graph(figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
