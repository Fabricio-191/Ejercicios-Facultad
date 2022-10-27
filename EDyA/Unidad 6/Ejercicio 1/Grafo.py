from __future__ import annotations
from typing import Any
import numpy as np
from numpy.typing import NDArray

"""
Defina TAD Grafo e implemente todas las operaciones vistas en teoría y determine la complejidad de cada una de ellas.
	a. Representación secuencial. 
	b. Representación encadenada.
"""

def contains(array: list[Any], subarray: list[Any]) -> bool:
	for elem in subarray:
		if elem not in array:
			return False

	return True

Nodo = int

class Grafo:
	__nodos: NDArray
	__adyacencia: NDArray

	def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]) -> None:
		N = len(nodos)
		self.__nodos = np.array(nodos)
		self.__adyacencia = np.full((len(nodos), len(nodos)), False)

		for nodo1, nodo2 in adyacencia:
			i = self.__posNodo(nodo1)
			j = self.__posNodo(nodo2)

			self.__adyacencia[i][j] = True
			self.__adyacencia[j][i] = True
				
	def __posNodo(self, nodo):
		for i in range(len(self.__nodos)):
			if self.__nodos[i] == nodo:
				return i
		
		raise Exception("Nodo invalido")

	def adyacentes(self, nodo: Nodo):
		posNodo = self.__posNodo(nodo)
		
		adyacentes = []
		for i in range(len(self.__adyacencia)):
			if self.__adyacencia[posNodo][i]:
				adyacentes.append(self.__nodos[i])

		return adyacentes

	def camino(self, nodo1: Nodo, nodo2: Nodo):
		self.__posNodo(nodo1)
		self.__posNodo(nodo2)

	def caminoMinimo(self, nodo1: Nodo, nodo2: Nodo):
		self.__posNodo(nodo1)
		self.__posNodo(nodo2)

	def esConexo(self):
		pass

	def esAciclico(self):
		pass

	def arbolDeRecubrimiento(self):
		pass

	def __inAncho(self, nodo, recorridos, callback):
		pass

	def inAncho(self, nodo, callback):
		self.__inAncho(nodo, [], callback)

	def __inProfundidad(self, nodo, recorridos, callback):
		callback(nodo)
		recorridos.append(nodo)

		for nodo in self.adyacentes(nodo):
			if nodo not in recorridos:
				self.__inProfundidad(nodo, recorridos, callback)

	def inProfundidad(self, nodo, callback):
		self.__inProfundidad(nodo, [], callback)

if __name__ == '__main__':
	nodos = [6, 7, 8, 9, 10]
	adyacencia = [(6, 7), (7, 8), (8, 9), (9, 10)]

	grafo = Grafo(nodos, adyacencia)

	grafo.inAncho(6, print)