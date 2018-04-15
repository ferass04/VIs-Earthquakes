# Animation Kinda working
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import pandas as pd
import datetime
import numpy as np
import io


def convert_time(time):
    converted_time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    # print(converted_time.date())
    return converted_time


def graph():
    # df = pd.read_csv(io.StringIO(csv_file.decode('utf-8')), header=0)
    # Load the data
    df = pd.read_csv("../data/query.csv", header=0)
    A = df.as_matrix()
    time = A[:, 0]
    latitude = A[:, 1]
    longitude = A[:, 2]
    depth = A[:, 3]
    mag = A[:, 4]
    place = A[:, 13]

    time_list = np.empty(10)
    for each_time in time:
        np.append(time_list, convert_time(each_time))
        convert_time(each_time)

    # Color used to render circles. Color differs by magnitude.
    colors = ["rgba(255, 204, 255, 0.1)", "rgba(204, 204, 255, 0.1)", "rgba(51, 204, 255, 0.1)", "rgba(0, 153, 204, 0.2)",
              "rgba(0, 255, 204, 0.2)", "rgba(0, 255, 0, 0.2)", "rgba(255, 255, 0, 0.3)", "rgba(255, 153, 0, 0.3)",
              "rgba(204, 51, 0, 0.5)", "rgba(255, 51, 0, 0.6)"]

    # Scale for the radius of circle.
    scale = 10
    circle_size = [1, 1.5, 2, 2.5, 3, 4, 5, 7, 9, 12]

    # Label for each magnitude group.
    labels = ['Magnitude 1', 'Magnitude 2', 'Magnitude 3', 'Magnitude 4', 'Magnitude 5', 'Magnitude 6', 'Magnitude 7',
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
            buttons=[
                {
                    'args': [None, {'frame': {'duration': 500, 'redraw': False},
                             'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                    'label': 'Play',
                    'method': 'animate'
                },
                {
                    'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                    'transition': {'duration': 0}}],
                    'label': 'Pause',
                    'method': 'animate'
                }],
            pad={'r': 100, 't': 600},
            x=0.1,
            xanchor='left',
            y=1.0,
            yanchor='buttom',
            bgcolor='AAAAAA',
            active=99,
            bordercolor='#FFFFFF',
            font=dict(size=11, color='#000000')
        ),
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

    mag_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    layout['updatemenus'] = updatemenus
    layout['annotations'] = annotations
    # layout['sliders'] = sliders_dict
    layout['hovermode'] = 'closest'
    layout['sliders'] = {
        'args': [
            'transition', {
                'duration': 400,
                'easing': 'cubic-in-out'
            }
        ],
        'initialValue': '1',
        'plotlycommand': 'animate',
        'values': mag_list,
        'visible': True
    }

    frames = []
    sliders_dict = {
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 20},
            'prefix': 'Year:',
            'visible': True,
            'xanchor': 'right'
        },
        'transition': {'duration': 300, 'easing': 'cubic-in-out'},
        'pad': {'b': 10, 't': 50},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
        'steps': []
    }
    for name, group in grouped:
        frame = {'data': [], 'name': str(name)}
        trace = dict(
            # mag = group[ group['key'] == name]['mag']
            lat=group['latitude'],
            lon=group['longitude'],
            text=group['place'] + '<br>Magnitude: ' + group['mag'].astype(str) + '<br>Depth: ' + group[
                'depth'].astype(str)
                 + ' km <br>Time: ' + group['time'],
            name='{0}'.format("Animation") + "<br><br><br><br><br><br><br>",
            marker=dict(
                size=circle_size[labels.index(name)] * scale,
                color=colors[labels.index(name)],
                line=dict(width=0.5, color='rgb(40,40,40)'),
                sizemode='area'
            ),
            type='scattermapbox'
        )
        frame['data'].append(trace)
        frames.append(frame)
        slider_step = {'args': [
            [name],
            {'frame': {'duration': 300, 'redraw': False},
             'mode': 'immediate',
             'transition': {'duration': 300}}
        ],
            'label': name,
            'method': 'animate'}
        sliders_dict['steps'].append(slider_step)

    layout['sliders'] = [sliders_dict]




    fig = dict(data=data, layout=layout, frames = frames)
    plot(fig, validate=False, filename='d3-bubble-map-populations.html')


graph()
