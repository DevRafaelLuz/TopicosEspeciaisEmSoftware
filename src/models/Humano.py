from models.Raca import Raca

class Humano(Raca):
    def __init__(self, movimento, infravisao, alinhamento, habilidades = []):
        super().__init__(movimento = 9, infravisao = 0, alinhamento = "Qualquer", habilidades = {"Aprendizado", "Adaptabilidade"})