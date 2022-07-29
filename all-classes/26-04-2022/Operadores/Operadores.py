lado1 = float(input("Escreva o lado de um retângulo em metros: "))
lado2 = float(input("Escreva o segundo lado de um retângulo em metros: "))

print(f'O perimetro do quadrado é igual: {lado1 * 2 + lado2 * 2}m' )
print(f'O área em metros do quadrado é igual: {lado1 * lado2}m²' )
print(f'O área em centímetros do quadrado é igual: {((lado1 * lado2)*100)*100}cm²' )
print(f'Nesse terreno podem ser plantados {(lado1 * lado2) // 3}')