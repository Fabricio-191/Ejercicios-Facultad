"""
La secretaria de modernización de presidencia de la Nación, cuenta con conjuntos de datos (Dataset):
Estadística de designaciones de magistrados de la Justicia Federal y Nacional por género.

Los datos del archivo están ordenados por año.

se pide

a) Generar la clase designación: con los atributos que posee el archivo.

b) Leer los datos del archivo csv, y generar una lista de designaciones.

c) Leer un tipo de cargo por teclado, y mostrar la cantidad de mujeres designadas en ese cargo por año.

d) Leer una materia, un cargo y un año y mostrar la cantidad de agentes designados en ese cargo,  esa materia en ese año.
"""
from Lista import Lista
from os import path
import csv

class Designacion:
	__año: int
	__materia: str
	__tipoCargo: str
	__esMujer: str

	def __init__(self, año, tipoCargo, materia, genero):
		self.__año = int(año)
		self.__tipoCargo = tipoCargo
		self.__materia = materia
		self.__esMujer = genero == 'Femenino'

	def getAño(self):
		return self.__año

	def getMateria(self):
		return self.__materia

	def getTipoCargo(self):
		return self.__tipoCargo

	def esMujer(self):
		return self.__esMujer

class ManejadorDesignaciones:
	__designaciones: Lista

	def __init__(self, tamaño):
		self.__designaciones = Lista(tamaño)

	def incisoC(self, cargo):
		cantidad = 0

		for designacion in self.__designaciones:
			if designacion.getTipoCargo() == cargo and designacion.esMujer():
				cantidad += 1

		return cantidad

	def incisoD(self, materia, cargo, año):
		cantidad = 0

		for designacion in self.__designaciones:
			if designacion.getMateria() == materia and designacion.getTipoCargo() == cargo and designacion.getAño() == año:
				cantidad += 1

		return cantidad

	def cargar(self, archivo):
		if not path.isfile(archivo):
			raise Exception('El archivo no existe')

		with open(archivo, 'r') as f:
			reader = csv.reader(f, delimiter=';')
			next(reader)
			
			for linea in reader:
				self.__designaciones.insertar(Designacion(*linea))

if __name__ == '__main__':
	manejador = ManejadorDesignaciones(100)
	manejador.cargar(path.dirname(__file__) + '/designaciones.csv')

	cargo = input('\nIngrese un cargo: ')
	cant = manejador.incisoC(cargo)
	print(f'La cantidad de mujeres asignadas al cargo {cargo} es {cant}')

	materia = input('\nIngrese una materia: ')
	año = int(input('Ingrese un año: '))
	cargo = input('Ingrese un cargo: ')
	cant = manejador.incisoD(materia, cargo, año)
	print(f'\nLa cantidad de agentes designados a la materia {materia} en el cargo {cargo} en el año {año} es {cant}')


"""
Juez
Fiscal de la Justicia Nacional
2022
Fiscal
"""