from controllers.ClassicoController import ClassicoController
from interfaces.Menu import Menu
from models.Aventureiro import Aventureiro
from models.Heroico import Heroico
import os

class MenuPrincipal(Menu):
    def exibir_menu(self):
        classico = ClassicoController()
        aventureiro = Aventureiro()
        heroico = Heroico()

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
                        try:
                            print("1. Estilo Clássico")
                            print("2. Estilo Aventureiro")
                            print("3. Estilo Heroico")

                            estilo = int(input("Escolha o estilo do personagem: "))

                            match estilo:
                                case 1:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    classico.definir_atributos()
                                    print(classico.exibir_atributos())
                                case 2:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    aventureiro.rolar_dados()
                                    aventureiro.definir_atributos()
                                    print(aventureiro.exibir_atributos())
                                case 3:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    heroico.rolar_dados()
                                    heroico.definir_atributos()
                                    print(heroico.exibir_atributos())
                                case _:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Estilo inválido. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número.")
                    case 2:
                        break
                    case _:
                        print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")