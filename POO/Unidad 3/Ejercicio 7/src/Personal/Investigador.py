from .Personal import Personal

class Investigador(Personal):
	__area: str
	__tipo: str

	def __init__(self, area: str, tipo: str, **kwargs):
		super().__init__(**kwargs)
		self.__area = area
		self.__tipo = tipo
