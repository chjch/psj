import os
from dotenv import load_dotenv

load_dotenv()
# Import Mapbox API Key from environment
mapbox_token = os.getenv("MAPBOX_TOKEN")
cesium_token = os.getenv("CESIUM_TOKEN")
mapbox_style_building = 'mapbox://styles/chjch/cl8d69pxo000m14mqbbttpqfa'
road_json = 'app/data/psj_road_segments.json'
bfp_json = 'app/data/psj_bfp_props.json'
asset_points_json = 'app/data/psj_asset_points.json'


def cesium_tile_url(asset_id):
    return f'https://assets.ion.cesium.com/{asset_id}/tileset.json'


def scn_tile_url(scn_code, year):
    return "https://tiles.arcgis.com/tiles/LBbVDC0hKPAnLRpO/arcgis/" + \
        f"rest/services/PSJ_{scn_code}_{year}/MapServer/WMTS/tile/" \
        f"1.0.0/PSJ_{scn_code}_{year}/default/default028mm" + \
        "/{z}/{y}/{x}.png"
