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
	__tiempoRestante: int

	__esperaTotal: int
	__turnosTotales: int

	def __init__(self, nombre):
		self.__turnos = Cola()
		self.__nombre = nombre
		self.__tiempoRestante = 1
		self.__esperaTotal = 0
		self.__turnosTotales = 0

	def getNombre(self):
		return self.__nombre

	def estaDisponible(self):
		return self.__tiempoRestante == 0

	def paso1min(self): 
		if self.__tiempoRestante != 0:
			self.__tiempoRestante -= 1
		
		self.__esperaTotal += self.cantTurnos()
		
		if self.estaDisponible() and self.cantTurnos() != 0:
			self.obtenerTurno()

	def darTurno(self, nombre, dni):
		self.__turnos.add(Turno(nombre, dni, self.__nombre))
		self.__turnosTotales += 1

	def obtenerTurno(self):
		if self.__turnos.estaVacia():
			raise Exception('No quedan elementos en la cola')

		self.__tiempoRestante = 20 # El tiempo promedio de atención del médico es de 20’. 
		return self.__turnos.get()

	def cantTurnos(self):
		return self.__turnos.tamaño()

	def tiempoPromedio(self):
		if self.__turnosTotales == 0:
			return 0
		
		return self.__esperaTotal / self.__turnosTotales

class Hospital:
	__especialidades: dict[str, Especialidad]
	__colaTurnos: Cola

	def __init__(self):
		self.__especialidades = {}

		for especialidad in especialidades:
			self.__especialidades[especialidad] = Especialidad(especialidad)

	def getEspecialidad(self, nombre):
		return self.__especialidades[nombre]

'''
Se pide
	a) calcular el tiempo promedio de espera en la cola de turnos.
	b) tiempo promedio de espera de los pacientes en cada especialidad.
	c) cantidad de personas que no pudieron obtener turnos.
'''

if __name__ == '__main__':
	hospital = Hospital()
	pacientesSinTurno = 0
	pacientesQueLlegaron = 0
	
	def darTurnoAleatorio():
		nombre = ''.join(random.choice(string.ascii_letters) for _ in range(20))
		dni = random.randint(10 ** 7, 10 ** 8)
		esp = random.choice(especialidades)
		especialidad = hospital.getEspecialidad(esp)
		
		if especialidad.cantTurnos() < 10:
			especialidad.darTurno(nombre, dni)
		else:
			pacientesSinTurno += 1

	for tiempoTranscurrido in range(60 * 4): # Nota: considere el tiempo de simulación de 4 horas
		# la frecuencia de llegada de los pacientes al hospital es de 1 por minutos aproximadamente;
		pacientesQueLlegaron += 1

		if tiempoTranscurrido % 2 == 0 and tiempoTranscurrido <= 60:
			darTurnoAleatorio()
		else:
			pacientesSinTurno += 1

		for esp in especialidades:
			hospital.getEspecialidad(esp).paso1min()

	print()
	for esp in especialidades:
		especialidad = hospital.getEspecialidad(esp)
		print('{} tiempo promedio de espera: {:.2f}'.format(esp, especialidad.tiempoPromedio()))
