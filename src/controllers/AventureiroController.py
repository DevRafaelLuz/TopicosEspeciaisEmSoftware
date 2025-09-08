from controllers.AtributosController import AtributosController
from controllers.EstiloController import EstiloController
from models.estilos.Aventureiro import Aventureiro
import random

class AventureiroController(EstiloController, Aventureiro, AtributosController):
    aventureiro = Aventureiro()

    def rolar_dados(self):
        valores = []
        for _ in range(6):
            soma = 0
            for _ in range(3):
                soma += random.randint(1, 6)
            valores.append(soma)
        return valores


    def definir_atributos(self):
        return super().definir_manualmente_atributos(self.aventureiro)
        
    def exibir_atributos(self):
        return super().exibir_atributos(self.aventureiro)