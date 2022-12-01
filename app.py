import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



main_title = html.Div(
    children=[
        html.H3(children="Review Sentiments")
])
main_image = html.Img(
    src='/Users/ananya.aj5gmail.com/Documents/CMPE256-AdvDataMining/256_sentimentanalysis/sentiment.png',
    className="sentiment-image"
)

hor = html.Div(children=[
    main_title,
    main_image
], className="d-flex justify-content-around hor")

app.layout = html.Div([
    dcc.Textarea(
        id='textarea-1',
        value='write a review',
        style={'width': '100%', 'height': 300},
    ),
    html.Div(id='textarea-1', style={'whiteSpace': 'pre-line'})
])


if __name__ == "__main__":
    app.run_server(debug=True)