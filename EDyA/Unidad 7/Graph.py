import matplotlib.pyplot as plt
from Path import Path, City

"""
https://upload.wikimedia.org/wikipedia/commons/2/2b/Bruteforce.gif
https://medium.com/analytics-vidhya/editing-data-visualization-in-python-64f42225ba21
https://pythonprogramming.net/python-matplotlib-live-updating-graphs/
https://stackoverflow.com/questions/39658717/plot-dynamically-changing-graph-using-matplotlib-in-jupyter-notebook
https://www.geeksforgeeks.org/change-plot-size-in-matplotlib-python/
https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
https://stackoverflow.com/questions/8595973/truncate-to-three-decimals-in-python
"""

class Graph: # to-do
	__cities: list[City]
	__soluciones: int
	__mejoresSoluciones: int

	def __init__(self, cities: list[City]):
		self.__soluciones = 0
		self.__mejoresSoluciones = 0
		self.__cities = cities
		self.__currentPathPlot = plt.subplot2grid((2, 4), (0, 0), 2, 2)
		self.__currentBestPathPlot = plt.subplot2grid((2, 4), (0, 2), 2, 2)

		self.__currentPathPlot.set_title("Current path")
		self.__currentBestPathPlot.set_title("Current best path")

		for city in cities:
			self.__currentPathPlot.plot(*city.getCoordinates(), 'bo')
			self.__currentBestPathPlot.plot(*city.getCoordinates(), 'bo')

		plt.tight_layout()
		plt.show()
	
	def updateCurrentPath(self, path: Path):
		self.__soluciones += 1
		plot = self.__currentPathPlot
		plot.clear()
		
		plt.suptitle('Distancia: {:.2f}'.format(path.getTravelledDistance()))
		for city in self.__cities:
			plot.plot(*city.getCoordinates(), 'ro')

		x = []
		y = []

		for city in path.getCities():
			coords = city.getCoordinates()
			x.append(coords[0])
			y.append(coords[1])

		plot.plot(x, y, 'r-')
		plt.show()

	def updateCurrentBestPath(self, path: Path):
		self.__mejoresSoluciones += 1
		plot = self.__currentPathPlot
		plot.clear()
		
		plt.suptitle('Distancia: {:.2f}'.format(path.getTravelledDistance()))
		for city in self.__cities:
			plot.plot(*city.getCoordinates(), 'ro')

		x = []
		y = []

		for city in path.getCities():
			coords = city.getCoordinates()
			x.append(coords[0])
			y.append(coords[1])

		plot.plot(x, y, 'r-')
		plt.show()

def staticGraph(cities: list[City], path: Path):
	fig = plt.figure()
	plot = fig.add_subplot(111)
	plot.set_title("Best path")

	for city in cities:
		plot.plot(*city.getCoordinates(), 'bo')

	x = []
	y = []

	for city in path.getCities():
		coords = city.getCoordinates()
		x.append(coords[0])
		y.append(coords[1])

	plot.plot(x, y, 'r-')
	plt.show()

if __name__ == '__main__':
	Graph([City(0, 0), City(1, 1), City(2, 2)])