from typing import Any

class Pila: # lifo
	__elementos: list[Any]

	def __init__(self):
		self.__elementos = []
	
	def getTamaño(self):
		return len(self.__elementos)

	def estaVacia(self):
		return len(self.__elementos) == 0

	def add(self, obj):
		self.__elementos.append(obj)

	def get(self):
		if self.getTamaño() == 0:
			raise Exception('No quedan elementos en la pila')

		return self.__elementos.pop()

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