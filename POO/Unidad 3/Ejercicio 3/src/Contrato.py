class Contrato:
	__fechaInicio: str
	__fechaFin: str
	__pagoMensual: int

	def __init__(self, fechaInicio: str, fechaFin: str, pagoMensual: str):
		self.__fechaInicio = fechaInicio
		self.__fechaFin = fechaFin
		self.__pagoMensual = int(pagoMensual)