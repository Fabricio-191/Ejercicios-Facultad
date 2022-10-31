from DiGrafoBase import DiGrafoBase, Nodo
import numpy as np
from ListaEnlazada import ListaEnlazada

class DiGrafoEncadenado(DiGrafoBase):
	def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]) -> None:
		super().__init__(nodos)
		self._adyacencia = np.array([ListaEnlazada() for i in range(len(nodos))])

		for nodo1, nodo2 in adyacencia:
			i = self._posNodo(nodo1)
			j = self._posNodo(nodo2)

			self._adyacencia[i].insertar(j)


if __name__ == '__main__':
	nodos = ['A', 'B', 'C', 'D', 'E']
	adyacencia = [('A', 'B'), ('B', 'C'), ('C', 'E'), ('C', 'D'), ('D', 'E')]

	grafo = DiGrafoEncadenado(nodos, adyacencia)

	print(grafo.caminoMinimo('A', 'D'))
	print(grafo.caminoMinimo('A', 'E'))
	print(grafo.caminoMinimo('A', 'B'))
	print(grafo.esAciclico())
	grafo.graficar(nodos, adyacencia)
