from sys import platform
import os
from Torre import Torre, Disco

class TorresHanoi:
	__torres: list[Torre]
	__cantidadDiscos: int

	def __init__(self, cantidadDiscos: int):
		self.__cantidadDiscos = cantidadDiscos
		self.__torres = [Torre(), Torre(), Torre()]

		for i in range(cantidadDiscos, 0, -1):
			self.__torres[0].añadirDisco(Disco(i))

	def moverDisco(self, de, a):
		desde = self.__torres[de]
		hasta = self.__torres[a]

		if desde.estaVacia():
			print('No quedan Discos en la torre')
			return

		if desde.tamañoUltimoDisco() >= hasta.tamañoUltimoDisco():
			print('No se puede poner un Disco encima de uno mas pequeño')
			return

		hasta.añadirDisco(desde.quitarDisco())

	def termino(self):
		return self.__torres[2].cantidadDiscos() == self.__cantidadDiscos

	def __repr__(self):
		string: str = '\n'

		for i in range(self.__cantidadDiscos, 0, -1):
			string += '    {}|{}         {}|{}         {}|{}    \n'.format(
				self.__torres[0].obtenerTamañoDisco(i),
				self.__torres[0].obtenerTamañoDisco(i),
				self.__torres[1].obtenerTamañoDisco(i),
				self.__torres[1].obtenerTamañoDisco(i),
				self.__torres[2].obtenerTamañoDisco(i),
				self.__torres[2].obtenerTamañoDisco(i),
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

if __name__ == '__main__':
	clearConsole()

	seguir = 'Y'
	while seguir == 'Y':
		cantidadDiscos = leerEntero('Introduzca la cantidad de discos: ')
		juego = TorresHanoi(cantidadDiscos)
		movimientos = 0

		while not juego.termino():
			print(juego)
			print('Introduzca el movimiento a hacer')
			de = leerEntero('de: ')
			a  = leerEntero('a: ')

			clearConsole()

			if 0 < de < 4 and 0 < a < 4:
				movimientos += 1
				juego.moverDisco(de - 1, a - 1)
				print('Movimientos: {}'.format(movimientos))
			else:
				print('Valores invalidos')

		print(juego)
		print('Movimientos: {}'.format(movimientos))
		print('Movimientos optimos: {}'.format(2 ** cantidadDiscos - 1))
		seguir = input('Seguir jugando ? (Y/N) ')
