from GrafoBase import GrafoBase, Nodo
import numpy as np


class GrafoSecuencial(GrafoBase):
	def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]) -> None:
		super().__init__(nodos)
		self._adyacencia = np.full((len(nodos), len(nodos)), False)
		
		for nodo1, nodo2 in adyacencia:
			i = self._posNodo(nodo1)
			j = self._posNodo(nodo2)

			self._adyacencia[i][j] = self._adyacencia[j][i] = True


if __name__ == '__main__':
	nodos = ['A', 'B', 'C', 'D', 'E', 'F']
	adyacencia = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]

	grafo = GrafoSecuencial(nodos, adyacencia)

	print(grafo.caminoMinimo('A', 'D'))
	print(grafo.caminoMinimo('A', 'E'))
	print(grafo.caminoMinimo('A', 'B'))
	print(grafo.esAciclico())
	GrafoSecuencial.graficar(nodos, adyacencia)
