from controllers.EstiloController import EstiloController
from models.estilos.Classico import Classico
import random

class ClassicoController(EstiloController, Classico):
    classico = Classico()

    def rolar_dados(self):
        soma = 0
        for _ in range(3):
            soma += random.randint(1, 6)
        return soma
    
    def definir_atributos(self):
        self.classico.forca = self.rolar_dados()
        self.classico.destreza = self.rolar_dados()
        self.classico.constituicao = self.rolar_dados()
        self.classico.inteligencia = self.rolar_dados()
        self.classico.sabedoria = self.rolar_dados()
        self.classico.carisma = self.rolar_dados()
    
    def exibir_atributos(self):
        return super().exibir_atributos(self.classico)