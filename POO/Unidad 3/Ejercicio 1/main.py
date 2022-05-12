"""
Composición

Usted es el programador de una empresa de software. El analista le ha entregado la siguiente parte del diagrama de clases del nuevo software que están desarrollando. 

Facultad-Carrera 

A. Implemente las clases del diagrama anterior.
B. Defina una clase ManejaFacultades que permita manejar las 5 facultades que posee la UNSJ.
C. Implemente un programa principal que permita:

a. Cargar los datos de las facultades en una instancia de la clase ManejaFacultades. Para esto debe considerar que la UNSJ ha provisto un archivo 'Facultades.csv' con los datos de las facultades. Este archivo presenta la siguiente estructura lógica: en una línea están los datos de la Facultad y a continuación, una línea por cada carrera con sus respectivos datos (repitiendo como primer dato, el código de Facultad). Esto se repite para cada facultad. A continuación se da un ejemplo.

D. A través de un menú de opciones implementar las siguientes funcionalidades:

1. Ingresar el código de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.

2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.
"""
from os import path
from Menu import Menu
from ControladorFacultades import ControladorFacultades

def opcion1(controladorFacultades: ControladorFacultades):
	codigoFacultad = input("Ingrese el código de la facultad: ")

	facultad = controladorFacultades.obtenerFacultad(codigoFacultad)

	if facultad is None:
		print(f"No existe la facultad {codigoFacultad}")
	else:
		print(f"\nNombre de la facultad: {facultad.getNombre()}")
		print("Carreras de la facultad: \n")
		for key, value in facultad.getCarreras().items():
			print(f"\t{key}: {value.getNombre()}")
			print(f"\tDuración: {value.getDuracion()}\n")

def opcion2(controladorFacultades: ControladorFacultades):
	nombreCarrera = input("Ingrese el nombre de la carrera: ")

	resultado = controladorFacultades.encontrarCarreraPorNombre(nombreCarrera)

	if resultado is None:
		print(f"No existe la carrera {nombreCarrera}")
	else:
		facultad, carrera = resultado
		print(f"\nCódigo {facultad.getCodigo()}:{carrera.getCodigo()}")
		print(f"Facultad donde se dicta: {facultad.getNombre()}")
		print(f"Localidad: {facultad.getLocalidad()}")

if __name__ == '__main__':
	controlador = ControladorFacultades(path.dirname(__file__) + '/datos.csv')

	menu = Menu()
	menu.registrarOpcion('1', 'Mostrar facultad y carreras', opcion1, controlador)
	menu.registrarOpcion('2', 'Encontrar carrera por nombre', opcion2, controlador)
	menu.iniciar()
