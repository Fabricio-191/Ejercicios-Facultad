from GestorPedidos import GestorPedidos
from GestorRepartidores import GestorRepartidores
from Menu import Menu
from os import path

if __name__ == '__main__':
	gestorPedidos = GestorPedidos(path.dirname(__file__) + '/pedidos.csv')
	gestorRepartidores = GestorRepartidores(path.dirname(__file__) + '/repartidores.csv', gestorPedidos)

	menu = Menu()
	menu.registrarOpcion('1', 'Listar pedidos sin entregar', gestorPedidos.listarPedidosRepartidorSinEntregar)
	menu.registrarOpcion('2', 'Listar repartidores y sus pedidos', gestorRepartidores.listarRepartidores)
	menu.registrarOpcion('3', 'Listar repartidores repetidos', gestorRepartidores.repartidoresRepetidos)
	menu.registrarOpcion('4', 'Listar repartidores ordenados', gestorRepartidores.repartidoresOrdenados)
	menu.iniciar()

	