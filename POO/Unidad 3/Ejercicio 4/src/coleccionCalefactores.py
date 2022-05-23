from calefactorAGas import CalefactorAGas
from calefactorElectrico import CalefactorElectrico
import numpy as np

class ColeccionCalefactores:
	__calefactores: np.ndarray[CalefactorElectrico | CalefactorAGas, np.dtype[np.object0]]

	def __init__(self, tamaño: int):
		self.__calefactores = np.empty(tamaño, dtype=CalefactorElectrico | CalefactorAGas)