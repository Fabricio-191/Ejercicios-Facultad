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
from os import path

class Viajero:
	def __init__(self, numero, dni, nombre, apellido, millas): 
		self.numero = numero
		self.dni = dni
		self.nombre = nombre
		self.apellido = apellido
		self.__millas = millas

	def cantidadTotaldeMillas(self):
		return self.__millas
	
	def acumularMillas(self, millas):
		self.__millas += millas
		return self.__millas
	
	def canjearMillas(self, millas):
		if self.__millas >= millas:
			self.__millas -= millas
		else:
			print("No hay millas suficientes")
		
		return self.__millas

def leerArchivo(path):
	with open(path, "r") as file:
		lista = []
		for line in file:
			line = line.strip().split(",")
			lista.append(Viajero(*line))
		
		return lista

if __name__ == "__main__":
	viajeros = leerArchivo(path.join(path.dirname(__file__), "/viajeros.txt"))

	num = int(input("Ingrese el numero de viajero: "))
	print("1- Consultar Cantidad de Millas")
	print("2- Acumular Millas")
	print("3- Canjear Millas")
	print("0- Salir")
	
	opcion = int(input("Ingrese la opcion: "))
	if opcion == 1:
		print(f"La cantidad de millas es: {viajeros[num-1].cantidadTotaldeMillas()}")
	elif opcion == 2:
		millas = int(input("Ingrese la cantidad de millas: "))
		print(f"La cantidad de millas es: {viajeros[num-1].acumularMillas(millas)}")
	elif opcion == 3:
		millas = int(input("Ingrese la cantidad de millas: "))
		print(f"La cantidad de millas es: {viajeros[num-1].canjearMillas(millas)}")
	else:
		print("Opcion incorrecta")