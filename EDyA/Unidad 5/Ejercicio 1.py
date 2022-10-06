"""
Ejercicio Nº 1
Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones
direccionamiento abierto, utilizando como función de transformación de claves el método
de la división, procesando las claves sinónimas a través de la secuencia de Prueba Lineal
y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a
través de la función rand.

Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en
cuenta:
1. El tamaño de la tabla Hash no es un número primo.
2. El tamaño de la tabla Hash sí es un número primo.
Realice un breve análisis comparativo basado en las dos consideraciones anteriores.
"""
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

	def __linearProbeSearch(self, key: int):
		index = self.__hash(key)
		while self.__table[index] is not None:
			if self.__table[index][0] == key:
				return index

			index = (index + 1) % self.__size

		return None

	def insertar(self, key: int, value):
		index = self.__hash(key)
		while self.__table[index] is not None:
			if self.__table[index][0] == key:
				raise ValueError('La clave ya existe')

			index = (index + 1) % self.__size

		self.__table[index] = (key, value)

	def buscar(self, key: int):
		index = self.__linearProbeSearch(key)
		if index is None:
			raise ValueError('No se encontró la clave')

		return self.__table[index][1]

	def eliminar(self, key: int):
		index = self.__linearProbeSearch(key)
		if index is None:
			raise ValueError('No se encontró la clave')

		self.__table[index] = None

	def __str__(self) -> str:
		return str(self.__table)

	def calcularFactorCarga(self):
		cantidad = sum(1 for i in self.__table if i is not None)

		return cantidad / self.__size

def randomString(stringLength = 10):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
	table = TablaHash(1000, False)

	dataset = [(random.randint(0, 100), randomString()) for i in range(1000)]
	for key, value in dataset:
		table.insertar(key, value)

	print('Factor de carga:', table.calcularFactorCarga())

	for key, value in dataset:
		table.buscar(key)
