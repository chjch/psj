import dash_deck
import pydeck as pdk
import json

mapbox_api_token = open('./mapbox_token.txt', mode='r').read()
mapbox_style = 'mapbox://styles/chjch/cl8d69pxo000m14mqbbttpqfa'

data_url = r"./data/psj_bldg.geojson"

tooltip_html = '''
    <table>
        <tr>
            <td><strong>Blockgroup ID</strong></td>
            <td>{property_Blockgroup}</td>
        </tr>
        <tr>
            <td><strong>Number of Floor</strong></td>
            <td>{property_fakefloors}</td>
        </tr>
        <tr>
            <td><strong>Square Footage</strong></td>
            <td>{property_sqft}</td>
        </tr>
    </table>
'''

tooltip_style = {
    "font-size": "14px",
    "backgroundColor": "white",
    "color": "black"
}


# modify the JSON data and bring properties one level upper
def flatten_geojson_property(
        json_dict: dict, key: str, add_comma: bool = False
) -> dict:
    for feature in json_dict['features']:
        if add_comma:
            feature[f'property_{key}'] = f"{feature['properties'][key]:,}"
        else:
            feature[f'property_{key}'] = feature['properties'][key]
    return json_dict


def building_deck():
    fill_color_rgba = [235, 235, 235, 170]
    line_color_rgba = [0, 0, 0, 255]

    geojson_data = json.load(open(data_url))
    geojson_layer = pdk.Layer(
        "GeoJsonLayer",
        data=geojson_data,
        id='geojson',
        opacity=1,
        stroked=True,
        filled=True,
        extruded=True,
        wireframe=True,
        get_elevation="properties.fakefloors * 3",
        get_fill_color=fill_color_rgba,
        get_line_color=line_color_rgba,
        pickable=True,
        material=False,
        tooltip=True
    )

    # Set viewport to Downtown PSJ
    view_state = pdk.ViewState(
        latitude=29.805019, longitude=-85.298468,
        bearing=28, pitch=55, zoom=15.2,
    )

    # Renderer
    r = pdk.Deck(
        layers=[geojson_layer],
        initial_view_state=view_state,
        map_style=mapbox_style,
        api_keys={'mapbox': mapbox_api_token},
    )

    # flatten GeoJSON data to create tooltip
    flatten_geojson_property(geojson_data, 'Blockgroup')
    flatten_geojson_property(geojson_data, 'fakefloors')
    flatten_geojson_property(geojson_data, 'sqft', add_comma=True)

    return dash_deck.DeckGL(r.to_json(), id="building-deck",
                            mapboxKey=mapbox_api_token,
                            tooltip={'html': tooltip_html,
                                     'style': tooltip_style}
                            )
