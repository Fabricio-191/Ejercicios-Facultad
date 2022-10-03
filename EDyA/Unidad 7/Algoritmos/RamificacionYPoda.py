from Path import Path
from Algoritmos.Base import Base

class RamificacionYPoda(Base):
	def _process(self, path: Path):
		self._graph(path)
		if path.length() == len(self._problem.getCities()):
			finalPath = path + self._problem.getStart()

			if finalPath.getTravelledDistance() < self._lessDistance:
				self._graph(finalPath)
				self._lessDistance = finalPath.getTravelledDistance()
				self._solution = finalPath
		elif path.getTravelledDistance() < self._lessDistance:
			for city in self._problem.getCities():
				if city not in path:
					self._process(path + city)