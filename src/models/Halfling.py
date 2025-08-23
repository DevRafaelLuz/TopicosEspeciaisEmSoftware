from models.Raca import Raca

class Halfling(Raca):
    def __init__(self, movimento, infravisao, alinhamento, habilidades = []):
        super().__init__(movimento = 7, infravisao = 0, alinhamento = "Neutro", habilidades = {"Furtivo", "Destemido", "Bons de Mira", "Pequenos", "Restrições"})