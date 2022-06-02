from .Docente import Docente
from .Investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
	__categoria: str
	__importeExtra: float

	def __init__(self, categoria: str, importe: float, **kwargs):
		Docente.__init__(self, **kwargs)
		Investigador.__init__(self, **kwargs)
		self.__categoria = categoria
		self.__importeExtra = importe

	def getCategoria(self):
		return self.__categoria
	
	def getImporteExtra(self):
		return self.__importeExtra