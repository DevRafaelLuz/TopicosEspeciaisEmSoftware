from models.estilos.Estilo import Estilo

class Classico(Estilo):
    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        super().__init__(forca, destreza, constituicao, inteligencia, sabedoria, carisma)

    def __init__(self):
        pass

    def __str__(self):
        return "Clássico"