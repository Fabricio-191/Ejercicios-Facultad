"""
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones direccionamiento abierto, utilizando como función de transformación de claves el método de la división, procesando las claves sinónimas a través de la secuencia de Prueba Pseudo Random y considerando trabajar con 1000 claves numéricas que serán generadas pseudoaleatoriamente a través de la función rand.

Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en cuenta:

1.    El tamaño de la tabla Hash no es un número primo.
2.    El tamaño de la tabla Hash sí es un número primo.
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

class TablaHash:
	__size: int
	__table: NDArray[Any]
	__randomNum: int

	def __init__(self, size: int, usarPrimo = True) -> None:
		self.__size = int(size / 0.7 + 1)

		if usarPrimo:
			self.__size = getPrimeNumber(self.__size)

		self.__randomNum = random.randint(1, self.__size)
		self.__table = np.full(self.__size, None)

	def __hash(self, key: int) -> int:
		return key % self.__size

	def getSize(self):
		return self.__size

	def __pseudoRandomProbe(self, key: int):
		originalIndex = index = self.__hash(key)

		while self.__table[index] is not None and self.__table[index][0] != key:
			index = self.__hash(index + self.__randomNum)

			if index == originalIndex:
				raise ValueError('Tabla llena')

		return index

	def insertar(self, key: int, value):
		index = self.__pseudoRandomProbe(key)
		self.__table[index] = (key, value)

	def buscar(self, key: int):
		index = self.__pseudoRandomProbe(key)

		if self.__table[index] is not None and self.__table[index][0] == key:
			return self.__table[index][1]
		else:
			return None

	def calcularLongitudSecuenciaBusqueda(self, key: int):
		index = self.__hash(key)
		count = 0

		while self.__table[index] is not None and self.__table[index][0] != key:
			index = self.__hash(index + 1)
			count += 1

		return count

	def calcularFactorCarga(self):
		cantidad = sum(1 for i in self.__table if i is not None)

		return cantidad / self.__size

	def __repr__(self) -> str:
		return str(self.__table)

if __name__ == '__main__':
	dataset = [(random.randint(0, 1000000), randomString()) for i in range(1000)]

	table1 = TablaHash(1000, False)
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