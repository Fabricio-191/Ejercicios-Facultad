from .Aparato import Aparato

class Lavarropa(Aparato):
	__capacidad: float
	__velocidad: int
	__carga: str
	__programas: int

	def cacularPrecioVenta(self):
		precio = self.__precio

		if self.__capacidad > 5:
			precio += self.__precio * 0.03
		else:
			precio += self.__precio * 0.01

		return precio
