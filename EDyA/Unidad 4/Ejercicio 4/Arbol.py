from Nodo import Nodo

class Arbol:
	__root = None

	def __init__(self, root):
		self.__root = root

	def buscar(self, dato):
		if self.__root is None:
			return None
		else:
			return self.__root.buscar(dato)

	def nivel(self, dato):
		if self.__root is None:
			return -1
		else:
			return self.__root.nivel(dato, 1)

	def esHoja(self, dato):
		nodo = self.buscar(dato)
		if nodo is None:
			return False
		else:
			return nodo.esHoja()

	def frontera(self):
		frontera = []

		self.inOrden(lambda nodo: frontera.append(nodo) if nodo.esHoja() else None)
		
		return frontera

	def getRaiz(self):
		return self.__root

	def esHijo(self, datoPadre, datoHijo):
		nodoPadre = self.buscar(datoPadre)

		if nodoPadre is None:
			return False
		else:
			if nodoPadre.getIzq() is not None and nodoPadre.getIzq().getDato() == datoHijo: # type: ignore
				return True
			elif nodoPadre.getDer() is not None and nodoPadre.getDer().getDato() == datoHijo: # type: ignore
				return True
			else:
				return False

	def esPadre(self, datoHijo, datoPadre):
		return self.esPadre(datoPadre, datoHijo)

	def camino(self, datoInicio, datoFinal):
		inicio = self.buscar(datoInicio)

		if inicio is None:
			return None

		final = inicio.buscar(datoFinal)

		return False if final is None else True

	def altura(self):
		return self.__altura(self.__root)

	def __altura(self, nodo):
		if nodo is None:
			return 0
		else:
			return 1 + max(self.__altura(nodo.getIzq()), self.__altura(nodo.getDer()))

	def inOrden(self, callback):
		if self.__root is not None:
			self.__root.inOrden(callback)

	def preOrden(self, callback):
		if self.__root is not None:
			self.__root.preOrden(callback)

	def postOrden(self, callback):
		if self.__root is not None:
			self.__root.postOrden(callback)

	def __repr__(self):
		if self.__root is None:
			return 'Arbol vacio'

		string = ''
		niveles: list[list[Nodo]] = [
			[self.__root]
		]

		cantNiveles = self.altura()

		for i in range(cantNiveles):
			niveles.append([])
			
			for nodo in niveles[i]:
				cantEspacios = 2 ** (cantNiveles - i)
				string += ' ' * cantEspacios +  f'{nodo} '
				if nodo.getIzq() is not None:
					niveles[i+1].append(nodo.getIzq()) # type: ignore
				if nodo.getDer() is not None:
					niveles[i+1].append(nodo.getDer()) # type: ignore

			string += '\n'

		return string
