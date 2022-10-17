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

class Node:
	__key: Any
	__data: Any
	__next: Any # 'Node' | None

	def __init__(self, key: Any, data: Any, next: Any = None): # 'Node' | None = None):
		self.__key = key
		self.__data = data
		self.__next = next

	def getKey(self): return self.__key
	def getData(self): return self.__data
	def setData(self, data: Any): self.__data = data
	def setNext(self, next: Any): self.__next = next # 'Node' | None): self.__next = next
	def getNext(self): return self.__next

class List:
	__head: Any # 'Node' | None
	__tail: Any # 'Node' | None
	__size: int

	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__size = 0

	def getHead(self): return self.__head
	def getTail(self): return self.__tail
	def getSize(self): return self.__size

	def insert(self, key: Any, data: Any):
		node = Node(key, data)

		if self.__head is None:
			self.__head = node
			self.__tail = node
		else:
			nodo = self.search(key)

			if nodo is None:
				self.__tail.setNext(node)
				self.__tail = node
			else:
				nodo.setData(data)

		self.__size += 1

	def search(self, key: Any):
		node = self.__head

		while node is not None:
			if node.getKey() == key:
				return node

			node = node.getNext()

		return None

	def delete(self, key: Any):
		node = self.__head
		prev = None

		while node is not None:
			if node.getKey() == key:
				if prev is None:
					self.__head = node.getNext()
				else:
					prev.setNext(node.getNext())

				self.__size -= 1
				return node

			prev = node
			node = node.getNext()

		return None

	def __iter__(self):
		nodo = self.__head

		while nodo is not None:
			yield nodo
			nodo = nodo.getNext()

	def __str__(self):
		node = self.__head
		result = ''

		while node is not None:
			result += f'[{node.getKey()}] -> '
			node = node.getNext()

		return result

class TablaHash:
	__size: int
	__table: Any # NDArray[Any]

	def __init__(self, size: int, usarPrimo = True) -> None:
		self.__size = int(size / 0.7 + 1)

		if usarPrimo:
			self.__size = getPrimeNumber(self.__size)

		self.__table = np.full(self.__size, None)
		for i in range(self.__size):
			self.__table[i] = List()

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
		self.__table[index].insert(key, value)

	def buscar(self, key: int):
		index = self.__hash(key)
		node = self.__table[index].search(key)

		return None if node is None else node.getData()

	def eliminar(self, key: int):
		index = self.__hash(key)
		self.__table[index].delete(key)

	def __iter__(self):
		return iter(self.__table)