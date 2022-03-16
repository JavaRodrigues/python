import requests
from bs4 import BeautifulSoup
 
pagina = requests.get('http://www.uninove.br')
 
sopa = BeautifulSoup(pagina.text, 'html.parser')
 
# encontra todos os links
uninove = sopa.find_all('a')
 
for i in uninove:
    print(i.prettify())
 
input('Tecle ENTER para sair...')