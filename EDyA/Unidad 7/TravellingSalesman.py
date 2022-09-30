from __future__ import annotations
import math

class City:
	__name: str
	__x: float
	__y: float

	def __init__(self, data):
		self.__name = data["name"]
		self.__x = data["x"]
		self.__y = data["y"]

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
		return f"Distancia: {self.__travelledDistance}, Camino: {self.__cities}"

class TravellingSalesman:
	__solutions: list[Path]
	__cities: list[City]
	__start: City
	__distancesBetweenCities: dict[City, dict[City, float]]
	__lessDistance: float

	def __init__(self, cities):
		self.__cities = cities
		self.__distancesBetweenCities = {}

		for city1 in cities:
			self.__distancesBetweenCities[city1] = {}

			for city2 in cities:
				self.__distancesBetweenCities[city1][city2] = city1.distance(city2)
	
	def __isSolution(self, solution: Path):
		return solution.length() == len(self.__cities)

	def __backtrack(self, path: Path):
		if self.__isSolution(path):
			finalSolution = path + self.__start
			
			if finalSolution.getTravelledDistance() < self.__lessDistance:
				self.__lessDistance = finalSolution.getTravelledDistance()
				self.__solutions.append(finalSolution)
		else:
			for city in self.__cities:
				if city not in path:
					newPath = path + city

					if newPath.getTravelledDistance() <= self.__lessDistance:
						self.__backtrack(newPath)

	def resolve(self, start: City):
		self.__lessDistance = math.inf
		self.__start = start
		self.__solutions = []
		self.__backtrack(Path([start], 0))

		return self.__solutions