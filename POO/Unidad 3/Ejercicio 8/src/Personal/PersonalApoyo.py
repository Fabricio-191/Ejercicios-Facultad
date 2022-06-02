from .Personal import Personal



class PersonalApoyo(Personal):
	__categoria: int
	__porcentaje: float

	def __init__(self, data: dict):
		super().__init__(data)
		self.__categoria = int(data['categoria'])
		self.__porcentaje = self.__obtenerPorcentaje()

	def __obtenerPorcentaje(self):
		res = 0
		if self.__categoria == 21 or self.__categoria == 22:
			res = 0.3
		elif self.__categoria >= 11 and self.__categoria <= 20:
			res = 0.2
		elif self.__categoria >= 1 and self.__categoria <= 10:
			res = 0.1

		return res

	def calcularSueldo(self):
		return super().calcularSueldo() + self.getSueldoBasico() * self.__porcentaje

	def setPorcentaje(self, porcentaje: float):
		self.__porcentaje = porcentaje
	
