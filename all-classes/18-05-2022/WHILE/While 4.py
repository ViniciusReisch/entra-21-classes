numero = 1
numeroMaior = 0
numeroMenor = 0
numeroMenor = 0
total = 0
a = 0
while numero != 0:
    numero = int(input("Escreva um número: "))
    if numero == 0:
        break
    total += numero
    if a == 0:
        numeroMenor = numero
        numeroMaior = numero
    if numeroMaior > numero:
        numeroMaior = numero
    if numeroMenor < numero:
        numeroMenor = numero
    a += 1
print(f"O maior número é {numeroMaior} e o menor número é {numeroMenor} e a média dos números é de {total/a}")