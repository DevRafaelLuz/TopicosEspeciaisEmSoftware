from models.Raca import Raca

class Elfo(Raca):
    def __init__(self, movimento, infravisao, alinhamento, habilidades = []):
        super().__init__(movimento = 9, infravisao = 18, alinhamento = "Neutro", habilidades = {"Percepção Natural", "Graciosos", "Treinamento Racial", "Imunidade"})