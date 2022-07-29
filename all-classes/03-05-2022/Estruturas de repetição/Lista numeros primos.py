num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva outro número: "))
cont = 0
div = 0

while num1 < num2:
    while cont <= num1:
        cont += 1
        if num1 == 1:
            print(f'{num1} não é primo')
            break
        if num1 % cont == 0:
            div += 1
        if div > 2:
            break
        elif div == 2 and cont == num1:
            print(f'{num1} é primo')
    div = 0
    cont = 0
    num1 += 1