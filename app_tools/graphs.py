import plotly.graph_objects as go
import plotly.express as px


def draw_bubble_map(data):

    limits = [(1000, 1500), (1501, 2500), (2501, 5000), (5001, 10000), (10001, 100000), (100000, 550000)]
    colors = ["lightgrey", "royalblue", "lightseagreen", "yellow", "orange", "crimson"]
    fig = go.Figure()
    for idx, limit in enumerate(limits):
        df_sub = data[(data['facebook_id'] >= limit[0]) & (data['facebook_id'] <= limit[1])]
        fig.add_trace(go.Scattergeo(
            locationmode='USA-states',
            lon=df_sub['Longitude'],
            lat=df_sub['Latitude'],
            text=df_sub['text'],
            marker=dict(
                size=df_sub['facebook_id'] / 500,
                line_color='rgb(40,40,40)',
                color=colors[idx],
                line_width=0.5,
                sizemode='area'
            ),
            name='{0} - {1}'.format(limit[0], limit[1])))

    fig.update_layout(
        title_text='2021 US Facebook Account Breaches<br>Click legend to toggle traces',
        showlegend=True,
        geo=dict(
            scope='usa',
            landcolor='rgb(217, 217, 217)',
        ),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    return fig


def top_5_barchart(data, x: str, y: str, n_results: int = 10):

    fig = px.bar(data.head(n_results), x=x, y=y)
    return fig
