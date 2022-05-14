from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Jugador import Jugador


class Equipo:
	__nombre: str
	__ciudad: str
	__jugadores: list[Jugador]

	def __init__(self, nombre: str, ciudad: str):
		pass
