from abc import ABC

class Raca(ABC):
    def __init__(self, movimento, infravisao, alinhamento, habilidades = []):
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades