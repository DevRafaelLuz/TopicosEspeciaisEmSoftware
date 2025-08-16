from interfaces.Menu import Menu

class MenuPrincipal(Menu):
    def exibir_menu(self):
        print("Bem-vindo ao Menu Principal!")

        while True:
            try:
                print("1. Criar Personagem")
                print("2. Sair")
                
                opcao = int(input("Escolha uma opção: "))
                
                match opcao:
                    case 1:
                        pass
                    case 2:
                        break
                    case _:
                        print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")