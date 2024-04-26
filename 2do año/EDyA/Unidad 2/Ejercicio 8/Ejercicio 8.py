import random, string
from clases import Cola, Turno, Paciente

especialidades = [
	'Ginecología',
	'Clínica médica',
	'Oftalmología',
	'Pediatría'
]

class Especialidad:
	__turnos: Cola
	__nombre: str
	__tiempoRestante: int

	__esperaTotal: int
	__turnosTotales: int

	def __init__(self, nombre):
		self.__turnos = Cola(10)
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

	def darTurno(self, paciente):
		self.__turnos.add(Turno(paciente, self.__nombre))
		self.__turnosTotales += 1

	def obtenerTurno(self):
		if self.__turnos.estaVacia():
			raise Exception('No quedan elementos en la cola')

		self.__tiempoRestante = 20 # El tiempo promedio de atención del médico es de 20’. 
		return self.__turnos.get()

	def cantTurnos(self):
		return self.__turnos.getTamaño()

	def tiempoPromedio(self):
		if self.__turnosTotales == 0:
			return 0
		
		return self.__esperaTotal / self.__turnosTotales

class Hospital:
	__especialidades: dict[str, Especialidad]
	__colaPacientes: Cola
	__pacienesConTurno: int

	def __init__(self):
		self.__especialidades = {}
		self.__colaPacientes = Cola(1000)
		self.__pacienesConTurno = 0

		for especialidad in especialidades:
			self.__especialidades[especialidad] = Especialidad(especialidad)

	def getEspecialidad(self, nombre):
		return self.__especialidades[nombre]

	def llegoPaciente(self):
		nombre = ''.join(random.choice(string.ascii_letters) for _ in range(20))
		dni = random.randint(10 ** 7, 10 ** 8)

		self.__colaPacientes.add(Paciente(dni, nombre))
	
	def darTurno(self):
		paciente = self.__colaPacientes.get()

		esp = random.choice(especialidades)
		especialidad = self.__especialidades[esp]
	
		if especialidad.cantTurnos() < 10:
			especialidad.darTurno(paciente)
			self.__pacienesConTurno += 1
			return True
		else:
			print('especialidad {} llena'.format(esp))
			return False

	def pacienesSinTurno(self):
		return self.__colaPacientes.getTamaño()

	def pacientesTotales(self):
		return self.__pacienesConTurno + self.pacienesSinTurno()

if __name__ == '__main__':
	hospital = Hospital()
	esperaPorTurnos = 0
	
	for tiempoTranscurrido in range(60 * 4):
		hospital.llegoPaciente()
		esperaPorTurnos += hospital.pacienesSinTurno()

		if tiempoTranscurrido % 2 == 0 and tiempoTranscurrido <= 60:
			hospital.darTurno()

		for esp in especialidades:
			hospital.getEspecialidad(esp).paso1min()
	
	print()
	print('Tiempo promedio de espera: {:.2f}'.format(esperaPorTurnos / hospital.pacientesTotales()))
	print()
	for esp in especialidades:
		especialidad = hospital.getEspecialidad(esp)
		print('Tiempo promedio de espera en {}: {:.2f}'.format(esp, especialidad.tiempoPromedio()))
	print()
	print('Pacientes sin turno: {}'.format(hospital.pacienesSinTurno()))
