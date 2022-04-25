from typing import Callable, Any
import os

class Menu:
	# dict[str, tuple[Literal['Salir del menu'], () -> None, tuple[()]]]
	__functions: dict[str, tuple[str, Callable, tuple[Any]]] = {
		'0': ('Salir del menu', lambda: None, ()) # type: ignore
	}
	__name: str
	__clear: bool

	def __init__(self, name: str = 'Menu', clear: bool = True):
		self.__name = name
		self.__clear = clear

	def registrarOpcion(self, key: str, description: str, value: Callable, *args):
		if key in self.__functions:
			raise Exception('La opcion ya existe')

		self.__functions[key] = (description, value, args)

	def __menu(self):
		print(f'\n====={self.__name}=====')
		print('Opciones:')
		for key in self.__functions:
			print(key, '-', self.__functions[key][0])
		print('===========\n')

	def iniciar(self):
		while True:
			self.__menu()
			opcion = input('Ingrese una opcion: ')
			if self.__clear: os.system('cls')
			if opcion == '0': break
			if opcion in self.__functions:
				entry = self.__functions[opcion]
				entry[1](*entry[2])
			else:
				print('Opcion invalida')

def Opcion1():
	print('Se ejecuto la opcion 1')

def Opcion2():
	print('Se ejecuto la opcion 2')

if __name__ == "__main__":
	menu = Menu()
	menu.registrarOpcion('1', 'Esto ejecutara la opcion 1', Opcion1)
	menu.registrarOpcion('2', 'Esto ejecutara la opcion 2', Opcion2)
	menu.registrarOpcion(
		'3',
		'Esto ejecutara la opcion 3',
		lambda: print('Se ejecuto la opcion 3')
	)
	menu.iniciar()