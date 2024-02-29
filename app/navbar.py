from dash import html, dcc, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc

NAVBAR_LOGO = "/assets/image/UFlogo.png"
NAVBAR_BRAND_TITLE = "Resilient Port St. Joe"

navbar_brand = html.A(
    # Use row and col to control vertical alignment of logo / brand
    dbc.Row(
        [
            dbc.Col(html.Img(src=NAVBAR_LOGO, height="45px")),
            dbc.Col(
                dbc.NavbarBrand(
                    NAVBAR_BRAND_TITLE,
                    className="ms-2",
                    style={
                        "font-size": "1.6em",
                        "font-family": "poppins",
                        "padding-left": "20px",
                        "color": "#0E3183",
                    },
                )
            ),
        ],
        align="center",
        className="g-0",
    ),
    href="/",
    style={"textDecoration": "none"},
)


def navbar_btn(name: str, href: str):
    return dbc.Col(
        dbc.Button(
            name,
            # color="primary",
            # active=True,
            id=f"{name.replace(' ', '').lower()}-button",
            href=f"/viewer/{href}",
            className="ms-2 rounded-pill btn",
            n_clicks=0,
        ),
        width="auto",
    )


navbar_right = dbc.Row(
    dbc.Row(
        children=[
            navbar_btn(
                "Housing", "housing"
            ),
            navbar_btn(
                "Transportation", "transportation"
            ),
            navbar_btn(
                "Critical Infrastructure", "critical-infrastructure"
            ),
            navbar_btn(
                "Community Services", "community-services"
            ),
            navbar_btn(
                "Natural & Cultural Resources", "natural-cultural-resources"
            ),
            navbar_btn(
                "Local Economy", "local-economy"
            ),
            navbar_btn("Adaptation", "adaptation"),
        ],
        className="g-0 flex-nowrap mt-3 mt-md-0",
        id="navbar-links-group",
    ),
    className="ms-auto hidden-1500 hidden-mobile",
    # align="center",
)

dropdown = html.Div(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(
                    "HOUSING",
                    id="dropdown-button",
                    href="/viewer/housing",
                ),
                dbc.DropdownMenuItem(
                    "TRANSPORTATION",
                    href="/viewer/transportation",
                ),
                dbc.DropdownMenuItem(
                    "CRITICAL INFRASTRUCTURE",
                    href="/viewer/critical-infrastructure",
                ),
                dbc.DropdownMenuItem(
                    "COMMUNITY SERVICES",
                    href="/viewer/community-services",
                ),
                dbc.DropdownMenuItem(
                    "NATURAL & CULTURAL",
                    href="/viewer/natural-cultural-resources",
                ),
                dbc.DropdownMenuItem(
                    "LOCAL ECONOMY",
                    href="/viewer/local-economy",
                ),
                dbc.DropdownMenuItem(
                    "ADAPTATION",
                    href="/viewer/adaptation",
                ),
            ],
            label="Category",
            align_end=True,
            className="show-1500 hidden-mobile",
        ),
    ]
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            navbar_brand,
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                navbar_right, id="navbar-collapse", is_open=False, navbar=True
            ),
            dropdown,
        ],
        fluid=True,
        class_name="px-4",
    ),
    id="navbar",
    color="#ffffff",
    dark=False,
    class_name="px-4 py-3",
    # style={'box-shadow': '1px 1px 1px black'}
)


@callback(
    Output("item-clicks", "children"), [Input("dropdown-button", "n_clicks")]
)
def count_clicks(n):
    if n:
        return f"Button clicked {n} times."
    return "Button not clicked yet."
