import numpy as np
from csv import reader
from .Contrato import Contrato

class GestorContratos:
	__contrato: np.ndarray[Contrato, np.dtype]

	def __init__(self, archivo: str):
		self.__contrato = np.array(self.__leerArchivo(archivo))

	def __leerArchivo(self, archivo: str) -> list[Contrato]:
		with open(archivo, 'r') as file:
			lector = reader(file, delimiter=';')
			next(lector, None)

			return list(map(lambda x: Contrato(*x), lector))