from .Personal import Personal

class Investigador(Personal):
	__area: str
	__tipo: str

	def __init__(self, data: dict):
		super().__init__(data)
		self.__area = data['area']
		self.__tipo = data['tipo']

	def getArea(self):
		return self.__area

