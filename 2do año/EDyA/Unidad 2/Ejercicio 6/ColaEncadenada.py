class Nodo:
	__elem = None
	__next = None

	def __init__(self, elem, next = None):
		self.__elem = elem
		self.__next = next

	def getNext(self):
		return self.__next

	def setNext(self, next):
		self.__next = next

	def getDato(self):
		return self.__elem

class ColaEnlazada:
	__cabeza = None
	__cola = None
	__tamaño = 0

	def __init__(self):
		self.__cabeza = None
		self.__cola = None
		self.__tamaño = 0

	def add(self, elem):
		nuevo = Nodo(elem)
		
		if self.__cola == None:
			self.__cabeza = nuevo
		else:
			self.__cola.setNext(nuevo)

		self.__cola = nuevo
		self.__tamaño += 1

	def get(self):
		if self.__cabeza == None:
			raise Exception('La cola no tiene elementos')

		nodo = self.__cabeza
		self.__cabeza = nodo.getNext()
		self.__tamaño -= 1

		return nodo

	def tamaño(self):
		return self.__tamaño

	def estaVacia(self):
		return self.__tamaño == 0