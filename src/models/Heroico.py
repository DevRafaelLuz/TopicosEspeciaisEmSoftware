from models.Personagem import Personagem
import random

class Heroico(Personagem):
    valores = []

    def __init__(self, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        super().__init__(forca, destreza, constituicao, inteligencia, sabedoria, carisma)

    def __init__(self):
        pass

    def rolar_dados(self):
        for _ in range(6):
            valores_gerados = []
            for _ in range(4):
                valor = random.randint(1, 6)
                valores_gerados.append(valor)
            valores_gerados.remove(min(valores_gerados))
            soma = sum(valores_gerados)
            self.valores.append(soma)
        return soma
    
    def definir_atributos(self):
        print(self.valores)
        forca = int(input("Escolha um valor para Força: "))
        self.forca = forca
        self.valores.remove(forca)

        print(self.valores)
        destreza = int(input("Escolha um valor para Destreza: "))
        self.destreza = destreza
        self.valores.remove(destreza)

        print(self.valores)
        constituicao = int(input("Escolha um valor para Constituição: "))
        self.constituicao = constituicao
        self.valores.remove(constituicao)

        print(self.valores)
        inteligencia = int(input("Escolha um valor para Inteligência: "))
        self.inteligencia = inteligencia
        self.valores.remove(inteligencia)

        print(self.valores)
        sabedoria = int(input("Escolha um valor para Sabedoria: "))
        self.sabedoria = sabedoria
        self.valores.remove(sabedoria)

        print(self.valores)
        carisma = int(input("Escolha um valor para Carisma: "))
        self.carisma = carisma
        self.valores.remove(carisma)

    def exibir_atributos(self):
        return {
            "Forca": self.forca,
            "Destreza": self.destreza,
            "Constituicao": self.constituicao,
            "Inteligencia": self.inteligencia,
            "Sabedoria": self.sabedoria,
            "Carisma": self.carisma
        }