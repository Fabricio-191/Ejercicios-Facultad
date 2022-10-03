from Path import City, Path
import random, math

class TravellingSalesman:
	__cities: list[City]
	__start: City
	__distancesBetweenCities: dict[City, dict[City, float]]

	def __init__(self, cities: list[City], start: City):
		self.__cities = cities
		self.__start = start
		self.__graph = None
		self.__distancesBetweenCities = {}

		for city1 in cities:
			self.__distancesBetweenCities[city1] = {}

			for city2 in cities:
				self.__distancesBetweenCities[city1][city2] = math.sqrt(
					(city1[0] - city2[0]) ** 2 +
					(city1[1] - city2[1]) ** 2
				)

	def getStart(self) -> City:
		return self.__start

	def getCities(self) -> list[City]:
		return self.__cities

	def distanceBetweenCities(self, city1: City, city2: City) -> float:
		return self.__distancesBetweenCities[city1][city2]

	@staticmethod
	def generateCities(n: int = 10) -> list[City]:
		return [
			(random.randint(0, 100), random.randint(0, 100)) for i in range(n)
		]
