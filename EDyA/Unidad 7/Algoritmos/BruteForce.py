from Path import Path
from Algoritmos.Base import Base

class BruteForce(Base):
	def _process(self, path: Path):
		self._problem.registerSolution(path)
		if path.length() == len(self._problem.getCities()):
			finalPath = path + self._problem.getStart()

			if finalPath.getTravelledDistance() < self._lessDistance:
				self._problem.registerSolution(finalPath)
				self._lessDistance = finalPath.getTravelledDistance()
				self._solutions.append(finalPath)
		else:
			for city in self._problem.getCities():
				if city not in path:
					self._process(path + city)