import pandas as pd
import plotly.express as px

depth_df = pd.read_csv("app/data/psj_all_assets_flooded.csv")
class_df = pd.read_csv("app/data/psj_all_assets_depth.csv")

asset_dict = {
    'CRITICAL COMMUNITY AND EMERGENCY FACILITIES': "Community Services",
    'CRITICAL INFRASTRUCTURE': "Critical Infrastructure",
    'NATURAL, CULTURAL, AND HISTORICAL RESOURCES': "Natural & Cultural Resources",
    'TRANSPORTATION': "Transportation",
    'ECONOMY': "Local Economy",
    'HOUSING': "Housing"
}

category_orders = {
    'Asset Class':
        [
            'HOUSING',
            'TRANSPORTATION',
            'CRITICAL INFRASTRUCTURE',
            'CRITICAL COMMUNITY AND EMERGENCY FACILITIES',
            'NATURAL, CULTURAL, AND HISTORICAL RESOURCES',
            'ECONOMY'
        ]
}


def line_chart(asset: str = 'HOUSING'):
    partial_df = depth_df[depth_df['asset'] == asset]
    fig = px.line(partial_df, x="year", y="percent", color='scenario',
                  symbol='scenario', template='plotly_white',
                  custom_data=['scenario'],
                  color_discrete_sequence=px.colors.qualitative.Plotly)
    fig.update_xaxes(
        ticktext=["2022", "2040", "2070"],
        tickvals=[2022, 2040, 2070],
        title=None
    )
    fig.update_yaxes(range=[-1, 101],
                     title='Assets inundated (%)')
    fig.update_layout(
        # title={'text': asset_dict[asset],
        #        'font': {'size': 16},
        #        'x': 0.5},
        legend=dict(
            title=dict(
                text='scenario<br>',
                font=dict(size=14)
            ),
            tracegroupgap=10
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig


def bar_chart(asset: str = 'HOUSING',
              scenario: str = 'CAT2',
              year: int = 2040):
    bar_trace = f"{scenario}_{str(year)}"
    # if asset != 'HOUSING':
    asset_title = asset_dict[asset]
    bar_df = class_df[class_df['Asset Class'] == asset]
    x_title = f"{asset_title} (%) by flood depth"
    # else:
    #     bar_df = class_df
    #     x_title = f"All critical assets (%) by flood depth"
    fig = px.bar(bar_df, x='Flood depth', y=bar_trace, color='Asset Class',
                 barmode='group', category_orders=category_orders,
                 template='plotly_white',
                 color_discrete_sequence=['#5289B0', '#AAB543', '#EA9731',
                                          '#838383', '#F6C540', '#D05E33'])
    fig.update_yaxes(range=[-1, 103],
                     title=None)
    fig.update_xaxes(title=x_title)
    fig.update_layout(
        legend=dict(
            orientation="h",
            itemwidth=70,
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=None,

        ),
        bargroupgap=0.15,
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig
