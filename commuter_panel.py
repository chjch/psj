from dash import html, dcc

njob_options = {
    'Less than 5 jobs': 1,
    'Between 5 and 15 jobs': 2,
    'Between 16 and 30 jobs': 3,
    'More than 30 jobs': (4, 5)
}

commuter_panel = html.Div(
    className='pretty_container',
    children=[
        html.Div("Filter by Number of Jobs"),
        dcc.Dropdown(id='njob-picker',
                     className='dropdown',
                     options=list(njob_options.keys()))
    ]
)
