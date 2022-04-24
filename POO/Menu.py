from typing import Callable

class Menu:
	__functions: dict[str, Callable[[], None]] = {}
	__descriptions: dict[str, str] = {
		'0': 'Salir del menu',
	}

	def registrarOpcion(self, key: str, value: Callable[[], None], description: str):
		if key in self.__descriptions:
			raise Exception('La opcion ya existe')

		self.__functions[key] = value
		self.__descriptions[key] = description

	def __menu(self):
		print('\n=====Menu=====')
		print('Opciones:')
		for key in self.__descriptions:
			print(key, '-', self.__descriptions[key])
		print('===========\n')

	def iniciar(self):
		while True:
			self.__menu()
			opcion = input('Ingrese una opcion: ')
			if opcion == '0': break
			if opcion in self.__functions:
				self.__functions[opcion]()
			else:
				print('Opcion invalida')

def Opcion1():
	print('Se ejecuto la opcion 1')

def Opcion2():
	print('Se ejecuto la opcion 2')

if __name__ == "__main__":
	menu = Menu()
	menu.registrarOpcion('1', Opcion1, 'Esto ejecutara la opcion 1')
	menu.registrarOpcion('2', Opcion2, 'Esto ejecutara la opcion 2')
	menu.registrarOpcion(
		'3',
		lambda: print('Se ejecuto la opcion 3'),
		'Esto ejecutara la opcion 3'
	)
	menu.iniciar()