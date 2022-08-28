import math

class Disco:
	__tamaño: int

	def __init__(self, tamaño: int):
		self.__tamaño = tamaño

	def getTamaño(self):
		return self.__tamaño

	def __repr__(self):
		return str(self.__tamaño)

class Torre:  # Pila
	__elementos: list[Disco]

	def __init__(self):
		self.__elementos = []

	def cantidadDiscos(self):
		return len(self.__elementos)

	def estaVacia(self):
		return len(self.__elementos) == 0

	def añadirDisco(self, disco: Disco):
		if(self.getTamañoUltimoDisco() <= disco.getTamaño()):
			print('No se puede poner un Disco encima de uno mas pequeño')
			raise Exception('No se puede poner un Disco encima de uno mas pequeño')
		else:
			self.__elementos.append(disco)


	def quitarDisco(self):
		if self.estaVacia():
			print('No quedan Discos en la torre')
			raise Exception('No quedan Discos en la torre')

		return self.__elementos.pop()

	def obtenerDisco(self, i: int):
		if len(self.__elementos) < i:
			return ' '

		return self.__elementos[i - 1]

	def getTamañoUltimoDisco(self):
		if(self.estaVacia()):
			return math.inf

		return self.__elementos[-1].getTamaño()