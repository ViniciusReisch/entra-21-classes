import sqlite3
import arrow
import requests


# Conexao com banco de dados
conexao = sqlite3.connect('mercado_ex.db')
cursor = conexao.cursor()


class Mercado:
    def __init__(self, cep):
        self.cep = cep

    def cadastrar_Cliente(self, nome, cpf, numero):
        self.cep = input('Qual seu cep? ')
        cep = requests.get('https://cep.awesomeapi.com.br/json/' + self.cep)
        cep_json = cep.json()
        cursor.execute('INSERT INTO clientes(nome, cpf, cep, estado, bairro, rua, numero)'
                       'VALUES(?,?,?,?,?,?,?)',
                       (nome, cpf, self.cep, cep_json['state'], cep_json['district'], cep_json['address_name'], numero))
        conexao.commit()

    def editar_Cliente(self):
        x = input('Qual cliente deseja editar [CPF]: ')
        infos = [
            '', 'nome', 'cpf', 'cep', 'estado', 'bairro', 'rua', 'numero'
        ]
        cursor.execute(f'SELECT * FROM clientes WHERE cpf={x}')
        for linha in cursor.fetchall():
            print(f'{linha[0]} - {linha[1]} - {linha[2]} - {linha[3]} - {linha[4]} - {linha[5]} - {linha[6]}')
        y = int(input('[1] Nome'
                      '\n[2] CPF'
                      '\n[3] CEP'
                      '\n[4] Estado'
                      '\n[5] Bairro'
                      '\n[6] Rua'
                      '\n[7] Numero'))
        new_info = input('Digite o novo:')
        cursor.execute(f'UPDATE clientes SET {infos[y]}="{new_info}" WHERE cpf={x}')
        conexao.commit()

    def excluir_cliente(self, clienteDesejado):
        cursor.execute(f'DELETE FROM clientes WHERE cpf={clienteDesejado}')
        conexao.commit()

    def cadastrar_Produto(self, nome, familia, barras):
        cursor.execute('INSERT INTO produtos(nome, familia, barras)'
                       'VALUES(?,?,?)',
                       (nome, familia, barras))
        conexao.commit()

    def editar_Produto(self):
        x = input('Qual o ID do produto? ')
        infos = [
            '', 'nome', 'familia', 'barras'
        ]
        y = int(input('[1] Nome'
                      '\n[2] Famiia'
                      '\n[3] Barras'))
        new_info = input('Digite o novo:')
        cursor.execute(f'SELECT * FROM produtos WHERE id={x}')
        for linha in cursor.fetchall():
            print(f'{linha[0]} - {linha[1]} - {linha[2]}')
        cursor.execute(f'UPDATE produtos SET {infos[y]}="{new_info}" WHERE id={x}')
        conexao.commit()

mercado = Mercado('')
while True:
    x = input('Mercado'
              '\n [1] Cadastrar cliente'
              '\n [2] Editar cliente'
              '\n [3] Excluir cliente'
              '\n [4] Cadastrar produto'
              '\n [5] Editar produto')
    if x == '1':
        mercado.cadastrar_Cliente(nome=input('Insira seu nome:'),
                                  cpf=input('Insira seu cpf:'),
                                  numero=input('Insira seu numero: '))

    if x == '2':
        mercado.editar_Cliente()

    if x == '3':
        mercado.excluir_cliente(clienteDesejado=input('Escreva o cpf da conta que deseja deletar: '))

    if x == '4':
        mercado.cadastrar_Produto(nome=input('Insira o nome do produto:'),
                                  familia=input('Insira sua familia:'),
                                  barras=input('Insira seu numero de codigo de barras: '))

    if x == '5':
        mercado.editar_Produto()


cursor.close()
conexao.close()
