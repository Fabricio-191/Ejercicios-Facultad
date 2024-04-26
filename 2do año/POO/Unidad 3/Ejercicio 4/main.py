"""
https://campusvirtual.unsj.edu.ar/mod/assign/view.php?id=182603
b-  Definir una clase colección basada en un arreglo cuyo tamaño se debe ingresar por teclado, para almacenar los  calefactores.
c-  Almacenar en memoria principal los calefactores obteniendo los datos de los archivos “calefactor-electrico.csv”, “calefactor-a-gas.csv” que contienen los datos de cada uno de los tipos de calefactores.
d-  Implementar un programa que a partir de la información almacenada en memoria permita:
    * Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.
    * Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.
    * Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo. 
"""
from csv import reader
from Menu import Menu
from src.coleccionCalefactores import ColeccionCalefactores
from src.calefactorElectrico import CalefactorElectrico
from src.calefactorAGas import CalefactorAGas
from os import path

def opcion1(coleccionGas: ColeccionCalefactores):
	CalefactorAGas.cantidadM3 = float(input("Ingrese la cantidad a consumir en m3: "))
	CalefactorAGas.costoM3 = float(input("Ingrese el costo por m3: "))

	menor = coleccionGas.menorCosto()

	print(f"El calefactor con menor costo de consumo es: {menor.getModelo()}, marca: {menor.getMarca()}")

def opcion2(coleccionElectrico: ColeccionCalefactores):
	CalefactorElectrico.cantidadKWh = float(input("Ingrese la cantidad a consumir en Kwh: "))
	CalefactorElectrico.costoKWh = float(input("Ingrese el costo por Kwh: "))

	menor = coleccionElectrico.menorCosto()

	print(f"El calefactor con menor costo de consumo es: {menor.getModelo()}, marca: {menor.getMarca()}")

def opcion3(coleccionElectrico: ColeccionCalefactores, coleccionGas: ColeccionCalefactores):
	menorGas = coleccionGas.menorCosto()
	menorElectrico = coleccionElectrico.menorCosto()

	if menorGas.calcularCosto() < menorElectrico.calcularCosto(): # type: ignore
		print(f"El calefactor con menor costo de consumo es: {menorGas.getModelo()}, marca: {menorGas.getMarca()}")
	else:
		print(f"El calefactor con menor costo de consumo es: {menorElectrico.getModelo()}, marca: {menorElectrico.getMarca()}")

	print("El calefactor con menor costo de consumo es:")
	
if __name__ == '__main__':
	tamaño = int(input("Ingrese el tamaño de la colección de calefactores electricos: "))
	coleccionElectrico = ColeccionCalefactores(tamaño, path.dirname(__file__) + "/calefactor-electrico.csv", CalefactorElectrico)

	tamaño = int(input("Ingrese el tamaño de la colección de calefactores a gas: "))
	coleccionGas = ColeccionCalefactores(tamaño, path.dirname(__file__) + "/calefactor-a-gas.csv", CalefactorAGas)

	menu = Menu()
	menu.registrarOpcion("1", "Calcular el costo de un calefactor a gas natural", opcion1, coleccionGas)
	menu.registrarOpcion("2", "Calcular el costo de un calefactor electrico", opcion2, coleccionElectrico)
	menu.registrarOpcion("3", "Calcular el costo de un calefactor con menor consumo", opcion3, coleccionElectrico, coleccionGas)
	menu.iniciar()
