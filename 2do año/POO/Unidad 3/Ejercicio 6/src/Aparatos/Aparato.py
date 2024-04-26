class Aparato:
	__marca: str
	__modelo: str
	__color: str
	__pais: str
	__precio: float
	
	def __init__(self, marca: str, modelo: str, color: str, pais: str, precio: float):
		self.__marca = marca
		self.__modelo = modelo
		self.__color = color
		self.__pais = pais
		self.__precio = precio

	def cacularPrecioVenta(self):
		pass

	def getMarca(self):
		return self.__marca

	def getModelo(self):
		return self.__modelo

	def getColor(self):
		return self.__color

	def getPais(self):
		return self.__pais

	def getPrecio(self):
		return self.__precio

	def toJSON(self):
		return {
			'marca': self.__marca,
			'modelo': self.__modelo,
			'color': self.__color,
			'pais': self.__pais,
			'precio': self.__precio
		}