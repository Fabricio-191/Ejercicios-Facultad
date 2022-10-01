from Path import Path, City
from TravellingSalesman import TravellingSalesman

class RamificacionYPoda:
	__problem: TravellingSalesman
	__lessDistance: float

	def __init__(self, problem):
		self.__problem = problem

	# baseCase creates a path to the closest city
	def __baseCase(self):
		start = self.__problem.getStart()
		path = Path([start], 0)

		for i in range(len(self.__problem.getCities()) - 1):
			closestCity = self.__problem.getCities()[0]
			closestDistance = float('inf')

			for city in self.__problem.getCities():
				if city not in path:
					distance = self.__problem.distanceBetweenCities(path.getCities()[-1], city)

					if distance < closestDistance:
						closestDistance = distance
						closestCity = city

			path = path + closestCity

		path = path + start
		self.__solutions.append(path)
		self.__lessDistance = path.getTravelledDistance()
		print('Caso base', path)

	def __backtrack(self, path: Path):
		if path.length() == len(self.__problem.getCities()):
			finalSolution = path + self.__problem.getStart()

			if finalSolution.getTravelledDistance() <= self.__lessDistance:
				self.__lessDistance = finalSolution.getTravelledDistance()
				self.__solutions.append(finalSolution)
				print(finalSolution)
		else:
			for city in self.__problem.getCities():
				if city not in path:
					newPath = path + city

					if newPath.getTravelledDistance() < self.__lessDistance:
						self.__backtrack(newPath)

	def resolve(self, baseCase = True):
		self.__lessDistance = float('inf')
		self.__solutions = []
		if baseCase: self.__baseCase()
		self.__backtrack(
			Path([self.__problem.getStart()], 0)
		)

		bestSolutions = list(filter(lambda path: path.getTravelledDistance() == self.__lessDistance, self.__solutions))

		return bestSolutions
