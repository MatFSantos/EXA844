from xml.dom.minidom import parse
import time
import json

map = parse("map.osm")
i = 0
print("Starting DOM Parser...")
start_time = time.time()
estabelecimentos = []
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
            estabelecimentos.append({
                "number": i,
                "type": type,
                "name": name,
                "lat": lat,
                "lon": lon,
            })
            print(f"""Estabelecimento [{i}]:""")
            print(f"""          tipo: {type} ; nome: {name if name else "não informado"} ; latitude: {lat} ; longitude: {lon}""")
end_time = time.time()
with open("establishmentsDOM.json", "w") as arquivo:     
    json.dump(estabelecimentos, arquivo, indent=4, ensure_ascii=False)


print(f"Tempo de execução do DOM Parser: {end_time - start_time} segundos")