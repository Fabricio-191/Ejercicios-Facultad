from .Docente import Docente
from .Investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
	__cartegoria: str
	__importeExtra: float

	def __init__(self, categoria: str, importe: float, **kwargs):
		Docente.__init__(self, **kwargs)
		Investigador.__init__(self, **kwargs)
		self.__cartegoria = categoria
		self.__importeExtra = importe
		
