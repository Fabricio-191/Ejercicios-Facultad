from src.GestorPesonal import GestorPesonal
from src.Personal.DocenteInvestigador import DocenteInvestigador
from src.Personal.Investigador import Investigador
from os import path


class Menu:
	__gestor: GestorPesonal
	__dictOpciones: dict

	def __init__(self, gestor: GestorPesonal):
		self.__gestor = gestor
		self.__dictOpciones = {
			1: self.opcion1,
			2: self.opcion2,
			3: self.opcion3,
			4: self.opcion4,
			5: self.opcion5,
			6: self.opcion6,
			7: self.opcion7,
			8: self.opcion8
		}

	def menu(self):
		print("0. Salir")
		print("1. Insertar a agentes a la colección.")
		print("2. Agregar agentes a la colección.")
		print("3. Mostrar tipo de agente en posicion")
		print("4. Docentes investigadores de una carrera")
		print("5. Investigadores y docentes investigadores de una area de investigacion")
		print("6. Listar personal")
		print("7. Calcular importe extra de categoria de investigacion")
		print("8. Guardar datos\n")

	def iniciar(self):
		self.menu()
		opcion = int(input("Ingrese una opcion: "))
		while opcion != 0:
			if opcion in self.__dictOpciones:
				self.__dictOpciones[opcion]()
			else:
				print("Opcion invalida")
			
			self.menu()
			opcion = int(input("Ingrese una opcion: "))

	def opcion1(self):
		personal = GestorPesonal.leerPersonal()
		pos = int(input("Ingrese una posicion: "))
	
		self.__gestor.insertarElemento(pos, personal)

	def opcion2(self):
		personal = GestorPesonal.leerPersonal()
		self.__gestor.agregarElemento(personal)

	def opcion3(self):
		pos = int(input("Ingrese una posicion: "))
		print(
			self.__gestor.encontrarElemento(pos).getDato().__class__.__name__)

	def opcion4(self):
		carrera = input("Ingrese una carrera: ")
		lista: list[DocenteInvestigador] = []

		for elem in self.__gestor:
			if isinstance(elem, DocenteInvestigador) and elem.getCarrera() == carrera:
				lista.append(elem)

		lista.sort(key=lambda x: x.getApellido())

		for elem in lista:
			print(elem.getNombre(), elem.getApellido())

	def opcion5(self):
		area = input("Ingrese una area de investigacion: ")
		cont = 0
		cont2 = 0

		for elem in self.__gestor:
			if isinstance(elem, Investigador) and elem.getArea() == area:
				if isinstance(elem, DocenteInvestigador):
					cont += 1
				else:
					cont2 += 1

		print('En esa area existen {} investigadores y {} investigadores docentes'.format(cont2, cont))

	def opcion6(self):
		lista = list(self.__gestor)
		lista.sort(key=lambda x: x.getApellido())

		for elem in lista:
			print(elem.getNombre(), elem.getApellido(), elem.__class__.__name__, elem.calcularSueldo())

	def opcion7(self):
		cat = input("Ingrese una categoria: ")
		total = 0
		
		for elem in self.__gestor:
			if isinstance(elem, DocenteInvestigador) and elem.getCategoria() == cat:
				total += elem.getImporteExtra()

				print(elem.getApellido(), elem.getNombre(), elem.getImporteExtra())

		print('El total es: {}'.format(total))
  
	def opcion8(self):
		self.__gestor.guardar(path.dirname(__file__) + "/personal.json")