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

class Bucket:
	__array: Any # NDArray[Any]
	__tope: int

	def __init__(self, bucketSize: int) -> None:
		self.__array = np.full(bucketSize, None)
		self.__tope = 0

	def estaLleno(self):
		return self.__array[-1] is not None

	def estaSubocupado(self):
		return self.__tope < (self.__array.size // 3)

	def insert(self, key, value):
		if self.estaLleno():
			raise Exception('El bucket esta completo')

		self.__array[self.__tope] = (key, value)
		self.__tope += 1

	def search(self, key):
		for pair in self.__array:
			if pair is not None and pair[0] == key:
				return pair[1]
		
		return None

	def __repr__(self):
		return str(self.__array)

class TablaHash:
	__extraccionLength: int
	__size: int
	__mainTable: Any # NDArray[Bucket]
	__overflowSize: int
	__overflowTable: Any # NDArray[Bucket]

	def __init__(self, size: int, bucketSize: int, usarPrimo = True) -> None:
		self.__size = size

		if usarPrimo:
			self.__size = getPrimeNumber(int(self.__size / 0.7 + 1))

		self.__extraccionLength = len(str(self.__size))
		self.__mainTable = np.empty(self.__size, dtype=Bucket)
		for i in range(self.__size):
			self.__mainTable[i] = Bucket(bucketSize)

		self.__overflowSize = self.__size // 10
		self.__overflowTable = np.empty(self.__overflowSize, dtype=Bucket)
		for i in range(self.__overflowSize):
			self.__overflowTable[i] = Bucket(bucketSize)

	def getSize(self) -> int:
		return self.__size

	def __hash(self, key: int) -> int:
		keyStr = str(key)
		hash = int(keyStr[-self.__extraccionLength:])

		return hash % self.__size

	def __overflowHash(self, key: int) -> int:
		return key % self.__overflowSize

	def insertar(self, key: int, data: Any):
		hash = self.__hash(key)
		bucket = self.__mainTable[ hash ]

		if bucket.estaLleno():
			overflowBucket = self.__overflowTable[ self.__overflowHash(hash) ]
			overflowBucket.insert(key, data)
		else:
			bucket.insert(key, data)

	def buscar(self, key: int) -> Any:
		hash = self.__hash(key)
		result = self.__mainTable[ hash ].search(key)

		if result is not None:
			return result

		overflowBucket = self.__overflowTable[ self.__overflowHash(hash) ]
		return overflowBucket.search(key)

	def __iter__(self):
		return iter(self.__mainTable)