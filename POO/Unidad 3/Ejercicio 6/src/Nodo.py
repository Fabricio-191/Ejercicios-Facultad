from __future__ import annotations
from .Aparatos.Aparato import Aparato

class Nodo:
	__dato: Aparato
	__next: Nodo | None

	def __init__(self, dato: Aparato, next: Nodo | None):
		self.__dato = dato
		self.__next = next
	
	def getDato(self):
		return self.__dato

	def getNext(self):
		return self.__next
	
	def setNext(self, next: Nodo | None):
		self.__next = next
