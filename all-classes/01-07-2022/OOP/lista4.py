class Bomba_Combustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_Combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_Combustivel = quantidade_Combustivel

    def abastecer_Por_Valor(self, valor):
        total = valor/self.valor_litro
        if self.quantidade_Combustivel < total:
            print('Não possui tantos litros na bomba')
        elif total > 0:
            print(f'Foi abastecido {total} Litros')
            self.quantidade_Combustivel -= total
            print('Abastecido com sucesso')
            print(f'Quantidade na bomba {self.quantidade_Combustivel}')
        else:
            print('Selecione um valor maior que 0')

    def abastecer_Por_Litros(self, litros):
        total = litros*self.valor_litro
        if self.quantidade_Combustivel < litros:
            print('Não possui tantos litros na bomba')
        elif litros > 0:
            print(f'Para esse total de litros será pago R${total},00')
            self.quantidade_Combustivel -= litros
            print('Abastecido com sucesso')
            print(f'Quantidade na bomba {self.quantidade_Combustivel}')
        else:
            print('Selecione um valor maior que 0 para abastecimento')

    def alterar_Valor(self, new_valor):
        self.valor_litro = new_valor

    def alterar_Combustivel(self, new_valor):
        self.tipo_combustivel = new_valor

    def quantidade_Bomba(self, new_valor):
        self.quantidade_Combustivel = new_valor


