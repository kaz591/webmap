import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

for lt, ln, elev in zip(lat, lon,elev):
    map.add_child(folium.CircleMarker(location=[lt, ln], popup=str(elev)+" m", fill_color = color_producer(elev), fill_opacity =0.8, color= "grey"))
#icon=folium.Icon(icon="cloud",color=color_producer(elev))))

map.save("Map1.html")