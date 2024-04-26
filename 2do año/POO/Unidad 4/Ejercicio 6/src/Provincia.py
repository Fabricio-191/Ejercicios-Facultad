# deac0445d1b10054075053075ac94217
class Provincia:
	__nombre: str
	__capital: str
	__habitantes: int
	__departamentos: int

	def __init__(self, data: dict):
		self.__nombre = data['nombre']
		self.__capital = data['capital']
		self.__habitantes = int(data['habitantes'])
		self.__departamentos = int(data['departamentos'])

	def getNombre(self):
		return self.__nombre
	
	def getCapital(self):
		return self.__capital
	
	def getHabitantes(self):
		return self.__habitantes
	
	def getDepartamentos(self):
		return self.__departamentos

	def toJSON(self):
		return {
			'nombre': self.__nombre,
			'capital': self.__capital,
			'habitantes': self.__habitantes,
			'departamentos': self.__departamentos,
		}