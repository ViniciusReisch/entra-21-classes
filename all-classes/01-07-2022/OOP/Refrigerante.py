from ex3Professor import Latas

print('Cadastrar Lata')
lata = Latas(altura=input('Altura:'), diametro=input('Diametro:'),
             cor=input('Cor da lata:'), peso=input('Peso:'),
             material=input('Material da lata'), volume=None)
lata.volume = int(lata.altura) * int(lata.diametro)
while True:
    x = input('Abrir [1]'
          '\nBeber [2]'
          '\nEsvaziar [3]'
          '\nAmassar [4]'
          '\nRetirar Lacre [5]'
          '\nDescartar [6]')

    if x == '1':
        lata.abrir()
    if x == '2':
        lata.beber(quantidade=int(input('Quanto você quer beber? ')))
    if x == '3':
        lata.esvaziar()
    if x == '4':
        lata.amassar()
    if x == '5':
        lata.retirar_lacre()
    if x == '6':
        lata.descartar(cor=input('Qual lixo você deseja descartar').lower())

