from xml.sax import make_parser
from Listener import Listener
import time

parser =  make_parser()
Handler = Listener(print=True)
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
start_time = time.time()
parser.parse("map.osm")
end_time = time.time()

print(f"Tempo de execução do SAX Parser: {end_time - start_time} segundos")