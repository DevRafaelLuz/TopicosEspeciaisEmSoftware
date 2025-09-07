from abc import abstractmethod

class AtributosController():
    def __init__(self):
        pass

    @abstractmethod
    def definir_manualmente_atributos(self, estilo):
        while True:
            print(self.valores)
            forca = int(input("Escolha um valor para Força: "))
            if forca in self.valores:
                estilo.forca = forca
                self.valores.remove(forca)
                break

        while True:
            print(self.valores)
            destreza = int(input("Escolha um valor para Destreza: "))
            if destreza in self.valores:
                estilo.destreza = destreza
                self.valores.remove(destreza)
                break

        while True:
            print(self.valores)
            constituicao = int(input("Escolha um valor para Constituição: "))
            if constituicao in self.valores:
                estilo.constituicao = constituicao
                self.valores.remove(constituicao)
                break

        while True:
            print(self.valores)
            inteligencia = int(input("Escolha um valor para Inteligência: "))
            if inteligencia in self.valores:
                estilo.inteligencia = inteligencia
                self.valores.remove(inteligencia)
                break

        while True:
            print(self.valores)
            sabedoria = int(input("Escolha um valor para Sabedoria: "))
            if sabedoria in self.valores:
                estilo.sabedoria = sabedoria
                self.valores.remove(sabedoria)
                break

        while True:
            print(self.valores)
            carisma = int(input("Escolha um valor para Carisma: "))
            if carisma in self.valores:
                estilo.carisma = carisma
                self.valores.remove(carisma)
                break