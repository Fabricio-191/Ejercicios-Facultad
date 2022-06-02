from __future__ import annotations
from .Personal.Personal import Personal

class Nodo:
	__dato: Personal
	__next: Nodo | None

	def __init__(self, dato: Personal, next: Nodo | None):
		self.__dato = dato
		self.__next = next

	def getDato(self):
		return self.__dato

	def getNext(self):
		return self.__next

	def setNext(self, next: Nodo | None):
		self.__next = next
