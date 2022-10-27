from __future__ import annotations

class Nodo:
	__value: int
	__next: 'Nodo' | None

	def __init__(self, value: int, next: Nodo | None = None) -> None:
		self.__value = value
		self.__next = next

	def value(self) -> int:
		return self.__value

	def next(self) -> Nodo | None:
		return self.__next

	def setNext(self, next: Nodo | None) -> None:
		self.__next = next

class ListaEnlazada:
	__cabeza: Nodo | None

	def __init__(self):
		self.__cabeza = None

	def insertar(self, value: int) -> None:
		self.__cabeza = Nodo(value, self.__cabeza)

	def has(self, value: int) -> bool:
		nodo = self.__cabeza

		while nodo is not None:
			if nodo.value() == value:
				return True

			nodo = nodo.next()

		return False
		

		
