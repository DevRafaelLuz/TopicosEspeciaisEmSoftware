from controllers.AventureiroController import AventureiroController
from controllers.ClassicoController import ClassicoController
from controllers.HeroicoController import HeroicoController
from interfaces.Menu import Menu
from models.Anao import Anao
from models.Barbaro import Barbaro
from models.Clerigo import Clerigo
from models.Elfo import Elfo
from models.Gnomo import Gnomo
from models.Guerreiro import Guerreiro
from models.Halfling import Halfling
from models.Humano import Humano
from models.Meio_Elfo import Meio_Elfo
from models.Paladino import Paladino
from models.Personagem import Personagem
from models.Ranger import Ranger

import os

class MenuPrincipal(Menu):
    classico = ClassicoController()
    aventureiro = AventureiroController()
    heroico = HeroicoController()
    
    def exibir_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bem-vindo ao Menu Principal!")

        while True:
            try:
                print("1. Novo Personagem")
                print("2. Sair")
                
                opcao = int(input("Escolha uma opção: "))
                
                match opcao:
                    case 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Escolha o estilo do personagem:")
                        print("1. Estilo Clássico")
                        print("2. Estilo Aventureiro")
                        print("3. Estilo Heroico")
                        estilo = int(input("Escolha o estilo do personagem: "))

                        try:
                            match estilo:
                                case 1:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    self.classico.definir_atributos()
                                    print(self.classico.exibir_atributos())
                                case 2:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    self.aventureiro.rolar_dados()
                                    self.aventureiro.definir_atributos()
                                    print(self.aventureiro.exibir_atributos())
                                case 3:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    self.heroico.rolar_dados()
                                    self.heroico.definir_atributos()
                                    print(self.heroico.exibir_atributos())
                                case _:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Estilo inválido. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número.")

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("Escolha a raça do personagem:")
                        print("1. Humano")
                        print("2. Elfo")
                        print("3. Anão")
                        print("4. Meio-Elfo")
                        print("5. Gnomo")
                        print("6. Halfling")
                        raca = int(input("Escolha a raça do personagem: "))

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("Escolha a classe do personagem:")
                        print("1. Guerreiro")
                        print("2. Bárbaro")
                        print("3. Paladino")
                        print("4. Clerigo")
                        print("5. Ranger")
                        classe = int(input("Escolha a classe do personagem: "))

                        self.criar_personagem(estilo, raca, classe)
                    case 2:
                        break
                    case _:
                        print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    def criar_personagem(self, estilo, raca, classe):
        humano = Humano()
        elfo = Elfo()
        meielfo = Meio_Elfo()
        gnomo = Gnomo()
        halfling = Halfling()
        anao = Anao()

        barbaro = Barbaro()
        clerigo = Clerigo()
        guerreiro = Guerreiro()
        paladino = Paladino()
        ranger = Ranger()

        estilos = {1: self.classico, 2: self.aventureiro, 3: self.heroico}
        racas = {1: humano, 2: elfo, 3: anao, 4: meielfo, 5: gnomo, 6: halfling}
        classes = {1: guerreiro, 2: barbaro, 3: paladino, 4: clerigo, 5: ranger}

        estilo_nome = estilos.get(estilo, "Desconhecido")
        raca_nome = racas.get(raca, "Desconhecido")
        classe_nome = classes.get(classe, "Desconhecido")

        personagem = Personagem(estilo_nome, raca_nome, classe_nome)

        print("Personagem criado:")
        print(f"Estilo: {personagem.estilo}")
        print(f"Raça: {personagem.raca}")
        print(f"Classe: {personagem.classe}")