from asyncio import get_event_loop
import pathlib
from turtle import color
from xml.etree.ElementPath import get_parent_map
import folium
from matplotlib.font_manager import json_load
import pandas
import os
import json


data = pandas.read_csv('volcano.csv')
data = data.head(50)


def colur_producer(elevation):

    if elevation <1000:

        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return "red"
 

lat = list(data['Latitude'])
lon = list(data['Longitude'])
vol_name= list(data['Volcano Name'])
elev = list(data['Elev'])

map = folium.Map(location=[28.46,77.28],zoom_start=9)

features=folium.FeatureGroup(name='my_map') 

for lt,ln,v_name,elv in zip(lat,lon,vol_name,elev):

    features.add_child(folium.Marker(location=[lt,ln] ,popup= v_name +' Volcano', icon=folium.Icon(colur_producer(elv))))

# my_world = open('world.json',encoding = 'cp1252').read()

features.add_child(folium.GeoJson(open('world.json',encoding = 'cp1252').read(),
style_function= lambda x: {'fillColor':'yellow'}))
''' if x['properties']['POP2005'] <10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'} ))
'''

map.add_child(features)
map.save('map1.html')
