from typing import Callable, Any
from os import system

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
		self.__menu()
		opcion = input('Ingrese una opcion: ')
		while opcion != '0':
			if self.__clear: system('cls') 

			if opcion in self.__functions:
				entry = self.__functions[opcion]
				entry[1](*entry[2])
			else:
				print('Opcion invalida')
			
			self.__menu()
			opcion = input('Ingrese una opcion: ')