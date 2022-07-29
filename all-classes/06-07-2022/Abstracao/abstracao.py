from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    @abstractmethod
    def alimentar(self):
        return True

    def nascer(self):
        print('Nasceu')

class Felinos(Animal):
    def __init__(self, nome, especie, garras, orelhas):
        super().__init__(nome, especie)
        self.garras = garras
        self.orelhas = orelhas

    def alimentar(self):
        print('hmam hmam')

        
a2 = Felinos('Milka', 'Gato', True, 2)
print(a2.alimentar())
