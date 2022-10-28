from typing import Any
import numpy as np
from numpy.typing import NDArray

from ListaEnlazada import ListaEnlazada

import networkx as nx
import matplotlib.pyplot as plt

"""
Defina TAD Grafo e implemente todas las operaciones vistas en teoría y determine la complejidad de cada una de ellas.
	a. Representación secuencial. 
	b. Representación encadenada.
"""

Nodo = str

class Grafo:
	__nodos: NDArray[Any]
	__adyacencia: NDArray[Any]

	def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]) -> None:
		self.__nodos = np.array(nodos)
		self.__adyacencia = np.array([ListaEnlazada() for i in range(len(nodos))])

		for nodo1, nodo2 in adyacencia:
			i = self.__posNodo(nodo1)
			j = self.__posNodo(nodo2)

			self.__adyacencia[i].insertar(j)
			self.__adyacencia[j].insertar(i)
				
	def __posNodo(self, nodo: Nodo):
		for i in range(len(self.__nodos)):
			if self.__nodos[i] == nodo:
				return i
		
		raise Exception("Nodo invalido")

	def adyacentes(self, nodo: Nodo):
		posNodo = self.__posNodo(nodo)
		
		adyacentes = []
		for i in range(len(self.__adyacencia)):
			if self.__adyacencia[posNodo].has(i):
				adyacentes.append(self.__nodos[i])

		return adyacentes

	def __camino(self, nodo1, nodo2, recorridos):
		if nodo1 == nodo2:
			return [nodo1]
		else:
			for nodo in self.adyacentes(nodo1):
				if nodo not in recorridos:
					camino = self.__camino(nodo, nodo2, recorridos + [nodo1])
					if camino is not None:
						return [nodo1] + camino

		return None

	# devulve el camino del nodo1 al nodo2
	def camino(self, nodo1: Nodo, nodo2: Nodo) -> list[Nodo] | None:
		self.__posNodo(nodo1)
		self.__posNodo(nodo2)
		
		camino = self.__camino(nodo1, nodo2, [])
		if camino is None:
			raise Exception("No existe camino entre los nodos")

		return camino

	def caminoMinimo(self, nodo1: Nodo, nodo2: Nodo):
		pass

	def esConexo(self):
		encontrados = []
		self.recorridoEnAncho(self.__nodos[0], lambda nodo: encontrados.append(nodo))

		return len(encontrados) == len(self.__nodos)

	def esAciclico(self):
		for nodo in self.__nodos:
			for adyacente in self.adyacentes(nodo):
				if self.camino(adyacente, nodo):
					return False

		return True

	def arbolDeRecubrimiento(self):
		pass
	
	# recorrido en ancho del grafo
	def recorridoEnAncho(self, nodo, callback):
		recorridos = []
		cola = [nodo]

		while len(cola) > 0:
			nodo = cola.pop(0)
			callback(nodo)
			recorridos.append(nodo)

			for nodo in self.adyacentes(nodo):
				if nodo not in recorridos:
					cola.append(nodo)
					recorridos.append(nodo)

	def __recorridoEnProfundidad(self, nodo, recorridos, callback):
		callback(nodo)
		recorridos.append(nodo)

		for nodo in self.adyacentes(nodo):
			if nodo not in recorridos:
				self.__recorridoEnProfundidad(nodo, recorridos, callback)

	def recorridoEnProfundidad(self, nodo, callback):
		self.__recorridoEnProfundidad(nodo, [], callback)

def graficar(nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
	G = nx.Graph()
	G.add_nodes_from(nodos)
	G.add_edges_from(adyacencia)
	nx.draw(G, with_labels=True)
	plt.show()

if __name__ == '__main__':
	nodos = ['A', 'B', 'C', 'D', 'E']
	adyacencia = [('A', 'B'), ('B', 'C'), ('C', 'E'), ('C', 'D')]

	grafo = Grafo(nodos, adyacencia)

	print(grafo.camino('A', 'E'))
	print(grafo.camino('A', 'D'))
	graficar(nodos, adyacencia)