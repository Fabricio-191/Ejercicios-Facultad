from .Docente import Docente
from .Investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
	__categoria: str
	__importeExtra: float

	def __init__(self, data: dict):
		Docente.__init__(self, data)
		Investigador.__init__(self, data)
		self.__categoria = data['categoria']
		self.__importeExtra = data['importe']

	def getCategoria(self):
		return self.__categoria
	
	def getImporteExtra(self):
		return self.__importeExtra

	def calcularSueldo(self):
		return Docente.calcularSueldo(self) + self.__importeExtra