import json
from zope.interface import implementer
from .IColeccion import IColeccion
from .Nodo import Nodo
from .Personal.Personal import Personal

from .Personal.Docente import Docente
from .Personal.Investigador import Investigador
from .Personal.DocenteInvestigador import DocenteInvestigador
from .Personal.PersonalApoyo import PersonalApoyo

dict = {
	'DocenteInvestigador': DocenteInvestigador,
	'PersonalApoyo': PersonalApoyo,
	'Investigador': Investigador,
	'Docente': Docente
}

@implementer(IColeccion)
class GestorPesonal:
	__head: Nodo | None = None
	__tail: Nodo | None = None

	def __init__(self, archivo: str):
		self.cargar(archivo)

	def encontrarElemento(self, posicion: int):
		if posicion < 0:
			raise Exception("Posicion invalida")

		actual = self.__head

		while actual != None and posicion != 0:
			actual = actual.getNext()
			posicion -= 1

		if actual == None:
			raise Exception("Posicion invalida")

		return actual

	def insertarElemento(self, posicion: int, dato: Personal):
		nodo = self.encontrarElemento(posicion)
		nodo.setNext(
			Nodo(dato, nodo.getNext())
		)

	def agregarElemento(self, dato: Personal):
		nuevoNodo = Nodo(dato, None)

		if self.__tail is None:
			self.__tail = self.__head = nuevoNodo
		else:
			self.__tail.setNext(nuevoNodo)
			self.__tail = nuevoNodo

	def mostrarElemento(self, posicion: int):
		nodo = self.encontrarElemento(posicion)

		print(f"Dato: {nodo.getDato()}")

	def __iter__(self):
		actual = self.__head
		while actual != None:
			yield actual.getDato()
			actual = actual.getNext()

	def cargar(self, archivo: str):
		with open(archivo, "r") as file:
			for elem in json.load(file):
				self.agregarElemento(
					dict[elem['__class__']](elem['__atributos__'])
				)

	def guardar(self, archivo: str):
		with open(archivo, "w") as file:
			json.dump(list(self), file)

	@staticmethod
	def leerPersonal() -> Personal:
		datos = {
			'cuil': input('Ingrese el CUIL: '),
			'apellido': input('Ingrese el apellido: '),
			'nombre': input('Ingrese el nombre: '),
			'sueldo': float(input('Ingrese el sueldo: ')),
			'antiguedad': int(input('Ingrese la antiguedad: '))
		}

		tipo = input('Ingrese el tipo de personal: ')

		if tipo == 'Docente':
			datos['carrera'] = input('Ingrese la carrera: ')
			datos['cargo'] = input('Ingrese el cargo: ')
			datos['catedra'] = input('Ingrese la catedra: ')

			return Docente(datos)
		elif tipo == 'Investigador':
			datos['area'] = input('Ingrese el area: ')
			datos['tipo'] = input('Ingrese el tipo: ')

			return Investigador(datos)
		elif tipo == 'DocenteInvestigador':
			datos['carrera'] = input('Ingrese la carrera: ')
			datos['cargo'] = input('Ingrese el cargo: ')
			datos['catedra'] = input('Ingrese la catedra: ')
			datos['area'] = input('Ingrese el area: ')
			datos['tipo'] = input('Ingrese el tipo: ')
			datos['categoria'] = input('Ingrese la categoria: ')
			datos['importeExtra'] = float(input('Ingrese el importe extra: '))

			return DocenteInvestigador(datos)
		elif tipo == 'PersonalApoyo':
			datos['categoria'] = input('Ingrese la categoria: ')
			datos['importeExtra'] = float(input('Ingrese el importe extra: '))

			return PersonalApoyo(datos)
		else:
			raise Exception("Tipo de personal invalido")