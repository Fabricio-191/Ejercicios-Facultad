from typing import Any
import numpy as np
from csv import reader
from .Equipo import Equipo
from .Jugador import Jugador
from numpy.typing import NDArray

class GestorEquipos:
	__equipos: NDArray[Any]

	def __init__(self, archivo: str):
		self.__equipos = np.array(self.__leerArchivo(archivo)) # type: ignore

	def __leerArchivo(self, archivo: str) -> list[Equipo]:
		with open(archivo, 'r') as file:
			lector = reader(file, delimiter=';')
			next(lector, None)

			return list(map(lambda x: Equipo(*x), lector))

	def getEquipo(self, nombre: str) -> Equipo:
		for equipo in self.__equipos:
			if equipo.getNombre() == nombre:
				return equipo

		raise ValueError('Equipo no encontrado')

	def getEquipos(self, equipos: list[str]) -> list[Equipo]:
		return list(map(self.getEquipo, equipos))

	@staticmethod
	def agregarJugadorAEquipos(jugador: Jugador, equipos: list[Equipo]) -> None:
		for equipo in equipos:
			equipo.añadirJugador(jugador)
