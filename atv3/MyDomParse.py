from xml.dom.minidom import parse
import time

map = parse("map.osm")
i = 0
print("Starting DOM Parser...")
start_time = time.time()
for node in map.getElementsByTagName("node"):
    tags = node.getElementsByTagName("tag")
    if tags.length > 0:
        type = None
        name = None
        for tag in tags:
            if tag.getAttribute("k") == "amenity":
                type = tag.getAttribute("v")
                i += 1
            elif tag.getAttribute("k") == "name" and type != None:
                name = tag.getAttribute("v")
        if type != None:
            lat = node.getAttribute("lat")
            lon = node.getAttribute("lon")
            print(f"""Estabelecimento [{i}]:""")
            print(f"""          tipo: {type} ; nome: {name if name else "não informado"} ; latitude: {lat} ; longitude: {lon}""")
end_time = time.time()

print(f"Tempo de execução do DOM Parser: {end_time - start_time} segundos")