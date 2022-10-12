from dash import Dash, html, dcc, Input, Output, ctx
import dash_bootstrap_components as dbc

from navbar import navbar
from commuter_deck import commuter_deck
from commuter_panel import commuter_panel, njob_options
from building_deck import building_deck

# external CSS stylesheets
external_stylesheets = [
    {'src': 'https://api.tiles.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.css',
     'rel': 'stylesheet'},
    dbc.themes.DARKLY
]

app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           suppress_callback_exceptions=True)

server = app.server

app.layout = html.Div([
    dcc.Location(id='map-link'),
    dbc.Row(navbar),
    dbc.Row(
        children=[dbc.Col(commuter_panel, width=3),
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

from terrain_deck import terrain_deck
terrain_map = html.Div(children=[terrain_deck],
                       id='terrain-map',
                       className='map_window')

from pointcloud_deck import point_cloud_deck
point_cloud_map = html.Div(children=[point_cloud_deck],
                           id='point-cloud-map',
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
    if pathname == "/3d-built-environment":
        return building_map
    elif pathname == '/flood-risk-and-slr':
        return terrain_map
    elif pathname == '/lidar-point-cloud':
        return point_cloud_map
    else:
        return commuter_map


if __name__ == "__main__":
    app.run_server()
