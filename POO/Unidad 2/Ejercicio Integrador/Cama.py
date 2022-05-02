from __future__ import annotations

"""
La clínica cuenta con 30 camas de internación, de cada cama se registra: idCama(1 a 30), habitación, estado (booleano, true indica ocupada, false indica libre), nombre y apellido del paciente (valor None si no está ocupada), diagnóstico, fecha de internación, fecha de alta (dato que se carga en el ítem 3). Los datos de las camas vienen en un archivo separado por comas denominado “camas.csv”.
"""

class Cama:
	__id: int
	__habitacion: int
	__estado: bool
	__paciente: str | None
	__diagnotisco: str | None
	__fechaInternacion: str | None
	__fechaAlta: str | None
	
	def __init__(
		self,
		id: int,
		habitacion: int,
		estado: bool,
		paciente: str | None,
		diagnostico: str | None,
		fechaInternacion: str | None,
		fechaAlta: str | None
	):
		self.__id = id
		self.__habitacion = habitacion
		self.__estado = estado
		self.__paciente = paciente
		self.__diagnostico = diagnostico
		self.__fechaInternacion = fechaInternacion
		self.__fechaAlta = fechaAlta

	def obtenerNyA(self) -> str:
		if(self.__paciente is None):
			return "Sin paciente"

		return self.__paciente 

	def obtenerID(self) -> int:
		return self.__id

	def obtenerHabitacion(self) -> int:
		return self.__habitacion

	def obtenerDiagnostico(self) -> str:
		return self.__diagnostico or "Sin paciente"

	def obtenerFechaInternacion(self) -> str:
		return self.__fechaInternacion or "Sin paciente"
