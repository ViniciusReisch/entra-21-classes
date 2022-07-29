class Cola:
    def __init__(self, marca, sabor, peso, diametro, altura, volume1):
        self.marca = marca
        self.sabor = sabor
        self.peso = peso
        self.diametro = diametro
        self.altura = altura
        self.volume1 = volume1

    def amassar(self):
        print('A Lata foi amassada')

    def abrir(self):
        print('A lata foi amassada')

    def beber(self):
        print('Bebeu a lata')

    def esvaziar(self):
        print('A lata esvaziou')

    def lacre(self):
        print('O lacre foi retirado')

    def descartar(self):
        print('Descartou a garrafa')

    def __repr__(self):
        return f'{lata.marca} {lata.sabor} {lata.peso} {lata.diametro} {lata.altura} {lata.volume1}'


def volume(altura, diametro):
    volume1 = altura * diametro
    return volume1


lata = Cola(marca=input("Marca"), sabor=input('Sabor'),
            peso=input('Peso'), diametro=input('Diametro'),
            altura=input('Altura'), volume1=None)
lata.volume1 = volume(int(lata.altura), int(lata.volume1))
print(Cola)
Cola.descartar(lata)