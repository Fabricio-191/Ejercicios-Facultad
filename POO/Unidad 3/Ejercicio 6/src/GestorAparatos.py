from .Lista import Lista
from .Aparatos.Aparato import Aparato
from .Aparatos.Heladera import Heladera
from .Aparatos.Lavarropa import Lavarropa
from .Aparatos.Televisor import Televisor

import json

dict = {
	"Heladera": Heladera,
	"Lavarropa": Lavarropa,
	"Televisor": Televisor
}

class GestorAparatos:
	__lista: Lista

	def __init__(self, archivo: str):
		self.__lista = Lista()
		self.__leerArchivo(archivo)

	def insertarAparato(self, posicion: int, dato: Aparato):
		self.__lista.insertarElemento(posicion, dato)

	def obtenerAparato(self, pos: int):
		return self.__lista.encontrarElemento(pos)

	def agregarAparato(self, dato: Aparato):
		self.__lista.agregarElemento(dato)

	def conteoMarca(self, marca: str):
		contador = 0

		for elem in self.__lista:
			if elem.getMarca() == marca:
				contador += 1

		return contador

	def getLista(self):
		return self.__lista

	def __leerArchivo(self, ruta: str):
		with open(ruta, 'r') as file:
			data = json.load(file)

			for elem in data:
				self.__lista.agregarElemento(
					dict[elem['__class__']](
						elem['__atributos__']
					)
				)

	def guardar(self, ruta: str):
		with open(ruta, 'w') as file:
			json.dump(
				[{
					'__class__': elem.__class__.__name__,
					'__atributos__': elem.__dict__
				} for elem in self.__lista],
				file,
				indent=4
			)