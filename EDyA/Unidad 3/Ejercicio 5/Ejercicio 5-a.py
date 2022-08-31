"""
Diseñe el algoritmo que, apoyado en el TAD Lista, elimine elementos con

valores repetidos de una lista de números naturales.

Entrada  L = ( 10, 5, 7, 5, 2, 10)      à       Salida  L = ( 10, 5, 7, 2)

a) Implemente el Código del ítem a.

d) Considere la lista dada, ordenada por contenido, y en función de esto optimice el código del ítem b. 
"""
from __future__ import annotations
from typing import Any
import numpy as np

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

def eliminarRepetidos(L: Lista):
	aux = []
	i = 0
	while i < L.getTamaño():
		elem = L.recuperar(i)
		if elem not in aux:
			aux.append(elem)
			i += 1
		else:
			L.eliminar(i)

if __name__ == '__main__':
	l = Lista(100)
	l.insertar(10, 0)
	l.insertar(5, 1)
	l.insertar(7, 2)
	l.insertar(5, 3)
	l.insertar(2, 4)
	l.insertar(10, 5)

	print(l)
	eliminarRepetidos(l)
	print(l)