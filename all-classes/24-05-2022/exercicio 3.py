valores = []
boleano = 0
string = 0
decimal = 0
inteiro = 0
while True:
    valor = input("Escreva um valor:")
    if valor == "0":
        break
    if type(valor) == bool:
        boleano += 1
    elif type(valor) == type(int):
        inteiro += 1
    elif type(valor) == type(float):
        decimal += 1
    elif type(valor) == type(str):
        string += 1

    valores.append(valor)
valores.reverse()
print(valores)
print(f"Boleano: {boleano}"
      f"\nString: {string}"
      f"\nDecimal: {decimal}"
      f"\nInteiro: {inteiro}")