from .Equipo import Equipo

class Jugador:
	__nombre: str
	__dni: str
	__ciudadNatal: str
	__paisOrigen: str
	__fechaNacimiento: str
	__equipos: list[Equipo]

	def __init__(self, nombre: str, dni: str, ciudadNatal: str, paisOrigen: str, fechaNacimiento: str, equipos: list[Equipo]):
		self.__nombre = nombre
		self.__dni = dni
		self.__ciudadNatal = ciudadNatal
		self.__paisOrigen = paisOrigen
		self.__fechaNacimiento = fechaNacimiento
		self.__equipos = []

	def getNombre(self):
		return self.__nombre

	def getDNI(self):
		return self.__dni
