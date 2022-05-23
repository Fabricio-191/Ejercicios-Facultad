from csv import reader
import numpy as np

class ColeccionCalefactores:
	__calefactores: np.ndarray
	__tipo: np._DTypeLike

	def __init__(self, tamaño: int, tipo: np._DTypeLike, archivo: str):
		self.__calefactores = np.empty(tamaño, dtype=tipo)
		self.__tipo = tipo
		self.__leerArchivo(archivo)

	def __leerArchivo(self, archivo: str):
		cont = 0

		with open(archivo, 'r') as f:
			for linea in reader(f, delimiter=';'):
				self.__calefactores[cont] = self.__tipo(linea) # type: ignore	
				cont += 1
				
				

	
	