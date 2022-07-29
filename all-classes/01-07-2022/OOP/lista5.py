class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_Bucho(self):
        print(f'Bucho: {self.bucho}')

    def digerir(self):
        self.bucho.clear()

