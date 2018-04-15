from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
import datetime

def convert_time(time):
    converted_time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    # print(converted_time.date())
    return converted_time

def generate_color(mag_group):
    temp_color = ["rgba(255, 204, 255, 0.1)", "rgba(204, 204, 255, 0.1)", "rgba(51, 204, 255, 0.1)", "rgba(0, 153, 204, 0.2)",
              "rgba(0, 255, 204, 0.2)", "rgba(0, 255, 0, 0.2)", "rgba(255, 255, 0, 0.3)", "rgba(255, 153, 0, 0.3)",
              "rgba(204, 51, 0, 0.5)", "rgba(255, 51, 0, 0.6)"]
    color = temp_color[0]
    if mag_group == 2:
        color = temp_color[1]
    elif mag_group == 3:
        color = temp_color[2]

    return color



def graph():
    # df = pd.read_csv(io.StringIO(csv_file.decode('utf-8')), header=0)
    # Load the data
    df = pd.read_csv("../data/query.csv", header=0)

    df["converted_time"] = pd.to_datetime(df["time"]).apply(
        lambda df: datetime.datetime(year=df.year, month=df.month, day=df.day, hour=df.hour, minute=df.minute, second=df.second))
    df['date_minus_time'] = df["converted_time"].apply(lambda df: datetime.datetime(year=df.year, month=df.month, day=df.day))

    # Color used to render circles. Color differs by magnitude.
    colors = ["rgba(255, 204, 255, 0.1)", "rgba(204, 204, 255, 0.1)", "rgba(51, 204, 255, 0.1)", "rgba(0, 153, 204, 0.2)",
              "rgba(0, 255, 204, 0.2)", "rgba(0, 255, 0, 0.2)", "rgba(255, 255, 0, 0.3)", "rgba(255, 153, 0, 0.3)",
              "rgba(204, 51, 0, 0.5)", "rgba(255, 51, 0, 0.6)"]

    # Scale for the radius of circle.
    scale = 100
    circle_size = [1, 2, 4, 8, 15, 30, 50, 70, 140]


    # Label for each magnitude group.
    labels = ['Magnitude 1', 'Magnitude 2', 'Magnitude 3', 'Magnitude 4', 'Magnitude 5', 'Magnitude 6', 'Magnitude 7',
            'Magnitude 8', 'Magnitude 9']

    # Group the data by magnitude range (e.g., M1-2, M2-3, M3-4, etc.)
    df['key'] = pd.cut(df['mag'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=labels)
    grouped = df.groupby('key')


    A = df.as_matrix()
    time = A[:, 0]
    latitude = A[:, 1]
    longitude = A[:, 2]
    depth = A[:, 3]
    mag = A[:, 4]
    place = A[:, 13]
    c_time = A[:, 23]
    key = A[:, 24]

    color_list = []
    radius_list = []
    for each_key in key:
        mag_group = labels.index(each_key)
        color_list.append(colors[mag_group])
        radius_list.append(int(circle_size[mag_group]*scale))

    df['color'] = color_list
    df['radius'] = radius_list



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
            zoom=1,
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
            # pad={'r': 100, 't': 600},
            direction='up',
            x=0.9,
            xanchor='left',
            y=0.1,
            yanchor='buttom',
            bgcolor='#000000',
            active=99,
            bordercolor='#FFFFFF',
            font=dict(size=11)
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
    ])

    layout['updatemenus'] = updatemenus
    layout['annotations'] = annotations
    layout['hovermode'] = 'closest'
    layout['sliders'] = {
        'args': [
            'transition', {
                'duration': 400,
                'easing': 'cubic-in-out'
            }
        ],
        'initialValue': '0',
        'plotlycommand': 'animate',
        'values': df['date_minus_time'],
        'visible': True
    }


    # Store the map data
    data = []

    # name is each magnitude, group is each data
    for name, group in grouped:
        trace = dict(
            # mag = group[ group['key'] == name]['mag']
            lat=group['latitude'],
            lon=group['longitude'],
            text=group['place'] + '<br>Magnitude: ' + group['mag'].astype(str) + '<br>Depth: ' + group['depth'].astype(str)
                + ' km <br>Time: ' + group['converted_time'].astype(str),
            name='{0}'.format(name) + "<br><br><br>",
            marker=dict(
                size=group['radius'],
                color=group['color'],
                line=dict(width=0.5, color='rgb(40,40,40)'),
                sizemode='area'
            ),
            type='scattermapbox'
        )
        data.append(trace)

    frames = []
    sliders_dict = {
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 20},
            'prefix': 'Date:',
            'visible': True,
            'xanchor': 'center'
        },
        'transition': {'duration': 300, 'easing': 'cubic-in-out'},
        'pad': {'b': 10, 't': 50},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
        'steps': []
    }

    grouped = df.groupby('date_minus_time')
    for name, group in grouped:
        frame = {'data': [], 'name': str(name)}
        trace = dict(
            # mag = group[ group['key'] == name]['mag']
            lat=group['latitude'],
            lon=group['longitude'],
            text=group['place'] + '<br>Magnitude: ' + group['mag'].astype(str) + '<br>Depth: ' +
                 group['depth'].astype(str) + ' km <br>Time: ' + group['time'],
            name='{0}'.format(name) + "<br><br><br>",
            marker=dict(
                size=group['radius'],
                color=group['color'],
                line=dict(width=0.5, color='rgb(40,40,40)'),
                sizemode='area'
            ),
            type='scattermapbox'
        )
        frame['data'].append(trace)
        frames.append(frame)
        slider_step = {'args': [
            [str(name)],
            {'frame': {'duration': 300, 'redraw': False},
             'mode': 'immediate',
             'transition': {'duration': 300}}
        ],
            'label': str(name.date()),
            'method': 'animate'}
        sliders_dict['steps'].append(slider_step)

    layout['sliders'] = [sliders_dict]
    fig = dict(data=data, layout=layout, frames=frames)
    plot(fig, validate=False, filename='d3-bubble-map-populations.html')


graph()
