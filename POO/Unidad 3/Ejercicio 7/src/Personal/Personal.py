class Personal:
	__cuil: str
	__apellido: str
	__nombre: str
	__sueldo: float
	__antiguedad: int

	def __init__(self, cuil: str, apellido: str, nombre: str, sueldo: float, antiguedad: int):
		self.__cuil = cuil
		self.__apellido = apellido
		self.__nombre = nombre
		self.__sueldo = sueldo
		self.__antiguedad = antiguedad
