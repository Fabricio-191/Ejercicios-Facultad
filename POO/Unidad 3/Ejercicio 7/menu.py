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
		print("4. ")
		print("5. ")
		print("6. ")
		print("7. ")
		print("8. Guardar datos")

	def opcion1(self):
		personal = GestorPesonal.leerPersonal()
		pos = int(input("Ingrese una posicion: "))
	
		self.__gestor.insertarElemento(pos, personal)

	def opcion2(self):
		personal = GestorPesonal.leerPersonal()
		self.__gestor.agregarElemento(personal)

	def opcion3(self):
		pos = int(input("Ingrese una posicion: "))
		print(self.__gestor.encontrarElemento(pos).__class__.__name__)

	def opcion4(self):
		carrera = input("Ingrese una carrera: ")
		lista: list[DocenteInvestigador] = []

		for elem in self.__gestor:
			if isinstance(elem, DocenteInvestigador) and elem.getCarrera() == carrera:
				lista.append(elem)

		lista.sort(key=lambda x: x.getApellido())

		for elem in lista:
			print(elem)

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
		
	"""
	Reglas de negocio para el cálculo del sueldo:

	Por cada año de antigüedad el sueldo se incrementa en un porcentaje sobre el sueldo básico por ejemplo: si tienen 5 años de antigüedad el sueldo sería sueldo básico + 5%(básico).

	Porcentaje por cargo: 10 % si el cargo es simple, 20% si el cargo es semiexclusivo, 50% si el cargo es exclusivo.
	Porcentaje por categoría: 10% si la categoría es de 1 a 10, 20 % si la categoría es de 11 a      20, 30% si la categoría es de 21 a 22.

	Todos los porcentajes se calculan sobre el sueldo básico.

	sueldoPersonalDeApoyo = Sueldo Básico + %antigüedad% + por categorías
	sueldoDocente = Sueldo Básico + %antigüedad% + por cargo
	sueldoInvestigador = Sueldo básico + %antigüedad%
	sueldoDocenteInvestigador = sueldoDocente() + importe extra por docencia e investigación.
	"""

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

	def iniciar(self):
		opcion = int(input("Ingrese una opcion: "))
		while opcion != 0:
			if opcion in self.__dictOpciones:
				self.__dictOpciones[opcion]()
			else:
				print("Opcion invalida")
			
			opcion = int(input("Ingrese una opcion: "))

