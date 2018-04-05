import pandas as pd
import folium

chiba_cities = pd.DataFrame({
    'city': ['千葉市', '館山市', '銚子市', '浦安市'],
    'latitude': [35.607451, 34.996596, 35.734795, 35.653146],
    'longtude': [140.106340, 139.869906, 140.826926, 139.902058],
    'population': [975535, 46349, 61674, 168169]
})

chiba_map = folium.Map(location=[35.607451, 140.106340], zoom_start=5)

for i, r in chiba_cities.iterrows():
    temp = r['population']
    print(temp)
    folium.CircleMarker([r['latitude'], r['longtude']],
                        radius=temp/10000,
                        popup=r['city'],
                        color='red',
                        fill=True,
                        fill_color='red',
                        ).add_to(chiba_map)
fn = "html/map.html"
chiba_map.save(fn)

import os
import time
from selenium import webdriver

tmpurl = "file://{path}/{mapfile}".format(path=os.getcwd(),mapfile=fn)
print(tmpurl)

browser = webdriver.Chrome()
browser.get(tmpurl)
#Give the map tiles some time to load
# time.sleep(1)
browser.save_screenshot('screenshots/map1.png')
browser.quit()
