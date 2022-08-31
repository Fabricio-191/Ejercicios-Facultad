from typing import Any
import numpy as np

class Elemento:
	__valor: Any
	__siguiente: int

	def __init__(self, valor, siguiente):
		self.__valor = valor
		self.__siguiente = siguiente

	def getValor(self):
		return self.__valor

	def setValor(self, valor):
		self.__valor = valor

	def getSiguiente(self):
		return self.__siguiente

	def setSiguiente(self, siguiente):
		self.__siguiente = siguiente

class Lista:
	__elementos: np.ndarray
	__inicio: int
	__inicioVacio: int
	__cantElementos: int

	def __init__(self, tamañoTotal):
		self.__elementos = np.empty(tamañoTotal, dtype=Elemento)
		self.__inicio = -1
		self.__inicioVacio = 0
		self.__cantElementos = 0

		for i in range(tamañoTotal - 1):
			self.__elementos[i] = Elemento(None, i + 1)
		
		self.__elementos[tamañoTotal - 1] = Elemento(None, -1)

	def __posicionValida(self, pos):
		return 0 <= pos <= self.__cantElementos

	def estaLlena(self):
		return self.__inicioVacio == -1

	def estaVacia(self):
		return self.__inicio == -1

	def getTamaño(self):
		return self.__cantElementos

	def insertar(self, dato, pos = 0):
		if self.estaLlena():
			raise Exception('La lista está llena')
		elif not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		posElem = self.__inicioVacio
		elemento = self.__elementos[posElem]

		elemento.setValor(dato)
		self.__inicioVacio = elemento.getSiguiente()

		if pos == 0:
			elemento.setSiguiente(self.__inicio)
			self.__inicio = posElem
		else:
			e = self.recuperar(pos - 1)
			
			elemento.setSiguiente(e.getSiguiente())
			e.setSiguiente(posElem)
		
		self.__cantElementos += 1

	def eliminar(self, pos):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

	def recuperar(self, pos):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		aux = self.__inicio
		while pos != -1:
			aux = self.__elementos[pos].getSiguiente()
			pos -= 1

		return self.__elementos[aux]

	def buscar(self, elem):
		pos = 0

		while pos != -1 and self.__elementos[pos].getValor() != elem:
			pos = self.__elementos[pos].getSiguiente()

		return pos if pos != self.__cantElementos else -1

	def primerElemento(self):
		return self.__elementos[self.__inicio].getValor() if not self.estaVacia() else None

	def ultimoElemento(self):
		if self.estaVacia():
			return None

		return self.recuperar(self.__cantElementos - 1)

	def mostrar(self):
		print(self.__inicio, self.__inicioVacio)

		for elem in self.__elementos:
			print(elem.getValor(), elem.getSiguiente())

	def __iter__(self):
		pos = self.__inicio
		while pos != -1:
			yield self.__elementos[pos].getValor()
			pos = self.__elementos[pos].getSiguiente()

	def __repr__(self):
		return str(list(self))

if __name__ == '__main__':
	lista = Lista(10)

	lista.insertar(1)
	lista.insertar(2)
	lista.insertar(3)
	lista.insertar(4, 2)

	print(lista)
	lista.mostrar()