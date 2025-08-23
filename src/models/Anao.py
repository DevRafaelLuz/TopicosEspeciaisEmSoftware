from models.Raca import Raca

class Anao(Raca):
    def __init__(self, movimento, infravisao, alinhamento, habilidades = []):
        super().__init__(movimento = 6, infravisao = 18, alinhamento = "Ordem", habilidades = {"Mineradores", "Vigoroso", "Armas Grandes", "Inimigos"})