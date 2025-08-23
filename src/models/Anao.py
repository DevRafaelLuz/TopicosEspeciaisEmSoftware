from models.Raca import Raca

class Anao(Raca):
    def __init__(self, movimento = 6, infravisao = 18, alinhamento = "Ordem", habilidades = {"Mineradores", "Vigoroso", "Armas Grandes", "Inimigos"}):
        super().__init__(movimento, infravisao, alinhamento, habilidades)

    def __str__(self):
        return "Anão"