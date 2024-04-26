import numpy as np
import math

class Disco:
	__tamaño: int

	def __init__(self, tamaño: int):
		self.__tamaño = tamaño

	def getTamaño(self):
		return self.__tamaño

class Torre: # lifo
	__elementos: np.ndarray
	__tope: int
	__tamañoTotal: int

	def __init__(self, tamañoTotal: int = 100):
		self.__elementos = np.full(tamañoTotal, None)
		self.__tope = 0
		self.__tamañoTotal = tamañoTotal
	
	def cantidadDiscos(self):
		return self.__tope

	def estaVacia(self):
		return self.__tope == 0

	def añadirDisco(self, elem):
		if self.__tope == self.__tamañoTotal:
			raise Exception('La pila esta llena')

		self.__elementos[self.__tope] = elem
		self.__tope += 1

	def quitarDisco(self):
		if self.__tope == 0:
			raise Exception('No quedan elementos en la pila')
		
		self.__tope -= 1
		valor = self.__elementos[self.__tope]
		self.__elementos[self.__tope] = None
		return valor

	def tamañoUltimoDisco(self):
		if(self.estaVacia()):
			return math.inf

		return self.__elementos[self.__tope - 1].getTamaño()

	def obtenerTamañoDisco(self, i: int):
		value = self.__elementos[i - 1]
		if value is None:
			return ' '

		return str(value.getTamaño())