from controllers.AtributosController import AtributosController
from controllers.EstiloController import EstiloController
from models.estilos.Aventureiro import Aventureiro
import random

class AventureiroController(EstiloController, Aventureiro, AtributosController):
    aventureiro = Aventureiro()
    valores = []

    def rolar_dados(self):
        soma = 0
        for _ in range(6):
            for _ in range(3):
                soma += random.randint(1, 6)
            self.valores.append(soma)
            soma = 0
        return soma

    def definir_atributos(self):
        return super().definir_manualmente_atributos(self.aventureiro)
        
    def exibir_atributos(self):
        return super().exibir_atributos(self.aventureiro)