# # from plotly import __version__
# # from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# # from plotly.graph_objs import Scatter, Figure, Layout
# # import pandas as pd
# # import datetime
# # import numpy as np
# #
# #
# # df = pd.read_csv("../data/query.csv", header=0)
# # A = df.as_matrix()
# # time = A[:, 0]
# # latitude = A[:, 1]
# # longitude = A[:, 2]
# # depth = A[:, 3]
# # mag = A[:, 4]
# # place = A[:, 13]
# #
# #
# # df['text'] = df['place'] + '<br>Magnitude ' + (df['mag']).astype(str)
# # limits = [(0,3), (4,5), (6,7), (8,9), (10, 11)]
# # colors = ["rgb(255,65,54)", "rgb(0,116,217)","rgb(133,20,75)","rgb(255,133,27)", "lightgrey"]
# # cities = []
# # scale = 100
# #
# # # for i in range(len(limits)):
# # #     lim = limits[i]
# # #     df_sub = df[lim[0]:lim[1]]
# # #     city = dict(
# # #         type = 'scattergeo',
# # #         locationmode = 'country names',
# # #         location = df['place'],
# # #         lon = df_sub['longitude'],
# # #         lat = df_sub['latitude'],
# # #         text = df_sub['text'],
# # #         marker = dict(
# # #             size = df_sub['mag']*scale,
# # #             color = colors[i],
# # #             line = dict(width=0.5, color='rgb(40,40,40)'),
# # #             sizemode = 'area'
# # #         ),
# # #         name = '{0} - {1}'.format(lim[0],lim[1]))
# # #     cities.append(city)
# #
# # for i in range(len(mag)):
# #     # selected_color = "rgb(255,65,54)";
# #     # if i <= 3:
# #     #     selected_color = colors[1]
# #     # elif i <= 5:
# #     #     selected_color = colors[2]
# #     # elif i <= 10:
# #     #     selected_color = colors[3]
# #     # else:
# #     #     selected_color = colors[4]
# #     city = dict(
# #             type = 'scattergeo',
# #             locationmode = 'country names',
# #             location = place[i],
# #             lon = longitude[i],
# #             lat = latitude[i],
# #             text = place[i] + "<br>Magnitude " + '{0}'.format(mag[i]),
# #             marker = dict(
# #                 size = mag[i]*scale,
# #                 color = colors[1],
# #                 line = dict(width=0.5, color='rgb(40,40,40)'),
# #                 sizemode = 'area'
# #             ),
# #             name = '{0} - {1}'.format(longitude[i],latitude[i]))
# #     cities.append(city)
# #
# # layout = dict(
# #         title = '2014 US city populations<br>(Click legend to toggle traces)',
# #         showlegend = True,
# #         geo = dict(
# #             scope='world',
# #             projection=dict( type='Orthographic'),
# #             showland = True,
# #             landcolor = 'rgb(217, 217, 217)',
# #             subunitwidth=1,
# #             countrywidth=1,
# #             subunitcolor="rgb(255, 255, 255)",
# #             countrycolor="rgb(255, 255, 255)"
# #         ),
# #     )
# #
# # fig = dict( data=cities, layout=layout )
# # plot( fig, validate=False, filename='d3-bubble-map-populations.html')
#
#
#
#
#
# from plotly import __version__
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# from plotly.graph_objs import Scatter, Figure, Layout
# import pandas as pd
# import datetime
# import numpy as np
#
#
# df = pd.read_csv("../data/query.csv", header=0)
# A = df.as_matrix()
# time = A[:, 0]
# latitude = A[:, 1]
# longitude = A[:, 2]
# depth = A[:, 3]
# mag = A[:, 4]
#
# df['text'] = df['place'] + '<br>Magnitude ' + (df['mag']).astype(str)
# limits = [(0,5), (6,10), (11,20), (21,30), (31, 50)]
# colors = ["rgba(255,65,54, 0.2)", "rgba(0,116,217, 0.2)","rgba(133,20,75, 0.2)","rgba(255,133,27, 0.2)", "rgba(255,133,27, 0.2)"]
# cities = []
# scale = 80
#
# for i in range(len(limits)):
#     lim = limits[i]
#     df_sub = df[lim[0]:lim[1]] # List from row(lim[0]) to row(lim[1]) in df
#     city = dict(
#         type = 'scattergeo',
#         locationmode = 'country names',
#         location = df['place'],
#         lon = df_sub['longitude'],
#         lat = df_sub['latitude'],
#         text = df_sub['text'],
#         marker = dict(
#             size = scale/(i+1),
#             color = colors[i],
#             line = dict(width=0.5, color='rgb(40,40,40)'),
#             sizemode = 'area'
#         ),
#         name = '{0} - {1}'.format(lim[0],lim[1]) + "<br><br><br><br><br><br>")
#     cities.append(city)
#
# layout = dict(
#         title = '2014 US city populations<br>(Click legend to toggle traces)',
#         showlegend = True,
#         geo = dict(
#             scope='world',
#             projection=dict( type='Orthographic'),
#             showland = True,
#             landcolor = 'rgba(217, 217, 217)',
#             subunitwidth=1,
#             countrywidth=1,
#             subunitcolor="rgb(255, 255, 255)",
#             countrycolor="rgb(255, 255, 255)"
#         ),
#     )
#
# fig = dict( data=cities, layout=layout )
# plot( fig, validate=False, filename='d3-bubble-map-populations.html')