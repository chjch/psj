import dash_deck
from utils import cesium_token, mapbox_api_token

mapbox_dark = 'mapbox://styles/mapbox/dark-v10'
mapbox_streets = 'mapbox://styles/mapbox/streets-v11'
mapbox_satellite_street = 'mapbox://styles/mapbox/satellite-streets-v11'
cesium_asset_id = '1355666'
DATA_URL = f'https://assets.cesium.com/{cesium_asset_id}/tileset.json'

ambient_light = {"@@type": "AmbientLight",
                 "color": [255, 255, 255],
                 "intensity": 2.8}
lighting_effect = {
    "@@type": "LightingEffect",
    "ambientLight": ambient_light,
}

data = {
    "initialViewState": {
        "bearing": 30,
        "latitude": 29.8126632,
        "longitude": -85.303558,
        "maxZoom": 18,
        "minZoom": 13,
        "pitch": 55,
        "zoom": 16
    },
    "layers": [
        {
            "@@type": "Tile3DLayer",
            "id": "tiles-psj",
            "loader": "@@#CesiumIonLoader",
            "pointSize": 1.5,
            "opacity": 1,
            "data": DATA_URL,
            "loadOptions": {
                "cesium-ion": {
                    "accessToken": cesium_token
                },
            }
        }
    ],
    "views": [
        {
            "@@type": "MapView",
            "mapStyle": mapbox_dark,
            "controller": True,
            "position": [0, 0, -30],  # down shift basemap to avoid overlapping
        }
    ],
    "effects": [lighting_effect]
}

tile3d_deck = dash_deck.DeckGL(data,
                               id="tile3d-deck",
                               mapboxKey=mapbox_api_token)
