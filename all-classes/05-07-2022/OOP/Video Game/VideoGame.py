class Console:
    def __init__(self, controle,armazenamento,midia, marca, cor='Preto'):
        self.controle = controle
        self.armazenamento = armazenamento
        self.midia = midia
        self.marca = marca
        self.cor = cor

    def ligar(self):
        print(f'Ligando o video gama {self.marca}')

    def desligar(self):
        print(f'Desligando o video game {self.marca}')


class Playstation(Console):
    def __init__(self, controle, armazenamento, midia, marca='Playstation'):
        super().__init__(controle, armazenamento, midia, marca)
        self.marca = marca

    def bugar(self):
        print('Bugou')


vd1 = Console(2, 'SSD', 'online', 'Nintendo', 'azul')
vd2 = Playstation(1, 'SSD', 'Online')

print(vd2.marca)
