from TravellingSalesman import TravellingSalesman
from Graph import Graph
from Algoritmos.RamificacionYPoda import RamificacionYPoda
from Algoritmos.BruteForce import BruteForce

if __name__ == '__main__':
	cities = TravellingSalesman.generateCities(7)
	print(len(cities), cities)

	tsp = TravellingSalesman(cities, cities[0])
	tsp.setGraph(Graph(tsp.getCities()))

	bestSolutions = RamificacionYPoda(tsp).resolve()
	print('Mejor solución:', bestSolutions[0])
	input('Presione enter para continuar...')	

# [(64, 46), (38, 36), (0, 74), (95, 65), (19, 13), (3, 12), (91, 10), (78, 74), (45, 50), (58, 70)]