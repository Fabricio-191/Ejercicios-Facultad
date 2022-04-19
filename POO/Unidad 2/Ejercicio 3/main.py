"""
Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.

Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.

Implemente un programa que:

1. Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.
2. Almacene en la lista bidimensional los datos registrados en el archivo.
3. Presente un menú de opciones permita realizar las siguientes tareas:
3.1. Mostrar para cada variable el día y hora de menor y mayor valor.
3.2. Indicar la temperatura promedio mensual por cada hora.
3.3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente 
"""
from os import path
from csv import reader
from Registro import Registro

def leerArchivo(path: str) -> list[list[Registro]]:
	lista: list[list[Registro]] = [[] * 24 for _ in range(30)] 

	with open(path, "r") as file:
		for line in reader(file, delimiter=','):
			lista[
				int(line[0]) - 1
			][
				int(line[1]) - 1
			] = Registro(float(line[2]), float(line[3]), int(line[4]))
		
		return lista

def menu():
	print("""
		1. Mostrar para cada variable el día y hora de menor y mayor valor.
		2. Indicar la temperatura promedio mensual por cada hora.
		3. Dado un número de día listar los valores de las tres variables para cada hora del día dado.
		4. Salir
	""")

# 3.1. Mostrar para cada variable el día y hora de menor y mayor valor.
def obtenerValores(lista: list[list[Registro]], variable: str):
	menor = 100
	mayor = -100

	for dia in range(0, 30):
		for hora in range(0, 23):
			valor = getattr(lista[dia][hora], variable)

			if valor < menor:
				menor = valor
				diaMenor = dia
				horaMenor = hora

			if valor > mayor:
				mayor = valor
				diaMayor = dia
				horaMayor = hora

	return (diaMenor, horaMenor, diaMayor, horaMayor)		

def inciso1(lista: list[list[Registro]]) -> None:
	print("Menor temperatura: %d, %d" % obtenerValores(lista, "getTemperatura"))
	print("Mayor temperatura: %d, %d" % obtenerValores(lista, "getTemperatura"))
	print("Menor humedad: %d, %d" % obtenerValores(lista, "getHumedad"))
	print("Mayor humedad: %d, %d" % obtenerValores(lista, "getHumedad"))
	print("Menor presion: %d, %d" % obtenerValores(lista, "getPresion"))
	print("Mayor presion: %d, %d" % obtenerValores(lista, "getPresion"))
	
# 3.2. Indicar la temperatura promedio por cada hora.
def inciso2(lista: list[list[Registro]]) -> None:
	for hora in range(0, 23):
		acum = 0

		for dia in range(0, 30):
			acum +=	lista[dia][hora].getTemperatura()
		
		print("%2d: %.2f" % (hora, acum / 30))

# 3.3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente 
def inciso3(lista: list[list[Registro]]) -> None:
	dia = int(input("Ingrese el día: "))
	horas = lista[dia]

	for hora in range(0, 23):
		print("%2d: %.2f, %.2f, %d" % (hora, horas[hora].getTemperatura(), horas[hora].getHumedad(), horas[hora].getPresion()))

if __name__ == "__main__":
	lista = leerArchivo(path.join(path.dirname(__file__) + "/mes.csv"))

	menu()
	opcion = int(input("Ingrese una opción: "))
	while opcion != 0:
		if(opcion == 1):
			inciso1(lista)
		elif(opcion == 2):
			inciso2(lista)
		elif(opcion == 3):
			inciso3(lista)
		else:
			print("Opción inválida")

		menu()
		opcion = int(input("Ingrese una opción: "))
