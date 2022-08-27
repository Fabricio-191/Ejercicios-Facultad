'''
la frecuencia de llegada de los pacientes al hospital es de 1 por minutos aproximadamente;
con un turno se da en un promedio de 2 minutos. dependiendo de la especialidad se le indica el numero de consultorio en que será atendido.
los turnos solamente se dan de 7 a 8 de la mañana.
en cada especialidad se atiende un máximo de 10 pacientes
El tiempo promedio de atención del médico es de 20’. 

Se pide
	a) calcular el tiempo promedio de espera en la cola de turnos.
	b) tiempo promedio de espera de los pacientes en cada especialidad.
	c) cantidad de personas que no pudieron obtener turnos.

Nota: considere el tiempo de simulación de 4 horas
'''
import random, string

especialidades = [
	'Ginecología',
	'Clínica médica',
	'Oftalmología',
	'Pediatría'
]

class Turno:
	__nombre: str
	__documento: str
	__especialidad: str
	
	def __init__(self, nombre, documento, especialidad):
		self.__nombre = nombre
		self.__documento = documento
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

class Especialidad:
	__turnos: Cola
	__nombre: str

	def __init__(self, nombre):
		self.__turnos = Cola()
		self.__nombre = nombre

	def getNombre(self):
		return self.__nombre

	def darTurno(self, nombre, dni):
		self.__turnos.add(Turno(nombre, dni, self.__nombre))

	def obtenerTurno(self):
		if self.__turnos.estaVacia():
			raise Exception('No quedan elementos en la cola')

		return self.__turnos.get()

	def quedanTurnos(self):
		return self.__turnos.tamaño() < 10

class Hospital:
	__especialidades: dict[str, Especialidad]

	def __init__(self):
		self.__especialidades = {}

		for especialidad in especialidades:
			self.__especialidades[especialidad] = Especialidad(especialidad)

	def getEspecialidad(self, esp):
		return self.__especialidades[esp]

def darTurnoAleatorio(hospital):
	nombre = ''.join(random.choice(string.ascii_letters) for _ in range(20))
	dni = random.randint(10 ** 7, 10 ** 8)
	especialidad = hospital.getEspecialidad(random.choice(especialidades))

	if especialidad.tieneEspacio():
		especialidad.darTurno(nombre, dni)

if __name__ == '__main__':
	tiempoTranscurrido = 0
	tiempoSimulacion = int(input('Ingrese el tiempo de la simulacion: '))
	hospital = Hospital()

	pacientesSinTurno = Cola()

	for tiempoTranscurrido in range(tiempoSimulacion):
		pacientesQueLlegaron += 1 # llega paciente

		if tiempoTranscurrido % 2 == 0 and tiempoTranscurrido <= 60: # se da turno
			darTurnoAleatorio(hospital)

		for especialidad in hospital.__especialidades.values():
			if especialidad.quedanTurnos():
				especialidad.obtenerTurno()
			else:
				print('No quedan turnos para la especialidad {}'.format(especialidad.getNombre()))
				pacientesQueLlegaron -= 1
