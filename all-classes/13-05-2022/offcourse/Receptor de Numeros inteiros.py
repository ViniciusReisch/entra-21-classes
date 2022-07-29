while True:
    n1=int(input("Escreva um número: "))
    if n1 == 0:
        break
    n2 = int(input("Escreva um número: "))
    if n2 == 0:
        break
    elif n1 > n2:
        print(f"O maior numero é {n1}")
    elif n1 < n2:
        print(f"O maior numero é {n2}")
    else:
        print(f'O os numeros são iguais')