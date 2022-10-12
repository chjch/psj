import os
import pandas as pd
from dash import Dash, html
import pydeck as pdk
import dash_deck

from dotenv import load_dotenv

load_dotenv()

MAPBOX_API_KEY = os.getenv("MAPBOX_TOKEN")
mapbox_style = 'dark'

# DATA_URL = 'data/psj_lidar_80_31_colorized_wgs84_nav88m_filtered.csv'
DATA_URL = "https://raw.githubusercontent.com/chjch/psj/main/data/psj_lidar_80_31_colorized_wgs84_nav88m_filtered.csv"
df = pd.read_csv(DATA_URL)
# df = df.iloc[:2000, :]

# target = [df.X.mean(), df.Y.mean(), df.Z.mean()]
# target = [df.x.mean(), df.y.mean(), df.z.mean()]

point_cloud_layer = pdk.Layer(
    "PointCloudLayer",
    data=DATA_URL,
    get_position=["X", "Y", "Z"],
    get_color=["R", "G", "B"],
    # get_position=["x", "y", "z"],
    # get_color=["r", "g", "b"],
    get_normal=[0, 0, 15],
    # auto_highlight=True,
    pickable=False,
    point_size=0.5,
)

# Set viewport to Downtown PSJ
view_state = pdk.ViewState(
    # target=target,
    controller=True,
    latitude=29.8097032, longitude=-85.308468,
    rotation_x=15, rotation_orbit=30,
    bearing=28, pitch=55,
    zoom=15, min_zoom=13, max_zoom=18
)

# view_state = pdk.ViewState(
#     # target=target,
#     controller=True,
#     bearing=28, pitch=55,
#     # rotation_x=15, rotation_orbit=30,
#     zoom=5.3
# )
# view = pdk.View(type="MapView")
#
r = pdk.Deck(point_cloud_layer, initial_view_state=view_state,
             # views=[view]
             )

# r = pdk.Deck(point_cloud_layer,
#              initial_view_state=view_state,
#              map_provider='mapbox',
#              map_style=mapbox_style,
#              api_keys={'mapbox': MAPBOX_API_KEY}, views=[view])

point_cloud_deck = dash_deck.DeckGL(r.to_json(), id="point-deck",
                                    mapboxKey=MAPBOX_API_KEY)

# r.to_html('point_cloud_layer.html')
#
# import json
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(r.to_json(), f, ensure_ascii=False, indent=4)

app = Dash(__name__)

app.layout = html.Div(
    dash_deck.DeckGL(r.to_json(), id="deck-gl",
                     # style={"background-color": "#add8e6"}
                     )
)


if __name__ == "__main__":
    app.run_server(debug=True)