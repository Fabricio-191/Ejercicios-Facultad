"""
Listas

En una aerolínea ofrece una promoción a sus viajeros frecuentes que consiste en acumular puntos por los viajes que realizan, pudiendo luego recibir beneficios a través del canje de puntos.

Usted trabaja en el área de sistemas de la aerolínea y le han solicitado la implementación de un sistema capaz de gestionar la promoción. Respetando el siguiente diseño de clase:


Atributos: número de viajero, DNI, nombre, apellido y millas acumuladas.
Métodos:

a- El constructor.
b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, las suma en el atributo correspondiente y retorna el valor del atributo actualizado.
d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. Para utilizar las millas debe verificarse que la cantidad a canjear sea menor o igual a la cantidad de millas acumuladas, caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad de millas acumuladas.

Implemente un programa que:

1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, y almacenarlas en una lista.
2- Lea por teclado un número de viajero frecuente y presente un menú con las siguientes opciones:
	a- Consultar Cantidad de Millas.
	b- Acumular Millas.
	c- Canjear Millas.

3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.
"""
class Viajero:
	__numero: int
	__dni: str
	__nombre: str
	__apellido: str
	__millas: float

	def __init__(self, numero: int, dni: str, nombre: str, apellido: str, millas: float): 
		self.__numero = numero
		self.__dni = dni
		self.__nombre = nombre
		self.__apellido = apellido
		self.__millas = millas

	def cantidadTotaldeMillas(self) -> float:
		return self.__millas
	
	def acumularMillas(self, millas: float) -> float:
		self.__millas += millas
		return self.__millas
	
	def canjearMillas(self, millas: float) -> float:
		if self.__millas >= millas:
			self.__millas -= millas
		else:
			print("No hay millas suficientes")
		
		return self.__millas

	def obtenerNumero(self) -> int:
		return self.__numero