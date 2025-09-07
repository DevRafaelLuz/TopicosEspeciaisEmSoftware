from controllers.AtributosController import AtributosController
from controllers.EstiloController import EstiloController
from models.estilos.Heroico import Heroico
import random

class HeroicoController(EstiloController, Heroico, AtributosController):
    heroico = Heroico()
    valores = []

    def rolar_dados(self):
        for _ in range(6):
            valores_gerados = []
            for _ in range(4):
                valor = random.randint(1, 6)
                valores_gerados.append(valor)
            valores_gerados.remove(min(valores_gerados))
            soma = sum(valores_gerados)
            self.valores.append(soma)
        return soma
    
    def definir_atributos(self):
        return super().definir_manualmente_atributos(self.heroico)

    def exibir_atributos(self):
        return super().exibir_atributos(self.heroico)