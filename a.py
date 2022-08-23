# Composicion
class Construccion:
	__pilares = None

	def __init__(self):
		self.__pilares = []

	def añadirPilar(self, pilar):
		self.__pilares.append(pilar)

class Pilar:
	__cargaMaxima = None

	def __init__(self, cargaMaxima):
		self.__cargaMaxima = cargaMaxima

	def getCargaMaxima(self):
		return self.__cargaMaxima

if __name__ == '__main__':
	construccion = Construccion()
	construccion.añadirPilar(Pilar(100))
	construccion.añadirPilar(Pilar(200))

# Agregacion
class EquipoDeFutbol:
	__jugadores = None

	def __init__(self):
		self.__jugadores = []

	def añadirJugador(self, jugador):
		self.__jugadores.append(jugador)

class Jugador:
	__nombre = None
	__edad = None

	def __init__(self, nombre, edad):
		self.__nombre = nombre
		self.__edad = edad

if __name__ == '__main__':
	equipo = EquipoDeFutbol()
	jugadores = [
		Jugador('Juan', 20),
		Jugador('Pedro', 25),
		Jugador('Ana', 30)
	]

	equipo.añadirJugador(jugadores[0])
	equipo.añadirJugador(jugadores[1])
	equipo.añadirJugador(jugadores[2])

class RegistroCivil:
	__direccion = None

	def __init__(self, direccion):
		self.__direccion = direccion

class Persona:
	__nombre = None
	__apellido = None

	def __init__(self, nombre, apellido):
		self.__nombre = nombre
		self.__apellido = apellido

class ActaNacimiento:
	__persona = None
	__fecha = None
	__registroCivil = None

	def __init__(self, persona, fecha, registroCivil):
		self.__persona = persona
		self.__fecha = fecha
		self.__registroCivil = registroCivil

if __name__ == '__main__':
	registroCivil = RegistroCivil('Calle falsa 123')
	personas = [
		Persona('Juan', 'Perez'),
		Persona('Pedro', 'Perez'),
		Persona('Ana', 'Perez')
	]

	actas = [
		ActaNacimiento(personas[0], '01/01/2000', registroCivil),
		ActaNacimiento(personas[1], '01/01/2000', registroCivil),
		ActaNacimiento(personas[2], '01/01/2000', registroCivil)
	]