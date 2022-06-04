from menu import Menu
from src.GestorPesonal import GestorPesonal
from os import path

if __name__ == "__main__":
	gestor = GestorPesonal(path.dirname(__file__) + "/personal.json")
	menu = Menu(gestor)
	menu.iniciar()

"""
Maria Castro PersonalApoyo 170800.0
Juan Dominguez Investigador 122400.0
Marcos Lopez DocenteInvestigador 161170.0
Agustin Lopez DocenteInvestigador 134470.0
Zariel Lopez DocenteInvestigador 161170.0
Nicolas Perez Docente 109470.0

Nicolas Perez Docente 246000.0

20-3454506-8

uDirector/ufC77#!1
"""