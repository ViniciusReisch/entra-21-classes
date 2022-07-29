class Veiculo:
    def __init__(self, cor, ano, modelo, marca, nome):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.nome = nome


carros = []
for i in range(5):
    carro = Veiculo(cor=input('Cor: '), ano=input('Ano: '), modelo=input('Modelo: '), marca=input('Marca: '), nome=input('Nome: '))
    cor = {'Cor': carro.cor}
    ano = {'Ano': carro.ano}
    modelo = {'Modelo': carro.modelo}
    marca = {'Marca': carro.marca}
    nome = {'Nome': carro.nome}
    carros.extend([cor, ano, modelo, marca, nome, "\n"])

print(*carros, end="\n")