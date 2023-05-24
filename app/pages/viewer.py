import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

from navbar import navbar
from slr_deck import slr_scenario
from charts import line_chart, bar_chart
from intro import intro_msg

dash.register_page(
    __name__,
    title="Port St. Joe Dashboard",
    path_template="/viewer/<asset_type>"
)

# chart dbc column
chart_panels = dbc.Col(
    [
        html.Div(
            children=[],
            id="intro-message",
            className="pretty_container",
            style={"height": "25vh", "overflow": "auto"},
        ),
        dcc.Graph(
            figure=line_chart(),
            id="line-chart",
            responsive=True,
            hoverData={"points": [{"x": 2040, "customdata": ["CAT1"]}]},
            className="pretty_container",
            style={"height": "33vh"},
        ),
        dcc.Graph(
            figure=bar_chart(),
            id="bar-chart",
            responsive=True,
            className="pretty_container",
            style={"height": "27vh"},
        ),
    ],
    width=4,
)

map_x_slider = html.Div(
    [
        html.Div(
            "Projection Year",
            style={
                "width": "200px",
                "font-size": "1.2em",
                "padding": "0px 0px 0px 50px",
            },
        ),
        html.Div(
            dcc.Slider(
                id="map-x-slider",
                step=None,
                marks={2022: "2022", 2040: "2040", 2070: "2070"},
                value=2040,
            ),
            style={
                "padding": "7px 25px 0px 0px",
                "width": "calc(100% - 200px)",
            },
        ),
    ],
    className="hstack gap-2",
)

marks = {
    1: "MHHW",
    2: "NFHL100",
    3: "CAT1",
    4: "CAT2",
    5: "CAT3",
    6: "CAT5",
}

map_y_slider = html.Div(
    [
        html.Div(
            "Scenario",
            style={"font-size": "1.2em", "padding": "30px 0px 0px 0px"},
        ),
        html.Div(
            dcc.Slider(
                id="map-y-slider",
                step=None,
                vertical=True,
                marks=marks,
                value=3,  # CAT1
            ),
            style={"padding": "0px 0px 0px 0px"},
        ),
    ],
    className="vstack gap-2",
    style={"height": "100%", "position": "relative"},
)

# map dbc column
map_panel = dbc.Col(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            children=[],
                            id="map-container",
                            className="map_window",
                        ),
                        dcc.Dropdown(
                            ["Satellite", "Road map"],
                            # "Road map",
                            id="basemap-dropdown",
                            placeholder="Choose a basemap",
                            clearable=False,
                            style={
                                "top": "25px",
                                "left": "25px",
                                "width": "41%",
                                "height": "30px",
                                "position": "absolute",
                                "z-index": 1,
                            },
                        ),
                        html.Img(
                            id="map-legend",
                            src="../assets/image/map-legend.png",
                            style={
                                "bottom": "70px",
                                "left": "45px",
                                "width": "10%",
                                "height": "auto",
                                "position": "absolute",
                                "z-index": 1,
                            },
                        ),
                    ],
                    className="pretty_container",
                ),
                map_x_slider,
            ],
            style={"width": "95%"},
        ),
        map_y_slider,
    ],
    className="hstack gap-2",
)


def layout(asset_type=None):
    return html.Div(
        [
            dcc.Location(id="sub-path"),
            dbc.Row(navbar),
            dbc.Row(
                children=[chart_panels, map_panel],
                class_name="g-0 px-3",
            ),
        ]
    )


@callback(
    Output("map-container", "children"),
    [
        Input("sub-path", "pathname"),
        Input("map-x-slider", "value"),
        Input("map-y-slider", "value"),
        Input("basemap-dropdown", "value"),
    ],
)
def update_map(pathname, x_value, y_value, basemap):
    pathname = "/" + pathname.split("/")[-1]
    if pathname == "/viewer":
        pathname = "/"
        return slr_scenario(pathname, marks[y_value], x_value, basemap)
    else:
        return slr_scenario(pathname, marks[y_value], x_value, basemap)


@callback(Output("intro-message", "children"), [Input("sub-path", "pathname")])
def update_intro_msg(pathname):
    pathname = "/" + pathname.split("/")[-1]
    if pathname == "/housing":
        return intro_msg("housing")
    elif pathname == "/critical-infrastructure":
        return intro_msg("infra")
    elif pathname == "/transportation":
        return intro_msg("trans")
    elif pathname == "/community-services":
        return intro_msg("comm")
    elif pathname == "/natural-cultural-resources":
        return intro_msg("resrc")
    elif pathname == "/local-economy":
        return intro_msg("economy")
    else:
        return intro_msg("overall")


@callback(Output("line-chart", "figure"), [Input("sub-path", "pathname")])
def update_line_chart(pathname):
    pathname = "/" + pathname.split("/")[-1]
    if pathname == "/housing":
        return line_chart("HOUSING")
    elif pathname == "/critical-infrastructure":
        return line_chart("CRITICAL INFRASTRUCTURE")
    elif pathname == "/transportation":
        return line_chart("TRANSPORTATION")
    elif pathname == "/community-services":
        return line_chart("CRITICAL COMMUNITY AND EMERGENCY FACILITIES")
    elif pathname == "/natural-cultural-resources":
        return line_chart("NATURAL, CULTURAL, AND HISTORICAL RESOURCES")
    elif pathname == "/local-economy":
        return line_chart("ECONOMY")
    else:
        return line_chart("overall")


@callback(
    Output("bar-chart", "figure"),
    [Input("line-chart", "hoverData"), Input("sub-path", "pathname")],
)
def update_bar_chart(hoverdata, pathname):
    pathname = "/" + pathname.split("/")[-1]
    year = hoverdata["points"][0]["x"]
    scenario = hoverdata["points"][0]["customdata"][0]
    if pathname == "/housing":
        return bar_chart("HOUSING", scenario, year)
    elif pathname == "/critical-infrastructure":
        return bar_chart("CRITICAL INFRASTRUCTURE", scenario, year)
    elif pathname == "/transportation":
        return bar_chart("TRANSPORTATION", scenario, year)
    elif pathname == "/community-services":
        return bar_chart("CRITICAL COMMUNITY AND EMERGENCY FACILITIES", scenario, year)
    elif pathname == "/natural-cultural-resources":
        return bar_chart("NATURAL, CULTURAL, AND HISTORICAL RESOURCES", scenario, year)
    elif pathname == "/local-economy":
        return bar_chart("ECONOMY", scenario, year)
    else:
        return bar_chart("overall", scenario, year)


# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
