import math, random

City = tuple[int, int]

class Path:
	__cities: list[City]
	travelledDistance: float

	def __init__(self, path, distance):
		self.__cities = path
		self.travelledDistance = distance

	def length(self):
		return len(self.__cities)

	def __contains__(self, city):
		return city in self.__cities

	def __add__(self, city: City):
		lastCity = self.__cities[-1]
		return Path(
			self.__cities + [city],
			self.travelledDistance + math.sqrt(
				(lastCity[0] - city[0]) ** 2 +
				(lastCity[1] - city[1]) ** 2
			)
		)

	def __repr__(self):
		return "Distance: {:.2f}, Path: {}".format(self.travelledDistance, self.__cities)

class TravellingSalesman:
	__cities: list[City]
	__start: City
	__lessDistance: float
	__solution: Path | None

	def __init__(self, cities: list[City]):
		self.__cities = cities

	def process(self, path: Path):
		if path.length() == len(self.__cities):
			finalPath = path + self.__start

			if finalPath.travelledDistance < self.__lessDistance:
				print(finalPath)
				self.__lessDistance = finalPath.travelledDistance
				self.__solution = finalPath
		elif path.travelledDistance < self.__lessDistance:
			for city in self.__cities:
				if city not in path:
					self.process(path + city)

	def resolve(self, start: City):
		self.__solution = None
		self.__lessDistance = float('inf')
		self.__start = start
		
		self.process(Path([self.__start], 0))

		if self.__solution is None:
			raise Exception('No se encontró solución')

		return self.__solution

	@staticmethod
	def generateCities(n: int = 10) -> list[City]:
		return [
			(random.randint(0, 100), random.randint(0, 100)) for i in range(n)
		]

if __name__ == '__main__':
	cities = TravellingSalesman.generateCities(7)
	print('Caminos posibles: ', math.factorial(len(cities) - 1) / 2)
	print('Ciudades: ', cities)

	tsp = TravellingSalesman(cities)

	solution = tsp.resolve(cities[0])
	print('Mejor solución:', solution)

"""
Caminos posibles:  60.0
Ciudades:  [(37, 95), (99, 31), (95, 87), (26, 33), (29, 94), (82, 25)]
Distance: 464.16, Path: [(37, 95), (99, 31), (95, 87), (26, 33), (29, 94), (82, 25), (37, 95)]
Distance: 384.50, Path: [(37, 95), (99, 31), (95, 87), (26, 33), (82, 25), (29, 94), (37, 95)]
Distance: 334.30, Path: [(37, 95), (99, 31), (95, 87), (82, 25), (26, 33), (29, 94), (37, 95)]
Distance: 327.24, Path: [(37, 95), (99, 31), (82, 25), (95, 87), (26, 33), (29, 94), (37, 95)]
Distance: 325.75, Path: [(37, 95), (99, 31), (82, 25), (26, 33), (95, 87), (29, 94), (37, 95)]
Distance: 258.42, Path: [(37, 95), (95, 87), (99, 31), (82, 25), (26, 33), (29, 94), (37, 95)]
Mejor solución: Distance: 258.42, Path: [(37, 95), (95, 87), (99, 31), (82, 25), (26, 33), (29, 94), (37, 95)]
"""