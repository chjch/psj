import pydeck as pdk
import os
from dotenv import load_dotenv
import dash_deck

load_dotenv()

# Import Mapbox API Key from environment
MAPBOX_API_KEY = os.getenv("MAPBOX_TOKEN")
# print(MAPBOX_API_KEY)
mapbox_style = 'mapbox://styles/chjch/cl8d69pxo000m14mqbbttpqfa'

pdk.settings.custom_libraries = [
    {
        "libraryName": "MyTileLayerLibrary",
        "resourceUri": "https://cdn.jsdelivr.net/gh/agressin/pydeck_myTileLayer@master/dist/bundle.js",
    }
]
#
SURFACE_IMAGE = "https://tiles.arcgis.com/tiles/LBbVDC0hKPAnLRpO/arcgis/rest/" \
                "services/psj_100_2070_int_high_depth_wgs84/MapServer/WMTS/tile/" \
                "1.0.0/psj_100_2070_int_high_depth_wgs84/default/default028mm/{z}/{y}/{x}.png"

custom_layer = pdk.Layer(
    "MyTileLayer",
    SURFACE_IMAGE,
    opacity=0.7
)

view_state = pdk.ViewState(
    latitude=29.805019, longitude=-85.298468,
    bearing=28, pitch=55, zoom=13,
)

r = pdk.Deck(custom_layer,
             initial_view_state=view_state,
             map_provider='mapbox',
             map_style='satellite',
             api_keys={'mapbox': MAPBOX_API_KEY}
             )

json_data = \
{
    "initialViewState": {
        "bearing": 28,
        "latitude": 29.805019,
        "longitude": -85.298468,
        "pitch": 55,
        "zoom": 13
    },
    "layers": [
        {
            "@@type": "TileLayer",
            "data": "https://tiles.arcgis.com/tiles/LBbVDC0hKPAnLRpO/arcgis/rest/services/psj_100_2070_int_high_depth_wgs84/MapServer/WMTS/tile/1.0.0/psj_100_2070_int_high_depth_wgs84/default/default028mm/{z}/{y}/{x}.png",
            "id": "f260c4b8-4122-4877-a581-31a276af6135",
            "opacity": 0.7
        }
    ],
    "mapProvider": "mapbox",
    "mapStyle": "mapbox://styles/mapbox/satellite-v9",
    "views": [
        {
            "@@type": "MapView",
            "controller": True
        }
    ]
}

terrain_deck = dash_deck.DeckGL(json_data, id="terrain-deck",
                                mapboxKey=MAPBOX_API_KEY)
