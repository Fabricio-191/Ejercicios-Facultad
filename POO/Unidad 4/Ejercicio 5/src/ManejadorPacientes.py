from Paciente import Paciente
import json

class ManejadorPacientes:
	__lista: list[Paciente]
	__ruta: str

	def __init__(self, ruta):
		self.__ruta = ruta
		self.cargarArchivo()

	def añadir(self, paciente: Paciente):
		self.__lista.append(paciente)
		self.guardar()
	
	def __iter__(self):
		return iter(self.__lista)

	def obtenerPaciente(self, pos):
		return self.__lista[pos]

	def cargarArchivo(self):
		with open(self.__ruta, 'r') as file:
			self.__lista = [Paciente(data) for data in json.load(file)]

	def first(self):
		return self.__lista[0]

	def guardar(self):
		with open(self.__ruta, 'w') as file:
			json.dump(
				[contacto.toJSON() for contacto in self.__lista],
				file,
				indent='\t'
			)