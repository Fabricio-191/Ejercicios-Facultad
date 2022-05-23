"""
https://campusvirtual.unsj.edu.ar/mod/assign/view.php?id=182603
b-  Definir una clase colección basada en un arreglo cuyo tamaño se debe ingresar por teclado, para almacenar los  calefactores.
c-  Almacenar en memoria principal los calefactores obteniendo los datos de los archivos “calefactor-electrico.csv”, “calefactor-a-gas.csv” que contienen los datos de cada uno de los tipos de calefactores.
d-  Implementar un programa que a partir de la información almacenada en memoria permita:
    * Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.
    * Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.
    * Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo. 
"""
from Menu import Menu
from src.coleccionCalefactores import ColeccionCalefactores

def opcion1(gestorCalefactores: ColeccionCalefactores):
	costo = input("Ingrese el costo por m3: ")

	

if __name__ == '__main__':
	menu = Menu()