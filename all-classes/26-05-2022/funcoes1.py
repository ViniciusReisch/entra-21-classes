def triangulo():
    medidas = []
    medida = 0
    for i in range(3):
        medida = int(input("Escreva uma medida de triângulo: "))
        medidas.append(medida)
    return medidas


def verifTriangulo(medidas):
    if medidas[0] + medidas[1] > medidas[2] or medidas[2] + medidas[1] > medidas[0] or medidas[2] + medidas[0] > medidas[1]:
        if medidas[0] == medidas[1] and medidas[1] != medidas[2] or medidas[2] == medidas[1] and medidas[1] != medidas[0] or medidas[2] == medidas[0] and medidas[0] != medidas[1]:
            print("O Triângulo é possivel e é Isóceles")
        elif medidas[0] != medidas[1] != medidas[2]:
            print("O Triângulo é possivel e é Escaleno")
        else:
            print("O Triângulo é possivel e é Equilátero")
    else:
        print("O Triângulo é impossivel")