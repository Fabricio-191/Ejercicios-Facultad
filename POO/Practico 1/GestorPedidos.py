from Pedido import Pedido
from csv import reader
import numpy as np

class GestorPedidos:
	__pedidos: np.ndarray

	def __init__(self, archivo: str):
		self.__leerArchivo(archivo)

	def listarPedidosRepartidorSinEntregar(self) -> None:
		idRepartidor = int(input('Ingrese el id del repartidor: '))

		for pedido in self.__pedidos:
			if pedido.getRepartidor() == idRepartidor and pedido.getEstado() == 'N':
				print(f'idPedido: {pedido.getNumeroPedido()}')
	
	def listarPedidos(self, idRepartidor: int) -> float:
		total = 0
		for pedido in self.__pedidos:
			if pedido.getRepartidor() == idRepartidor:
				total += pedido.getTotal()

				print('      %d           %25s            %d            %.2f       %.2f' % (
					pedido.getNumeroPedido(),
					pedido.getDescripcion(),
					pedido.getCantidad(),
					pedido.getPrecioUnitario(),
					pedido.getTotal()
				))

		return total

	def pedidosSinEntregar(self, idRepartidor: int) -> int:
		cont = 0

		for pedido in self.__pedidos:
			if pedido.getRepartidor() == idRepartidor and pedido.getEstado() == 'N':
				cont += 1

		return cont

	def calcularComisionRepartidor(self, idRepartidor: int) -> float:
		total = 0
		for pedido in self.__pedidos:
			if pedido.getRepartidor() == idRepartidor and pedido.getEstado() == 'E':
				total += pedido.getTotal()

		return total * 0.05

	def __leerArchivo(self, archivo: str) -> None:
		with open(archivo, 'r') as f:
			lector = reader(f, delimiter=';')
			next(lector, None)
			
			self.__pedidos = np.array([
				Pedido(linea) for linea in lector
			])