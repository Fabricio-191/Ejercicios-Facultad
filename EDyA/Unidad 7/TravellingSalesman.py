from Path import City, Path
from Graph import Graph
import random

class TravellingSalesman:
	__solutions: list[Path]
	__cities: list[City]
	__start: City
	__distancesBetweenCities: dict[City, dict[City, float]]
	__graph: Graph | None

	def __init__(self, cities: list[City], start: City, graph: Graph | None = None):
		self.__cities = cities
		self.__start = start
		self.__graph = graph
		self.__distancesBetweenCities = {}

		for city1 in cities:
			self.__distancesBetweenCities[city1] = {}

			for city2 in cities:
				self.__distancesBetweenCities[city1][city2] = city1.distance(city2)

	def addCity(self, city: City):
		self.__cities.append(city)
		self.__distancesBetweenCities[city] = {}

		for otherCity in self.__cities:
			self.__distancesBetweenCities[city][otherCity] = city.distance(otherCity)
			self.__distancesBetweenCities[otherCity][city] = city.distance(otherCity)
	
	def removeCity(self, city: City):
		self.__cities.remove(city)
		self.__distancesBetweenCities.pop(city)

		for otherCity in self.__cities:
			self.__distancesBetweenCities[otherCity].pop(city)
	
	def setStart(self, start: City):
		self.__start = start
	
	def getStart(self) -> City:
		return self.__start

	def distanceBetweenCities(self, city1: City, city2: City) -> float:
		return self.__distancesBetweenCities[city1][city2]

	def getCities(self) -> list[City]:
		return self.__cities

	def addSolution(self, solution: Path):
		self.__solutions.append(solution)
		if self.__graph: self.__graph.updateCurrentBestPath(solution)

	def intermediateSolution(self, path: Path):
		if self.__graph: self.__graph.updateCurrentPath(path)

	def restart(self):
		self.__solutions = []

	@staticmethod
	def generateCities(n: int = 10) -> list[City]:
		cities = []

		for i in range(n):
			cities.append(
				City(random.randint(0, 100), random.randint(0, 100))
			)

		return cities
