from Flor import Flor
from typing import Literal

class Ramo:
	__flores: list[Flor]
	__tamaño: Literal['grande', 'mediano', 'chico']

	def __init__(self, tamaño: Literal['grande', 'mediano', 'chico']) -> None:
		self.__flores = []
		self.__tamaño = tamaño

	def agregarFlor(self, flor: Flor) -> None:
		self.__flores.append(flor)

	def cantidadFlores(self) -> int:
		return len(self.__flores)