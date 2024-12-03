import folium
import branca
from coordinates_corp import corp
from coordinates_dormitories import dormitories

def block_a(m):
    color = corp["color"]
    weight = corp["weight"]
    for i in range (len(corp["building"])):
        locat = corp["building"][i]["loc"]
        name = corp["building"][i]["name"]
        html = f"""
            <body style=background-color:PaleTurquoise>
            <h1> <font face="impact" size="7" color="DarkBlue"> {corp["building"][i]["name"]} </font></h1>
            <p><font face="Arial" size="3"> {corp["building"][i]["address"]} </font></p>
            <p><font face="Arial" size="3"> {corp["building"][i]["info"]} </font></p>
            <img src={corp["building"][i]["img"]} width=490 height=280>
        """
        iframe = branca.element.IFrame(html=html, width=510, height=500)
        popup = folium.Popup(iframe, max_width=500)
        folium.Polygon(
            locations=locat,
            color=color,
            weight=weight,
            fill_color= color,
            fill_opacity=0.3,
            fill=True,
            popup=popup,
            tooltip=name).add_to(m)

def block_b(m):
    color = dormitories["color"]
    weight = dormitories["weight"]
    for j in range (len(dormitories["building"])):
        locat = dormitories["building"][j]["loc"]
        name = dormitories["building"][j]["name"]
        html = f"""
            <h1> <font face="impact" size="7" color="gray"> {dormitories["building"][j]["name"]} </font></h1>
            <p><font face="Arial" size="3"> {dormitories["building"][j]["address"]} </font></p>
            <p><font face="Arial" size="3"> {corp["building"][j]["info"]} </font></p>
            <img src={dormitories["building"][j]["img"]} width=300 height=280>
        """
        iframe = branca.element.IFrame(html=html, width=510, height=500)
        popup = folium.Popup(iframe, max_width=500)
        folium.Polygon(
            locations=locat,
            color=color,
            weight=weight,
            fill_color= color,
            fill_opacity=0.3,
            fill=True,
            popup=popup,
            tooltip=name).add_to(m)
    
