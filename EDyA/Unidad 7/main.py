from TravellingSalesman import TravellingSalesman
from Graph import staticGraph
from math import factorial

if __name__ == '__main__':
	cities = TravellingSalesman.generateCities(12)
	print('Caminos posibles: ', factorial(len(cities) - 1) / 2)
	print('Ciudades: ', cities)

	tsp = TravellingSalesman(cities)

	solution = tsp.resolve(cities[0], baseCase=True, graph=False)
	print('Mejor solución:', solution)
	staticGraph(solution)

# [(99, 17), (28, 39), (18, 83), (71, 28), (53, 57), (31, 83), (84, 62), (81, 3), (66, 76), (65, 94), (24, 21), (90, 47)]
# [(64, 46), (38, 36), (0, 74), (95, 65), (19, 13), (3, 12), (91, 10), (78, 74), (45, 50), (58, 70)]
# [(1, 77), (55, 46), (50, 94), (44, 1), (15, 61), (10, 95), (95, 91)]
