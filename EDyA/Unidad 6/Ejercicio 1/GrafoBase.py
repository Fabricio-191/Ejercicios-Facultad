import numpy as np
from typing import Any
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

class GrafoBase:
	_nodos: NDArray[Any]
	_adyacencia: NDArray[Any]
	_pesos: NDArray[Any]

	def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]) -> None:
		self._nodos = np.array(nodos)
		self._pesos = np.full((len(nodos), len(nodos)), 1)

	def _posNodo(self, nodo):
		for i in range(len(self._nodos)):
			if self._nodos[i] == nodo:
				return i
		
		raise Exception("Nodo invalido")

	def peso(self, nodo1, nodo2):
		return self._pesos[self._posNodo(nodo1)][self._posNodo(nodo2)]

	def setPesos(self, pesos: list[tuple[Nodo, Nodo, float]]):
		for nodo1, nodo2, peso in pesos:
			i = self._posNodo(nodo1)
			j = self._posNodo(nodo2)

			self._pesos[i][j] = self._pesos[j][i] = peso

	def adyacentes(self, nodo: Nodo) -> list[Nodo]:
		raise NotImplementedError

	def grado(self, nodo):
		return len(self.adyacentes(nodo))

	def esConexo(self):
		encontrados = []
		self.recorridoEnAncho(self._nodos[0], lambda nodo: encontrados.append(nodo))

		return len(encontrados) == len(self._nodos)


	def caminoMinimo(self, nodo1, nodo2):
		# Inicializar tabla
		tabla = {}
		for nodo in self._nodos:
			tabla[nodo] = Registro(nodo, False, np.inf, None)
		tabla[nodo1].distancia = 0

		# Dijkstra
		for i in range(len(self._nodos)):
			# Buscar vertice con distancia mas corta y desconocido
			v = None
			for nodo in self._nodos:
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

	def _camino(self, inicio, destino, recorridos):
		if inicio == destino:
			return [destino]

		recorridos.append(inicio)

		for nodo in self.adyacentes(inicio):
			if nodo not in recorridos:
				camino = self._camino(nodo, destino, recorridos)
				if camino != None:
					return [inicio] + camino

		return None

	def camino(self, inicio, destino):
		return self._camino(inicio, destino, [])


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

	def _recorridoEnProfundidad(self, nodo, recorridos, callback):
		callback(nodo)
		recorridos.append(nodo)

		for nodo in self.adyacentes(nodo):
			if nodo not in recorridos:
				self._recorridoEnProfundidad(nodo, recorridos, callback)

	def recorridoEnProfundidad(self, nodo, callback):
		self._recorridoEnProfundidad(nodo, [], callback)


	def _todosLosCaminosPosibles(self, nodo, destino, recorridos, caminos):
		recorridos.append(nodo)

		if nodo == destino:
			caminos.append(recorridos[:])
		else:
			for nodo in self.adyacentes(nodo):
				if nodo not in recorridos:
					self._todosLosCaminosPosibles(nodo, destino, recorridos, caminos)

		recorridos.pop()
		return caminos

	# devuelve true si el grafo tiene un ciclo de longitud 3 o mas
	def tieneCicloDeLongitud3omas(self):
		for nodo in self._nodos:
			adyacentes = self.adyacentes(nodo)
			for nodo2 in adyacentes:
				caminos = self._todosLosCaminosPosibles(nodo2, nodo, [], [])
				for camino in caminos:
					if len(camino) >= 3:
						return True

		return False

	def esAciclico(self):
		return not self.tieneCicloDeLongitud3omas()
	
	@staticmethod
	def graficar(nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
		G = nx.Graph()
		G.add_nodes_from(nodos)
		G.add_edges_from(adyacencia)
		nx.draw(G, with_labels=True)
		plt.show()
