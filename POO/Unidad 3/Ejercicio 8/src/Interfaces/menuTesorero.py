from zope.interface import implementer
from ITesorero import ITesorero
from ..GestorPesonal import GestorPesonal

@implementer(ITesorero)
class MenuTesorero:
	__gestor: GestorPesonal

	def __init__(self, gestor: GestorPesonal):
		self.__gestor = gestor
		self.iniciar()

	def menu(self):
		print("0. Salir del menu del tesorero")
		print("1. Consultar sueldos")

	def iniciar(self):
		self.menu()
		opcion = int(input("Ingrese una opcion: "))
		while opcion != 0:
			if opcion == 1:
				self.consultarSueldos()
			else:
				print("Opcion invalida")
			
			self.menu()
			opcion = int(input("Ingrese una opcion: "))

	def consultarSueldos(self):
		numeroDocumento = int(input("Ingrese el CUIL del agente: "))
		
		for elem in self.__gestor:
			if elem.getCUIL() == numeroDocumento:
				print("El sueldo del agente es: ", elem.calcularSueldo())