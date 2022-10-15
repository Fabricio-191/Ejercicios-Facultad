"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones encadenamiento, utilizando como función de transformación de claves el método de plegado, y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand.

Se pide informar:

1.    La longitud de cada una de las listas de claves sinónimas.
2.    La cantidad de esas listas que registran una longitud que varía en hasta 3 unidades, por exceso o por defecto, respecto al promedio de las longitudes de dichas listas.

Considerando:

1.    La cantidad de listas de claves sinónimas no es un número primo.
2.    La cantidad de listas de claves sinónimas sí es un número primo.
"""
from numpy.typing import NDArray
from typing import Any

import numpy as np
import string, random

def getPrimeNumber(size):
	for i in range(size, 2 * size):
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			return i

	raise ValueError('No se encontró un número primo')

def randomString(stringLength = 10):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

class Node:
	__key: Any
	__data: Any
	__next: 'Node' | None

	def __init__(self, key: Any, data: Any, next: 'Node' | None = None):
		self.__key = key
		self.__data = data
		self.__next = next

	def getKey(self): return self.__key
	def getData(self): return self.__data
	def setData(self, data: Any): self.__data = data
	def setNext(self, next: 'Node' | None): self.__next = next
	def getNext(self): return self.__next

class TablaHash:
	__size: int
	__table: NDArray[Any]

	def __init__(self, size: int, usarPrimo = True) -> None:
		self.__size = int(size / 0.7 + 1)

		if usarPrimo:
			self.__size = getPrimeNumber(self.__size)

		self.__table = np.full(self.__size, None)

	def __hash(self, key: int) -> int:
		result = 0

		while key != 0:
			result += key % 100
			key //= 100

		return result % self.__size

	def getSize(self):
		return self.__size

	def insertar(self, key: int, value):
		index = self.__hash(key)

		nodo = self.__table[index]

		if nodo is None:
			self.__table[index] = Node(key, value)
		elif nodo.getKey() == key:
			nodo.setData(value)
		else:
			while nodo.getNext() is not None:
				nodo = nodo.getNext()

				if nodo.getKey() == key:
					nodo.setData(value)
					return

			nodo.setNext(Node(key, value))

	def buscar(self, key: int):
		index = self.__hash(key)

		nodo = self.__table[index]
		while nodo is not None:
			if nodo.getKey() == key:
				return nodo.getKey()

			nodo = nodo.getNext()

		return None

	def eliminar(self, key: int):
		index = self.__hash(key)

		nodo = self.__table[index]
		ant = None

		while nodo is not None:
			if nodo.getKey() == key:
				if ant is None:
					self.__table[index] = nodo.getNext()
				else:
					ant.setNext(nodo.getNext())

				return True

			ant = nodo
			nodo = nodo.getNext()

		return False

	def calcularFactorCarga(self):
		cantidad = sum(1 for i in self.__table if i is not None)

		return cantidad / self.__size

	def __repr__(self) -> str:
		return str(self.__table)

if __name__ == '__main__':
	dataset = [(random.randint(0, 1000000), randomString()) for i in range(1000)]

	table1 = TablaHash(1000, False)
	"""
	table2 = TablaHash(1000, True)

	for key, value in dataset:
		table1.insertar(key, value)
		table2.insertar(key, value)

	searchKey = random.choice(dataset)[0]

	print('Tabla 1 (sin usar un numero primo)')
	print(f'Longitud de búsqueda: {table1.calcularLongitudSecuenciaBusqueda(searchKey)}')
	print(f'Factor de carga: {table1.calcularFactorCarga() * 100:.2f}%')

	print('Tabla 2 (usando un numero primo)')
	print(f'Longitud de búsqueda: {table2.calcularLongitudSecuenciaBusqueda(searchKey)}')
	print(f'Factor de carga: {table2.calcularFactorCarga() * 100:.2f}%')
	"""