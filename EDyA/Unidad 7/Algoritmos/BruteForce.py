from Path import Path, City
from TravellingSalesman import TravellingSalesman

def bruteForce(tsp: TravellingSalesman) -> list[Path]:
	solutions = []
	lessDistance = float('inf')

	def process(path: Path):
		nonlocal lessDistance, solutions

		if path.length() == len(tsp.getCities()):
			finalPath = path + tsp.getStart()

			if finalPath.getTravelledDistance() <= lessDistance:
				print(finalPath)
				lessDistance = finalPath.getTravelledDistance()
				solutions.append(finalPath)
		else:
			for city1 in tsp.getCities():
				if city1 not in path:
					process(path + city1)

	process(Path([tsp.getStart()], 0))

	return list(filter(lambda path: path.getTravelledDistance() == lessDistance, solutions))

"""
class BruteForce:
	__problem: TravellingSalesman
	__lessDistance: float

	def __init__(self, problem: TravellingSalesman):
		self.__problem = problem

	def process(self, path: Path):
		if path.length() == len(self.__problem.getCities()):
			finalPath = path + self.__problem.getStart()

			if finalPath.getTravelledDistance() <= self.__lessDistance:
				print(finalPath)
				self.__lessDistance = finalPath.getTravelledDistance()
				self.__solutions.append(finalPath)
		else:
			for city1 in self.__problem.getCities():
				if city1 not in path:
					self.process(path + city1)

	def resolve(self) -> list[Path]:
		self.__solutions = []
		self.__lessDistance = float('inf')
		self.process(Path([self.__problem.getStart()], 0))

		bestSolutions = list(filter(lambda path: path.getTravelledDistance() == self.__lessDistance, self.__solutions))

		return bestSolutions

"""