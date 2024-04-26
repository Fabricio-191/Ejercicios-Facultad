import numpy as np

class Pila: # lifo
	__elementos: np.ndarray
	__tope: int
	__tamañoTotal: int

	def __init__(self, tamañoTotal: int = 100):
		self.__elementos = np.full(tamañoTotal, None)
		self.__tope = 0
		self.__tamañoTotal = tamañoTotal
	
	def getTamaño(self):
		return self.__tope

	def estaVacia(self):
		return self.__tope == 0

	def add(self, elem):
		if self.__tope == self.__tamañoTotal:
			raise Exception('La pila esta llena')

		self.__elementos[self.__tope] = elem
		self.__tope += 1

	def get(self):
		if self.__tope == 0:
			raise Exception('No quedan elementos en la pila')
		
		self.__tope -= 1
		valor = self.__elementos[self.__tope]
		self.__elementos[self.__tope] = None
		return valor

def factorial(num: int):
	pila = Pila()

	resultado: int = num
	while num != 2:
		num -= 1
		pila.add(num)

	while not pila.estaVacia():
		resultado *= pila.get()

	return resultado

def factorialSinPila(num: int):
	resultado: int = num

	while num != 2:
		num -= 1
		resultado *= num

	return resultado

print(factorial(6))
print(factorialSinPila(6))