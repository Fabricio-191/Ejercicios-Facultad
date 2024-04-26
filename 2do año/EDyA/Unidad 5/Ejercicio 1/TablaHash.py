# from numpy.typing import NDArray
from typing import Any
import numpy as np

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
	__table: Any # NDArray[Any]

	def __init__(self, size: int, usarPrimo = True) -> None:
		self.__size = size

		if usarPrimo:
			self.__size = getPrimeNumber(int(self.__size / 0.7) + 1)

		self.__table = np.full(self.__size, None)
		self.probeLength = 0

	def __hash(self, key: int) -> int:
		return key % self.__size

	def getSize(self):
		return self.__size

	probeLength: int = 0
	def __linearProbe(self, key: int):
		originalIndex = index = self.__hash(key)

		while self.__table[index] is not None and self.__table[index][0] != key:
			self.probeLength += 1
			index = self.__hash(index + 1)

			if index == originalIndex:
				raise ValueError('Tabla llena')

		return index

	def insertar(self, key: int, value):
		index = self.__linearProbe(key)
		self.__table[index] = (key, value)

	def buscar(self, key: int):
		index = self.__linearProbe(key)

		if self.__table[index] is not None and self.__table[index][0] == key:
			return self.__table[index][1]
		else:
			return None

	def calcularFactorCarga(self):
		cantidad = sum(1 for i in self.__table if i is not None)

		return cantidad / self.__size
