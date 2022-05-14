import numpy as np
from csv import reader
from .Equipo import Equipo

class GestorEquipos:
	__equipos: np.ndarray

	def __init__(self, archivo: str):
		self.__equipos = np.array(self.__leerArchivo(archivo))

	def __leerArchivo(self, archivo: str) -> list[Equipo]:
		with open(archivo, 'r') as file:
			lector = reader(file, delimiter=';')
			next(lector, None)

			return list(map(lambda x: Equipo(*x), lector))
