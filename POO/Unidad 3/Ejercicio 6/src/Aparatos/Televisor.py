from .Aparato import Aparato

class Televisor(Aparato):
	__tipoPantalla: str # crt, vga, svga, plasma, lcd, led, TouchScreen, MultiTouch
	__pulgadas: int
	__tipoDefinicion: str # SD | HD | FULL HD
	__internet: bool

	def __init__(self, marca: str, modelo: str, color: str, pais: str, precio: float, tipoPantalla: str, pulgadas: int, tipoDefinicion: str, internet: bool):
		super().__init__(marca, modelo, color, pais, precio)
		self.__tipoPantalla = tipoPantalla
		self.__pulgadas = pulgadas
		self.__tipoDefinicion = tipoDefinicion
		self.__internet = internet

	def cacularPrecioVenta(self):
		precio = self.__precio

		if self.__tipoDefinicion == "SD":
			precio += self.__precio * 0.01
		elif self.__tipoDefinicion == "HD":
			precio += self.__precio * 0.02
		elif self.__tipoDefinicion == "FULL HD":
			precio += self.__precio * 0.03

		if self.__internet:
			precio += self.__precio * 0.1

		return precio

	def toJSON(self):
		data = super().toJSON()
		data['tipoPantalla'] = self.__tipoPantalla
		data['pulgadas'] = self.__pulgadas
		data['tipoDefinicion'] = self.__tipoDefinicion
		data['internet'] = self.__internet
		return data