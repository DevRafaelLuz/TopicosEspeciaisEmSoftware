from models.Personagem import Personagem

class Aventureiro(Personagem):
    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        super().__init__(forca, destreza, constituicao, inteligencia, sabedoria, carisma)

    def definir_atributos(self):
        return {
            "forca": self.forca,
            "destreza": self.destreza,
            "constituicao": self.constituicao,
            "inteligencia": self.inteligencia,
            "sabedoria": self.sabedoria,
            "carisma": self.carisma
        }