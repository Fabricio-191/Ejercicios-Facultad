from .Ramo import Ramo
from .Flor import Flor
from .GestorFlores import GestorFlores
from csv import reader

class GestorRamos:
	__gestorFlores: GestorFlores
	__ramosVendidos: list[Ramo]
	__tamañosValidos = ['grande', 'mediano', 'chico']

	def __init__(self, gestorFlores: GestorFlores):
		self.__ramosVendidos = []
		self.__gestorFlores = gestorFlores

	# Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que lo que se pondrán en el ramo.
	def venderRamo(self):
		tamaño = input('Ingrese el tamaño del ramo a vender: ')

		if tamaño not in self.__tamañosValidos:
			print('Ese tamaño de ramo no es valido')
		else:
			lista: list[Flor] = []
			nombreFlor = input('Ingrese la flor a agregar al ramo ("terminar" para salir): ')

			while(len(lista) < 4 or nombreFlor != 'terminar'):
				flor = self.__gestorFlores.obtenerFlor(nombreFlor)

				if flor is None:
					print('La flor no existe')
				else:
					lista.append(flor)

				nombreFlor = input('Ingrese la flor a agregar al ramo ("terminar" para salir): ')

			self.__ramosVendidos.append(
				Ramo(tamaño, lista) # type: ignore
			)
	
	# Mostrar el nombre de las 5 flores más pedidas en un ramo, considerando todos los ramos vendidos.
	def mostrar5FloresMasVendidas(self) -> None:
		diccionario: dict[str, int] = {}

		for ramo in self.__ramosVendidos:
			for flor in ramo.getFlores():
				nom = flor.getNombre()
				if nom in diccionario:
					diccionario[nom] += 1
				else:
					diccionario[nom] = 1

		lista = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)

		i = 0
		while i < 5 and i < len(lista):
			print(lista[i][0])
			i += 1

	# Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.
	def indicarFloresVendidasEnTamaño(self) -> None:
		tipo = input('Tipo de ramo: ')

		if tipo not in ['grande', 'mediano', 'chico']:
			print('Ese tipo de ramo no es valido')
		else:
			vendidas = set()

			for ramo in self.__ramosVendidos:
				if ramo.getTamaño() == tipo:
					for flor in ramo.getFlores():
						vendidas.add(flor.getNombre())
			
			for flor in vendidas:
				print(flor)
	
	def leerArchivo(self, ruta: str) -> None:
		with open(ruta, 'r', encoding='utf8') as f:
			for linea in reader(f, delimiter=';'):
				flores: list[Flor] = []

				for flor in linea[1].split(','):
					flores.append(
						self.__gestorFlores.obtenerFlor(flor) # type: ignore
					)
				self.__ramosVendidos.append(
					Ramo(linea[0], flores) #type: ignore
				)
