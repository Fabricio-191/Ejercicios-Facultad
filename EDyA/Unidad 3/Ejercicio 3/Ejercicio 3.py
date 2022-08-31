"""
El gobierno de la Nación cuenta con conjunto de datos dataset: Estadística de incendios forestales descritos por superficie (hectárea), número de focos por departamento y por provincia.

se pide:

b) Leer los datos del archivo csv, y generar una lista donde cada componente contenga: Nombre de provincia y superficie total afectada.
c) Mostrar, Nombre de provincia y superficie afectada ordenada de mayor a menor por superficie total afectada. 
"""

import numpy as np
import csv
from os import path

class Lista:
	__elementos: np.ndarray	
	__tope: int
	__tamañoTotal: int

	def __init__(self, tamañoTotal):
		self.__elementos = np.full(tamañoTotal, None)
		self.__tope = 0
		self.__tamañoTotal = tamañoTotal

	def __posicionValida(self, pos):
		return 0 <= pos <= self.__tope

	def __shift(self, pos, forward = True):
		if forward:
			for i in range(self.__tope, pos, -1):
				self.__elementos[i] = self.__elementos[i - 1]
		else:
			for i in range(pos, self.__tope):
				self.__elementos[i] = self.__elementos[i + 1]

	def estaLlena(self):
		return self.__tope == self.__tamañoTotal

	def estaVacia(self):
		return self.__tope == 0

	def getTamaño(self):
		return self.__tope

	def insertar(self, elemento, pos):
		if self.estaLlena():
			raise Exception('La lista está llena')

		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		self.__shift(pos)
		self.__elementos[pos] = elemento
		self.__tope += 1

	def eliminar(self, pos):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		self.__shift(pos, False)
		self.__tope -= 1

	def recuperar(self, pos):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		return self.__elementos[pos]

	def buscar(self, elem):
		pos = 0

		while pos < self.__tope and self.__elementos[pos] != elem:
			pos += 1

		return pos if pos != self.__tope else -1

	def primerElemento(self):
		return self.__elementos[0] if not self.estaVacia() else None

	def ultimoElemento(self):
		return self.__elementos[self.__tope - 1] if not self.estaVacia() else None

	def __iter__(self):
		return iter(self.__elementos[:self.__tope])

	def __repr__(self):
		return str(list(self))

if __name__ == '__main__':
	with open(path.dirname(__file__) + '/incendios.csv', 'r') as archivo:
		reader = csv.reader(archivo, delimiter=';')
		next(reader)

		lista = Lista(1000)

		for fila in reader:
			lista.insertar(fila, lista.getTamaño())
			
		print(lista)