"""
Una entidad bancaria que realiza el cobro de servicios, habilita una caja que atiende a una cola de clientes.

Cada cliente avanza para realizar su pago cuando la caja está desocupada. Considerar que el tiempo de atención del cajero es de 5 minutos y la frecuencia de llegada de los clientes es de 2 minutos. Realizar un programa que simule esta realidad.

Obtener el tiempo máximo de espera de los clientes en la cola.

Nota: Ingresar el tiempo de atención de cajero y la frecuencia de llegada de los clientes a la cola.
"""
class Cola:
	__elementos: list

	def __init__(self):
		self.__elementos = []

	def longitud(self):
		return len(self.__elementos)

	def add(self, obj):
		self.__elementos.append(obj)

	def get(self):
		if len(self.__elementos) == 0:
			raise Exception('No quedan elementos en la cola')

		return self.__elementos.pop(0)

class Cliente:
	__tiempoEspera: int

	def __init__(self):
		self.__tiempoEspera = 0

	def incrementarTiempoEspera(self):
		self.__tiempoEspera += 1

	def getTiempoEspera(self):
		return self.__tiempoEspera

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
	tiempoAtencionCajero = int(input('Ingrese el tiempo que el cajero atiende (en minutos): '))
	tiempoFrecuenciaLlegadaClientes = int(input('Ingrese la frecuencia de los clientes (en minutos): '))

	tiempoTranscurrido = 0 # minutos
	clientesTotales = 0
	clientesAtendidos = 0
	tiempoEsperaTotal = 0
	cola = Cola()
	caja = Caja()

	while tiempoTranscurrido < tiempoSimulacion:
		tiempoEsperaTotal += cola.longitud()

		if tiempoTranscurrido % tiempoFrecuenciaLlegadaClientes == 0:
			clientesTotales += 1
			print('llego cliente: {}'.format(clientesTotales))
			cola.add(Cliente())

		if tiempoTranscurrido % tiempoAtencionCajero == 0 and cola.longitud() != 0:
			clientesAtendidos += 1
			print('se atendio un cliente: {}'.format(clientesAtendidos))
			caja.atenderCliente(cola.get())

		tiempoTranscurrido += 1

	promedio = tiempoEsperaTotal / clientesTotales
	print('Tiempo de espera promedio {} minutos'.format(promedio))