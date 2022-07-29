from lista3 import Retangulo

retangulo = Retangulo(ladoA=float(input('Informe o comprimento: ')),
                      ladoB=float(input('Informe a altura: ')))

retangulo.area()
retangulo.perimetro()
while True:
    retangulo.mudar_Valor(valorLado=input('Mudar valores do perimetro'
                                      '\n[1] Comprimento'
                                      '\n[2] Altura'))
    retangulo.retornar()
    retangulo.area()
    retangulo.perimetro()