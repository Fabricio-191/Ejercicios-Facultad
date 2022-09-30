import matplotlib.pyplot as plt
from TravellingSalesman import Path
from itertools import cycle

colors = cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])

def Graph(data, solution: Path):
	plt.xlabel('Eje x')
	plt.ylabel('Eje y')
	
	plt.title('Grafo de ciudades')
	plt.suptitle('Distancia: {:.2f}'.format(solution.getTravelledDistance()))

	for city in data['cities']:
		plt.plot(city['x'], city['y'], 'ro')

	x = []
	y = []

	for city in solution.getCities():
		coords = city.getCoordinates()
		x.append(coords[0])
		y.append(coords[1])

	plt.plot(x, y, colors.__next__())
	plt.show()