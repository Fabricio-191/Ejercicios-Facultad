from __future__ import annotations
from typing import Any
import numpy as np
from numpy.typing import NDArray

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
	__pesos: NDArray[Any]

	def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]) -> None:
		self.__nodos = np.array(nodos)
		self.__adyacencia = np.full((len(nodos), len(nodos)), False)
		self.__pesos = np.full((len(nodos), len(nodos)), 1)

		for par in adyacencia:
			i = self.__posNodo(par[0])
			j = self.__posNodo(par[1])

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

	def __esAciclico(self, nodo, recorridos, padres):
		recorridos.append(nodo)

		for nodo in self.adyacentes(nodo):
			if nodo in padres:
				return False

			if nodo not in recorridos:
				if not self.__esAciclico(nodo, recorridos, padres + [nodo]):
					return False

		return True

	def esAciclico(self):
		return self.__esAciclico(self.__nodos[0], [], [])

	def arbolDeRecubrimiento(self):
		pass

	def __algoritmoDijkstra(self, nodo, pesos, recorridos, padres):
		recorridos.append(nodo)

		for nodo in self.adyacentes(nodo):
			if nodo not in recorridos:
				padres[nodo] = nodo
				pesos[nodo] = pesos[nodo] + pesos[nodo]

				self.__algoritmoDijkstra(nodo, pesos, recorridos, padres)
	
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
	adyacencia = [('A', 'B'), ('B', 'C'), ('C', 'E'), ('C', 'D'), ('A', 'E')]

	grafo = Grafo(nodos, adyacencia)

	print(grafo.camino('A', 'E'))
	print(grafo.camino('A', 'D'))
	print(grafo.esAciclico())
	graficar(nodos, adyacencia)