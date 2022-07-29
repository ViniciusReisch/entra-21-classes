from bs4 import BeautifulSoup
import requests

produtos = []
promocao = []
precos = []
geral = []


alvo = "https://www.pichau.com.br/promocao/stranger?utm_source=home&utm_medium=banner&utm_campaign=stranger"
response = requests.get(alvo)
html = BeautifulSoup(response.text, 'html.parser')

for produto in html.select('h2'):
    produtos.append(produto.text)
for preco in html.select('a div div:nth-child(1) div span+ div'):
    precos.append(preco.text)

print(produtos, precos)
produtos.a