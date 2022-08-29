import numpy as np

class Paciente:
	__documento: str
	__nombre: str

	def __init__(self, documento, nombre):
		self.__documento = documento
		self.__nombre = nombre

class Turno:
	__paciente: Paciente
	__especialidad: str
	
	def __init__(self, paciente, especialidad):
		self.__paciente = paciente
		self.__especialidad = especialidad

class Cola: # lifo
	__elementos: np.ndarray
	__tope: int
	__tamañoTotal: int

	def __init__(self, tamañoTotal: int = 100):
		self.__elementos = np.full(tamañoTotal, None)
		self.__tope = 0
		self.__tamañoTotal = tamañoTotal
	
	def getTamaño(self):
		return self.__tope

	def estaVacia(self):
		return self.__tope == 0

	def add(self, elem):
		if self.__tope == self.__tamañoTotal:
			raise Exception('La cola esta llena')

		self.__elementos[self.__tope] = elem
		self.__tope += 1

	def get(self):
		if self.__tope == 0:
			raise Exception('No quedan elementos en la cola')
		
		valor = self.__elementos[0]
		
		for i in range(1, self.__tope):
			self.__elementos[i-1] = self.__elementos[i]

		self.__tope -= 1

		return valor