from Repartidor import Repartidor
from csv import reader
from GestorPedidos import GestorPedidos

class GestorRepartidores:
	__repartidores: list[Repartidor]
	__gestorPedidos: GestorPedidos

	def __init__(self, archivo: str, gestorPedidos: GestorPedidos):
		self.__leerArchivo(archivo)
		self.__gestorPedidos = gestorPedidos

	def listarRepartidores(self) -> None:
		self.calcularComision()
		for repartidor in self.__repartidores:
			print('Apellido: %-20s          Nombre: %s' % (repartidor.getApellido(), repartidor.getNombre()))
			print('Teléfono: %-20s          Tipo Movilidad: %s' % (repartidor.getTelefono(), repartidor.getTipoMovilidad()))
			print('Número de pedido                Descripción          Cantidad     Precio Unitario     Total')

			total = self.__gestorPedidos.listarPedidos(repartidor.getIdRepartidor())

			print('\n                                                               Total: %.2f' % total)
			print('Importe a pagar por comisión: %.2f\n\n' % (repartidor.getComision()))

	def repartidoresOrdenados(self) -> None:
		self.calcularComision()

		for repartidor in sorted(self.__repartidores, reverse=True):
			print(f'ID: {repartidor.getIdRepartidor()} comision: {repartidor.getComision()}')

	def calcularComision(self) -> None:
		for repartidor in self.__repartidores:
			repartidor.setComision(
				self.__gestorPedidos.calcularComisionRepartidor(
					repartidor.getIdRepartidor()
				)
			)

	def encontrarRepartidor(self, id: int) -> Repartidor | None:
		i = 0
		band = True
		while i < len(self.__repartidores) and band:
			if self.__repartidores[i].getIdRepartidor() == id:
				band = False
			else: i += 1

		value = None
		if i < len(self.__repartidores):
			value = self.__repartidores[i]
		
		return value

	def repartidoresRepetidos(self) -> None:
		id = int(input('Ingrese el id del repartidor: '))

		repartidor = self.encontrarRepartidor(id)
		if repartidor is None:
			print('El repartidor no existe')
		else:
			paraEliminar: list[int] = []
			coincidencias: int = 0
			i = 0
			for repartidor2 in self.__repartidores:
				if repartidor == repartidor2:
					coincidencias += 1
					if self.__gestorPedidos.pedidosSinEntregar(repartidor2.getIdRepartidor()) == 0:
						paraEliminar.append(i)
				i += 1

			if coincidencias == 0:
				raise Exception('__eq__ esta andando mal')
			elif coincidencias == 1:
				print('El repartidor no esta repetido')
			else:
				print('El repartidor esta repetido')

				if len(paraEliminar) == coincidencias:
					# para no eliminar todas las coincidencias en caso de que ninguna tenga pedidos sin entregar
					paraEliminar.pop()
				
				for index in paraEliminar:
					del self.__repartidores[index]
					print('Repeticion eliminada')

	def __leerArchivo(self, archivo: str) -> None:
		with open(archivo, 'r') as f:
			lector = reader(f, delimiter=';')
			next(lector, None)

			self.__repartidores = [Repartidor(linea) for linea in lector]
