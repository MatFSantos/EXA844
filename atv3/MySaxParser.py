import xml.sax
import time
import json

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.num = 0
    self.lon = ""
    self.lat = ""
    self.type = ""
    self.name = ""
    self.establishments = []

  def startElement(self, tag, attributes):    
    
    if tag =="node":
      self.lon = attributes.get("lon")
      self.lat = attributes.get("lat")
    if tag == "tag":
        if attributes.get("k") == "amenity":
            self.type = attributes.get("v")
            self.num += 1
        elif attributes.get("k") == "name":
            self.name = attributes.get("v")

  def endElement(self, tag):
    if tag =="node":
      if self.type != "":
        print(f"""Estabelecimento [{self.num}]:""")
        print(f"""          tipo: {self.type} ; nome: {self.name if self.name else "não informado"} ; latitude: {self.lat} ; longitude: {self.lon}""")
        self.establishments.append({
          "number": self.num,
          "type": self.type,
          "name": self.name,
          "lat": self.lat,
          "lon": self.lon,
        })
      self.clear()

  def clear(self):
    self.type = ""
    self.name = ""
    self.lat = ""
    self.lon = ""

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
start_time = time.time()
parser.parse("map.osm")
end_time = time.time()

with open("establishmentsSAX.json", "w") as arquivo:     
    json.dump(Handler.establishments, arquivo, indent=4, ensure_ascii=False)

print(f"Tempo de execução do SAX Parser: {end_time - start_time} segundos")