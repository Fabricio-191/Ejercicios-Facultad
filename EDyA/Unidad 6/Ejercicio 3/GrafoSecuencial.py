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
