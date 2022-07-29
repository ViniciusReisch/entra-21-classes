class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def trocar_Tamanho(self, new_lado):
        self.lado = new_lado

    def mostrar_Lado(self):
        print(f'Novo tamanho de lado atribuido {self.lado}')

    def calcular_Area(self):
        print(f'A area do quadrado agora é {int(self.lado) * int(self.lado)}')
