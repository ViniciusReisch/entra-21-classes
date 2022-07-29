nome1 = input("escreva um nome: ")
nome2 = input("escreva um nome: ")

if nome1.__len__() > nome2.__len__():
    print(f'Nome {nome1} tem mais caracteres que {nome2}')

elif nome1.__len__() == nome2.__len__():
    print(f'Nome {nome1} tem a mesma quantidade de caracteres que {nome2}')

else:
    print(f'Nome {nome2} tem mais caracteres que {nome1}')