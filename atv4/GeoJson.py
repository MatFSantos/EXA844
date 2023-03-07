from xml.sax import make_parser
from atv3.Listener import Listener
import json

parser =  make_parser()

Handler = Listener(print=False)
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("../atv3/map.osm")

with open("establishments.json", "w") as arquivo:
  json.dump({
    "type": "FeatureCollection",
    "features": Handler.establishments,
  }, arquivo, indent=2, ensure_ascii=False)