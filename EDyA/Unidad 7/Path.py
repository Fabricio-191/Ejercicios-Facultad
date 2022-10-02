from __future__ import annotations
import math

City = tuple[int, int]

class Path:
	__travelledDistance: float
	__cities: list[City]

	def __init__(self, path, distance):
		self.__cities = path
		self.__travelledDistance = distance

	def getTravelledDistance(self):
		return self.__travelledDistance

	def length(self):
		return len(self.__cities)

	def getCities(self):
		return self.__cities

	def __add__(self, city: City):
		lastCity = self.__cities[-1]
		return Path(
			self.__cities + [city],
			self.__travelledDistance + math.sqrt(
				(lastCity[0] - city[0]) ** 2 +
				(lastCity[1] - city[1]) ** 2
			)
		)

	def __contains__(self, city: City):
		return city in self.__cities

	def __repr__(self):
		return "Distancia: {:.2f}, Camino: {}".format(self.__travelledDistance, self.__cities)
