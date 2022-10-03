from TravellingSalesman import TravellingSalesman
from Algoritmos.RamificacionYPoda import RamificacionYPoda
from Algoritmos.BruteForce import BruteForce

if __name__ == '__main__':
	cities = [(1, 77), (55, 46), (50, 94), (44, 1), (15, 61), (10, 95), (95, 91)]
	print('Ciudades: ', cities)

	tsp = TravellingSalesman(cities, cities[0])
	# tsp.setGraph(Graph(tsp.getCities()))

	solution = RamificacionYPoda(tsp).resolve()
	print('Mejor solución:', solution)
	input('Presione enter para continuar...')	

# [(64, 46), (38, 36), (0, 74), (95, 65), (19, 13), (3, 12), (91, 10), (78, 74), (45, 50), (58, 70)]
# [(1, 77), (55, 46), (50, 94), (44, 1), (15, 61), (10, 95), (95, 91)]