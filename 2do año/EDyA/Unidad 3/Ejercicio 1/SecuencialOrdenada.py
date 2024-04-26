import numpy as np

class Lista:
	__elementos: np.ndarray	
	__tope: int
	__tamañoTotal: int

	def __init__(self, tamañoTotal):
		self.__elementos = np.full(tamañoTotal, None)
		self.__tope = 0
		self.__tamañoTotal = tamañoTotal

	def __posicionValida(self, pos):
		return 0 <= pos <= self.__tope

	def estaLlena(self):
		return self.__tope == self.__tamañoTotal

	def estaVacia(self):
		return self.__tope == 0

	def getTamaño(self):
		return self.__tope

	def insertar(self, elemento):
		if self.estaLlena():
			raise Exception('La lista está llena')

		pos = 0

		while pos < self.__tope and self.__elementos[pos] < elemento:
			pos += 1

		for i in range(self.__tope, pos, -1):
			self.__elementos[i] = self.__elementos[i - 1]
			
		self.__elementos[pos] = elemento
		self.__tope += 1

	def eliminar(self, pos):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		for i in range(pos, self.__tope):
			self.__elementos[i] = self.__elementos[i + 1]

		self.__tope -= 1

	def recuperar(self, pos):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		return self.__elementos[pos]

	def buscar(self, elem):
		low = 0
		high = self.__tope - 1

		while low <= high:
			mid = (low + high) // 2

			if self.__elementos[mid] == elem:
				return mid
			elif self.__elementos[mid] < elem:
				low = mid + 1
			else:
				high = mid - 1

		return -1

	def primerElemento(self):
		return self.__elementos[0] if not self.estaVacia() else None

	def ultimoElemento(self):
		return self.__elementos[self.__tope - 1] if not self.estaVacia() else None

	def __iter__(self):
		return iter(self.__elementos[:self.__tope])

	def __repr__(self):
		return str(list(self))

if __name__ == '__main__':
	lista = Lista(100)

	lista.insertar(4)
	lista.insertar(1)
	lista.insertar(2)
	lista.insertar(3)

	print(lista)
	print(lista.buscar(4))