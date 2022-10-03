from __future__ import annotations

class Nodo:
	__dato = None
	__izq: Nodo | None
	__der: Nodo | None

	def __init__(self, dato):
		self.__dato = dato
		self.__izq = None
		self.__der = None

	def getDato(self):
		return self.__dato

	def getIzq(self) -> Nodo | None:
		return self.__izq

	def getDer(self) -> Nodo | None:
		return self.__der

	def setDato(self, dato):
		self.__dato = dato

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

	def insertar(self, dato):
		if dato == self.__dato:
			raise Exception('Dato duplicado')
		elif dato < self.__dato:
			if self.__izq is None:
				self.__izq = Nodo(dato)
			else:
				self.__izq.insertar(dato)
		else:
			if self.__der is None:
				self.__der = Nodo(dato)
			else:
				self.__der.insertar(dato)

	def buscar(self, dato):
		if dato == self.__dato:
			return self
		elif dato < self.__dato:
			if self.__izq is None:
				return None
			else:
				return self.__izq.buscar(dato)
		else:
			if self.__der is None:
				return None
			else:
				return self.__der.buscar(dato)

	def nivel(self, dato, nivel):
		if dato == self.__dato:
			return nivel
		elif dato < self.__dato:
			if self.__izq is None:
				return -1
			else:
				return self.__izq.nivel(dato, nivel+1)
		else:
			if self.__der is None:
				return -1
			else:
				return self.__der.nivel(dato, nivel+1)

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

	def suprimir(self, dato, anterior: Nodo | None, der: bool):
		if dato == self.__dato and anterior is not None:
			if self.esHoja():
				if der:
					anterior.setDer(None)
				else:
					anterior.setIzq(None)
			elif self.grado() == 1:
				if self.__izq is None:
					if der:
						anterior.setDer(self.__der)
					else:
						anterior.setIzq(self.__der)
				else:
					if der:
						anterior.setDer(self.__izq)
					else:
						anterior.setIzq(self.__izq)
			else: # grado 2 (tiene dos hijos)
				minimo = self.__der.minimo() # type: ignore
				self.__der.suprimir(minimo.getDato(), self, True) # type: ignore
				if der:
					anterior.setDer(minimo)
				else:
					anterior.setIzq(minimo)
				
				minimo.setIzq(self.__izq)
				minimo.setDer(self.__der)
		elif dato < self.__dato:
			if self.__izq is not None:
				self.__izq.suprimir(dato, self, False)
		else:
			if self.__der is not None:
				self.__der.suprimir(dato, self, True)

	def minimo(self) -> Nodo:
		if self.__izq is None:
			return self

		aux = self.__izq

		while aux.getIzq() is not None: # type: ignore
			aux = aux.getIzq() # type: ignore
		
		return aux # type: ignore

	def __repr__(self):
		return f'( {self.__dato} )'