from controllers.AtributosController import AtributosController
from controllers.EstiloController import EstiloController
from models.estilos.Heroico import Heroico
import random

class HeroicoController(EstiloController, Heroico, AtributosController):
    heroico = Heroico()

    def rolar_dados(self):
        valores = []
        for _ in range(6):
            rolagem = [random.randint(1, 6) for _ in range(4)]
            rolagem.remove(min(rolagem))
            valores.append(sum(rolagem))
        return valores
    
    def definir_atributos(self):
        return super().definir_manualmente_atributos(self.heroico)

    def exibir_atributos(self):
        return super().exibir_atributos(self.heroico)