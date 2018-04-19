from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
import datetime
import io

# References:
#   https://plot.ly/python/dropdowns/
#   https://plot.ly/python/animations/

# Scale for the radius of circle.
scale = 100
colors_RGB = ["rgb(156, 174, 183)", "rgb(255, 255, 224)", "rgb(137, 195, 235)",
          "rgb(0, 121, 194)", "rgb(255, 255, 10)", "rgb(10, 255, 132)",
          "rgb(240, 128, 128)", "rgb(255, 20, 147)", "rgb(230, 0, 18)"]


colors_RGBA = ["rgba(156, 174, 183, 0.3)", "rgba(255, 255, 224, 0.3)", "rgba(137, 195, 235, 0.3)",
               "rgba(0, 121, 194, 0.4)", "rgba(255, 255, 10, 0.4)", "rgba(10, 255, 132, 0.4)",
               "rgba(240, 128, 128, 0.5)", "rgba(255, 20, 147, 0.5)", "rgba(230, 0, 18, 0.6)"]


circle_size = [4, 8, 12, 16, 24, 40, 56, 80, 140]
# circle_size = [1, 2, 4, 8, 15, 30, 50, 70, 140]


def convert_time(time):
    converted_time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    # print(converted_time.date())
    return converted_time


def get_update_menu(animated):
    animation_menu = dict(
            buttons=[
                {
                    'args': [None, {'frame': {'duration': 500, 'redraw': False},
                                    'fromcurrent': True,
                                    'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                    'label': 'Play',
                    'method': 'animate'
                },
                {
                    'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                                      'transition': {'duration': 0}}],
                    'label': 'Pause',
                    'method': 'animate'
                }],
            # pad={'r': 10, 't': 87},
            direction='up',
            x=0.5,
            xanchor='left',
            y=0.05,
            yanchor='bottom',
            bgcolor='#000000',
            active=99,
            bordercolor='#FFFFFF',
            font=dict(size=11)
        )

    map_menu = dict(
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
            x=0.85,
            xanchor='left',
            y=0.05,
            yanchor='bottom',
            bgcolor='#000000',
            bordercolor='#FFFFFF',
            font=dict(size=11)
        )

    updatemenus = list([])

    if animated:
        updatemenus.append(animation_menu)
    updatemenus.append(map_menu)

    return updatemenus


def get_annotation():
    annotations = list([
        dict(text='World Epic Earthquakes (scroll to zoom when paused)', font=dict(color='magenta', size=14), borderpad=10,
             x=0.05, y=0.05, xref='page', yref='page', align='left', showarrow=False, bgcolor='black'),
    ])

    return annotations


def graph(csv_file, animation):
    # animation = True

    # Load the data
    # df = pd.read_csv("../data/query.csv", header=0)
    # df = pd.read_csv(csv_file, header=0)
    df = pd.read_csv(io.StringIO(csv_file.decode('utf-8')), header=0)

    df["converted_time"] = pd.to_datetime(df["time"]).apply(
        lambda df: datetime.datetime(year=df.year, month=df.month, day=df.day, hour=df.hour, minute=df.minute,
                                     second=df.second))
    df['date_minus_time'] = df["converted_time"].apply(
        lambda df: datetime.datetime(year=df.year, month=df.month, day=df.day))

    # Label for each magnitude group.
    labels = ['Magnitude 1', 'Magnitude 2', 'Magnitude 3', 'Magnitude 4', 'Magnitude 5', 'Magnitude 6', 'Magnitude 7',
              'Magnitude 8', 'Magnitude 9']

    # Group the data by magnitude range (e.g., M1-2, M2-3, M3-4, etc.)
    df['key'] = pd.cut(df['mag'], [1, 2, 3, 4, 5, 6,
                                   7, 8, 9, 10], right=False, labels=labels)

    A = df.as_matrix()
    # time = A[:, 0]
    # latitude = A[:, 1]
    # longitude = A[:, 2]
    # depth = A[:, 3]
    # mag = A[:, 4]
    # place = A[:, 13]
    # c_time = A[:, 23]
    key = A[:, 24]

    # Set the color and radius for each earthquake.
    color_list = []
    radius_list = []
    for each_key in key:
        mag_group = labels.index(each_key)
        color_list.append(colors_RGBA[mag_group])
        radius_list.append(int(circle_size[mag_group] * scale))

    # Add color and radius into the original data.
    df['color'] = color_list
    df['radius'] = radius_list

    # mapboc API key.
    mapbox_access_token = 'pk.eyJ1Ijoia21pbmFtaXNhd2EiLCJhIjoiY2pmeG82bWNmMDIyNzJ3b2RwcDFmOGFxMCJ9.pOlnj41jR4nhv8-dD7f_0Q'

    layout = dict(
        # autosize=False, height=800, width=700,
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

    updatemenus = get_update_menu(animation)
    annotations = get_annotation()

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

    grouped = df.groupby('key')
    # name is each magnitude, group is each data
    for name, group in grouped:
        trace = dict(
            # mag = group[ group['key'] == name]['mag']
            lat=group['latitude'],
            lon=group['longitude'],
            text=group['place'] + '<br>Magnitude: ' + \
                 group['mag'].astype(str) + '<br>Depth: ' + \
                 group['depth'].astype(str)
                 + ' km <br>Time: ' + group['converted_time'].astype(str),
            name='<br>{0}<br>Count: {1}<br>'.format(name, len(group)),
            marker=dict(
                size=group['radius'],
                color=group['color'],
                line=dict(width=0.5, color='rgb(40,40,40)'),
                sizemode='area'
            ),
            type='scattermapbox'
        )
        data.append(trace)

    if animation:
        frames = []
        sliders_dict = {
            'active': 0,
            'yanchor': 'top',
            'xanchor': 'left',
            'currentvalue': {
                'font': {'color': 'magenta', 'size': 24},
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

        grouped_by_date = df.groupby('date_minus_time')
        for each_date_name, each_date_group in grouped_by_date:
            frame = {'data': [], 'name': str(each_date_name)}
            grouped_by_each_date = each_date_group.groupby('key')
            for name, group in grouped_by_each_date:
                trace = dict(
                    # mag = group[ group['key'] == name]['mag']
                    lat=group['latitude'],
                    lon=group['longitude'],
                    text=group['place'] + '<br>Magnitude: ' + group['mag'].astype(str) + '<br>Depth: ' +
                         group['depth'].astype(str) + ' km <br>Time: ' + group['converted_time'].astype(str),
                    name='<br>{0}<br>Count: {1}<br>'.format(name, len(group)),
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
                [str(each_date_name)],
                {'frame': {'duration': 300, 'redraw': False},
                 'mode': 'immediate',
                 'transition': {'duration': 300}}
            ],
                'label': str(each_date_name.date()),
                'method': 'animate'}
            sliders_dict['steps'].append(slider_step)

        layout['sliders'] = [sliders_dict]
        fig = dict(data=data, layout=layout, frames=frames)
        plot(fig, validate=False, filename='../html/earthquake_visualization_animation.html')
    else:
        fig = dict(data=data, layout=layout)
        plot(fig, validate=False, filename='../html/earthquake_visualization_overall.html')


# graph(
#     "https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2011-02-01T00:00:00&endtime=2011-06-01T00:00:00&minmagnitude=3&maxmagnitude=10")
