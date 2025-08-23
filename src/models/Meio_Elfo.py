from models.Raca import Raca

class Meio_Elfo(Raca):
    def __init__(self, movimento, infravisao, alinhamento, habilidades = []):
        super().__init__(movimento = 9, infravisao = 9, alinhamento = "Caos", habilidades = {"Aprendizado", "Gracioso e Vigoroso", "Idioma Extra", "Imunidade"})