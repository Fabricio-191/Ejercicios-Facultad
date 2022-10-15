"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones usando Buckets, utilizando como función de transformación de claves el método de extracción, y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand; teniendo en cuenta:

Se pide informar:

1.    La cantidad de Buckets desbordados; esto es, todas sus componentes ocupadas.
2.    La cantidad de Buckets subocupados; esto es, menos de la tercera parte ocupada.

Considerando:

1.    La cantidad de Buckets del Área Primaria no es un número primo.          
2.    La cantidad de Buckets del Área Primaria sí es un número primo.
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

class Bucket:
	__items: NDArray[Any]
	__written: NDArray[Any]

	def __init__(self, size: int) -> None:
		self.__items = np.full(size, None)
		self.__written = np.full(size, None)

	def getEmptyPos(self):
		"""Returns first empty pos. If not, returns None"""
		return np.where(self.__items == None)[0][0]

	def write(self, pos: int, item: Any) -> None:
		self.__items[pos] = item
		self.__written[pos] = 1

	def isWritten(self, pos: int):
		return self.__written[pos]

	def __len__(self):
		return len(self.__items)

	def __getitem__(self, index: int):
		return self.__items[index]

class TablaHash:
	__size: int
	__area_prim: NDArray[Any]

	def __init__(self, size: int, usarPrimo = True) -> None:
		self.__size = int(size / 0.7 + 1)

		if usarPrimo:
			self.__size = getPrimeNumber(self.__size)

		self.__area_prim = np.array([
			Bucket(np.random.randint(1, 5)) # Random bucket size
			for _ in range(self.__size)
		])

		def __hash(self, key: int) -> int:
			return key % self.__size					