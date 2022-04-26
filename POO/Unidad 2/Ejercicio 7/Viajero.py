from __future__ import annotations
from csv import reader

"""
EJERCICIO 7
Sobrecarga por derecha (reverse operators)
Dada la clase ViajeroFrecuente definida en el ejercicio 2 con las sobrecargas de operadores solicitadas en el ejercicio 6, resolver lo siguiente:
1-    Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero a través de la sobrecarga del operador igual (== o __eq__). Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar tanto v ==  100 como 100 == v.
2-    Acumular millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 + v.
3-    Canjear millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 - v.
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

	def mostrar(self) -> None:
		print(f"{self.__numero}, {self.__dni}, {self.__nombre}, {self.__apellido}, {self.__millas}")

	def __gt__(self, otro: Viajero) -> bool:
		if(type(otro) != Viajero):
			raise TypeError("No se puede comparar un viajero con un valor")

		return self.__millas > otro.__millas

	def __add__(self, millas: int) -> Viajero:
		if(type(millas) != int):
			raise TypeError("No se puede sumar un viajero con un no-entero")

		self.acumularMillas(millas)

		return self

	def __sub__(self, millas: int) -> Viajero:
		if(type(millas) != int):
			raise TypeError("No se puede restar un viajero con un no-entero")

		return self.__add__(-millas)

	def __eq__(self, otro: Viajero | object | int) -> bool:
		if(type(otro) == Viajero):
			return self.__millas == otro.__millas  # type: ignore
		elif(type(otro) == int):
			return self.__millas == otro
		else:
			raise TypeError("No se puede comparar un viajero con un valor que no sea un entero u otro viajero")

	def __radd__(self, millas: int) -> Viajero:
		return self.__add__(millas)
	
	def __rsub__(self, millas: int) -> Viajero:
		return self.__sub__(millas)

	@staticmethod
	def leerArchivo(filePath: str) -> list[Viajero]:
		with open(filePath, "r") as file:
			fileReader = reader(file, delimiter=',')
			next(fileReader, None)

			lista: list[Viajero] = []
			for line in fileReader:
				lista.append(
					Viajero(
						int(line[0]),
						line[1],
						line[2],
						line[3],
						float(line[4])
					)
				)
			
			return lista


	