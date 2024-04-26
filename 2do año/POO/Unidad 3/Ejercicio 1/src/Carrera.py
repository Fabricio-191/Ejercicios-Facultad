class Carrera:
	__codigo: int
	__nombre: str
	__duracion: str
	__fechaInicio: str
	__titulo: str

	def __init__(self, codigo: str, nombre: str, duracion: str, fechaInicio: str, titulo: str):
		self.__codigo = int(codigo)
		self.__nombre = nombre
		self.__duracion = duracion
		self.__fechaInicio = fechaInicio
		self.__titulo = titulo

	def getCodigo(self) -> int:
		return self.__codigo

	def getNombre(self) -> str:
		return self.__nombre

	def getDuracion(self) -> str:
		return self.__duracion

	def __repr__(self) -> str:
		return f"Carrera {self.__codigo}"
