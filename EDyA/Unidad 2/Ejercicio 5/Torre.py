import math

class Disco:
	__tamaño: int

	def __init__(self, tamaño: int):
		self.__tamaño = tamaño

	def getTamaño(self):
		return self.__tamaño

class Torre:  # Pila
	__elementos: list[Disco]

	def __init__(self):
		self.__elementos = []

	def cantidadDiscos(self):
		return len(self.__elementos)

	def estaVacia(self):
		return len(self.__elementos) == 0

	def añadirDisco(self, disco: Disco):
		self.__elementos.append(disco)

	def quitarDisco(self):
		return self.__elementos.pop()

	def tamañoUltimoDisco(self):
		if(self.estaVacia()):
			return math.inf

		return self.__elementos[-1].getTamaño()

	def obtenerTamañoDisco(self, i: int):
		if len(self.__elementos) < i:
			return ' '

		return str(self.__elementos[i - 1].getTamaño())