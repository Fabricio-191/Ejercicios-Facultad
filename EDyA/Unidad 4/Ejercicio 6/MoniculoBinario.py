"""
Ejercicio Nº6: Codifique un programa que simule el funcionamiento de la lista de espera del quirófano de un hospital. Cada vez que el quirófano esté desocupado, se operará al paciente de mayor urgencia, dentro de esa lista de espera. Al ingresar un paciente al hospital, además de solicitarle los datos personales, se le asignará una prioridad relacionada con la gravedad de su caso.
"""

import numpy as np
import math

class MonticuloBinario:
	__elementos: np.ndarray
	__cant = 0

	def __init__(self, cant: int):
		self.__elementos = np.full(cant, None)
		self.__cant = 0
		self.__elementos[0] = -math.inf

	def insertar(self, elemento):
		self.__cant += 1
		self.__elementos[self.__cant] = elemento

		actual = self.__cant
		padre = self.__cant // 2
		while self.__elementos[padre] > self.__elementos[actual]:
			aux = self.__elementos[padre]
			self.__elementos[padre] = self.__elementos[actual]
			self.__elementos[actual] = aux

			actual = padre
			padre = actual // 2

	def eliminar(self):
		elemento = self.__elementos[1]
		self.__eliminar(1)

		return elemento
	
	def __grado(self, indice):
		posizq = indice * 2
		posder = indice * 2 + 1

		if posizq > self.__cant:
			return 0
		elif posder > self.__cant:
			return 1
		else:
			return 2

	def __eliminar(self, indice):
		if self.__grado(indice) == 0:
			self.__elementos[indice] = None
			return
		
		posizq = indice * 2
		posder = indice * 2 + 1

		elemizq = self.__elementos[posizq]
		elemder = self.__elementos[posder]

		if self.__grado(indice) == 1:
			if elemizq is None:
				self.__elementos[indice] = elemder
				self.__eliminar(posder)
			else:
				self.__elementos[indice] = elemizq
				self.__eliminar(posizq)
		elif self.__grado(indice) == 2:
			if elemizq < elemder:
				self.__elementos[indice] = elemizq
				self.__eliminar(posizq)
			else:
				self.__elementos[indice] = elemder
				self.__eliminar(posder)

	def __repr__(self):        
		cantniveles = math.ceil(math.log2(self.__cant))
		niveles = []

		for i in range(cantniveles):
			niveles.append([])
			for j in range(2**i):
				niveles[i].append(self.__elementos[2**i + j] or '-1')
		
		string = ''
		
		for i in range(cantniveles):
			cantEspacios = 2 ** (cantniveles - i)
			for j in range(2**i):
				string += ' ' * cantEspacios +  f'{niveles[i][j]} '
			string += '\n'

		return string # str(self.__elementos[:self.__cant+1])

if __name__ == '__main__':
	monticulo = MonticuloBinario(100)
	monticulo.insertar(1)
	monticulo.insertar(2)
	monticulo.insertar(3)
	monticulo.insertar(4)
	monticulo.insertar(8)
	monticulo.insertar(9)
	monticulo.insertar(10)
	monticulo.insertar(5)
	monticulo.insertar(6)
	monticulo.insertar(7)
	
	print(monticulo)
	monticulo.eliminar()
	print(monticulo)
