from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def exibir_menu():
        pass