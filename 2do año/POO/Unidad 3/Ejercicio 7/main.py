from menu import Menu
from src.GestorPesonal import GestorPesonal
from os import path

if __name__ == "__main__":
	gestor = GestorPesonal(path.dirname(__file__) + "/personal.json")
	menu = Menu(gestor)
	menu.iniciar()