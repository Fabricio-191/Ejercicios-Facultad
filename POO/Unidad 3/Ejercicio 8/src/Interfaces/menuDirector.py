from zope.interface import implementer
from IDirector import IDirector
from ..GestorPesonal import GestorPesonal
from ..Personal.Docente import Docente
from ..Personal.Investigador import Investigador
from ..Personal.DocenteInvestigador import DocenteInvestigador
from ..Personal.PersonalApoyo import PersonalApoyo


"""
permite modificar el sueldo básico de todos los agentes,
el porcentaje que se paga por cargo a un docente,
el porcentaje que se paga por categoría a un personal de apoyo,
y el porcentaje extra que se paga a un docente investigador;

para ello debe proveerse el cuil del agente, y el valor que corresponda según lo que se quiera modificar.
"""

@implementer(IDirector)
class MenuDirector:
	__gestor: GestorPesonal
	def __init__(self, gestor: GestorPesonal):
		self.__gestor = gestor
		self.iniciar()

	def menu(self):
		print("0. Salir del menu del director")
		print("1. Modificar sueldo")
		print("2. Modificar porcentaje docente")
		print("3. Modificar porcentaje personal apoyo")
		print("4. Modificar porcentaje docente investigador")

	def iniciar(self):
		self.menu()
		opcion = int(input("Ingrese una opcion: "))
		while opcion != 0:
			if opcion == 1:
				self.modificarSueldo()
			elif opcion == 2:
				self.modificarPorcentajeDocente()
			elif opcion == 3:
				self.modificarPorcentajePersonalApoyo()
			elif opcion == 4:
				self.modificarPorcentajeDocenteInvestigador()
			else:
				print("Opcion invalida")
			
			self.menu()
			opcion = int(input("Ingrese una opcion: "))

	def modificarSueldo(self):
		cuil = input("Ingrese el CUIL del agente: ")
		for elem in self.__gestor:
			if elem.getCUIL() == cuil:
				sueldo = float(input("Ingrese el nuevo sueldo: "))
				elem.setSueldoBasico(sueldo)

	def modificarPorcentajeDocente(self):
		porcentaje = float(input("Ingrese el nuevo porcentaje: "))
		for elem in self.__gestor:
			if isinstance(elem, Docente):
				elem.setPorcentaje(porcentaje)

	def modificarPorcentajePersonalApoyo(self):
		porcentaje = float(input("Ingrese el nuevo porcentaje: "))
		for elem in self.__gestor:
			if isinstance(elem, PersonalApoyo):
				elem.setPorcentaje(porcentaje)

	def modificarPorcentajeDocenteInvestigador(self):
		porcentaje = float(input("Ingrese el nuevo porcentaje: "))
		for elem in self.__gestor:
			if isinstance(elem, DocenteInvestigador):
				elem.setPorcentaje(porcentaje)