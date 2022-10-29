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

class Registro:
    def __init__(self, nodo, conocido, distancia, camino):
        self.nodo = nodo
        self.conocido = conocido
        self.distancia = distancia
        self.camino = camino

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

			self.__adyacencia[i][j] = self.__adyacencia[j][i] = True

	def __posNodo(self, nodo):
		for i in range(len(self.__nodos)):
			if self.__nodos[i] == nodo:
				return i
		
		raise Exception("Nodo invalido")

	def peso(self, nodo1, nodo2):
		return self.__pesos[self.__posNodo(nodo1)][self.__posNodo(nodo2)]

	def setPesos(self, pesos: list[tuple[Nodo, Nodo, float]]):
		for nodo1, nodo2, peso in pesos:
			i = self.__posNodo(nodo1)
			j = self.__posNodo(nodo2)

			self.__pesos[i][j] = self.__pesos[j][i] = peso

	def adyacentes(self, nodo: Nodo):
		posNodo = self.__posNodo(nodo)
		
		adyacentes = []
		for i in range(len(self.__adyacencia)):
			if self.__adyacencia[posNodo][i]:
				adyacentes.append(self.__nodos[i])

		return adyacentes

	def grado(self, nodo):
		return len(self.adyacentes(nodo))

	def esConexo(self):
		encontrados = []
		self.recorridoEnAncho(self.__nodos[0], lambda nodo: encontrados.append(nodo))

		return len(encontrados) == len(self.__nodos)


	def caminoMinimo(self, nodo1, nodo2):
		# Inicializar tabla
		tabla = {}
		for nodo in self.__nodos:
			tabla[nodo] = Registro(nodo, False, np.inf, None)
		tabla[nodo1].distancia = 0

		# Dijkstra
		for i in range(len(self.__nodos)):
			# Buscar vertice con distancia mas corta y desconocido
			v = None
			for nodo in self.__nodos:
				if not tabla[nodo].conocido:
					if v == None or tabla[nodo].distancia < tabla[v].distancia:
						v = nodo

			tabla[v].conocido = True

			# Actualizar tabla
			for w in self.adyacentes(v): # type: ignore
				if not tabla[w].conocido:
					if tabla[v].distancia + self.peso(v, w) < tabla[w].distancia:
						tabla[w].distancia = tabla[v].distancia + self.peso(v, w)
						tabla[w].camino = v
		
		# Construir camino
		camino = []
		nodo = nodo2
		while nodo != None:
			camino.append(nodo)
			nodo = tabla[nodo].camino

		return camino[::-1]

	def __camino(self, inicio, destino, recorridos):
		if inicio == destino:
			return [destino]

		recorridos.append(inicio)

		for nodo in self.adyacentes(inicio):
			if nodo not in recorridos:
				camino = self.__camino(nodo, destino, recorridos)
				if camino != None:
					return [inicio] + camino

		return None

	def camino(self, inicio, destino):
		return self.__camino(inicio, destino, [])


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


	def __todosLosCaminosPosibles(self, nodo, destino, recorridos, caminos):
		recorridos.append(nodo)

		if nodo == destino:
			caminos.append(recorridos[:])
		else:
			for nodo in self.adyacentes(nodo):
				if nodo not in recorridos:
					self.__todosLosCaminosPosibles(nodo, destino, recorridos, caminos)

		recorridos.pop()
		return caminos

	# devuelve true si el grafo tiene un ciclo de longitud 3 o mas
	def tieneCicloDeLongitud3omas(self):
		for nodo in self.__nodos:
			adyacentes = self.adyacentes(nodo)
			for nodo2 in adyacentes:
				caminos = self.__todosLosCaminosPosibles(nodo2, nodo, [], [])
				for camino in caminos:
					if len(camino) >= 3:
						return True

		return False

	def esAciclico(self):
		return not self.tieneCicloDeLongitud3omas()


def graficar(nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
	G = nx.Graph()
	G.add_nodes_from(nodos)
	G.add_edges_from(adyacencia)
	nx.draw(G, with_labels=True)
	plt.show()

if __name__ == '__main__':
	nodos = ['A', 'B', 'C', 'D', 'E']
	adyacencia = [('A', 'B'), ('B', 'C'), ('C', 'E'), ('C', 'D'), ('D', 'E')]

	grafo = Grafo(nodos, adyacencia)

	print(grafo.caminoMinimo('A', 'D'))
	print(grafo.caminoMinimo('A', 'E'))
	print(grafo.caminoMinimo('A', 'B'))
	print(grafo.esAciclico())
	graficar(nodos, adyacencia)
