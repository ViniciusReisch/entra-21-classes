from lista2 import Quadrado

quadrado = Quadrado(lado=int(input('Digite o valor de um dos lados do quadrado: ')))
quadrado.calcular_Area()
quadrado.trocar_Tamanho(new_lado=int(input('Digite um novo valor para o lado do quadrado: ')))
quadrado.mostrar_Lado()
quadrado.calcular_Area()
