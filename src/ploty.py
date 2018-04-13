from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import pandas as pd

from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML

import pandas as pd


def test(events):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
    df.head()

    df['text'] = df['name'] + '<br>Population ' + (df['pop'] / 1e6).astype(str) + ' million'
    limits = [(0, 2), (3, 10), (11, 20), (21, 50), (50, 3000)]
    colors = ["rgb(0,116,217)", "rgb(255,65,54)", "rgb(133,20,75)", "rgb(255,133,27)", "lightgrey"]
    cities = []
    scale = 5000
    lats = []
    lons = []
    for event in events:
        lats.append(event.latitude)

    for event in events:
        lons.append(event.longitude)

    # layout = dict(
    #     title='2014 US city populations<br>(Click legend to toggle traces)',
    #     showlegend=True,
    #     geo=dict(
    #         scope='world',
    #         showland=True,
    #         landcolor='rgb(217, 217, 217)',
    #         subunitwidth=1,
    #         countrywidth=1,
    #         subunitcolor="rgb(255, 255, 255)",
    #         countrycolor="rgb(255, 255, 255)"
    #     ),
    # )

    # fig = dict(data=cities, layout=layout)
    # plot(fig, validate=False, filename='d3-bubble-map-populations')

    trace = dict(
        type='scattergeo',
        lon=lons, lat=lats, mode='markers')
    plot([trace])
