"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones encadenamiento, utilizando como función de transformación de claves el método de plegado, y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand.

Se pide informar:

1.    La longitud de cada una de las listas de claves sinónimas.
2.    La cantidad de esas listas que registran una longitud que varía en hasta 3 unidades, por exceso o por defecto, respecto al promedio de las longitudes de dichas listas.

Considerando:

1.    La cantidad de listas de claves sinónimas no es un número primo.
2.    La cantidad de listas de claves sinónimas sí es un número primo.
"""

from enum import IntEnum
import numpy as np
from typing import Any
from numpy.typing import NDArray
import string, random

def getPrimeNumber(size):
	for i in range(size, 2 * size):
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			return i

	raise ValueError("No se encontró un número primo")

def randomString(stringLength = 10):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

class TablaHash:
	__size: int
	__table: NDArray[Any]

	def __init__(self, size: int, usarPrimo = True) -> None:
		if usarPrimo:
			self.__size = getPrimeNumber(size)
		else:
			self.__size = size

		self.__table = np.full(self.__size, None)

	def __hash(self, key: int) -> int:
		indices = [key % 10_000 // 100, key % 100 // 10]
		index = 0
		contador = 0
		for (power, indice) in zip(range(2, 0, -1), indices):
			if contador == power:
				index += contador

			contador = (contador * 10 + indice) % self.__size

		return index

	def getSize(self):
		return self.__size

	def insertar(self, key: int):
		index = self.__hash(key)
		if self.__table[index] is None:
			self.__table[index] = Node(endNode = True)

		self.__table[index] = Node(key, self.__table[index])


class Node:
	__key: int
	__next: Any

	def __init__(self, key: int, next: Any = None, endNode = False) -> None:
		self.__key = key
		self.__next = next

		if endNode:
			self.__next = Node()

	def getKey(self):
		return self.__key

	def getNext(self):
		return self.__next

	def setNext(self, next: Any):
		self.__next = next

	def isEndNode(self):
		return self.__next is None

	def __str__(self) -> str:
		return f"({self.__key}, {self.__next})"