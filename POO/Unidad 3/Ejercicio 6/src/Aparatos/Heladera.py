from .Aparato import Aparato

class Heladera(Aparato):
	__capacidad: float
	__freezer: bool
	__cyclica: bool

	def __init__(self, marca: str, modelo: str, color: str, pais: str, precio: float, capacidad: float, freezer: bool, cyclica: bool):
		super().__init__(marca, modelo, color, pais, precio)
		self.__capacidad = capacidad
		self.__freezer = freezer
		self.__cyclica = cyclica

	def cacularPrecioVenta(self):
		precio = self.__precio

		if self.__freezer:
			precio += self.__precio * 0.05
		else:
			precio += self.__precio * 0.01
		
		if self.__cyclica:
			precio += self.__precio * 0.1

		return precio

	def toJSON(self):
		data = super().toJSON()
		data['capacidad'] = self.__capacidad
		data['freezer'] = self.__freezer
		data['cyclica'] = self.__cyclica
		return data