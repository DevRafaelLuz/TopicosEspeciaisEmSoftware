from controllers.EstiloController import EstiloController
from models.estilos.Heroico import Heroico
import random

class HeroicoController(EstiloController, Heroico):
    heroico = Heroico()
    valores = []

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
        while True:
            print(self.valores)
            forca = int(input("Escolha um valor para Força: "))
            if forca in self.valores:
                self.heroico.forca = forca
                self.valores.remove(forca)
                break

        while True:
            print(self.valores)
            destreza = int(input("Escolha um valor para Destreza: "))
            if destreza in self.valores:
                self.heroico.destreza = destreza
                self.valores.remove(destreza)
                break

        while True:
            print(self.valores)
            constituicao = int(input("Escolha um valor para Constituição: "))
            if constituicao in self.valores:
                self.heroico.constituicao = constituicao
                self.valores.remove(constituicao)
                break

        while True:
            print(self.valores)
            inteligencia = int(input("Escolha um valor para Inteligência: "))
            if inteligencia in self.valores:
                self.heroico.inteligencia = inteligencia
                self.valores.remove(inteligencia)
                break

        while True:
            print(self.valores)
            sabedoria = int(input("Escolha um valor para Sabedoria: "))
            if sabedoria in self.valores:
                self.heroico.sabedoria = sabedoria
                self.valores.remove(sabedoria)
                break

        while True:
            print(self.valores)
            carisma = int(input("Escolha um valor para Carisma: "))
            if carisma in self.valores:
                self.heroico.carisma = carisma
                self.valores.remove(carisma)
                break

    def exibir_atributos(self):
        return super().exibir_atributos(self.heroico)