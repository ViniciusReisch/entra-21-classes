from bs4 import BeautifulSoup
import requests
from operator import itemgetter


valores = []
geral = []
produtos = []
for i in range(60):
    alvo = f'https://www.bistek.com.br/bebidas/vinhos-e-espumantes.html?p={i}'
    response = requests.get(alvo)
    html = BeautifulSoup(response.text, 'html.parser')

    for produto in html.select('.product-item-link'):
        produtos.append(produto.text.strip())

    for valor in html.select('.price-wrapper .price'):
        valores.append(float(valor.text.strip().replace('R$', '').replace(',', '.')))

for i in range(len(produtos)):
    dic = {'Produto': produtos[i], 'Valor': valores[i]}
    geral.append(dic)

geral_novo = sorted(geral, key=itemgetter('Valor'))

for i in geral_novo:
    print(i)

