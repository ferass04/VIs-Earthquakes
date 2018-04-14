from plotly import __version__from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import pandas as pd
import datetime
import numpy as np


df = pd.read_csv("../data/query.csv", header=0)
A = df.as_matrix()
time = A[:, 0]
latitude = A[:, 1]
longitude = A[:, 2]
depth = A[:, 3]
mag = A[:, 4]

df['text'] = df['place'] + '<br>Magnitude ' + (df['mag']).astype(str)
limits = [(0, 5), (6, 10), (11, 20), (21, 30), (31, 50)]
colors = ["rgba(255,65,54, 0.5)", "rgba(0,116,217, 0.4)", "rgba(133,20,75, 0.3)", "rgba(255,133,27, 0.2)",
          "rgba(204, 206, 192, 0.2)"]
cities = []
scale = 80

data = []
for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]  # List from row(lim[0]) to row(lim[1]) in df

    trace = dict(
        lat=df_sub['latitude'],
        lon=df_sub['longitude'],
        text=df_sub['text'],
        name='{0} - {1}'.format(lim[0], lim[1]) + "<br><br><br><br><br><br>",
        marker=dict(
            size=scale / (i + 1),
            color=colors[i],
            line=dict(width=0.5, color='rgb(40,40,40)'),
            sizemode='area'
        ),
        type='scattermapbox'
    )
    data.append(trace)

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


updatemenus = list([
    dict(
        buttons=mag[0:10],
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
    dict(text='Trace type:', x=0, y=1.085,
         yref='paper', align='left', showarrow=False)
])
layout['annotations'] = annotations

layout['updatemenus'] = updatemenus
layout['annotations'] = annotations

fig = dict(data=data, layout=layout)
plot(fig, validate=False, filename='d3-bubble-map-populations.html')
