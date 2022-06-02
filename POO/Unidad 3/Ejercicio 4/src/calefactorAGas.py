from .calefactor import Calefactor

class CalefactorAGas(Calefactor):
	__matricula: str # ejemplo: GN01-00001-06-057
	__calorias: int  # ejemplo: 4000 kilocalorias/m3. 
	costoM3: float = 0
	cantidadM3: float = 0

	def __init__(self, marca: str, modelo: str, matricula: str, calorias: str):
		super().__init__(marca, modelo)
		self.__matricula = matricula
		self.__calorias = int(calorias)

	def calcularCosto(self):
		return self.__calorias * self.cantidadM3 * self.costoM3
