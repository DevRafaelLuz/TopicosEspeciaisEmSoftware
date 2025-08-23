from models.Raca import Raca

class Halfling(Raca):
    def __init__(self, movimento = 7, infravisao = 0, alinhamento = "Neutro", habilidades = {"Furtivo", "Destemido", "Bons de Mira", "Pequenos", "Restrições"}):
        super().__init__(movimento, infravisao, alinhamento, habilidades)

    def __str__(self):
        return "Halfling"