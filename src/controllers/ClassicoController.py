from controllers.EstiloController import EstiloController
from models.estilos.Classico import Classico
import random

class ClassicoController(EstiloController, Classico):
    classico = Classico()

    def rolar_dados(self):
        atributos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']
        valores = []

        for _ in range(6):
            soma = sum(random.randint(1, 6) for _ in range(3))
            valores.append(soma)

        return dict(zip(atributos, valores))
    
    def definir_atributos(self):
        self.classico.forca = self.rolar_dados()
        self.classico.destreza = self.rolar_dados()
        self.classico.constituicao = self.rolar_dados()
        self.classico.inteligencia = self.rolar_dados()
        self.classico.sabedoria = self.rolar_dados()
        self.classico.carisma = self.rolar_dados()
    
    def exibir_atributos(self):
        return super().exibir_atributos(self.classico)