'''
                    COVID FINAL MAP
                    ===============
    This is the final map
    It contains covid data of World as well as India
    
    I've used test.py and test1.py to manipulate and clean the data.
    Extracted only required columns from csv files & injected those values into geojson of world & india 
    as key-value pairs.
'''

import folium, pandas

map = folium.Map(location = [20.5937, 78.9629], zoom_start=4, tiles="CartoDB positron")

fg1 = folium.FeatureGroup("World wide")   
fg2 = folium.FeatureGroup("India wide",show=False)   

gjson1 = folium.GeoJson(data= open("covid_world.json","r",encoding="utf-8-sig").read(),
                       style_function=lambda x :{'fillColor':'green' if type(x['properties']['active'])==str 
                                                 else 'green' if x['properties']['active']<1000
                                                 else 'orange' if 1000 <x['properties']['active']<50000 else 'red'})

folium.features.GeoJsonTooltip(
    fields = ('NAME','active','confirmed','recovered','deaths'),
    aliases=('Country: ','Active: ','Confirmed: ','Recovered: ','Deaths: '),
    localize=True,    
    ).add_to(gjson1)

fg1.add_child(gjson1)

gjson2 = folium.GeoJson(data= open('covid_india.json','r',encoding='utf-8-sig').read(),
                        style_function=lambda x :{'fillColor':'green' if x['properties']['active']<5000 
                                                  else 'orange' if 5000 <= x['properties']['active']< 20000 
                                                  else 'red'})

folium.features.GeoJsonTooltip(
    fields = ('NAME_1','confirmed','active','recovered','death'),
    aliases=('State: ','Total Confirmed: ','Active: ','Recovered: ','Deaths: '),
    localize=True,    
    ).add_to(gjson2)

fg2.add_child(gjson2)

map.add_child(fg1)
map.add_child(fg2)

folium.TileLayer(tiles="OpenStreetMap").add_to(map)
folium.TileLayer(tiles="Stamen Terrain").add_to(map)
folium.TileLayer(tiles="Stamen Toner").add_to(map)
folium.TileLayer(tiles="Stamen Watercolor").add_to(map)
folium.TileLayer(tiles="CartoDB dark_matter").add_to(map)

map.add_child(folium.LayerControl())
title_html = '''
             <h6 align="center" style="font-size:15px"><b>Covid Data Visualization - Sai Teja Erukude</b></h6>
             '''
map.get_root().html.add_child(folium.Element(title_html))

map.save('Covid.html')
print('Your final covid map is ready.')