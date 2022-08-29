"""
Una entidad bancaria que realiza el cobro de servicios, habilita una caja que atiende a una cola de clientes.

Cada cliente avanza para realizar su pago cuando la caja está desocupada. Considerar que el tiempo de atención del cajero es de 5 minutos y la frecuencia de llegada de los clientes es de 2 minutos. Realizar un programa que simule esta realidad.

Obtener el tiempo máximo de espera de los clientes en la cola.

Nota: Ingresar el tiempo de atención de cajero y la frecuencia de llegada de los clientes a la cola.
"""
import numpy as np

class Cola: # lifo
	__elementos: np.ndarray
	__tope: int
	__tamañoTotal: int

	def __init__(self, tamañoTotal: int = 100):
		self.__elementos = np.full(tamañoTotal, None)
		self.__tope = 0
		self.__tamañoTotal = tamañoTotal
	
	def getTamaño(self):
		return self.__tope

	def estaVacia(self):
		return self.__tope == 0

	def add(self, elem):
		if self.__tope == self.__tamañoTotal:
			raise Exception('La cola esta llena')

		self.__elementos[self.__tope] = elem
		self.__tope += 1

	def get(self):
		if self.__tope == 0:
			raise Exception('No quedan elementos en la cola')
		
		valor = self.__elementos[0]
		
		for i in range(1, self.__tope):
			self.__elementos[i-1] = self.__elementos[i]

		self.__tope -= 1

		return valor

class Cliente:
	__num: int

	def __init__(self, num):
		self.__num = num

	def getNum(self):
		return self.__num

class Caja:
	__ocupada: bool
	__cliente: Cliente | None

	def __init__(self):
		self.__ocupada = False
		self.__cliente = None

	def estaOcoupada(self):
		return self.__ocupada
		
	def atenderCliente(self, cliente):
		self.__cliente = cliente
		self.__ocupada = True

	def clienteAtendido(self):
		self.__cliente = None
		self.__ocupada = False

if __name__ == '__main__':
	tiempoSimulacion = int(input('Ingrese el tiempo de la simulacion: '))
	frecuenciaLlegadaClientes = int(input('Ingrese la frecuencia de los clientes (en minutos): '))
	tiempoAtencionCajero = int(input('Ingrese el tiempo que el cajero atiende (en minutos): '))

	clientesTotales = 0
	tiempoEsperaTotal = 0
	cola = Cola(tiempoSimulacion)
	caja = Caja()
	
	for tiempoTranscurrido in range(tiempoSimulacion):
		tiempoEsperaTotal += cola.getTamaño()

		if tiempoTranscurrido % frecuenciaLlegadaClientes == 0:
			clientesTotales += 1
			cola.add(Cliente(clientesTotales))
			print('llego cliente: {}'.format(clientesTotales))

		if tiempoTranscurrido % tiempoAtencionCajero == 0 and not cola.estaVacia():
			cliente = cola.get()
			caja.atenderCliente(cliente)
			print('se atendio un cliente: {}'.format(cliente.getNum()))

	promedio = tiempoEsperaTotal / clientesTotales
	print('Tiempo de espera promedio {:.2f} minutos'.format(promedio))