class Pessoa:
    # atributos
    def __init__(self, idade, sexo, nome):
        self.idade = idade
        self.sexo = sexo
        self.nome = nome


pessoa1 = Pessoa(16, 'Masculino', 'Vinicius')
pessoa2 = Pessoa(18, 'Masculino', 'Nunes')

print(pessoa1.nome)