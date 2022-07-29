lista = []
while True:
    data = int(input("Qual seu ano de nascimento? "))
    if data == 0:
        break
    nome = input("Digite seu nome.txt: ")
    CTPS = int(input("Escreva o numero da sua carteira de traalho"))
    if CTPS != 0:
        ano = int(input("Qual seu ano de contratação? "))
        sal = int(input("Qual seu salario? "))
    idade = 2022 - data
    dic = {'Idade: ': idade, 'Nome: ': nome, 'CTPS: ': CTPS, 'Vai se aposentar em': 65 - idade}
    lista.append(dic)
    dic = {}
print(lista)
