"""
Composición

Usted es el programador de una empresa de software. El analista le ha entregado la siguiente parte del diagrama de clases del nuevo software que están desarrollando. 

    Facultad-Carrera                    

A. Implemente las clases del diagrama anterior.
B. Defina una clase ManejaFacultades que permita manejar las 5 facultades que posee la UNSJ.
C. Implemente un programa principal que permita:

a. Cargar los datos de las facultades en una instancia de la clase ManejaFacultades. Para esto debe considerar que la UNSJ ha provisto un archivo 'Facultades.csv' con los datos de las facultades. Este archivo presenta la siguiente estructura lógica: en una línea están los datos de la Facultad y a continuación, una línea por cada carrera con sus respectivos datos (repitiendo como primer dato, el código de Facultad). Esto se repite para cada facultad. A continuación se da un ejemplo.


D. A través de un menú de opciones implementar las siguientes funcionalidades:

1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.

2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.
"""
from os import path
from csv import reader
from Menu import Menu

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

	def __repr__(self) -> str:
		return f"Carrera {self.__codigo}"

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

	def __repr__(self) -> str:
		str = f"Facultad {self.__codigo} {{\n"
		
		for key, value in self.__carreras.items():
			str += f"\t\t{key}: {value}\n"

		return str + "\t}"

	def agregarCarrera(self, codigo: str, nombre: str, duracion: str, fechaInicio: str, titulo: str):
		self.__carreras[codigo] = Carrera(codigo, nombre, duracion, fechaInicio, titulo)

class ManejadorFacultades:
	__facultades: dict[str, Facultad]

	def __init__(self, rutaArchivo: str):
		self.__facultades = {}
		self.__cargarFacultades(rutaArchivo)

	def obtenerFacultad(self, codigo: str) -> Facultad:
		if codigo in self.__facultades:
			return self.__facultades[codigo]
		else:
			raise Exception(f'No existe la facultad {codigo}')

	def mostrarFacultad(self, codigo: str) -> None:
		facultad = self.obtenerFacultad(codigo)

		


	def __repr__(self) -> str:
		str = "ManejadorFacultades: {\n"
		
		for key, value in self.__facultades.items():
			str += f"\t{key}: {value}\n"

		return str + "}"

	def __cargarFacultades(self, rutaArchivo: str):
		with open(rutaArchivo, 'r', encoding='utf8') as archivo:
			for line in reader(archivo, delimiter=';'):
				if len(line) == 5:
					self.__facultades[line[0]] = Facultad(
						line[0],
						line[1],
						line[2],
						line[3],
						line[4]
					)
				else:
					if line[0] not in self.__facultades:
						raise Exception(f'No existe la facultad {line[0]}')

					self.__facultades[line[0]].agregarCarrera(
						line[1],
						line[2],
						line[3],
						line[4],
						line[5]
					)

"""
1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.

2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.
"""

def opcion1(manejadorFacultades: ManejadorFacultades):
	codigoFacultad = input("Ingrese el código de la facultad: ")

if __name__ == '__main__':
	manejador = ManejadorFacultades(path.dirname(__file__) + '/datos.csv')

	menu = Menu()
	menu.registrarOpcion('1', 'Obtener y mostrar facultad', manejador.__cargarFacultades)
	menu.registrarOpcion('2', )

	print(manejador)