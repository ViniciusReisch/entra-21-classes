class Conta:
    def __init__(self, conta, nome, saldo=0.0):
        self.conta = conta
        self.nome = nome
        self.__saldo = saldo

    def ver_Saldo(self):
        print(self.__saldo)
        self.__falarnome()

    def __falarnome(self):
        print(f'Bom dia {self.nome}')


c1 = Conta(123123, 'Jonas', 150)
c1.ver_Saldo()
