class Carro:
    def __init__(self, consumo, tanque=0.0, capacidade=50.0):
        self.consumo = consumo
        self.tanque = tanque
        self.capacidade = capacidade

    def andar(self, quilometro):
        consumo = quilometro / self.consumo
        if self.tanque < consumo:
            print('Você não possui gasolina o bastante para o percurso')
        else:
            print(f'O consumo para o percurso vai ser de {round(consumo, 2)}L')
            self.tanque -= consumo

    def adicionar_gasolina(self, quantidade):
        if quantidade > self.capacidade:
            print('O tanque não suporta tanta gasolina')
        else:
            self.tanque += quantidade

    def obter_Gasolina(self):
        print(f'Quantidade de gasolina no tanque é de {round(self.tanque, 2)}L')

