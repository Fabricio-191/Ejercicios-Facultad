"""
El gobierno de la Nación cuenta con conjunto de datos dataset: Estadística de incendios forestales descritos por superficie (hectárea), número de focos por departamento y por provincia.

se pide:

b) Leer los datos del archivo csv, y generar una lista donde cada componente contenga: Nombre de provincia y superficie total afectada.
c) Mostrar, Nombre de provincia y superficie afectada ordenada de mayor a menor por superficie total afectada. 
"""
from ListaOrdenada import Lista
import csv
from os import path

class Incendio:
	__provincia: str
	__superficie: int

	def __init__(self, provincia, superficie):
		self.__provincia = provincia
		self.__superficie = int(superficie)

	def getProvincia(self):
		return self.__provincia

	def getSuperficie(self):
		return self.__superficie

	def __gt__(self, other):
		if not isinstance(other, Incendio):
			raise Exception('No se puede comparar un incendio contra algo que no sea otro incendio')

		return self.__superficie < other.getSuperficie()

class ManejadorIncendios:
	__incendios: Lista

	def __init__(self, tamaño):
		self.__incendios = Lista(tamaño)


	def mostrarIncendios(self):
		print('\n       Incendios')
		print('Hectareas      Provincia')
		for incendio in self.__incendios:
			print(' {}            {}'.format(
				incendio.getSuperficie(), incendio.getProvincia(), 
			))

	def cargarIncendios(self, archivo):
		if not path.isfile(archivo):
			raise Exception('El archivo no existe')

		with open(archivo, 'r') as f:
			reader = csv.reader(f, delimiter=';')
			next(reader)
			
			for linea in reader:
				self.__incendios.insertar(
					Incendio(linea[0], linea[1])
				)

if __name__ == '__main__':
	manejador = ManejadorIncendios(100)
	manejador.cargarIncendios(path.dirname(__file__) + '/incendios.csv')
	manejador.mostrarIncendios()