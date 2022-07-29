from lista5 import Macaco

macaco1 = Macaco(nome='Celso', bucho=[])
macaco2 = Macaco(nome='Jorge', bucho=[])
while True:
    macaco1.comer(alimento=input('De um alimento pra o macaco: '))
    macaco1.ver_Bucho()
    macaco2.comer(alimento=input('De um alimento para o macaco: '))
    macaco2.ver_Bucho()
