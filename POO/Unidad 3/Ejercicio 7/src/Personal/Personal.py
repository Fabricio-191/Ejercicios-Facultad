class Personal:
	__cuil: str
	__apellido: str
	__nombre: str
	__sueldo: float
	__antiguedad: int

	def __init__(self, data: dict):
		self.__cuil = data['cuil']
		self.__apellido = data['apellido']
		self.__nombre = data['nombre']
		self.__sueldo = data['sueldo']
		self.__antiguedad = data['antiguedad']

	def getApellido(self):
		return self.__apellido

	def getNombre(self):
		return self.__nombre

	def calcularSueldo(self):
		return self.__sueldo + self.__sueldo * (self.__antiguedad / 100)

	def getSueldoBasico(self):
		return self.__sueldo