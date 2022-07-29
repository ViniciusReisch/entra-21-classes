lado1 = float(input("Escreva um lado do triângulo: "))
lado2 = float(input("Escreva um lado do triângulo: "))
lado3 = float(input("Escreva um lado do triângulo: "))

if lado1 + lado2 > lado3 or lado3 + lado2 > lado1 or lado3 + lado1 > lado2:
    if lado1 == lado2 and lado2 != lado3 or lado3 == lado2 and lado2 != lado1 or lado3 == lado1 and lado1 != lado2:
        print("O Triângulo é possivel e é Isóceles")
    elif lado1 != lado2 != lado3:
        print("O Triângulo é possivel e é Escaleno")
    elif lado1 == lado2 == lado3:
        print("O Triângulo é possivel e é Equilátero")
else:
    print("O Triângulo é impossivel")
