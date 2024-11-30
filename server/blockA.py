import folium


def block_a(m, data, index):
    color = data["color"]
    loc = data["building"][index]["loc"]
    weight = data["weight"]
    name = data["building"][index]["name"]
    folium.Polygon(
        locations=loc,
        color=color,
        weight=weight,
        fill_color= color,
        fill_opacity=1,
        fill=True,
        popup=name)
    
