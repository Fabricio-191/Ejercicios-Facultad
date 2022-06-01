from .Nodo import Nodo

class Lista:
	__head: Nodo | None = None
	__tail: Nodo | None = None

	def agregar(self, dato):
		nuevoNodo = Nodo(dato, None)

		if self.__tail is None:
			self.__tail = self.__head = nuevoNodo
		else:
			self.__tail.setNext(nuevoNodo)
			self.__tail = nuevoNodo
	
	def __iter__(self):
		actual = self.__head
		while actual != None:
			yield actual.getDato()
			actual = actual.getNext()