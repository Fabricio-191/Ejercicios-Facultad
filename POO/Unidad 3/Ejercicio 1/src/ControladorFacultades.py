from .Facultad import Facultad
from .Carrera import Carrera
from csv import reader

class ControladorFacultades:
	__facultades: dict[str, Facultad]

	def __init__(self, rutaArchivo: str):
		self.__facultades = {}
		self.__cargarFacultades(rutaArchivo)

	def obtenerFacultad(self, codigo: str) -> Facultad | None:
		if codigo not in self.__facultades:
			return None

		return self.__facultades[codigo]

	def encontrarCarreraPorNombre(self, nombre: str) -> tuple[Facultad, Carrera] | None:
		found = False
		facultades = list(self.__facultades.values())
		i = 0
		facultad = None
		carrera = None

		while not found and i < len(facultades):
			facultad = facultades[i]
			carreras = list(facultad.getCarreras().values())
			y = 0
			while not found and y < len(carreras):
				carrera = carreras[y]
				if(carrera.getNombre() == nombre):
					found = True
				else: 
					y += 1
			i += 1

		if not found:
			return None

		return facultad, carrera #type: ignore

		for facultad in self.__facultades.values():
			for carrera in facultad.getCarreras().values():
				if carrera.getNombre() == nombre:
					return facultad, carrera

	def __repr__(self) -> str:
		str = "ManejadorFacultades: {\n"
		
		for key, value in self.__facultades.items():
			str += f"\t{key}: {value}\n"

		return str + "}"

	def __cargarFacultades(self, rutaArchivo: str):
		with open(rutaArchivo, 'r', encoding='utf8') as archivo:
			for line in reader(archivo, delimiter=';'):
				if len(line) == 5:
					self.__facultades[line[0]] = Facultad(*line)
				else:
					if line[0] not in self.__facultades:
						raise Exception(f'No existe la facultad {line[0]}')

					self.__facultades[line[0]].agregarCarrera(*line[1:])
