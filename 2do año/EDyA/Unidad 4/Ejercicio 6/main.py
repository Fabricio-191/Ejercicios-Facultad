"""
Ejercicio Nº6: Codifique un programa que simule el funcionamiento de la lista de espera del quirófano de un hospital. Cada vez que el quirófano esté desocupado, se operará al paciente de mayor urgencia, dentro de esa lista de espera. Al ingresar un paciente al hospital, además de solicitarle los datos personales, se le asignará una prioridad relacionada con la gravedad de su caso.
"""
from MonticuloBinario import MonticuloBinario

class Paciente:
	__nombre: str
	__edad: int
	__prioridad: int

	def __init__(self, nombre: str, edad: int, prioridad: int):
		self.__nombre = nombre
		self.__edad = edad
		self.__prioridad = prioridad

	def __str__(self):
		return f"{self.__nombre} - {self.__edad} - {self.__prioridad}"

	def __lt__(self, other):
		if isinstance(other, Paciente):
			return self.__prioridad < other.__prioridad
		else:
			return self.__prioridad < other

	def __gt__(self, other):
		return not self.__lt__(other)

	def __repr__(self):
		return f"( {self.__nombre} )"

if __name__ == '__main__':
	monticulo = MonticuloBinario(20)

	monticulo.insertar(Paciente("Pedro", 20, 2))
	monticulo.insertar(Paciente("Maria", 20, 3))
	monticulo.insertar(Paciente("Juan", 20, 1))
	monticulo.insertar(Paciente("Jose", 20, 4))
	monticulo.insertar(Paciente("Luis", 20, 5))
	monticulo.insertar(Paciente("Ana", 20, 6))
	monticulo.insertar(Paciente("Luisa", 20, 8))
	monticulo.insertar(Paciente("Lorena", 20, 7))

	while True:
		opcion = int(input("""1. Agregar paciente

2. Atender paciente

3. Salir

Opcion: """))

		if opcion == 1:
			nombre = input("Nombre: ")
			edad = int(input("Edad: "))
			prioridad = int(input("Prioridad: "))

			paciente = Paciente(nombre, edad, prioridad)
			monticulo.insertar(paciente)
		elif opcion == 2:
			if monticulo.estaVacio():
				print("No hay pacientes en la lista de espera")
			else:
				paciente = monticulo.eliminar()
				print(f"Se atendió a {paciente}")
		elif opcion == 3:
			break
		else:
			print("Opción inválida")

"""
1
Eduardo
20
5
1
Pepe
35
10
1
Toto
8
8
"""