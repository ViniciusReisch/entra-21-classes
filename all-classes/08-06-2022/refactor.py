import pandas as pd
from operator import itemgetter


# Recebendo os valores do .json
df = pd.read_json (r'C:\Users\vinicius.reisch\PycharmProjects\pythonProject\main\main\dados.json')
precos = []
lojas = []
dic = {}
lista1 = [df]
lista = []

# Transformando os preços em float
for i in range(len(lista1[0]['Preco'])):
    x = lista1[0]['Preco'][i].replace("R$", '')
    x = x.replace(".", '')
    x = x.replace(",", ".")
    precos.append(float(x))

# Ordenando os nomes de loja na posição dos preços
for i in range(len(lista1[0]['Loja'])):
    lojas.append(lista1[0]['Loja'][i])

# Ordenando os valores em Dicionario
print(lojas,precos)
for i in range(len(lista1[0]['Loja'])):
    dic = {lojas[i]: precos[i]}
    lista.append(dic)
    dic = {}
print(lista)


# Obtendo o menor preço
dic_new = sorted(dic.items(), key=itemgetter(1), reverse=True)

