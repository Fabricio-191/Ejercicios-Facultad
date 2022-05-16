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
			coincidencias: list[Repartidor] = []
			for repartidor2 in self.__repartidores:
				if repartidor == repartidor2:
					coincidencias.append(repartidor2)

			if len(coincidencias) == 0:
				raise Exception('__eq__ esta andando mal')
			elif len(coincidencias) == 1:
				print('El repartidor no esta repetido')
			else:
				print('El repartidor esta repetido')
				print('Se intentara eliminar el repartidor repetido')
				self.intentarEliminarRepartidor(coincidencias)

	def intentarEliminarRepartidor(self, coincidencias: list[Repartidor]) -> None:
		i = 0
		while len(coincidencias) > 1 and i < len(coincidencias):
			# intetara eliminar cualquiera de las repeticiones, hasta que solo quede una
			print(f'Intentando con la instancia {i + 1}')
			if self.__gestorPedidos.pedidosSinEntregar(coincidencias[i].getIdRepartidor()) == 0:
				self.__repartidores.remove(coincidencias[i])
				print('El repartidor fue eliminado')
			else:
				print('No se puede eliminar un repartidor que posee pedidos sin entregar')
			i += 1

	def __leerArchivo(self, archivo: str) -> None:
		with open(archivo, 'r') as f:
			lector = reader(f, delimiter=';')
			next(lector, None)

			self.__repartidores = [Repartidor(linea) for linea in lector]
