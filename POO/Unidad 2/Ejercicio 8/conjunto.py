from __future__ import annotations

"""
EJERCICIO 8
Sobrecarga de operadores
Defina una clase “Conjunto” que represente un conjunto matemático de números enteros.
Implemente un programa que presente un menú de opciones que permita lo siguiente:
1- La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+). Teniendo en cuenta que la unión es un nuevo conjunto que posee los elementos de ambos conjuntos, en caso de haber elementos repetidos solo aparecen una vez en el resultado. Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A+B = {1,2,3,4,6,9}
2- La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-). Teniendo en cuenta que el resultado de la diferencia de conjuntos es un nuevo conjunto que posee los elementos del primer operando que no se encuentren en el segundo operando. Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A-B = {1,2}
3- Verificar si dos conjuntos son iguales, para ello sobrecargue el operador “==” teniendo en cuenta que dos conjuntos se consideran iguales si tienen la misma cantidad de elementos y sus valores son iguales (sin importar el orden de los elementos).
"""

class Conjunto:
	__conjunto: list[int]
	def __init__(self, conjunto: list[int] = []):
		self.__conjunto = conjunto.copy()

	def __add__(self, other: Conjunto) -> Conjunto:
		resultado: list[int] = self.__conjunto.copy()
	
		for elemento in other.__conjunto:
			if elemento not in resultado:
				resultado.append(elemento)
	
		return Conjunto(resultado)

	def __sub__(self, other: Conjunto) -> Conjunto:
		resultado: list[int] = []

		for elemento in self.__conjunto:
			if elemento not in other.__conjunto:
				resultado.append(elemento)

		return Conjunto(resultado)

	def __eq__(self, other: Conjunto) -> bool:
		if(type(other) != Conjunto):
			raise TypeError("El objeto no es un conjunto")

		if len(self.__conjunto) != len(other.__conjunto):  # type: ignore
			return False

		for elemento in self.__conjunto:
			if elemento not in other.__conjunto:  # type: ignore
				return False

		return True

	def __str__(self) -> str:
		return '{ ' + str(self.__conjunto)[1:-1] + ' }'

	def __repr__(self) -> str:
		return self.__str__()