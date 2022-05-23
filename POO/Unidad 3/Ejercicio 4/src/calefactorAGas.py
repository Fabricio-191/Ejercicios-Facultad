from .calefactor import Calefactor

class CalefactorAGas(Calefactor):
	__matricula: str # ejemplo: GN01-00001-06-057
	__calorias: int # ejemplo: 4000 kilocalorias/m3. 

	def __init__(self, marca: str, modelo: str, matricula: str, calorias: str):
		super().__init__(marca, modelo)
		self.__matricula = matricula
		self.__calorias = int(calorias)
