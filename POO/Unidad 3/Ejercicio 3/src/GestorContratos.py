from .Jugador import Jugador
from .Equipo import Equipo
from .Contrato import Contrato
from .GestorEquipos import GestorEquipos
from .GestorJugadores import GestorJugadores
from csv import reader
import numpy as np

class GestorContratos:
	__gestorEquipos: GestorEquipos
	__gestorJugadores: GestorJugadores
	__contratos: np.ndarray

	def __init__(self, archivo: str, gestorEquipos: GestorEquipos, gestorJugadores: GestorJugadores):
		self.__gestorEquipos = gestorEquipos
		self.__gestorJugadores = gestorJugadores
		self.__contratos = np.array(self.__leerArchivo(archivo))

	def __leerArchivo(self, archivo: str) -> list[Contrato]:
		with open(archivo, 'r') as file:
			lector = reader(file, delimiter=';')
			next(lector, None)

			lista = []

			for line in lector:
				jugador = self.__gestorJugadores.getJugador(line[3])
				equipo = self.__gestorEquipos.getEquipo(line[4])

				lista.append(
					Contrato(float(line[0]), line[1], line[2], jugador, equipo)
				)

			return lista