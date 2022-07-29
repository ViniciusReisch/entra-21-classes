num = []
numero = 1
while numero != 0:
    numero = int(input("Escreva um numero"))
    if numero == 0:
        break
    num.append(numero)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(sum(num))
print(sum(num)/len(num))
