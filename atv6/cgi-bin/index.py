import os
from urllib.parse import parse_qs
import json  
import datetime

qs = os.environ["QUERY_STRING"]
list = parse_qs(qs, encoding="latin-1")
var = list["name"][0]
var2 = list["message"][0]
with open('banco.json', 'r') as openfile: 
    json_object = json.load(openfile) 
json_object["arquivos"].append({"nome":var,"data":str(datetime.datetime.now()),"mensagem":var2})
with open('banco.json', 'w') as outfile: 
    outfile.write(json.dumps(json_object, indent = 4))

print("Content-type: text/html")
print()
print("<html><head><title>Exemplo CGI</title></head><body>")
print("<div style='display: flex; width: 100%; flex-direction: column; align-items: center; justify-content: center; gap: 16px;'>")
for arquivo in json_object["arquivos"]:
    print("Nome = '" + arquivo['nome']+"'" + "<br>   Data =" + arquivo["data"] + "<br>" +"   Mensagem =" + arquivo["mensagem"] + "<br><br><br>")
print("</div></body></html>")