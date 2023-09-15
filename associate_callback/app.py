from dash import Dash, html, dcc, callback, Output, Input
from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import visdcc

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
    visdcc.Run_js(id='javascript'),
    html.Div([
        dcc.Input(id='selected-text', value='Afghanistan'),
        html.Button(id='exec-button')
    ], hidden=True),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('selected-text', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

@callback(
    Output('javascript', 'run'),
    Input('exec-button','n_clicks')
)
def event_from_button(x):
    return '''
    var country = $("#sources").val()

    setProps({ 
            'event': {'country':country}
        })
    '''

@callback(
    Output('selected-text', 'value'),
    Input('javascript', 'event')
)
def set_country(evt):

    if evt is None:
        return 'Afghanistan'

    return evt['country']

if __name__ == '__main__':
    app.run(debug=True)
