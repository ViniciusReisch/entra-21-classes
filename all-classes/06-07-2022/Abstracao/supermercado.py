from abc import ABC, abstractmethod


class Supermercado(ABC):
    def __init__(self, validade, preco, nome, compra):
        self.validade = validade
        self.preco = preco
        self.nome = nome
        self.compra = compra

    @abstractmethod
    def comprar(self, dinheiroCarteira):
        return True

    @abstractmethod
    def consumir(self):
        return True

    def estragar(self, dia):
        if dia > self.validade:
            print('Passou da validade')
        else:
            print(f'Ainda faltam {self.validade - dia} dias pra estragar')


class Cerveja(Supermercado):
    def __init__(self, validade, preco, nome, compra, litros):
        super().__init__(validade, preco, nome, compra)
        self.litros = litros

    def comprar(self, dinheiroCarteira):
        if dinheiroCarteira < self.preco:
            print('Você não tem dinheiro')
        else:
            dinheiroCarteira -= self.preco
            print('Compra da cerveja realizada com sucesso')
            self.compra = True

    def consumir(self):
        if self.compra:
            print('Você bebeu, está bebado')
        else:
            print('Você deve comprar primeiro, para beber')


class Cebola(Supermercado):
    def __init__(self, validade, preco, nome, compra, quantidade):
        super().__init__(validade, preco, nome, compra)
        self.quantidade = quantidade

    def comprar(self, dinheiroCarteira):
        if dinheiroCarteira < self.preco:
            print('Você não tem dinheiro')
        else:
            dinheiroCarteira -= self.preco
            print(f'Compra das {self.quantidade} cebolas realizada com sucesso')
            self.compra = True

    def consumir(self):
        if self.compra:
            print('Você comeu uma cebola crua, está maluco?')
        else:
            print('Você deve comprar primeiro, para comer')


class Linguica(Supermercado):
    def __init__(self, validade, preco, nome, compra, peso):
        super().__init__(validade, preco, nome, compra)
        self.peso = peso

    def comprar(self, dinheiroCarteira):
        if dinheiroCarteira < self.preco:
            print('Você não tem dinheiro')
        else:
            dinheiroCarteira -= self.preco
            print(f'Compra de {self.peso}g de linguiça realizada com sucesso')
            self.compra = True

    def consumir(self):
        if self.compra:
            print('HMM')
        else:
            print('Você deve comprar primeiro, para comer')


class Leite(Supermercado):
    def __init__(self, validade, preco, nome, compra, fardos):
        super().__init__(validade, preco, nome, compra)
        self.fardos = fardos

    def comprar(self, dinheiroCarteira):
        if dinheiroCarteira < self.preco:
            print('Você não tem dinheiro')
        else:
            dinheiroCarteira -= self.preco
            print(f'Compra de {self.fardos} fardos de leite realizada com sucesso')
            self.compra = True

    def consumir(self):
        if self.compra:
            print('HMM calcio')
        else:
            print('Você deve comprar primeiro, para beber')


class Salgadinho(Supermercado):
    def __init__(self, validade, preco, nome, compra, tempero):
        super().__init__(validade, preco, nome, compra)
        self.tempero = tempero

    def comprar(self, dinheiroCarteira):
        if dinheiroCarteira < self.preco:
            print('Você não tem dinheiro')
        else:
            dinheiroCarteira -= self.preco
            print(f'Compra de {self.nome} realizada com sucesso')
            self.compra = True

    def consumir(self):
        if self.compra:
            print(f'Você acabou de consumir {self.tempero}g de tempero está maluco')
        else:
            print('Você deve comprar primeiro, para comer')


p1 = Cerveja(23,12, 'cerveja', False, 2)
p2 = Cebola(12, 3, 'cebola', False, 12)
p3 = Linguica(2, 12, 'Linguica', False, 212)
p4 = Leite(31, 6, 'Leite', False, 1)
p5 = Salgadinho(4, 12, 'Salgadinho', False, 12)
