from typing import Any
from Flor import Flor
from csv import reader
import numpy as np

class GestorFlores:
	__flores: np.ndarray[Flor, Any]

	def __init__(self, archivo: str):
		self.__flores = np.array(self.__leerArchivo(archivo), dtype=Flor)

	def listaFlores(self) -> list[str]:
		return list(map(lambda flor: flor.getNumero(), self.__flores))

	def obtenerFlor(self, num: int) -> Flor | None:
		return self.__flores[num] or None

	def __leerArchivo(self, archivo: str) -> list[Flor]:
		with open(archivo) as file:
			return list(map(Flor, reader(file, delimiter=';')))
