from __future__ import annotations
from typing import Any

class Nodo:
	__dato: Any
	__next: Nodo | None

	def __init__(self, dato, next: Nodo | None = None):
		self.__dato = dato
		self.__next = next

	def getDato(self):
		return self.__dato

	def getNext(self) -> Nodo:
		return self.__next # type: ignore

	def setNext(self, next: Nodo | None):
		self.__next = next

class Lista: # lifo
	__cabeza: Nodo
	__tamaño: int

	def __init__(self):
		self.__cabeza = None # type: ignore
		self.__tamaño = 0
	
	def __posicionValida(self, pos):
		return 0 <= pos <= self.__tamaño
	
	def getTamaño(self):
		return self.__tamaño

	def estaVacia(self):
		return self.__cabeza is None

	def insertar(self, dato, pos = 0):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		self.__tamaño += 1

		if pos == 0:
			self.__cabeza = Nodo(dato, self.__cabeza)
		else:
			prev = self.__recuperarNodo(pos - 1)
			nodo = Nodo(dato, prev.getNext())
			prev.setNext(nodo)

	def eliminar(self, pos):
		if not self.__posicionValida(pos - 1):
			raise Exception('La posición no es válida')

		self.__tamaño -= 1
		if pos == 0:
			nodo = self.__cabeza
			self.__cabeza = nodo.getNext()
		else:
			prev = self.__recuperarNodo(pos - 1)
			nodo = prev.getNext()
			prev.setNext(nodo.getNext())

		return nodo.getDato()

	def __recuperarNodo(self, pos) -> Nodo:
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		nodo = self.__cabeza
		for i in range(pos):
			nodo = nodo.getNext()

		return nodo

	def recuperar(self, pos):
		return self.__recuperarNodo(pos).getDato()

	def buscar(self, dato):
		nodo = self.__cabeza
		i = 0
		while nodo is not None and nodo.getDato() != dato:
			nodo = nodo.getNext()
			i += 1
		
		return i if nodo is not None else -1

	def primerElemento(self):
		return self.__cabeza.getDato() if not self.estaVacia() else None

	def ultimoElemento(self):
		return self.recuperar(self.__tamaño - 1) if not self.estaVacia() else None

	def __iter__(self):
		nodo = self.__cabeza
		while nodo is not None:
			yield nodo.getDato()
			nodo = nodo.getNext()

	def __repr__(self):
		return str(list(self))

if __name__ == '__main__':
	pila = Lista()

	pila.insertar(4, 0)
	pila.insertar(5, 1)
	pila.insertar(6, 2)

	pila.insertar(8, 2)

	print(pila)

	print(pila.eliminar(2))
	print(pila.eliminar(1))
	print(pila.eliminar(0))
