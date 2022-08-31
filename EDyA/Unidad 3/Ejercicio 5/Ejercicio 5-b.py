
import numpy as np

class ListaOrdenada:
	__elementos: np.ndarray	
	__tope: int
	__tamañoTotal: int

	def __init__(self, tamañoTotal):
		self.__elementos = np.full(tamañoTotal, None)
		self.__tope = 0
		self.__tamañoTotal = tamañoTotal

	def __posicionValida(self, pos):
		return 0 <= pos <= self.__tope

	def __shift(self, pos, forward = True):
		if forward:
			for i in range(self.__tope, pos, -1):
				self.__elementos[i] = self.__elementos[i - 1]
		else:
			for i in range(pos, self.__tope):
				self.__elementos[i] = self.__elementos[i + 1]

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

		self.__shift(pos)
		self.__elementos[pos] = elemento
		self.__tope += 1

	def eliminar(self, pos):
		if not self.__posicionValida(pos):
			raise Exception('La posición no es válida')

		self.__shift(pos, False)
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

def eliminarRepetidosOptimizado(L: ListaOrdenada):
	prevelem = L.recuperar(0)
	i = 1
	while i < L.getTamaño():
		elem = L.recuperar(i)
		if prevelem == elem:
			L.eliminar(i)
		else:
			i += 1
			prevelem = elem

if __name__ == '__main__':
	l = ListaOrdenada(10)
	l.insertar(10)
	l.insertar(5)
	l.insertar(7)
	l.insertar(5)
	l.insertar(2)
	l.insertar(10)

	print(l)
	eliminarRepetidosOptimizado(l)
	print(l)
