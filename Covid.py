import folium, pandas

# creating a map object
map = folium.Map(location = [20.5937, 78.9629], zoom_start = 4, tiles = "CartoDB positron")

# creating two feature groups
fg1 = folium.FeatureGroup("World wide")   
fg2 = folium.FeatureGroup("India wide", show=False)   


# creating a geojson object for world wide data and adding style to it
gjson1 = folium.GeoJson(data= open("covid_world.json", "r", encoding="utf-8-sig").read(),
                       style_function=lambda x :{'fillColor':'green' if type(x['properties']['active']) == str 
                                                 else 'green' if x['properties']['active'] < 1000
                                                 else 'orange' if 1000 < x['properties']['active'] < 50000 else 'red'})


# adding tooltips so that the info will be visible when hovered on the map
folium.features.GeoJsonTooltip(
    fields = ('NAME','active','confirmed','recovered','deaths'),
    aliases=('Country: ','Active: ','Confirmed: ','Recovered: ','Deaths: '),
    localize=True,    
    ).add_to(gjson1)

# adding geojson object to feature group
fg1.add_child(gjson1)

# creating a geojson object for India wide data and styling it
gjson2 = folium.GeoJson(data= open('covid_india.json','r',encoding = 'utf-8-sig').read(),
                        style_function=lambda x :{'fillColor':'green' if x['properties']['active'] < 5000 
                                                  else 'orange' if 5000 <= x['properties']['active'] < 20000 
                                                  else 'red'})

# adding tooltip
folium.features.GeoJsonTooltip(
    fields = ('NAME_1','confirmed','active','recovered','death'),
    aliases=('State: ','Total Confirmed: ','Active: ','Recovered: ','Deaths: '),
    localize=True,    
    ).add_to(gjson2)

# adding geojson object to feature group
fg2.add_child(gjson2)

# adding all the feature groups to the map
map.add_child(fg1)
map.add_child(fg2)

# adding different tiles(types of maps) to the map.
folium.TileLayer(tiles="OpenStreetMap").add_to(map)
folium.TileLayer(tiles="Stamen Terrain").add_to(map)
folium.TileLayer(tiles="Stamen Toner").add_to(map)
folium.TileLayer(tiles="Stamen Watercolor").add_to(map)
folium.TileLayer(tiles="CartoDB dark_matter").add_to(map)

# adding a layer control to the map which will be usefull to switch between the layers.
map.add_child(folium.LayerControl())

# creating and adding a title to the map
title_html = '''
             <h6 align="center" style="font-size:15px"><b>Covid Data Visualization - Sai Teja Erukude</b></h6>
             '''
map.get_root().html.add_child(folium.Element(title_html))

# saving the map
map.save('Covid.html')
print('Your covid map is ready.')