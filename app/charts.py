import pandas as pd
import plotly.express as px

from utils import (
    flooded_csv,
    flooded_by_depth_csv,
    asset_axis_title,
    line_color_map
)

flooded_df = pd.read_csv(flooded_csv)
flooded_by_depth_df = pd.read_csv(flooded_by_depth_csv)

color_map = {}


def line_chart(asset, scenario):
    partial_df = flooded_df[flooded_df['asset'] == asset]
    global color_map
    color_map = line_color_map('G10', scenario, 0.2)
    fig = px.line(
        partial_df, x="year", y="percent", color='scenario',
        symbol='scenario', template='plotly_white',
        custom_data=['scenario'],
        color_discrete_map=color_map
    )
    fig.update_xaxes(
        ticktext=["2022", "2040", "2070"],
        tickvals=[2022, 2040, 2070],
        title=None
    )
    fig.update_yaxes(
        range=[-1, 101],
        title='Total Assets Flooded (%)'
    )
    fig.update_layout(
        legend=dict(
            title=dict(
                text='scenario<br>',
                font=dict(size=14)
            ),
            tracegroupgap=10
        ),

        margin=dict(l=10, r=0, t=10, b=0)
    )
    return fig


def bar_chart(asset, scenario, year):
    bar_trace = f"{scenario}_{str(year)}"
    bar_df = flooded_by_depth_df[flooded_by_depth_df['Asset Class'] == asset]
    x_title = f"Assets Flooded by Depth (%) under {scenario} in {year}"
    fig = px.bar(
        bar_df, x='Flood depth', y=bar_trace,
        # color='Asset Class',
        # barmode='group',
        template='plotly_white',
        category_orders={'Flood depth': ['0-1 ft', '1-3 ft', '3-6 ft',
                                        '6-9 ft', '9-18 ft', '18-27 ft',
                                        '>27 ft']},
    )
    fig.update_yaxes(
        range=[-1, 101],
        title=None
    )
    fig.update_xaxes(title=x_title)
    fig.update_traces(marker_color=color_map[scenario])
    fig.update_layout(
        legend=dict(
            orientation="h",
            itemwidth=70,
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=None
        ),
        bargroupgap=0.15,
        showlegend=False,
        margin=dict(l=20, r=0, t=20, b=0)
    )
    fig.add_annotation(
        x='>27 ft', y=85,
        # xshift=-40,
        text=f"{asset_axis_title[asset]}",
        showarrow=False,
        yshift=10,
        font=dict(size=14)
    )
    return fig
