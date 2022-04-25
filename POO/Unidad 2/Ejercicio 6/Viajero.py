from __future__ import annotations
from csv import reader

"""
Sobrecarga de operadores
Dada la clase ViajeroFrecuente definida en el ejercicio 2, resolver lo siguiente:
1-    Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).
2-    Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de acumular millas se resuelve de la siguiente forma v = v + 100.
3-    Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas se resuelve de la siguiente forma v = v - 100.
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
		return self.__millas > otro.__millas

	def __add__(self, millas: int) -> Viajero:
		self.acumularMillas(millas)

		return self

	def __sub__(self, millas: int) -> Viajero:
		return self.__add__(-millas)

	@staticmethod
	def leerArchivo(filePath: str) -> list[Viajero]:
		with open(filePath, "r") as file:
			fileReader = reader(file, delimiter=',')
			next(fileReader, None)

			lista = []
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


	