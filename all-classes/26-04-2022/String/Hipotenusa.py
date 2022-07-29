cateto1 = int(input("Escreva o valor de um cateto: "))
cateto2 = int(input("Escreva o valor de mais um cateto "))

hipotenusa = cateto1 ** 2 + cateto2 ** 2
hipotenusa = hipotenusa ** 0.5

print(f'O valor da Hipotenusa é igual a: {hipotenusa}')