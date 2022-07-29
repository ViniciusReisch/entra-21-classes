class Computador:
    def __init__(self, teclado='Razer', mouse='Multilaser'):
        self.energia = False
        self.estado = False
        self.__teclado = teclado
        self.__mouse = mouse

    def ligar(self):
        if self.energia:
            print('Pc já está ligado')
        else:
            print('Pc ligou!')
            self.energia = True

    def desligar(self):
        if self.energia:
            print('Pc desligado')
            self.energia = False
        else:
            print('Pc já esta desligado')

    def quebrar(self, pedacos):
        if self.energia:
            print('Você deve desligar o pc para quebrar')
        elif pedacos > 1:
            print(f'O pc foi quebrado em {pedacos} pedaços ')
            self.estado = True
        else:
            print('Não da pra quebrar em tao poucos pedaços')


class Asus(Computador):
    def __init__(self, marca='Asus'):
        super().__init__()
        self.marca = marca

    def conferir_estado(self):
        if self.estado:
            print('O pc está quebrado')
        elif self.energia == False and self.estado == False:
            print('O pc está desligado')
        elif self.energia:
            print('O pc está ligado')

pc = Computador()

pcAsus = Asus()

pcAsus.ligar()
pcAsus.quebrar(4)
pcAsus.desligar()
pcAsus.quebrar(2)
pcAsus.conferir_estado()
