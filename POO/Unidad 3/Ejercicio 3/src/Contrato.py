from .Jugador import Jugador
from .Equipo import Equipo

class Contrato:
	__fechaInicio: str
	__fechaFin: str
	__pagoMensual: float
	__equipo: Equipo
	__jugador: Jugador

	def __init__(self,  pagoMensual: float, fechaInicio: str, fechaFin: str, jugador: Jugador, equipo: Equipo):
		self.__fechaInicio = fechaInicio
		self.__fechaFin = fechaFin
		self.__pagoMensual = pagoMensual
		self.__equipo = equipo
		self.__jugador = jugador

	def getEquipo(self) -> Equipo:
		return self.__equipo

	def getJugador(self) -> Jugador:
		return self.__jugador

	def getFechaFinalizacion(self) -> str:
		return self.__fechaFin
