from 

class Menu:
	def __init__(self, lista):
		self.lista = lista

	def menu(self):
		opcion = 0
		while opcion != 5:
			print("0. Salir")
			print("1. Cargar archivo")
			print("2. Agregar agente")
			print("3. Mostrar agente")
			print("4. Buscar agente")
