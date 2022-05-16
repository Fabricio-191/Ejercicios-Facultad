from .Jugador import Jugador
from csv import reader
from .GestorEquipos import GestorEquipos

class GestorJugadores:
	__jugadores: list[Jugador]
	__gestorEquipos: GestorEquipos

	def __init__(self, archivo: str, gestorEquipos: GestorEquipos):
		self.__jugadores = []
		self.__gestorEquipos = gestorEquipos
		self.__leerArchivo(archivo)

	def getJugador(self, DNI: str) -> Jugador:
		for jugador in self.__jugadores:
			if jugador.getDNI() == DNI:
				return jugador

		raise ValueError('Jugador no encontrado')

	def __leerArchivo(self, archivo: str) -> None:
		with open(archivo, 'r') as file:
			lector = reader(file, delimiter=';')
			next(lector, None)
			
			for line in lector:
				equipos = self.__gestorEquipos.getEquipos(line[5].split(','))

				if None in equipos:
					raise ValueError('Equipo no encontrado')

				jugador = Jugador(line[0], line[1], line[2], line[3], line[4], equipos) # type: ignore

				self.__jugadores.append(jugador)

				GestorEquipos.agregarJugadorAEquipos(jugador, equipos)
