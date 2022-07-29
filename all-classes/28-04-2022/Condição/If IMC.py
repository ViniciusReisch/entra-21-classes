nome = input("Escreva seu Nome: ")
peso = float(input("Escreva seu Peso em kg: "))
idade = int(input("Escreva sua Idade: "))
altura = float(input("Escreva sua Altura em centimetros: "))

imc = peso / ((altura / 100) ** 2)

if imc < 18.5:
    IMC1 = "Abaixo do peso"
elif imc < 24.9:
    IMC1 = "Peso normal"
elif imc < 29.9:
    IMC1 = "Sobre peso"
elif imc < 34.9:
    IMC1 = "Obesidade grau I"
elif imc < 39.9:
    IMC1 = "Obesidade grau II"
else:
    IMC1 = "Obesidade grau III"

print("-" * 65)
print(f'{nome.upper()} de {idade} anos, de peso {peso}kg e altura de '
      f'{altura/100}m, tem imc de {round(imc , 2)} e está {IMC1}')
print("-" * 65)
