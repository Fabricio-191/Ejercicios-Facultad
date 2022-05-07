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
from typing import Literal
from Registro import Registro
from Menu import Menu

def leerArchivo(path: str) -> list[list[Registro]]:
	lista: list[list[Registro]] = []

	for dia in range(30):
		horas = []

		for hora in range(24):
			horas.append(None)

		lista.append(horas)

	with open(path, "r") as file:
		fileReader = reader(file, delimiter=",")
		next(fileReader, None)

		for line in reader(file, delimiter=','):
			dia = int(line[0]) - 1
			hora = int(line[1]) - 1

			lista[dia][hora] = Registro(float(line[2]), float(line[3]), int(line[4]))
		
		return lista

# 3.1. Mostrar para cada variable el día y hora de menor y mayor valor.
def obtenerValores(
	lista: list[list[Registro]],
	variable: Literal["getTemperatura", "getHumedad", "getPresion"]
) -> tuple[int, int, int, int]:
	menor = mayor = getattr(lista[0][0], variable)()
	diaMenor = horaMenor = diaMayor = horaMayor = 0

	for dia in range(30):
		for hora in range(24):
			valor = getattr(lista[dia][hora], variable)()

			if valor < menor:
				menor = valor
				diaMenor = dia
				horaMenor = hora

			if valor > mayor:
				mayor = valor
				diaMayor = dia
				horaMayor = hora

	return (diaMenor + 1, horaMenor + 1, diaMayor + 1, horaMayor + 1)

# 3.1. Mostrar para cada variable el día y hora de menor y mayor valor.
def inciso1(lista: list[list[Registro]]) -> None:
	temperaturas = obtenerValores(lista, "getTemperatura")
	humedades = obtenerValores(lista, "getHumedad")
	presiones = obtenerValores(lista, "getPresion")

	print(f"Menor temperatura, dia: {temperaturas[0]} hora: {temperaturas[1]}")
	print(f"Mayor temperatura, dia: {temperaturas[2]} hora: {temperaturas[3]}")
	print(f"Menor humedad, dia: {humedades[0]} hora: {humedades[1]}")
	print(f"Mayor humedad, dia: {humedades[2]} hora: {humedades[3]}")
	print(f"Menor presion, dia: {presiones[0]} hora: {presiones[1]}")
	print(f"Mayor presion, dia: {presiones[2]} hora: {presiones[3]}")
	
# 3.2. Indicar la temperatura promedio por cada hora.
def inciso2(lista: list[list[Registro]]) -> None:
	for hora in range(24):
		acum = 0

		for dia in range(30):
			acum +=	lista[dia][hora].getTemperatura()
		
		print("%2d: %.2f" % (hora + 1, acum / 30))

# 3.3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente 
def inciso3(lista: list[list[Registro]]) -> None:
	dia = int(input("Ingrese el día: "))
	horas = lista[dia]

	for hora in range(24):
		print("%2d: %3.2f - %3.2f - %5d" % (hora + 1, horas[hora].getTemperatura(), horas[hora].getHumedad(), horas[hora].getPresion()))

def test():
	Registro(1, 2, 3)

if __name__ == "__main__":
	test()
	lista = leerArchivo(path.join(path.dirname(__file__) + "/mes.csv"))

	menu = Menu()
	menu.registrarOpcion("1", "Mostrar para cada variable el día y hora de menor y mayor valor.", inciso1, lista)
	menu.registrarOpcion("2", "Indicar la temperatura promedio mensual por cada hora.", inciso2, lista)
	menu.registrarOpcion("3", "Dado un número de día listar los valores de las tres variables para cada hora del día dado.", inciso3, lista)
	menu.iniciar()