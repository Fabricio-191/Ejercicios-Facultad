import pygad # pip3 install pygad==2.19.2
import random
import matplotlib.pyplot as plt
from os import path
dirname = path.dirname(__file__)

# Ejercicio 4.3) (0,8P) Resuelva el mismo problema anterior, pero tratando de que al partir de una ciudad y llegar a la misma en un 
# total de 5000Km recorra la mayor cantidad de ciudades. Encuentre una representación y análisis de la función objetivo que le permita 
# resolver el problema, mediante AG y ACO. Implementarlo en GAlib y ACO en la herramienta que el disponga.  

population_size = 1000

with open(f'{dirname}/DIST100a.TXT', 'r') as file:
	distances = {}

	data = file.read().strip().split('\n')
	for line in data:
		line = line.strip().split()[1:]
		ciudadA = int(line[0])
		ciudadB = int(line[1])
		distancia = float(line[2])
		distances[(ciudadA - 1, ciudadB - 1)] = distancia
		distances[(ciudadB - 1, ciudadA - 1)] = distancia

with open(f'{dirname}/DIST100.txt', 'r') as file:
	data = file.read().strip().split('\n')
	CITIES = []
	for line in data:
		x = float(line.split()[1])
		y = float(line.split()[2])
		CITIES.append((x, y))
	CITIES_QTY = len(CITIES)

gene_space = list(range(-CITIES_QTY + 2, 0)) + list(range(1, CITIES_QTY))
initial_population = []

def closest_city(city, visited):
	closer_city = -1
	min_distance = 999999999

	for i in range(0, CITIES_QTY):
		if i in visited: continue

		distance = distances[(city, i)]
		if distance < min_distance:
			closer_city = i
			min_distance = distance

	return closer_city

for i in range(0, 100): # make sequences cities next to each other
	cities = [i]
	distance = 0
	while distance < 4000:
		next_city = closest_city(cities[-1], cities)
		if next_city == -1: break
		cities.append(next_city)
		distance += distances[(cities[-2], cities[-1])]

	path = list(range(-100 + len(cities), 0))
	random_index = random.randint(0, 98)
	path = path[:random_index] + cities + path[random_index:]

	initial_population.append(path)

def path_distance(path):
	distance = distances[(0, path[0])]
	for i in range(len(path) - 1):
		if path[i] < 1 or path[i + 1] < 1: continue
		distance += distances[(path[i], path[i+1])]

	distance += distances[(path[-1], 0)]

	return distance

def fitness_func(solution):
	solution = list(filter(lambda x: x >= 0, solution))
	cities = len(solution)
	if cities < 1: return -10000

	distance = path_distance(solution)
	if distance > 5000: return -10000

	return cities / distance

def on_generation(ga_instance):
	best_solution, best_solution_fitness = ga_instance.best_solution()

	print(f"Generation: {ga_instance.generations_completed}, Best fitness: {best_solution_fitness}")

ga = pygad.GA(
	gene_space=gene_space,
	fitness_func=lambda solution, _: fitness_func(solution),
	gene_type=int,
	
	# num_genes=CITIES_QTY,
	initial_population=initial_population,
	num_generations=100,
	
	# Selecciona los padres
	parent_selection_type="rank", # random, rank, tournament, rws, sss 
	# K_tournament=3

	num_parents_mating=20,
	keep_parents=0,
	keep_elitism=1,

	# Intercambia genes entre poblaciones
	crossover_type='single_point', # single_point, two_points, uniform, scattered
	crossover_probability=0.5,

	# Mete cambios aleatorios en los genes de una poblacion
	mutation_type='inversion', # random, swap, inversion, scramble
	mutation_probability=0.1,

	suppress_warnings=True,
	allow_duplicate_genes=False,
	# random_seed=0,

	on_generation=on_generation,
	# stop_criteria="saturate_20"
)

ga.run()


best_solution, best_solution_fitness, best_solution_idx = ga.best_solution()

print("Mejor solucion encontrada:")
print(best_solution)
path = list(filter(lambda x: x >= 0, best_solution))
print(len(path), path, path_distance(path))

# print(ga.summary())

ga.plot_fitness()
# ga.plot_genes()
# ga.plot_new_solution_rate()

plt.figure()
plt.scatter(*zip(*CITIES), c='r')
x = [CITIES[0][0]] + [CITIES[i][0] for i in path] + [CITIES[0][0]]
y = [CITIES[0][1]] + [CITIES[i][1] for i in path] + [CITIES[0][1]]
plt.plot(x, y, c='b')

plt.show()
