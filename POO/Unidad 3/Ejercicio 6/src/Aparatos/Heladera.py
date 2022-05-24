from .Aparato import Aparato

class Heladera(Aparato):
	__capacidad: float
	__freezer: bool
	__cyclica: bool

	def cacularPrecioVenta(self):
		precio = self.__precio

		if self.__freezer:
			precio += self.__precio * 0.05
		else:
			precio += self.__precio * 0.01
		
		if self.__cyclica:
			precio += self.__precio * 0.1

		return precio

