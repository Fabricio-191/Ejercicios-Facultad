from .Jugador import Jugador
from .Equipo import Equipo

class Contrato:
	fechaInicio: str
	fechaFin: str
	pagoMensual: float
	equipo: Equipo
	jugador: Jugador

	def __init__(self,  pagoMensual: float, fechaInicio: str, fechaFin: str, jugador: Jugador, equipo: Equipo):
		self.fechaInicio = fechaInicio
		self.fechaFin = fechaFin
		self.pagoMensual = pagoMensual
		self.equipo = equipo
		self.jugador = jugador
