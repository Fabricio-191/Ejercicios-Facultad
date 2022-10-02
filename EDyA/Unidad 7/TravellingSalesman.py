from Path import City, Path
from Graph import Graph
import random, math

class TravellingSalesman:
	__solutions: list[Path]
	__cities: list[City]
	__start: City
	__distancesBetweenCities: dict[City, dict[City, float]]
	__graph: Graph | None

	def __init__(self, cities: list[City], start: City):
		self.__cities = cities
		self.__start = start
		self.__graph = None
		self.__solutions = []
		self.__distancesBetweenCities = {}

		for city1 in cities:
			self.__distancesBetweenCities[city1] = {}

			for city2 in cities:
				self.__distancesBetweenCities[city1][city2] = math.sqrt(
					(city1[0] - city2[0]) ** 2 +
					(city1[1] - city2[1]) ** 2
				)

	def setGraph(self, graph):
		self.__graph = graph

	def getStart(self) -> City:
		return self.__start

	def getCities(self) -> list[City]:
		return self.__cities

	def registerSolution(self, path: Path):
		if path.length() == len(self.__cities) + 1:
			print(path)
			self.__solutions.append(path)
			if self.__graph: self.__graph.updateCurrentBestPath(path)
		elif self.__graph: self.__graph.updateCurrentPath(path)

	def distanceBetweenCities(self, city1: City, city2: City) -> float:
		return self.__distancesBetweenCities[city1][city2]

	def restart(self):
		self.__solutions = []

	@staticmethod
	def generateCities(n: int = 10) -> list[City]:
		return [
			(random.randint(0, 100), random.randint(0, 100)) for i in range(n)
		]
