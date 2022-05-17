"""
b-  Definir una clase colección basada en un arreglo cuyo tamaño se debe ingresar por teclado, para almacenar los  calefactores.
c-  Almacenar en memoria principal los calefactores obteniendo los datos de los archivos “calefactor-electrico.csv”, “calefactor-a-gas.csv” que contienen los datos de cada uno de los tipos de calefactores.
d-  Implementar un programa que a partir de la información almacenada en memoria permita:
    Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.
    Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.
    Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo. 
"""
import numpy as np

class Calefactor:
	__marca: str
	__modelo: str

	def __init__(self, marca: str, modelo: str):
		self.__marca = marca
		self.__modelo = modelo

class CalefactorElectrico(Calefactor):
	__potencia: int # ejemplo: 500 watts.

	def __init__(self, marca: str, modelo: str, potencia: str):
		super().__init__(marca, modelo)
		self.__potencia = int(potencia)

class CalefactorAGas(Calefactor):
	__matricula: str # ejemplo: GN01-00001-06-057
	__calorias: int # ejemplo: 4000kilocalorias/m3. 

	def __init__(self, marca: str, modelo: str, matricula: str, calorias: str):
		super().__init__(marca, modelo)
		self.__matricula = matricula
		self.__calorias = int(calorias)