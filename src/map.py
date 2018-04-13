# import pandas as pd
# import folium
#
# chiba_cities = pd.DataFrame({
#     'city': ['千葉市', '館山市', '銚子市', '浦安市'],
#     'latitude': [35.607451, 34.996596, 35.734795, 35.653146],
#     'longtude': [140.106340, 139.869906, 140.826926, 139.902058],
#     'population': [975535, 46349, 61674, 168169]
# })
#
# chiba_map = folium.Map(location=[35.607451, 140.106340], tiles='Stamen Toner', zoom_start=5)
#
# for i, r in chiba_cities.iterrows():
#     temp = r['population']
#     print(temp)
#     folium.CircleMarker([r['latitude'], r['longtude']],
#                         radius=500,
#                         popup=r['city'],
#                         color='red',
#                         fill=True,
#                         fill_color='red',
#                         ).add_to(chiba_map)
# fn = "html/map.html"
# chiba_map.save(fn)
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
fig = plt.figure(num=None, figsize=(12, 8) )
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
plt.title("Mercator Projection")

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6,
            lat_0=45, lon_0=-100,)
m.etopo(scale=0.5, alpha=0.5)

# Map (long, lat) to (x, y) for plotting
x, y = m(-122.3, 47.6)
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Seattle', fontsize=12);
plt.title("Mercator Projection")