"""
Ejercicio Nº3: Usando el mismo objeto de datos del ej. 1, implemente una función para c/u de los siguientes incisos:
a) Mostrar el nodo padre y el nodo hermano, de un nodo previamente ingresado por teclado; éste puede o no existir en el árbol.
b) Mostrar la cantidad de nodos del árbol en forma recursiva.
c) Mostrar la altura de un árbol.
d) Mostrar los sucesores de un nodo ingresado previamente por teclado.
"""

from Arbol import Arbol

class Menu:
	def __init__(self, arbol):
		self.__arbol = arbol

	def incisoA(self):
		nodoABuscar = int(input('Ingrese el dato a buscar: '))
		nodo = self.__arbol.buscar(nodoABuscar)

		if nodo is None:
			print('El nodo no existe')
		else:
			padre = None

			def callback(n):
				nonlocal padre
				if n.getIzq() == nodo or nodo.getDer() == nodo:
					padre = n

			self.__arbol.inOrden(callback)

			if padre is None:
				print(f'El nodo {nodo} no tiene padre (es la raiz)')
			else:
				print(f'El nodo {nodo} tiene como padre a: {padre}')
				print(f'El nodo {nodo} tiene como hermano a: {padre.getIzq() if padre.getDer() == nodo else padre.getDer()}')
	
	def incisoB(self): # forma recursiva ?
		cantNodos = 0

		def contarNodos(nodo):
			nonlocal cantNodos
			cantNodos += 1

		self.__arbol.inOrden(contarNodos)

		print(f'La cantidad de nodos del arbol es: {cantNodos}')

	def incisoC(self):
		print(f'La altura del arbol es: {self.__arbol.altura()}')

	def incisoD(self):
		nodoABuscar = int(input('Ingrese el dato a buscar: '))
		nodo = self.__arbol.buscar(nodoABuscar)

		if nodo is None:
			print('El nodo no existe')
		else:
			print(f'El nodo {nodo} tiene como sucesor a: ')
			if nodo.getDer() is not None:
				nodo.getDer().inOrden(print)
			if nodo.getIzq() is not None:
				nodo.getIzq().inOrden(print)

if __name__ == '__main__':
	arbol = Arbol()

	arbol.insertar(5)
	arbol.insertar(3)
	arbol.insertar(7)
	arbol.insertar(2)
	arbol.insertar(4)
	arbol.insertar(6)
	arbol.insertar(8)

	print(arbol)
	menu = Menu(arbol)
	menu.incisoA()
	print()
	menu.incisoB()
	print()
	menu.incisoC()
	print()
	menu.incisoD()


