from GrafoBase import GrafoBase, Nodo
import numpy as np
from ListaEnlazada import ListaEnlazada

class GrafoEncadenado(GrafoBase):
	def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]) -> None:
		super().__init__(nodos)
		self._adyacencia = np.array([ListaEnlazada() for i in range(len(nodos))])

		for nodo1, nodo2 in adyacencia:
			i = self._posNodo(nodo1)
			j = self._posNodo(nodo2)

			self._adyacencia[i].insertar(j)
			self._adyacencia[j].insertar(i)

if __name__ == '__main__':
	nodos = ['A', 'B', 'C', 'D', 'E', 'F']
	adyacencia = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]

	grafo = GrafoEncadenado(nodos, adyacencia)

	print(grafo.caminoMinimo('A', 'D'))
	print(grafo.caminoMinimo('A', 'E'))
	print(grafo.caminoMinimo('A', 'B'))
	print(grafo.esAciclico())
	grafo.graficar(nodos, adyacencia)
