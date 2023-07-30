import folium
import pandas as pd
map = folium.Map(location=[-5.905472, 34.007870], zoom_start=6, tiles = "Stamen Terrain")
#Adding a marker
fg = folium.FeatureGroup(name="Tanzanian map")
fg.add_child(folium.Marker(location=[-1.282301, 31.781384], popup="Kihome boy", icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[-6.139816, 35.738931], popup="Capital city", icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[-5.072118, 39.102198], popup="Mikanjuni stadium", icon=folium.Icon(color="green")))

#For passing coordinates from the file
data = pd.read_csv("F:/TUTORIALS/The Python Mega Course Build 10 Real World Applications/17. Application 2 Create Webmaps with Python and Folium/4.1 Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])
status = list(data["STATUS"])

fgv=folium.FeatureGroup(name="Volcanoes")
for lt,lon,el,stat in zip(lat,long,elev,status):
    if el<1000:
        color="green"
    elif 1000<=el<=3000:
        color="orange"
    else:
        color="red"
    # Adding attributes to a feature groug
    # fg.add_child(folium.Marker(location=[lt,lon], popup=str(el)+" m, "+stat, icon=folium.Icon(color=color), tooltip=stat))

    # Creating a round marker
    
    fgv.add_child(folium.CircleMarker(location=[lt,lon], popup=str(el)+" m, "+stat, radius=7, 
                                      fill_color=color, color="grey", fill_opacity=0.8, tooltip=stat ))
#Adding geojson colors
fgp= folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(open("F:/TUTORIALS/The Python Mega Course Build 10 Real World Applications/17. Application 2 Create Webmaps with Python and Folium/world.json",
                                   "r", encoding="UTF-8-sig").read(), style_function=lambda x: {"fillColor": "orange" 
                                                                                                if x["properties"]["POP2005"]<100000000 
                                                                                                else "green" if 100000000 >=
                                                                                                x ["properties"]["POP2005"]<=20000000 else "red" }))

map.add_child(fg)
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")