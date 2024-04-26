"""
Ejercicio Nº6: Codifique un programa que simule el funcionamiento de la lista de espera del quirófano de un hospital. Cada vez que el quirófano esté desocupado, se operará al paciente de mayor urgencia, dentro de esa lista de espera. Al ingresar un paciente al hospital, además de solicitarle los datos personales, se le asignará una prioridad relacionada con la gravedad de su caso.
"""

import numpy as np
import math

class MonticuloBinario:
	__elementos: np.ndarray
	__cant = 0

	def __init__(self, cant: int):
		self.__elementos = np.full(cant, None)
		self.__cant = 0
		self.__elementos[0] = -math.inf

	def __intercambiar(self, pos1, pos2):
		aux = self.__elementos[pos1]
		self.__elementos[pos1] = self.__elementos[pos2]
		self.__elementos[pos2] = aux

	def insertar(self, elemento):
		self.__cant += 1
		self.__elementos[self.__cant] = elemento

		actual = self.__cant
		padre = self.__cant // 2
		while self.__elementos[padre] > self.__elementos[actual]:
			self.__intercambiar(padre, actual)

			actual = padre
			padre = actual // 2

	def eliminar(self):
		elementoEliminado = self.__elementos[1]
		self.__elementos[1] = None

		self.__intercambiar(1, self.__cant)
		
		actual = 1
		elemActual = self.__elementos[actual]
		hijoIzq = actual * 2
		hijoDer = actual * 2 + 1
		while hijoDer < len(self.__elementos) and (
			elemActual > self.__elementos[hijoIzq] or
			elemActual > self.__elementos[hijoDer]
		):
			if self.__elementos[hijoIzq] < self.__elementos[hijoDer]:
				self.__intercambiar(actual, hijoIzq)
				actual = hijoIzq
			else:
				self.__intercambiar(actual, hijoDer)
				actual = hijoDer
			
			elemActual = self.__elementos[actual]
			hijoIzq = actual * 2
			hijoDer = actual * 2 + 1

		self.__cant -= 1

		return elementoEliminado

	def estaVacio(self):
		return self.__cant == 0

	def inOrden(self, callback, nivel = 0, posicion = 1):
		if posicion < len(self.__elementos):
			self.inOrden(callback, nivel + 1, posicion * 2)
			callback(self.__elementos[posicion], nivel)
			self.inOrden(callback, nivel + 1, posicion * 2 + 1)

	def __repr__(self):
		if self.__cant == 0:
			return "Monticulo vacio"
		
		string = ''

		def callback(elemento, nivel):
			nonlocal string
			string += ' ' * 4 * nivel + str(elemento) + '\n'

		self.inOrden(callback)

		return string

if __name__ == '__main__':
	monticulo = MonticuloBinario(16)
	monticulo.insertar(1)
	monticulo.insertar(2)
	monticulo.insertar(3)
	monticulo.insertar(4)
	monticulo.insertar(8)
	monticulo.insertar(9)
	monticulo.insertar(10)
	monticulo.insertar(5)
	monticulo.insertar(6)
	monticulo.insertar(7)
	
	print(monticulo)
	monticulo.eliminar()
	print(monticulo)