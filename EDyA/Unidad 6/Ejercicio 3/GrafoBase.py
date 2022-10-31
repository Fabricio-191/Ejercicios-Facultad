from re import S
import numpy as np
from typing import Any
# from numpy.typing import NDArray  # type: ignore

import networkx as nx
import matplotlib.pyplot as plt

Nodo = str

class GrafoBase:
	__nodos: Any # NDArray[Any]
	_adyacencia: Any # NDArray[Any]

	def __init__(self, nodos: list[Nodo]) -> None:
		self.__nodos = np.array(nodos)

	def _posNodo(self, nodo):
		for i in range(len(self.__nodos)):
			if self.__nodos[i] == nodo:
				return i
		
		raise Exception("Nodo invalido")

	def adyacentes(self, nodo: Nodo):
		posNodo = self._posNodo(nodo)
		
		adyacentes = []
		for i in range(len(self._adyacencia)):
			if self._adyacencia[posNodo][i]:
				adyacentes.append(self.__nodos[i])

		return adyacentes

	def grado(self, nodo):
		return len(self.adyacentes(nodo))

	def esConexo(self):
		encontrados = []
		self.recorridoEnAncho(self.__nodos[0], lambda nodo: encontrados.append(nodo))

		return len(encontrados) == len(self.__nodos)

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

	@staticmethod
	def graficar(nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
		G = nx.Graph()
		G.add_nodes_from(nodos)
		G.add_edges_from(adyacencia)
		nx.draw(G, with_labels=True)
		plt.show()
