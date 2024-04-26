class Flor:
	__numero: int
	__nombre: str
	__color: str
	__descripcion: str

	def __init__(self, datos: list[str]):
		self.__numero = int(datos[0])
		self.__nombre = datos[1]
		self.__color = datos[2]
		self.__descripcion = datos[3]

	def getNumero(self) -> int:
		return self.__numero

	def getNombre(self) -> str:
		return self.__nombre