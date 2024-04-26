from .Flor import Flor
from typing import Literal

class Ramo:
	__flores: list[Flor]
	__tamaño: Literal['grande', 'mediano', 'chico']

	def __init__(self, tamaño: Literal['grande', 'mediano', 'chico'], flores: list[Flor]) -> None:
		self.__flores = flores
		self.__tamaño = tamaño

	def getFlores(self) -> list[Flor]:
		return self.__flores

	def getTamaño(self) -> Literal['grande', 'mediano', 'chico']:
		return self.__tamaño