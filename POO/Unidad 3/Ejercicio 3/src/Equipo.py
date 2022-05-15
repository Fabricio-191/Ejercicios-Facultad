from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Jugador import Jugador

class Equipo:
	__nombre: str
	__ciudad: str
	__jugadores: list[Jugador]

	def __init__(self, nombre: str, ciudad: str):
		self.__nombre = nombre
		self.__ciudad = ciudad
		self.__jugadores = []

	def getNombre(self):
		return self.__nombre

	def añadirJugador(self, jugador: Jugador) -> None:
		self.__jugadores.append(jugador)
