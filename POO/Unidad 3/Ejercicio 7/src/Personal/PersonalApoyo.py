from .Personal import Personal

class PersonalApoyo(Personal):
	__categoria: int

	def __init__(self, data: dict):
		super().__init__(data)
		self.__categoria = int(data['categoria'])

	def calcularSueldo(self):
		percent = 0.1

		if self.__categoria == 21 or self.__categoria == 22:
			percent = 0.3
		elif self.__categoria >= 11 and self.__categoria <= 20:
			percent = 0.2
		elif self.__categoria >= 1 and self.__categoria <= 10:
			percent = 0.1

		return super().calcularSueldo() + self.getSueldoBasico() * percent
