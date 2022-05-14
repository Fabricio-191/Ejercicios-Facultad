from .Equipo import Equipo

class Jugador:
	__nombre: str
	__DNI: str
	__ciudadNatal: str
	__paisOrigen: str
	__fechaNacimiento: str
	__equipos: list[Equipo]

	def __init__(self, nombre: str, DNI: str, ciudadNatal: str, paisOrigen: str, fechaNacimiento: str):
		self.__nombre = nombre
		self.__DNI = DNI
		self.__ciudadNatal = ciudadNatal
		self.__paisOrigen = paisOrigen
		self.__fechaNacimiento = fechaNacimiento