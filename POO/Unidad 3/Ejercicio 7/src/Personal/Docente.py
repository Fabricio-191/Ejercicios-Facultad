from pyparsing import srange
from .Personal import Personal

class Docente(Personal):
	__carrera: str
	__cargo: str
	__catedra: str

	def __init__(self, carrera: str, cargo: str, catedra: str, **kwarg):
		super().__init__(**kwarg)
		self.__carrera = carrera
		self.__cargo = cargo		
		self.__catedra = catedra

	def getCarrera(self):
		return self.__carrera
		