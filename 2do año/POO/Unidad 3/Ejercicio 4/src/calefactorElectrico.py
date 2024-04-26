from .calefactor import Calefactor

class CalefactorElectrico(Calefactor):
	__potencia: int # ejemplo: 500 watts.
	costoKWh: float = 0
	cantidadKWh: float = 0

	def __init__(self, marca: str, modelo: str, potencia: str):
		super().__init__(marca, modelo)
		self.__potencia = int(potencia)

	def calcularCosto(self):
		return self.__potencia * self.cantidadKWh * self.costoKWh