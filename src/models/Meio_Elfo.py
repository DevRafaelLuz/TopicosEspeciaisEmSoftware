from models.Raca import Raca

class Meio_Elfo(Raca):
    def __init__(self, movimento = 9, infravisao = 9, alinhamento = "Caos", habilidades = {"Aprendizado", "Gracioso e Vigoroso", "Idioma Extra", "Imunidade"}):
        super().__init__(movimento, infravisao, alinhamento, habilidades)

    def __str__(self):
        return "Meio-Elfo"