def converter(valor):
    numConvertido = valor/1048576
    return numConvertido


def percentual(numero):
    perc = (numero/2581.57) * 100
    return perc

arquivo = open("usuarios.txt", "rt", encoding="utf-8")
nomes = arquivo.read().splitlines()
lista = []
dic = {}

print("ACME Inc.               Uso do espaço em disco pelos usuários")
print(100*'-')
print("Nr.  Usuário        Espaço utilizado     % do uso")
for i in range(len(nomes)):
    nomes1 = nomes[i].split()
    dic[nomes1[0]] = round(converter(int(nomes1[1])), 2)

for k, v in dic.items():
    numPerc = round(percentual(v), 2)
    print(f'{str(k): <20}{str(v) + "MB": <21}{str(numPerc) + "%": <20}')
