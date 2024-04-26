import numpy as np
from typing import Any
# from numpy.typing import NDArray  # type: ignore

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
	__nodos: Any # NDArray[Any]
	_adyacencia: Any # NDArray[Any]
	__pesos: Any # NDArray[Any]

	def __init__(self, nodos: list[Nodo]) -> None:
		self.__nodos = np.array(nodos)
		self.__pesos = np.full((len(nodos), len(nodos)), 1)

	def _posNodo(self, nodo):
		for i in range(len(self.__nodos)):
			if self.__nodos[i] == nodo:
				return i
		
		raise Exception("Nodo invalido")

	def peso(self, nodo1, nodo2):
		return self.__pesos[self._posNodo(nodo1)][self._posNodo(nodo2)]

	def setPesos(self, pesos: list[tuple[Nodo, Nodo, float]]):
		for nodo1, nodo2, peso in pesos:
			i = self._posNodo(nodo1)
			j = self._posNodo(nodo2)

			self.__pesos[i][j] = self.__pesos[j][i] = peso
	
	def adyacentes(self, nodo: Nodo):
		posNodo = self._posNodo(nodo)
		
		adyacentes = []
		for i in range(len(self._adyacencia)):
			if self._adyacencia[posNodo][i]:
				adyacentes.append(self.__nodos[i])

		return adyacentes

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

		if camino[0] != nodo1:
			raise Exception("No hay camino")
			
		return camino[::-1]

	def camino(self, inicio, destino, recorridos = []):
		if inicio == destino:
			return [destino]

		recorridos.append(inicio)

		for nodo in self.adyacentes(inicio):
			if nodo not in recorridos:
				camino = self.camino(nodo, destino, recorridos)
				if camino != None:
					return [inicio] + camino
		
		raise Exception("No hay camino")


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

	def recorridoEnProfundidad(self, nodo, callback, recorridos = []):
		callback(nodo)
		recorridos.append(nodo)

		for nodo in self.adyacentes(nodo):
			if nodo not in recorridos:
				self.recorridoEnProfundidad(nodo, recorridos, callback)


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

	def esAciclico(self):
		for nodo in self.__nodos:
			for nodo2 in self.adyacentes(nodo):
				caminos = self._todosLosCaminosPosibles(nodo2, nodo, [], [])
				for camino in caminos:
					if len(camino) >= 2:
						return False

		return True

	"""
	def esAciclico(self):
		for nodo in self.__nodos:
			for nodo2 in self.adyacentes(nodo):
				for nodo3 in self.adyacentes(nodo2):
					if nodo3 in self.adyacentes(nodo):
						return False

		return True
	"""
	
	@staticmethod
	def graficar(nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
		G = nx.Graph()
		G.add_nodes_from(nodos)
		G.add_edges_from(adyacencia)
		nx.draw(G, with_labels=True)
		plt.show()

"""
def AlgoritmoWarshall(matrizAdyacencia: Any): # NDArray[Any]):
	# inicializar matriz de adyacencia
	matrizAdyacencia = np.array(matrizAdyacencia, dtype=bool)

	# algoritmo de warshall
	for k in range(len(matrizAdyacencia)):
		for i in range(len(matrizAdyacencia)):
			for j in range(len(matrizAdyacencia)):
				matrizAdyacencia[i][j] = matrizAdyacencia[i][j] or (matrizAdyacencia[i][k] and matrizAdyacencia[k][j])

	return matrizAdyacencia

def AlgoritmoFloyd(matrizAdyacencia: Any): # NDArray[Any]):
	# inicializar matriz de adyacencia
	matrizAdyacencia = np.array(matrizAdyacencia, dtype=int)

	# algoritmo de floyd
	for k in range(len(matrizAdyacencia)):
		for i in range(len(matrizAdyacencia)):
			for j in range(len(matrizAdyacencia)):
				a = matrizAdyacencia[i][k] + matrizAdyacencia[k][j]
				if matrizAdyacencia[i][j] > a:
					matrizAdyacencia[i][j] = a

	return matrizAdyacencia

def AlgoritmoDijkstra(self, nodo1, nodo2):
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
		for w in self.nodosSalida(v): # type: ignore
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
"""
