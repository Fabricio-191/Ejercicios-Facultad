"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones direccionamiento abierto, utilizando como función de transformación de claves el método de la división, procesando las claves sinónimas a través de la secuencia de Prueba Pseudo Random y considerando trabajar con 1000 claves numéricas que serán generadas pseudoaleatoriamente a través de la función rand.

Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en cuenta:

1.    El tamaño de la tabla Hash no es un número primo.

2.    El tamaño de la tabla Hash sí es un número primo.
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

	raise ValueError('No se encontró un número primo')

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
		return key % self.__size

	def getSize(self):
		return self.__size

	def __randomProbeInsert(self, key: int):
		index = self.__hash(key)
		while self.__table[index] is not None:
			if self.__table[index][0] == key:
				raise ValueError('La clave ya existe')

			index = (index + 1) % self.__size

		return index

	def insertar(self, key: int, value):
		index = self.__randomProbeInsert(key)
		self.__table[index] = (key, value)

	def __randomProbeSearch(self, key: int):
		index = self.__hash(key)
		while self.__table[index] is not None:
			if self.__table[index][0] == key:
				return index

			index = (index + 1) % self.__size

		raise ValueError('No se encontró la clave')

	def buscar(self, key: int):
		index = self.__randomProbeSearch(key)
		return self.__table[index][1]

	def eliminar(self, key: int):
		index = self.__randomProbeSearch(key)
		self.__table[index] = None

	def __str__(self) -> str:
		return str(self.__table)

	def calcularFactorCarga(self):
		cantidad = sum(1 for i in self.__table if i is not None)

		return cantidad / self.__size

if __name__ == '__main__':
	table = TablaHash(1000, False)

	dataset = [(random.randint(0, 100), randomString()) for i in range(1000)]
	for key, value in dataset:
		table.insertar(key, value)

	print('Factor de carga:', table.calcularFactorCarga())

	for key, value in dataset:
		table.buscar(key)
