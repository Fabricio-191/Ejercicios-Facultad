from Ramo import Ramo
from GestorFlores import GestorFlores
from typing import Literal

class GestorRamos:
	__gestorFlores: GestorFlores
	__ramosVendidos: list[Ramo]

	def __init__(self, archivoFlores: str):
		self.__ramosVendidos = []
		self.__gestorFlores = GestorFlores(archivoFlores)

	def registrarVenta(self, ramo: Ramo) -> None:
		self.__ramosVendidos.append(ramo)

	# Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que lo que se pondrán en el ramo.
	def venderRamo(self):
		tamaño = input('Ingrese el tamaño del ramo a vender: ')

		if tamaño not in ['grande', 'mediano', 'chico']:
			print('Ese tamaño de ramo no es valido')
		else:
			ramo = Ramo(tamaño) # type: ignore

			while(ramo.cantidadFlores() <= 5):
				s = input('Ingrese la flor a agregar al ramo: ')
				flor = self.__gestorFlores.obtenerFlor(s)

				
	# Mostrar el nombre de las 5 flores más pedidas en un ramo, considerando todos los ramos vendidos.
	def mostrar5FloresMasVendidas(self) -> None:
		dict = {}

		for flor in self.__gestorFlores.listaFlores()

	# Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.
	def indicarFloresVendidasEnTamaño(self, tamaño: Literal['grande', 'mediano', 'chico']) -> None:
		tipo = input('tipo de ramo: ')

		