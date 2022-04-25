from os import path
from Viajero import Viajero

def obtenerViajero(viajeros: list[Viajero]) -> Viajero:
	num = int(input("Ingrese el numero de viajero: "))

	for viajero in viajeros:
		if(viajero.obtenerNumero() == num):
			return viajero

	print("ese viajero no existe")
	return obtenerViajero(viajeros)

if __name__ == "__main__":
	viajeros = Viajero.leerArchivo(path.dirname(__file__) + "/viajeros.csv")
	viajero = obtenerViajero(viajeros)

	print("""
	1- Consultar Cantidad de Millas
	2- Acumular Millas
	3- Canjear Millas
	0- Salir
	""")

	opcion = int(input("Ingrese la opcion: "))
	while opcion != 0:
		print()
		if opcion == 1:
			print(f"La cantidad de millas es: {viajero.cantidadTotaldeMillas()}")
		elif opcion == 2:
			millas = int(input("Ingrese la cantidad de millas a acumular: "))
			print(f"La nueva cantidad de millas es: {viajero.acumularMillas(millas)}")
		elif opcion == 3:
			millas = int(input("Ingrese la cantidad de millas a canjear: "))
			print(f"La nueva cantidad de millas es: {viajero.canjearMillas(millas)}")
		else:
			print("Opcion incorrecta")
		
		opcion = int(input("Ingrese la opcion: "))

	print()
	print("Fin del programa")
