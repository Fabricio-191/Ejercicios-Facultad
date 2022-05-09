from conjunto import Conjunto

"""
EJERCICIO 8
Sobrecarga de operadores
Defina una clase “Conjunto” que represente un conjunto matemático de números enteros.
Implemente un programa que presente un menú de opciones que permita lo siguiente:
1- La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+). Teniendo en cuenta que la unión es un nuevo conjunto que posee los elementos de ambos conjuntos, en caso de haber elementos repetidos solo aparecen una vez en el resultado. Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A+B = {1,2,3,4,6,9}
2- La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-). Teniendo en cuenta que el resultado de la diferencia de conjuntos es un nuevo conjunto que posee los elementos del primer operando que no se encuentren en el segundo operando. Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A-B = {1,2}
3- Verificar si dos conjuntos son iguales, para ello sobrecargue el operador “==” teniendo en cuenta que dos conjuntos se consideran iguales si tienen la misma cantidad de elementos y sus valores son iguales (sin importar el orden de los elementos).
"""

def test():
	conjuntoA = Conjunto([1, 2, 3, 4])
	conjuntoB = Conjunto([3, 6, 9])
	conjuntoC = Conjunto([1, 2, 3, 4])

	assert conjuntoA == conjuntoC
	assert conjuntoA != conjuntoB
	assert conjuntoA + conjuntoB == Conjunto([1, 2, 3, 4, 6, 9])
	assert conjuntoA - conjuntoB == Conjunto([1, 2, 4])


if __name__ == '__main__':
	test()
	
	conjuntoA = Conjunto([1, 2, 3, 4])
	conjuntoB = Conjunto([3, 6, 9])
	conjuntoC = Conjunto([1, 2, 3, 4])

	print("Conjunto A:", conjuntoA)
	print("Conjunto B:", conjuntoB)
	print("Conjunto C:", conjuntoC)
	print("A + B:",  conjuntoA +  conjuntoB)
	print("A - B:",  conjuntoA -  conjuntoB)
	print("A == B:", conjuntoA == conjuntoB)
	print("A == C:", conjuntoA == conjuntoC)