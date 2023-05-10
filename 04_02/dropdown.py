import dash
from dash import dcc, Output, Input
from dash import html
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")

app = dash.Dash(__name__)
app.title = "Precious Metal Prices 2018-2021"

metal_filter_id = 'metal-filter'
price_chart_id = 'price-chart'

app.layout = html.Div(
    id="app-container",
    children=[
        html.Div(
            id="header-area",
            children=[
                html.H1(
                    id="header-title",
                    children="Precious Metal Prices",

                ),
                html.P(
                    id="header-description",
                    children=("The cost of precious metals", html.Br(), "between 2018 and 2021"),
                ),
            ],
        ),
        html.Div(
            id="menu-area",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className="menu-title",
                            children="Metal"
                        ),
                        dcc.Dropdown(
                            id=metal_filter_id,
                            className="dropdown",
                            options=[{"label": metal, "value": metal} for metal in data.columns[1:]],
                            clearable=False,
                            value='Silver',
                        )
                    ]
                )
            ]
        ),
        html.Div(
            id="graph-container",
            children=dcc.Graph(
                id=price_chart_id,
                config={"displayModeBar": False}
            ),
        ),
    ]
)


@app.callback(
    Output(price_chart_id, 'figure'),
    Input(metal_filter_id, 'value')
)
def update_chart(metal: str):
    fig = px.line(
        data,
        title="Precious Metal Prices 2018-2021",
        x="DateTime",
        y=[metal],
        color_discrete_map={
            "Gold": "gold",
            'Silver': 'silver',
            'Platinum': '#E5E4E2',
            'Palladium': '#CED0DD',
            'Rhodium': '#E2E7E1',
            'Iridium': '#3D3C3A',
            'Ruthenium': '#C9CBC8',
        }
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Date",
        yaxis_title="Price (USD/oz)",
        font=dict(
            family="Verdana, sans-serif",
            size=18,
            color="white"
        ),
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
