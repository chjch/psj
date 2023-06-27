import os
from dotenv import load_dotenv

import plotly.express as px

load_dotenv()
# Import Mapbox API Key from environment
mapbox_token = os.getenv("MAPBOX_TOKEN")
cesium_token = os.getenv("CESIUM_TOKEN")
mapbox_style_building = 'mapbox://styles/chjch/cl8d69pxo000m14mqbbttpqfa'
road_json = 'app/data/psj_road_segments.json'
bfp_json = 'app/data/psj_bfp_props.json'
asset_points_json = 'app/data/psj_asset_points.json'

flooded_csv = "app/data/psj_all_assets_flooded.csv"
flooded_by_depth_csv = "app/data/psj_all_assets_flooded_by_depth.csv"

scenarios = ['MHHW', 'NFHL100', 'CAT1', 'CAT2', 'CAT3', 'CAT5']
asset_axis_title = {
    'CRITICAL COMMUNITY AND EMERGENCY FACILITIES':
        "Community Services",
    'CRITICAL INFRASTRUCTURE':
        "Critical Infrastructure",
    'NATURAL, CULTURAL, AND HISTORICAL RESOURCES':
        "Natural & Cultural Resources",
    'TRANSPORTATION':
        "Transportation",
    'ECONOMY':
        "Local Economy",
    'HOUSING':
        "Housing"
}


def cesium_tile_url(asset_id):
    return f'https://assets.ion.cesium.com/{asset_id}/tileset.json'


def scn_tile_url(scn_code, year):
    return "https://tiles.arcgis.com/tiles/LBbVDC0hKPAnLRpO/arcgis/" + \
        f"rest/services/PSJ_{scn_code}_{year}/MapServer/WMTS/tile/" \
        f"1.0.0/PSJ_{scn_code}_{year}/default/default028mm" + \
        "/{z}/{y}/{x}.png"


def line_color_map(color_sequence_name, scenario=None, opacity=0):
    colors = getattr(px.colors.qualitative, color_sequence_name)
    color_map = {}
    i = 0
    for scn in scenarios:
        color_map[scn] = (
            f'rgba{px.colors.hex_to_rgb(colors[i])}'
            .replace(')', f', {opacity})')
        )
        i += 1
    color_map[scenario] = color_map[scenario].replace(f'{opacity})', '1)')
    return color_map
