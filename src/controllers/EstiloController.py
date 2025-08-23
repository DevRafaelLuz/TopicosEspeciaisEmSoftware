from abc import abstractmethod
from interfaces.Atributos import Atributos

class EstiloController(Atributos):
    @abstractmethod
    def rolar_dados(self):
        pass

    @abstractmethod
    def definir_atributos(self):
        pass

    @abstractmethod
    def exibir_atributos(self):
        pass