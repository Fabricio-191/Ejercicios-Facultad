from __future__ import annotations

class Nodo:
	__caracter = None
	__frequencia = None
	__izq: Nodo | None = None
	__der: Nodo | None = None

	def __init__(self, caracter, frequencia):
		self.__caracter = caracter
		self.__frequencia = frequencia
		self.__izq = None
		self.__der = None

	def getFreq(self):
		return self.__frequencia

	def getChar(self):
		return self.__caracter

	def getIzq(self) -> Nodo | None:
		return self.__izq

	def getDer(self) -> Nodo | None:
		return self.__der

	def setIzq(self, nodo):
		self.__izq = nodo

	def setDer(self, nodo):
		self.__der = nodo

	def grado(self):
		if self.__izq is None and self.__der is None:
			return 0
		elif self.__izq is None or self.__der is None:
			return 1
		else:
			return 2

	def esHoja(self):
		return self.__izq is None and self.__der is None

	def inOrden(self, callback):
		if self.__izq is not None:
			self.__izq.inOrden(callback)
		callback(self)
		if self.__der is not None:
			self.__der.inOrden(callback)

	def preOrden(self, callback):
		callback(self)
		if self.__izq is not None:
			self.__izq.preOrden(callback)
		if self.__der is not None:
			self.__der.preOrden(callback)

	def postOrden(self, callback):
		if self.__izq is not None:
			self.__izq.postOrden(callback)
		if self.__der is not None:
			self.__der.postOrden(callback)
		callback(self)

	def __repr__(self):
		return f'( {self.__frequencia} - {self.__caracter} )'
