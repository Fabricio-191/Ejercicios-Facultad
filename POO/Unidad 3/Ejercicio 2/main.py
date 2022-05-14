# https://campusvirtual.unsj.edu.ar/mod/assign/view.php?id=182615

from Menu import Menu
from src.GestorRamos import GestorRamos
from src.GestorFlores import GestorFlores
from os import path

def opcion3(gestorRamos: GestorRamos):
	gestorRamos.indicarFloresVendidasEnTamaño()

if __name__ == '__main__':
	gestorFlores = GestorFlores(path.dirname(__file__) + '/flores.csv')
	gestorRamos = GestorRamos(gestorFlores)
	# gestorRamos.leerArchivo(path.dirname(__file__) + '/ramos.csv')

	menu = Menu()
	menu.registrarOpcion('1', 'Vender ramo', gestorRamos.venderRamo)
	menu.registrarOpcion('2', 'Mostrar 5 flores mas vendidas', gestorRamos.mostrar5FloresMasVendidas)
	menu.registrarOpcion('3', 'Indicar flores vendidas en tamaño', opcion3, gestorRamos)
	menu.iniciar()


# el archivo ramos.csv esta para evitar hacer la carga de los ramos vendidos a mano
"""
1
grande
Rosa
Girasol
terminar
1
grande
Rosa
terminar
1
grande
Girasol
terminar

"""