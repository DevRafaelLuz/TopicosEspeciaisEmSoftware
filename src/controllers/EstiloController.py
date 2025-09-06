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
    def exibir_atributos(self, estilo):
        atributos = (
            f"Força: {estilo.forca}\n"
            f"Destreza: {estilo.destreza}\n"
            f"Constituição: {estilo.constituicao}\n"
            f"Inteligência: {estilo.inteligencia}\n"
            f"Sabedoria: {estilo.sabedoria}\n"
            f"Carisma: {estilo.carisma}"
        )
        return atributos