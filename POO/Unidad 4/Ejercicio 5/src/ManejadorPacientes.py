from .Paciente import Paciente
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

	def actualizar(self, ops: int, paciente: Paciente):
		self.__lista[ops] = paciente
		self.guardar()

	def obtener(self, pos):
		valor = None

		if len(self.__lista) > pos:
			valor = self.__lista[pos]
		
		return valor

	def borrar(self, ops):
		del self.__lista[ops]
		self.guardar()

	def cargarArchivo(self):
		with open(self.__ruta, 'r') as file:
			self.__lista = [Paciente(data) for data in json.load(file)]

	def guardar(self):
		with open(self.__ruta, 'w') as file:
			json.dump(
				[paciente.toJSON() for paciente in self.__lista],
				file,
				indent='\t'
			)
	
	def __iter__(self):
		return iter(self.__lista)
	