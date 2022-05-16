from .Jugador import Jugador
from .Equipo import Equipo
import datetime

def parseDate(str: str) -> datetime.date:
	return datetime.datetime.strptime(str, '%d/%m/%Y').date()

class Contrato:
	__fechaInicio: datetime.date
	__fechaFin: datetime.date
	__pagoMensual: float
	__equipo: Equipo
	__jugador: Jugador

	def __init__(self,  pagoMensual: float, fechaInicio: str, fechaFin: str, jugador: Jugador, equipo: Equipo):
		self.__fechaInicio = parseDate(fechaInicio)
		self.__fechaFin = parseDate(fechaFin)
		self.__pagoMensual = pagoMensual
		self.__equipo = equipo
		self.__jugador = jugador

	def getEquipo(self) -> Equipo:
		return self.__equipo

	def getJugador(self) -> Jugador:
		return self.__jugador

	def getPagoMensual(self) -> float:
		return self.__pagoMensual

	def getFechaFinalizacion(self) -> datetime.date:
		return self.__fechaFin

	def getFechaInicio(self) -> datetime.date:
		return self.__fechaInicio