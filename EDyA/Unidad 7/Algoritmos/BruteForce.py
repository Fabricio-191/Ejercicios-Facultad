from Path import Path, City
from TravellingSalesman import TravellingSalesman

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
