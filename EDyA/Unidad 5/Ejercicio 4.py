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
	__array: NDArray[Any]
	size = 3

	def __init__(self) -> None:
		self.__array = np.full(Bucket.size, None, dtype=tuple[int, Any])

	def insert(self, key, value):
		if self.__array[-1] is not None:
			raise Exception('El bucket esta completo')

		for i in range(Bucket.size):
			if self.__array[i] is None:
				self.__array[i] = (key, value)
				return True

		return False

	def search(self, key):
		for pair in self.__array:
			if pair is not None and pair[0] == key:
				return pair[1]
		
		return None

class TablaHash:
	__size: int
	__table: NDArray[Any]

	def __init__(self, size: int, usarPrimo = True) -> None:
		self.__size = int(size / 0.7 + 1)

		if usarPrimo:
			self.__size = getPrimeNumber(self.__size)

		self.__table = np.empty(self.__size, dtype=Bucket)
		for i in range(self.__size):
			self.__table[i] = Bucket()

	def getSize(self) -> int:
		return self.__size

	def __hash(self, key: int) -> int:
		return key % self.__size

	def insert(self, key: Any, data: Any):
		self.__table[ self.__hash(key) ].insertar(key, data)

	def search(self, key: int) -> Any:
		return self.__table[ self.__hash(key) ].search(key)

