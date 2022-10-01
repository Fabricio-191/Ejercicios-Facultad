from __future__ import annotations
import math

class City:
	__x: float
	__y: float

	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	def getCoordinates(self):
		return (self.__x, self.__y)

	def __repr__(self):
		return str(self.getCoordinates())

	def distance(self, city: City):
		return math.sqrt(
			abs(self.__x - city.__x) ** 2 +
			abs(self.__y - city.__y) ** 2
		)

class Path:
	__cities: list[City]
	__travelledDistance: float

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
		return Path(
			self.__cities + [city],
			self.__travelledDistance + self.__cities[-1].distance(city)
		)

	def __contains__(self, city: City):
		return city in self.__cities

	def __repr__(self):
		return "Distancia: {:.2f}, Camino: {}".format(self.__travelledDistance, self.__cities)
