import requests
from bs4 import BeautifulSoup
 
pagina = requests.get('http://www.uninove.br')
 
sopa = BeautifulSoup(pagina.text, 'html.parser')
 
# encontra todos os paragrafos
uninove = sopa.find_all('p')
 
for i in uninove:
    print(i.prettify())
 
input('Tecle ENTER para sair...')