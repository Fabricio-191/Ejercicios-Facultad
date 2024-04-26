from zope.interface import Interface

class IColeccion(Interface):  # type: ignore
	def insertarElemento(self, posicion, elemento):
		pass

	def agregarElemento(self, elemento):
		pass

	def mostrarElemento(self, posicion):
		pass
