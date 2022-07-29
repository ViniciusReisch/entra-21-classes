boleano = 0
string = 0
decimal = 0
inteiro = 0
lista = []
while True:
    x = input("Escreva um valor: ")
    if x == "":
        break
    if x == "True":
        boleano += 1
        lista.append(bool(x))
    elif x == "False":
        boleano += 1
        lista.append(bool(False))
    else:
        try:
            valorDecimal = float(x)
            if valorDecimal % 1 == 0:
                inteiro += 1
                lista.append(int(x))
            else:
                decimal += 1
                lista.append(float(x))
        except:
            string += 1
            lista.append(x)
lista.reverse()
print(f"Lista Invertida {lista}"
          f"\nForam registrados um total de {boleano} valores boleanos"
          f"\nForam registrados um total de {inteiro} valores inteiros"
          f"\nForam registrados um total de {decimal} valores decimais"
          f"\nForam registrados um total de {string} valores string")