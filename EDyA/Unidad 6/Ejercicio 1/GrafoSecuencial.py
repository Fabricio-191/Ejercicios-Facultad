from GrafoBase import GrafoBase, Nodo
import numpy as np
class GrafoSecuencial(GrafoBase):
	def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]) -> None:
		super().__init__(nodos, adyacencia)

		self._adyacencia = np.full((len(nodos), len(nodos)), False)
		for par in adyacencia:
			i = self._posNodo(par[0])
			j = self._posNodo(par[1])

			self._adyacencia[i][j] = self._adyacencia[j][i] = True
	
	def adyacentes(self, nodo: Nodo):
		posNodo = self._posNodo(nodo)
		
		adyacentes = []
		for i in range(len(self._adyacencia)):
			if self._adyacencia[posNodo][i]:
				adyacentes.append(self._nodos[i])

		return adyacentes

if __name__ == '__main__':
	nodos = ['A', 'B', 'C', 'D', 'E']
	adyacencia = [('A', 'B'), ('B', 'C'), ('C', 'E'), ('C', 'D'), ('D', 'E')]

	grafo = GrafoSecuencial(nodos, adyacencia)

	print(grafo.caminoMinimo('A', 'D'))
	print(grafo.caminoMinimo('A', 'E'))
	print(grafo.caminoMinimo('A', 'B'))
	print(grafo.esAciclico())
	grafo.graficar(nodos, adyacencia)
