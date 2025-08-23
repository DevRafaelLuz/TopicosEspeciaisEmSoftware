from models.Raca import Raca

class Gnomo(Raca):
    def __init__(self, movimento, infravisao, alinhamento, habilidades = []):
        super.__init__(movimento = 6, infravisao = 18, alinhamento = "Neutro", habilidades = {"Avaliadores", "Sagazes e Vigoroso", "Restrições"})