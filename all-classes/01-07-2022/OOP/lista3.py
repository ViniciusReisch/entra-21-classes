class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_Valor(self, valorLado):
        if valorLado == '1':
            comprimento = float(input('Qual o novo valor do comprimento? '))
            self.ladoA = comprimento
        if valorLado == '2':
            altura = float(input('Qual o novo valor da altura'))
            self.ladoB = altura

    def retornar(self):
        print(f'O valor atual dos lados do retangulo é de {self.ladoA} x {self.ladoB}')

    def area(self):
        print(f'A area do retangulo é de {self.ladoA*self.ladoB}')

    def perimetro(self):
        print(f'O perimetro do retangulo é de {self.ladoA*2 + self.ladoB*2}')