#!/usr/bin/env python3

import os
from urllib.parse import parse_qs
import json  
import datetime

qs = os.environ["QUERY_STRING"]
list = parse_qs(qs, encoding="latin-1")
var = list["nome"][0]
var2 = list["mensagem"][0]
with open('banco.json', 'r') as openfile: 
    json_object = json.load(openfile) 
json_object["arquivos"].append({"nome":var,"data":str(datetime.datetime.now()),"mensagem":var2})
with open('banco.json', 'w') as outfile: 
    outfile.write(json.dumps(json_object, indent = 4))

print("Content-type: text/html")
print()
print("<html><head><title>Exemplo CGI</title></head><body>")
print("QUERY_STRING = '" + qs + "'<br>")
for arquivo in json_object["arquivos"]:
    print("Nome = '" + arquivo['nome']+"'" + "Data =" + arquivo["data"] + "<br>" +"   Mensagem =" + arquivo["mensagem"] + "<br>")
print("</body></html>")