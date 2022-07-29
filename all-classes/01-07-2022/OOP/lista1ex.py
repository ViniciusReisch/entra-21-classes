from lista1 import Bola

bola = Bola(circunferencia=input('Escreva a circunferencia da bola:'),
            cor=input('Escreva a cor da bola: '),
            material=input('Escreva o material que a bola é feita: '))

new_cor = input('Pra qual cor quer trocar a bola? ')
bola.troca_Cor(new_cor)
bola.mostra_Cor()