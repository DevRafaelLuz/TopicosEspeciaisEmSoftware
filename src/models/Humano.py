from models.Raca import Raca

class Humano(Raca):
    def __init__(self, movimento = 9, infravisao = 0, alinhamento = "Qualquer", habilidades = {"Aprendizado", "Adaptabilidade"}):
        super().__init__(movimento, infravisao, alinhamento, habilidades)

    def __str__(self):
        return "Humano"