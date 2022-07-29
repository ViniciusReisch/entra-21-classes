while True:
    cont = 0
    div = 0
    primo = int(input("Escreva um numero: "))
    if primo == 0:
        break
    while cont <= primo:
        cont += 1
        if primo == 1:
            print(f'{primo} não é primo')
            break
        if primo % cont == 0:
            div += 1
        if div > 2:
            print(f'{primo} não é primo')
            break
        elif div == 2 and cont == primo:
            print(f'{primo} é primo')
