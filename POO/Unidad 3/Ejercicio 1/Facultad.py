from Carrera import Carrera

class Facultad:
	__codigo: int
	__nombre: str
	__direccion: str
	__localidad: str
	__telefono: str
	__carreras: dict[str, Carrera]

	def __init__(self, codigo: str, nombre: str, direccion: str, localidad: str, telefono: str):
		self.__codigo = int(codigo)
		self.__nombre = nombre
		self.__direccion = direccion
		self.__localidad = localidad
		self.__telefono = telefono
		self.__carreras = {}
	
	def getCodigo(self) -> int:
		return self.__codigo

	def getNombre(self) -> str:
		return self.__nombre

	def getLocalidad(self) -> str:
		return self.__localidad

	def getCarreras(self) -> dict[str, Carrera]:
		return self.__carreras

	def getCarrera(self, codigo: str) -> Carrera | None:
		if codigo in self.__carreras:
			return self.__carreras[codigo]

		return None

	def agregarCarrera(self, codigo: str, nombre: str, duracion: str, fechaInicio: str, titulo: str):
		if codigo in self.__carreras:
			raise Exception(f"La facultad {self.__codigo} ya tiene una carrera con el código {codigo}")

		self.__carreras[codigo] = Carrera(codigo, nombre, duracion, fechaInicio, titulo)

	def __repr__(self) -> str:
		str = f"Facultad {self.__codigo} {{\n"
		
		for key, value in self.__carreras.items():
			str += f"\t\t{key}: {value}\n"

		return str + "\t}"
