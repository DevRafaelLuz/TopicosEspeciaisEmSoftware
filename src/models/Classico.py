from models import Personagem

class Classico(Personagem):
    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        super().__init__(forca, destreza, constituicao, inteligencia, sabedoria, carisma)