import os
import socket
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

from navbar import navbar
from commuter_deck import commuter_deck
from commuter_panel import commuter_panel, njob_options
from building_deck import building_deck
from critical_asset_deck import icon_deck
from terrain_deck import terrain_deck
from tile3d_deck import tile3d_deck

# external CSS stylesheets
external_stylesheets = [
    {'src': 'https://api.tiles.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.css',
     'rel': 'stylesheet'},
    dbc.themes.DARKLY
]

app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           suppress_callback_exceptions=True)
app.title = 'Port St. Joe Dashboard'

server = app.server

try:
    IS_DEV = int(os.environ['PYCHARM_HOSTED'])
except KeyError:
    IS_DEV = 0

if IS_DEV:
    brand_href = 'http://127.0.0.1:8050/'
else:
    brand_href = socket.gethostname()


app.layout = html.Div([
    dcc.Location(id='map-link'),
    dbc.Row(navbar(brand_href)),
    dbc.Row(
        children=[dbc.Col(html.Div(children=commuter_panel,
                                   id='commuter_panel'),
                          width=3),
                  dbc.Col(html.Div(children=[],
                                   id='map-container',
                                   className='pretty_container'))],
        class_name='g-0 px-3')
])

commuter_map = html.Div(children=[],
                        id='commuter-map',
                        className='map_window')

building_map = html.Div(children=building_deck(),
                        id='building-map',
                        className='map_window')

terrain_map = html.Div(children=[terrain_deck],
                       id='terrain-map',
                       className='map_window')

point_cloud_map = html.Div(children=[tile3d_deck],
                           id='point-cloud-map',
                           className='map_window')

report_asset = html.A('Report An Asset',
                      href='https://www.arcgis.com/apps/CrowdsourceReporter/'
                           'index.html?appid=95373653e2fc4373be0d8b572f20e501',
                      className='external-link',
                      target='_blank')


icon_map = html.Div(children=[icon_deck, report_asset],
                    id='icon-map',
                    className='map_window')


@app.callback(
    Output('commuter-map', 'children'),
    [Input('njob-picker', 'value')]
)
def update_commuter_deck(selected_njob_option):
    if selected_njob_option:
        if type(njob_options[selected_njob_option]) is int:
            selected_njob_option = [njob_options[selected_njob_option]]
        else:
            selected_njob_option = list(njob_options[selected_njob_option])
        return commuter_deck(selected_njob_option)
    else:
        return commuter_deck()


@app.callback(
    Output("map-container", "children"),
    [Input("map-link", "pathname")]
)
def update_map(pathname):
    # if pathname == "/3d-built-environment":
    #     return building_map
    if pathname == '/flood-risk-and-slr':
        return terrain_map
    elif pathname == '/lidar-point-cloud':
        return point_cloud_map
    elif pathname == '/critical-assets':
        return icon_map
    else:
        return commuter_map


if __name__ == "__main__":
    app.run_server()
