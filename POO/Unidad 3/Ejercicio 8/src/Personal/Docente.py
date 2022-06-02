from pyparsing import srange
from .Personal import Personal

class Docente(Personal):
	__carrera: str
	__cargo: str
	__catedra: str

	def __init__(self, data: dict):
		super().__init__(data)
		self.__carrera = data['carrera']
		self.__cargo = data['cargo']		
		self.__catedra = data['catedra']

	def getCarrera(self):
		return self.__carrera

	def calcularSueldo(self):
		percent = 0.1

		if self.__cargo == "semiexclusivo":
			percent = 0.2
		elif self.__cargo == "exclusivo":
			percent = 0.5
		
		return super().calcularSueldo() + self.getSueldoBasico() * percent
		
