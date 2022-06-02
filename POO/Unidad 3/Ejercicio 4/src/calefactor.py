class Calefactor:
	__marca: str
	__modelo: str

	def __init__(self, marca: str, modelo: str):
		self.__marca = marca
		self.__modelo = modelo

	def getMarca(self) -> str:
		return self.__marca

	def getModelo(self) -> str:
		return self.__modelo

	def calcularCosto(self):
		pass