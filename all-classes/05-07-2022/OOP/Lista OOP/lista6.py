class Tamagochi:
    def __init__(self,nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_Nome(self):
        self.nome = input('Escreva seu novo nome: ')

    