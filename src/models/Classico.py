from models.Personagem import Personagem
import random

class Classico(Personagem):

    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        super().__init__(forca, destreza, constituicao, inteligencia, sabedoria, carisma)

    def __init__(self):
        pass

    def rolar_dados(self):
        soma = 0
        for _ in range(3):
            soma += random.randint(1, 6)
        return soma
    
    def definir_atributos(self):
        self.forca = self.rolar_dados()
        self.destreza = self.rolar_dados()
        self.constituicao = self.rolar_dados()
        self.inteligencia = self.rolar_dados()
        self.sabedoria = self.rolar_dados()
        self.carisma = self.rolar_dados()
    
    def exibir_atributos(self):
        return {
            "Forca": self.forca,
            "Destreza": self.destreza,
            "Constituicao": self.constituicao,
            "Inteligencia": self.inteligencia,
            "Sabedoria": self.sabedoria,
            "Carisma": self.carisma
        }