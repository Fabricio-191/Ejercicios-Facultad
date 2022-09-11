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

	def __repr__(self):
		return f'[{self.__valor} => {self.__siguiente}]'

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

	def insertar(self, dato, pos = -1):
		if pos == -1:
			pos = self.__cantElementos

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
			anterior = self.__recuperar(pos - 1)

			elemento.setSiguiente(anterior.getSiguiente())
			anterior.setSiguiente(posElem)

		self.__cantElementos += 1

	def eliminar(self, pos):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		if pos == 0:
			aux = self.__inicio
			self.__inicio = self.__elementos[aux].getSiguiente()
			self.__elementos[aux].setSiguiente(self.__inicioVacio)
			self.__inicioVacio = aux
		else:
			anterior = self.__recuperar(pos - 1)
			aux = anterior.getSiguiente()
			anterior.setSiguiente(self.__elementos[aux].getSiguiente())
			self.__elementos[aux].setSiguiente(self.__inicioVacio)
			self.__inicioVacio = aux

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

	def __recuperar(self, pos) -> Elemento:
		aux = self.__inicio
		while pos != 0:
			aux = self.__elementos[aux].getSiguiente()
			pos -= 1

		return self.__elementos[aux]

	def recuperar(self, pos):
		return self.__recuperar(pos).getValor() if self.__posicionValida(pos) else None

	def mostrar(self):
		print('\n')
		print('Inicio:', self.__inicio)
		print('Inicio vacio:', self.__inicioVacio)

		i = 0
		for elem in self.__elementos:
			print(f'{i}: {elem}')
			i += 1

	def __iter__(self):
		pos = self.__inicio
		while pos != -1:
			yield self.__elementos[pos].getValor()
			pos = self.__elementos[pos].getSiguiente()

	def __repr__(self):
		return str(list(self))

if __name__ == '__main__':
	lista = Lista(10)

	lista.insertar(100)
	lista.insertar(200)
	lista.insertar(300)
	lista.insertar(400)
	lista.insertar(500)
	lista.insertar(600)
	
	lista.eliminar(3)
	lista.insertar(800, 2)

	print(lista)
	lista.mostrar()