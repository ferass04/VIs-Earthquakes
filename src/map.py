import pandas as pd
import folium

chiba_cities = pd.DataFrame({
    'city': ['千葉市', '館山市', '銚子市', '浦安市'],
    'latitude': [35.607451, 34.996596, 35.734795, 35.653146],
    'longtude': [140.106340, 139.869906, 140.826926, 139.902058],
    'population': [975535, 46349, 61674, 168169]
})

chiba_map = folium.Map(location=[35.607451, 140.106340], zoom_start=9)

for i, r in chiba_cities.iterrows():
    folium.CircleMarker(location=[r['latitude'], r['longtude']], popup=r['city']).add_to(chiba_map)

chiba_map.save("../html/map.html")