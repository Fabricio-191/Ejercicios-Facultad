from zope.interface import implementer
from .Nodo import Nodo
from .IColeccion import IColeccion
from .Aparatos.Aparato import Aparato

@implementer(IColeccion)
class Lista:
	__head: Nodo | None
	__tail: Nodo | None

	def __init__(self) -> None:
		self.__head = None
		self.__tail = None

	def agregarElemento(self, dato: Aparato):
		if self.__tail is None:
			self.__head = Nodo(dato, None)
			self.__tail = self.__head
		else:
			nodo = Nodo(dato, None)

			self.__tail.setNext(nodo)
			self.__tail = nodo

	def encontrarElemento(self, posicion: int):
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
		nodo = self.encontrarElemento(posicion)
		siguiente = nodo.getNext()

		nodo.setNext(Nodo(dato, siguiente))

	def mostrarElemento(self, posicion: int):
		nodo = self.encontrarElemento(posicion)

		print(f"Dato: {nodo.getDato()}")

	def __iter__(self):
		actual = self.__head
		while actual != None:
			yield actual.getDato()
			actual = actual.getNext()