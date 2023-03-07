from xml.sax import ContentHandler

class Listener(ContentHandler):
  def __init__(self, print):
    self.num = 0
    self.lon = ""
    self.lat = ""
    self.type = ""
    self.name = ""
    self.print = print
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
        if self.print:
          print(f"""Estabelecimento [{self.num}]:""")
          print(f"""          tipo: {self.type} ; nome: {self.name if self.name else "não informado"} ; latitude: {self.lat} ; longitude: {self.lon}""")
        else:
          self.establishments.append({
            "type": "Feature",
            "geometry": {
            "type":"Point",
            "coordinates": [float(self.lon), float(self.lat)],
            },
            "properties": {
            "name": self.name if self.name else "",
            "type": self.type,
            }
          })
      self.clear()

  def clear(self):
    self.type = ""
    self.name = ""
    self.lat = ""
    self.lon = ""
