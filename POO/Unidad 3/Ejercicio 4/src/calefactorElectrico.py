from .calefactor import Calefactor

class CalefactorElectrico(Calefactor):
	__potencia: int # ejemplo: 500 watts.

	def __init__(self, marca: str, modelo: str, potencia: str):
		super().__init__(marca, modelo)
		self.__potencia = int(potencia)
