'''
import requests
import json
rest = requests.get("https://dadosabertos.camara.leg.br/api/v2/deputados?itens=50&pagina=1").json()
for i in rest["dados"]:
    print(i["nome"],i["siglaUf"],i["id"])
print(rest)
'''

from bs4 import BeautifulSoup
import requests
page = requests.get("http://www.oab.org.br/institucionalconselhofederal/quadroadvogados")
soup = BeautifulSoup(page.content, 'html.parser')
dados = []
for body in soup.findAll('tbody'):
    dados.append(body.text)
print (dados[0])
print (dados[1])
print (dados[2])