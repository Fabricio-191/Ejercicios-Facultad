from typing import Any
from sys import platform
import os


class Disco:
	__tamaño: int

	def __init__(self, tamaño: int):
		self.__tamaño = tamaño

	def getTamaño(self):
		return self.__tamaño

	def __repr__(self):
		return str(self.__tamaño)


class Torre:  # Pila
	__elementos: list[Disco]

	def __init__(self):
		self.__elementos = []

	def cantidadDiscos(self):
		return len(self.__elementos)

	def getTamañoUltimoDisco(self):
		if(self.cantidadDiscos() == 0):
			return 999999

		return self.__elementos[-1].getTamaño()

	def añadirDisco(self, obj: Disco):
		if(self.getTamañoUltimoDisco() <= obj.getTamaño()):
			print('No se puede poner un Disco encima de uno mas pequeño')
			raise Exception('No se puede poner un Disco encima de uno mas pequeño')
		else:
			self.__elementos.append(obj)

	def obtenerDisco(self, i):
		if len(self.__elementos) < i:
			return ' '

		return self.__elementos[i - 1]

	def quitarDisco(self):
		if self.cantidadDiscos() == 0:
			print('No quedan Discos en la torre')
			raise Exception('No quedan Discos en la torre')

		return self.__elementos.pop()


class TorresDeHanoi:
	__torres: list[Torre]
	__cantidadDiscos: int

	def __init__(self, cantidadDiscos: int):
		self.__torres = [Torre() for _ in range(3)]

		for i in range(cantidadDiscos, 0, -1):
			self.__torres[0].añadirDisco(Disco(i))

		self.__cantidadDiscos = cantidadDiscos

	def moverDisco(self, de, a):
		try:
			disco = self.__torres[de].quitarDisco()
		except:
			return

		try:
			self.__torres[a].añadirDisco(disco)
		except:
			self.__torres[de].añadirDisco(disco)

	def termino(self):
		return self.__torres[2].cantidadDiscos() == self.__cantidadDiscos

	def esTorre(self, num):
		if num < 0 or num > 3:
			return False

		return True

	def __repr__(self):
		string: str = '\n'

		"""
		for i in range(self.__cantidadDiscos, 0, -1):
			string += '    |{}|         |{}|         |{}|   \n'.format(
				self.__torres[0].obtenerDisco(i),
				self.__torres[1].obtenerDisco(i),
				self.__torres[2].obtenerDisco(i),
			)
		"""
		for i in range(self.__cantidadDiscos, 0, -1):
			string += '    {}|{}         {}|{}         {}|{}    \n'.format(
				self.__torres[0].obtenerDisco(i),
				self.__torres[0].obtenerDisco(i),
				self.__torres[1].obtenerDisco(i),
				self.__torres[1].obtenerDisco(i),
				self.__torres[2].obtenerDisco(i),
				self.__torres[2].obtenerDisco(i),
			)

		string += '=================================='

		return string

def clearConsole():
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "darwin":
		pass
	elif platform == "win32":
		os.system('cls')

def leerEntero(msg: str) -> int:
	try:
		return int(input(msg))
	except ValueError:
		print('Valor incorrecto')
		return leerEntero(msg)
		

clearConsole()

while True:
	cantidadDiscos = leerEntero('Introduzca la cantidad de discos: ')
	juego = TorresDeHanoi(cantidadDiscos)
	movimientos = 0

	while not juego.termino():
		print(juego)
		print('introduzca el movimiento a hacer')
		de = leerEntero('de: ')
		a = leerEntero('a: ')

		clearConsole()

		if juego.esTorre(de) and juego.esTorre(a):
			movimientos += 1
			juego.moverDisco(de - 1, a - 1)
			print('Movimientos: {}'.format(movimientos))
		else:
			print('Valores invalidos')

	print('Movimientos optimos: {}'.format(2 ** cantidadDiscos - 1))
	seguir = input('Seguir jugando ? (Y/N) ')

	if seguir != 'Y':
		break