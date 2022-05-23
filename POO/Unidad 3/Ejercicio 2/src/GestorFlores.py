from typing import Any
from .Flor import Flor
from csv import reader
import numpy as np

class GestorFlores:
	__flores: np.ndarray[Flor, Any]

	def __init__(self, archivo: str):
		self.__flores = np.empty(0, dtype=Flor)
		self.__leerArchivo(archivo)

	def __leerArchivo(self, archivo: str) -> None:
		with open(archivo, encoding='utf8') as file:
			for line in reader(file, delimiter=';'):
				self.__flores = np.append(self.__flores, Flor(line)) # type: ignore

	def obtenerFlor(self, nombre: str) -> Flor | None:
		for flor in self.__flores:
			if flor.getNombre() == nombre:
				return flor

