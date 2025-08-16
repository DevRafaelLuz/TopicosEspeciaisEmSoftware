from abc import abstractmethod
from interfaces.Atributos import Atributos

class Personagem(Atributos):
    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    def __init__(self):
        pass

    @abstractmethod
    def rolar_dados(self):
        pass

    @abstractmethod
    def definir_atributos(self):
        pass

    @abstractmethod
    def exibir_atributos(self):
        pass