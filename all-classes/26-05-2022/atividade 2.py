def contador(palavra, x):
    print(f"Existem {palavra.count(x)} {x} letras na palavra {palavra}")


final = contador(input("Escreva uma palavra: "), input("Escreva uma letra:"))
