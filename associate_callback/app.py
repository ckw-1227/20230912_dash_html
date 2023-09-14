from dash import Dash, html, dcc, callback, Output, Input
from flask import Flask, render_template
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

flaskapp = Flask(__name__)
app = Dash(server=flaskapp, url_base_pathname='/app1/')

@flaskapp.route("/")
def index():

    return render_template(
        "index.html",
        dash_app=app.index()
    )

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection')
    ], hidden=True),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)
