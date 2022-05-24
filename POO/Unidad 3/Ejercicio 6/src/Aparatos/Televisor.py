from .Aparato import Aparato

class Televisor(Aparato):
	__tipoPantalla: str # crt, vga, svga, plasma, lcd, led, TouchScreen, MultiTouch
	__pulgadas: int
	__tipoDefinicion: str # SD | HD | FULL HD
	__internet: bool

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
