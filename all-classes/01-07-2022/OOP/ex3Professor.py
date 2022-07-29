class Latas:
    def __init__(self, altura, diametro, cor, peso, material, volume):
        self.altura = altura
        self.diametro = diametro
        self.cor = cor
        self.peso = peso
        self.material = material
        self.volume = volume
        self.aberta = False
        self.amassada = False
        self.descartada = False
        self.lacre = True

    def abrir(self):
        if self.aberta:
            print('Já está aberta')
        else:
            print('POC')
            self.aberta = True

    def beber(self, quantidade):
        if self.descartada:
            print('A lata ja foi descartada')
        elif self.aberta:
            if quantidade <= self.volume:
                self.volume -= quantidade
                print(f'Ainda restam {self.volume}')
            elif quantidade > self.volume:
                print(f'Você bebeu {self.volume} mL e faltou {-(self.volume-quantidade)}')
            else:
                print('Be')
        else:
            print('A lata está fechada')

    def esvaziar(self):
        if not self.aberta:
            print('Como vai esvaziar a lata sem abrir')
        elif self.volume == 0:
            print('Já esta vazia')
        elif self.descartada:
            print('A lata ja foi descartada')
        elif self.amassada:
            print('A lata está amassada')
        else:
            self.volume = 0
            print('A lata está vazia')

    def amassar(self):
        if self.amassada:
            print('Já está amassada')
        elif self.descartada:
            print('Já foi descartada')
        elif self.volume == 0:
            print('A lata foi amassada')
            self.amassada = True
        else:
            print('Você precisa beber tudo, antes da amassar')

    def retirar_lacre(self):
        if self.descartada:
            print('A lata ja foi embora')
        elif not self.lacre:
            print('Você ja tirou o lacre')
        else:
            print('lacre removido')
            self.lacre = False

    def descartar(self, cor):
        if self.descartada:
            print('Já foi descartada')
        elif not self.amassada:
            print('Só pode descartar depois de amassar')
        elif cor != 'amarelo':
            print('Não pode ser descartado nessa lixeira')
        else:
            print('Lata descartada no lugar correto')
            self.descartada = True

