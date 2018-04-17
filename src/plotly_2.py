# from plotly import __version__
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# from plotly.graph_objs import Scatter, Figure, Layout
# import pandas as pd
# import datetime
# import numpy as np
#
# A = usgs
# time = A[:, 0]
# latitude = A[:, 1]
# longitude = A[:, 2]
# depth = A[:, 3]
# mag = A[:, 4]
#
# df['text'] = df['place'] + '<br>Magnitude ' + (df['mag']).astype(str)
# limits = [(0,3), (4,5), (6,7), (8,9), (10, 11)]
# colors = ["rgb(255,65,54)", "rgb(0,116,217)","rgb(133,20,75)","rgb(255,133,27)", "lightgrey"]
# cities = []
# scale = 100
#
# for i in range(len(limits)):
#     lim = limits[i]
#     df_sub = df[lim[0]:lim[1]]
#     city = dict(
#         type = 'scattergeo',
#         locationmode = 'country names',
#         location = df['place'],
#         lon = df_sub['longitude'],
#         lat = df_sub['latitude'],
#         text = df_sub['text'],
#         marker = dict(
#             size = df_sub['mag']*scale,
#             color = colors[i],
#             line = dict(width=0.5, color='rgb(40,40,40)'),
#             sizemode = 'area'
#         ),
#         name = '{0} - {1}'.format(lim[0],lim[1]))
#     cities.append(city)
#
# layout = dict(
#         title = '2014 US city populations<br>(Click legend to toggle traces)',
#         showlegend = True,
#         geo = dict(
#             scope='world',
#             projection=dict( type='Orthographic'),
#             showland = True,
#             landcolor = 'rgb(217, 217, 217)',
#             subunitwidth=1,
#             countrywidth=1,
#             subunitcolor="rgb(255, 255, 255)",
#             countrycolor="rgb(255, 255, 255)"
#         ),
#     )
#
# fig = dict( data=cities, layout=layout )
# plot( fig, validate=False, filename='d3-bubble-map-populations.html')