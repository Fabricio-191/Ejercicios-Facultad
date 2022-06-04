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
						**elem['__atributos__']
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

	@staticmethod
	def leerAparato() -> Aparato:
		tipo = input('Ingrese el tipo de aparato: ')
		marca = input('Ingrese la marca: ')
		modelo = input('Ingrese el modelo: ')
		color = input('Ingrese el color: ')
		pais = input('Ingrese el pais: ')
		precio = float(input('Ingrese el precio: '))

		if tipo == 'Heladera':
			capacidad = float(input('Ingrese la capacidad: '))
			freezer = input('Tiene freezer? (Si/No): ') == 'Si'
			cyclica = input('Tiene cyclica? (Si/No): ') == 'Si'
			return Heladera(marca, modelo, color, pais, precio, capacidad, freezer, cyclica)
		elif tipo == 'Lavarropa':
			capacidad = float(input('Ingrese la capacidad: '))
			velocidad = int(input('Ingrese la velocidad: '))
			carga = input('Ingrese la carga: ')
			programas = int(input('Ingrese la cantidad de programas: '))
			return Lavarropa(marca, modelo, color, pais, precio, capacidad, velocidad, carga, programas)
		elif tipo == 'Televisor':
			resolucion = input('Ingrese la resolucion: ')
			sintonizador = input('Tiene sintonizador? (Si/No): ') == 'Si'
			tipoDefinicion = input('Ingrese el tipo de definicion: ')
			internet = input('Tiene internet? (Si/No): ') == 'Si'
			return Televisor(marca, modelo, color, pais, precio, resolucion, sintonizador, tipoDefinicion, internet)
		else:
			raise ValueError('Tipo de aparato invalido')
