from .Aparato import Aparato

class Lavarropa(Aparato):
	__capacidad: float
	__velocidad: int
	__carga: str
	__programas: int

	def __init__(self, marca: str, modelo: str, color: str, pais: str, precio: float, capacidad: float, velocidad: int, carga: str, programas: int):
		super().__init__(marca, modelo, color, pais, precio)
		self.__capacidad = capacidad
		self.__velocidad = velocidad
		self.__carga = carga
		self.__programas = programas

	def cacularPrecioVenta(self):
		precio = self.__precio

		if self.__capacidad > 5:
			precio += self.__precio * 0.03
		else:
			precio += self.__precio * 0.01

		return precio

	def cargaSuperior(self):
		return self.__carga == 'Superior'
