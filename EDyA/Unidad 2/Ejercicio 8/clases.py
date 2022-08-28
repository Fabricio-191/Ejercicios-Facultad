class Paciente:
	__documento: str
	__nombre: str

	def __init__(self, documento, nombre):
		self.__documento = documento
		self.__nombre = nombre

class Turno:
	__paciente: Paciente
	__especialidad: str
	
	def __init__(self, paciente, especialidad):
		self.__paciente = paciente
		self.__especialidad = especialidad

class Cola:
	__elementos: list

	def __init__(self):
		self.__elementos = []

	def add(self, obj):
		self.__elementos.append(obj)

	def get(self):
		if len(self.__elementos) == 0:
			raise Exception('No quedan elementos en la cola')

		return self.__elementos.pop(0)

	def tamaño(self):
		return len(self.__elementos)

	def estaVacia(self):
		return len(self.__elementos) == 0
