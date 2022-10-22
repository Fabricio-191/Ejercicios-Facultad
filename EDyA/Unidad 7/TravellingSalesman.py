import random, math
from Graph import Graph
from Path import Path, City

class TravellingSalesman:
	cities: list[City]
	start: City
	distancesBetweenCities: dict[City, dict[City, float]]
	__graph: None # Graph | None

	def __init__(self, cities: list[City]):
		self.cities = cities
		self.distancesBetweenCities = {}

		for city1 in cities:
			self.distancesBetweenCities[city1] = {}

			for city2 in cities:
				self.distancesBetweenCities[city1][city2] = math.sqrt(
					(city1[0] - city2[0]) ** 2 +
					(city1[1] - city2[1]) ** 2
				)

	def process(self, path: Path):
		self.graph(path)
		if path.length() == len(self.cities):
			finalPath = path + self.start

			if finalPath.travelledDistance < self.lessDistance:
				self.graph(finalPath)
				self.lessDistance = finalPath.travelledDistance
				self.solution = finalPath
		elif path.travelledDistance < self.lessDistance:
			for city in self.cities:
				if city not in path.cities:
					self.process(path + city)
 
	def graph(self, path: Path):
		if path.length() == len(self.cities) + 1:
			print(path)
			if self.__graph: self.__graph.updateBestPath(path)
		elif self.__graph: self.__graph.updatePath(path)

	def __closestCity(self, path: Path):
		lastCity = path.cities[-1]
		closestCity = min(
			filter(lambda city: city not in path.cities, self.cities),
			key = lambda city: self.distancesBetweenCities[lastCity][city]
		)

		return closestCity

	def baseCase(self):
		path = Path([self.start], 0)

		for i in range(len(self.cities) - 1):
			path += self.__closestCity(path)

		self.solution = path + self.start
		self.lessDistance = self.solution.travelledDistance
		self.graph(self.solution)

	def resolve(self, start: City, baseCase = True, graph = True):
		self.solution = None
		self.lessDistance = float('inf')
		self.start = start
		
		Path.distancesBetweenCities = self.distancesBetweenCities
		self.__graph = Graph(self.cities) if graph else None
		if baseCase: self.baseCase()

		self.process(
			Path([self.start], 0)
		)

		if self.solution is None:
			raise Exception('No se encontró solución')

		return self.solution

	@staticmethod
	def generateCities(n: int = 10) -> list[City]:
		return [
			(random.randint(0, 100), random.randint(0, 100)) for i in range(n)
		]
