from bs4 import BeautifulSoup
import requests
import arrow

produtos = []
precos = []
promo = []

for i in range(306):
    link = requests.get(f'https://www.kabum.com.br/ofertas/julhogamer?pagina={i}')
    html = BeautifulSoup(link.text, 'html.parser')

    for produto in html.select('nameCard'):
        produtos.append(produto.text.strip())

    for preco in html.select('.priceCard'):
        precos.append(preco.text.strip())

print(produtos, precos)