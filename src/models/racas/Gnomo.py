from models.racas.Raca import Raca

class Gnomo(Raca):
    def __init__(self, movimento = 6, infravisao = 18, alinhamento = "Neutro", habilidades = {"Avaliadores", "Sagazes e Vigoroso", "Restrições"}):
        super().__init__(movimento, infravisao, alinhamento, habilidades)

    def __str__(self):
        return "Gnomo"