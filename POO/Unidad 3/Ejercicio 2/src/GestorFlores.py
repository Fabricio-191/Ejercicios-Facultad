from typing import Any
from .Flor import Flor
from csv import reader
import numpy as np

class GestorFlores:
	__flores: np.ndarray[Flor, Any]

	def __init__(self, archivo: str):
		self.__flores = np.array( # type: ignore
			GestorFlores.__leerArchivo(archivo),
			dtype=Flor
		)

	def listaFlores(self) -> list[str]:
		return list(map(lambda flor: flor.getNumero(), self.__flores))

	def obtenerFlor(self, nombre: str) -> Flor | None:
		for flor in self.__flores:
			if flor.getNombre() == nombre:
				return flor

	@staticmethod
	def __leerArchivo(archivo: str) -> list[Flor]:
		with open(archivo, encoding='utf8') as file:
			return list(map(Flor, reader(file, delimiter=';')))
