class Registro:
	__temperatura: float
	__humedad: float
	__presion: int

	def __init__(self, temperatura: float, humedad: float, presion: int):
		self.__temperatura = temperatura
		self.__humedad = humedad
		self.__presion = presion

	def getTemperatura(self) -> float:
		return self.__temperatura

	def getHumedad(self) -> float:
		return self.__humedad

	def getPresion(self) -> int:
		return self.__presion
