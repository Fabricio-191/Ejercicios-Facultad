from .Lista import Lista
from .Personal.Personal import Personal
from .Personal.Investigador import Investigador
from .Personal.DocenteInvestigador import DocenteInvestigador
from .Personal.Docente import Docente
import json

dict = {
	'Docente': Docente,
	'Investigador': Investigador,
	'DocenteInvestigador': DocenteInvestigador
}

class Gestor:
	__lista: Lista

	def __init__(self, archivo: str):
		self.cargar(archivo)

	def cargar(self, archivo: str):
		self.__lista = Lista()

		with open(archivo, "r") as file:
			for elem in json.load(file):
				self.__lista.agregar(dict[elem['__class__']](**elem))

	def guardar(self, archivo: str):
		with open(archivo, "w") as file:
			json.dump(list(self.__lista), file)

