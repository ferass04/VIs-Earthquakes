from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import pandas as pd
import datetime
import numpy as np
import io


def convert_time(time):
    converted_time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return converted_time

def graph(csv_file):

    df = pd.read_csv(io.StringIO(csv_file.decode('utf-8')), header=0)
    # Load the data
    # df = pd.read_csv("../data/query.csv", header=0)
    A = df.as_matrix()
    time = A[:, 0]
    latitude = A[:, 1]
    longitude = A[:, 2]
    depth = A[:, 3]
    mag = A[:, 4]
    place = A[:, 13]
    # df['text'] = df['place'] + '<br>Magnitude ' + (df['mag']).astype(str)
    # limits = [(0, 4), (4, 5), (6, 7), (8, 9), (9, 10)]

    # Color used to render circles. Color differs by magnitude.
    colors = ["rgba(255, 204, 255, 0.1)", "rgba(204, 204, 255, 0.1)", "rgba(51, 204, 255, 0.1)", "rgba(0, 153, 204, 0.2)",
              "rgba(0, 255, 204, 0.2)", "rgba(0, 255, 0, 0.2)", "rgba(255, 255, 0, 0.3)", "rgba(255, 153, 0, 0.3)",
              "rgba(204, 51, 0, 0.5)", "rgba(255, 51, 0, 0.6)"]

    # Scale for the radius of circle.
    scale = 10
    circle_size = [1, 1.5, 2, 2.5, 3, 4, 5, 7, 9, 12]

    # Label for each magnitude group.
    labels=['Magnitude 1', 'Magnitude 2', 'Magnitude 3', 'Magnitude 4', 'Magnitude 5', 'Magnitude 6', 'Magnitude 7',
            'Magnitude 8', 'Magnitude 9']

    # Group the data by magnitude range (e.g., M1-2, M2-3, M3-4, etc.)
    df['key'] = pd.cut(df['mag'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=labels)
    grouped = df.groupby('key')

    # Store the map data
    data = []

    # name is each magnitude, group is each data
    for name, group in grouped:
        trace = dict(
            # mag = group[ group['key'] == name]['mag']
            lat=group['latitude'],
            lon=group['longitude'],
            text=group['place'] + '<br>Magnitude: ' + group['mag'].astype(str) + '<br>Depth: ' + group['depth'].astype(str)
                + ' km <br>Time: ' + group['time'],
            name='{0}'.format(name) + "<br><br><br><br><br><br><br>",
            marker=dict(
                size=circle_size[labels.index(name)] * scale,
                color=colors[labels.index(name)],
                line=dict(width=0.5, color='rgb(40,40,40)'),
                sizemode='area'
            ),
            type='scattermapbox'
        )
        data.append(trace)

    # for mfr in list(df_sum.index):
    #     size = df[ df['mag'] == mfr ]['mag']
    #     trace = dict(
    #             lat=df[ df['mag'] == mfr ]['latitude'],
    #             lon=df[ df['mag'] == mfr ]['longitude'],
    #             text= df[ df['mag'] == mfr ]['place'] + '<br>Magnitude ' + (df[ df['mag'] == mfr ]['mag']).astype(str),
    #             name= mfr,
    #             marker=dict(
    #                 size=df[ df['mag'] == mfr ]['mag']*scale,
    #                 color=colors[0],
    #                 line=dict(width=0.5, color='rgb(40,40,40)'),
    #                 sizemode='area'
    #             ),
    #             type='scattermapbox'
    #         )
    #     data.append(trace)

    # mapboc API key.
    mapbox_access_token = 'pk.eyJ1Ijoia21pbmFtaXNhd2EiLCJhIjoiY2pmeG82bWNmMDIyNzJ3b2RwcDFmOGFxMCJ9.pOlnj41jR4nhv8-dD7f_0Q'

    layout = dict(
        height=800,
        margin=dict(t=0, b=0, l=0, r=0),
        font=dict(color='#FFFFFF', size=11),
        paper_bgcolor='#000000',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=38,
                lon=-94
            ),
            pitch=0,
            zoom=3,
            style='dark'
        ),
    )

    # TODO: Update the mneu.
    updatemenus = list([
        dict(
            buttons=place[0:10],
            pad={'r': 0, 't': 10},
            x=0.1,
            xanchor='left',
            y=1.0,
            yanchor='top',
            bgcolor='AAAAAA',
            active=99,
            bordercolor='#FFFFFF',
            font=dict(size=11, color='#000000')
        ),
        dict(
            buttons=list([
                dict(
                    args=['mapbox.style', 'dark'],
                    label='Dark',
                    method='relayout'
                ),
                dict(
                    args=['mapbox.style', 'light'],
                    label='Light',
                    method='relayout'
                ),
                dict(
                    args=['mapbox.style', 'satellite'],
                    label='Satellite',
                    method='relayout'
                ),
                dict(
                    args=['mapbox.style', 'satellite-streets'],
                    label='Satellite with Streets',
                    method='relayout'
                )
            ]),
            direction='up',
            x=0.75,
            xanchor='left',
            y=0.05,
            yanchor='bottom',
            bgcolor='#000000',
            bordercolor='#FFFFFF',
            font=dict(size=11)
        ),
    ])

    annotations = list([
        dict(text='World Epic Earthquakes (scroll to zoom)', font=dict(color='magenta',size=14), borderpad=10,
             x=0.05, y=0.05, xref='page', yref='page', align='left', showarrow=False, bgcolor='black'),
        dict(text='Location', x=0.01, y=0.99, yref='paper', align='left', showarrow=False,font=dict(size=14))
    ])
    # layout['annotations'] = annotations

    layout['updatemenus'] = updatemenus
    layout['annotations'] = annotations

    fig = dict(data=data, layout=layout)
    plot(fig, validate=False, filename='d3-bubble-map-populations.html')
