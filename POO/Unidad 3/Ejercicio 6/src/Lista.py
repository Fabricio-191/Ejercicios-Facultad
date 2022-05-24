from zope.interface import implementer
from .Nodo import Nodo
from .IColeccion import IColeccion
from .Aparatos.Aparato import Aparato

@implementer(IColeccion)
class Lista:
	__head: Nodo
	__tail: Nodo

	def agregarElemento(self, dato: Aparato):
		if self.__head == None:
			self.__head = Nodo(dato, None)
			self.__tail = self.__head
		else:
			self.__tail.__next = Nodo(dato, None)
			self.__tail = self.__tail.__next

	def __encontrarElemento(self, posicion: int):
		if posicion < 0:
			raise Exception("Posicion invalida")

		actual = self.__head

		while actual != None and posicion != 0:
			actual = actual.getNext()
			posicion -= 1

		if actual == None:
			raise Exception("Posicion invalida")

		return actual

	def insertarElemento(self, posicion: int, dato: Aparato):
		nodo = self.__encontrarElemento(posicion)
		nodo.setNext(
			Nodo(dato, nodo.getNext())
		)

	def mostrarElemento(self, posicion: int):
		nodo = self.__encontrarElemento(posicion)

		print(f"Dato: {nodo.getDato()}")

	def __iter__(self):
		actual = self.__head
		while actual != None:
			yield actual.getDato()
			actual = actual.getNext()
