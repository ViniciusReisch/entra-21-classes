class Bola:
    def __init__(self, circunferencia, cor, material):
        self.circunferencia = circunferencia
        self.cor = cor
        self.material = material

    def troca_Cor(self, new_cor):
        self.cor = new_cor

    def mostra_Cor(self):
        print(f'Nova cor atribuida para bola {self.cor}')
