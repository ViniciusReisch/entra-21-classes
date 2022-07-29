from bs4 import BeautifulSoup
import requests
import sqlite3
import arrow

ar = arrow.now().format('DD/MM/YYYY')
conexao = sqlite3.connect('teste do scrapy.db')
cursor = conexao.cursor()

# valores = []
# produtos = []
# for i in range(60):
#     alvo = f'https://www.bistek.com.br/bebidas/vinhos-e-espumantes.html?p={i}'
#     response = requests.get(alvo)
#     html = BeautifulSoup(response.text, 'html.parser')
#
#     for produto in html.select('.product-item-link'):
#         produtos.append(produto.text.strip())
#
#     for valor in html.select('.price-wrapper .price'):
#         valores.append(float(valor.text.strip().replace('R$', '').replace(',', '.')))
#
# for i in range(len(produtos)):
#     cursor.execute('INSERT INTO scrapyT(data, produto, valor) '
#                    'VALUES(?,?,?)', (ar, produtos[i], valores[i]))
#     conexao.commit()

cursor.execute('SELECT * FROM scrapyT WHERE valor > 200')
for linha in cursor.fetchall():
    print(f'{linha[0]} - {linha[1]} - {linha[2]} - {linha[3]:.2f}')
cursor.close()
conexao.close()