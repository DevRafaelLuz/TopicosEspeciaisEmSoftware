from models.Raca import Raca

class Elfo(Raca):
    def __init__(self, movimento = 9, infravisao = 18, alinhamento = "Neutro", habilidades = {"Percepção Natural", "Graciosos", "Treinamento Racial", "Imunidade"}):
        super().__init__(movimento, infravisao, alinhamento, habilidades)

    def __str__(self):
        return "Elfo"