import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('Home-Employment Dynamics',
                                id='commuter-map-link',
                                href='/home-employment-dynamic',
                                )),
        dbc.NavItem(dbc.NavLink('3D Built Environment',
                                id='building-map-link',
                                href='/3d-built-environment',
                                )),
        dbc.NavItem(dbc.NavLink('Flood Risk and SLR',
                                id='terrain-map-link',
                                href='/flood-risk-and-slr',
                                )),
        dbc.NavItem(dbc.NavLink('LiDAR Point Cloud',
                                id='lidar-point-cloud',
                                href='/lidar-point-cloud',
                                ))
    ],
    brand='Resilient Port St. Joe',
    brand_href="http://127.0.0.1:8050/",
    color="#",
    fluid=True,
    dark=True,
    class_name='px-4',
    style={'box-shadow': '1px 1px 1px black'}
)
