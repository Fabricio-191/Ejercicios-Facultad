import pygad # pip3 install pygad==2.19.2
import random
import matplotlib.pyplot as plt

# Ejercicio 4.2) (0,8P) Sea el problema del viajante de comercio: Resolverlo aplicando AG y TS para el ejemplo de cien ciudades que 
# se adjunta en DIST100.txt. Aquí se propone recorrer las cien ciudades partiendo de la inicial y volviendo a la misma.   La distancia 
# óptima está en alrededor de 25.000 Km. Implementarlo de tal forma que de cada 10 corridas en 7 la distancia obtenida esté por debajo 
# de los 30000 Km.  

dirname = 'D:/Programacion/Ejercicios-Facultad/4to año/IA/Practico/Ejercicio 4'

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

print(CITIES)

initial_solution = 3
if initial_solution == 1:
	initial_population = [list(range(1, CITIES_QTY))] * population_size
elif initial_solution == 2:
	initial_population = [random.sample(range(1, CITIES_QTY), CITIES_QTY - 1) for _ in range(population_size)]
elif initial_solution == 3:
	path = [0]
	not_visited = list(range(1, CITIES_QTY))
	
	for _ in range(CITIES_QTY - 1):
		not_visited.sort(key=lambda x: distances[(path[-1], x)])
		path.append(not_visited.pop(0))

	path.pop(0)

	initial_population = [path] * population_size
elif initial_solution == 4:
	string = """24 77  1 17 46 40 12 28 25 37 15 36 76 56 41 33 67  7 94 86 93 38 45 74
 60 82 62 66 21 18 23 83 70 89 81  6 78 85 98 35 97 14 16 73 71 26 44 54
  8 30 96 49 42 19 20 39  2 68 64 75 31 90 51 69 84 50 11 48 57 80 43 29
 32  5 27 22 72 47 79 55 34  3 95 53 10 13 91 52 58 65 61 59 92 63 99  4
  9 88 87"""
	intital_solution = [int(x) for x in string.split()]
	initial_population = [intital_solution] * population_size

print(initial_population[0])

def path_distance(path):
	if len(set(path)) != len(path): raise ValueError("Path has repeated cities")
	if len(path) != 99: raise ValueError("Path has wrong length")

	distance = distances[(0, path[0])]
	for i in range(len(path) - 1):
		distance += distances[(path[i], path[i+1])]

	distance += distances[(path[-1], 0)]

	return distance

def on_generation(ga_instance):
	best_solution, best_solution_fitness, best_solution_idx = ga_instance.best_solution()

	print(f"Generation: {ga_instance.generations_completed}, Best fitness: {int(1 / best_solution_fitness)}")


ga = pygad.GA(
	gene_space=range(1, CITIES_QTY),
	fitness_func=lambda solution, _: 1 / path_distance(solution),
	gene_type=int,
	
	# num_genes=CITIES_QTY,
	initial_population=initial_population,
	num_generations=1,
	
	# Selecciona los padres
	parent_selection_type="rank", # random, rank, tournament, rws, sss 
	# K_tournament=3

	num_parents_mating=10,
	keep_parents=0,
	keep_elitism=1,

	# Intercambia genes entre poblaciones
	crossover_type="two_points", # single_point, two_points, uniform, scattered
	crossover_probability=0.3,

	# Mete cambios aleatorios en los genes de una poblacion
	mutation_type="inversion", # random, swap, inversion, scramble
	mutation_probability=0.1,

	suppress_warnings=True,
	allow_duplicate_genes=False,
	random_seed=0,

	on_generation=on_generation,
	# stop_criteria="saturate_20"
)

ga.run()


best_solution, best_solution_fitness, best_solution_idx = ga.best_solution()

print("Mejor solucion encontrada:")
print(1 / best_solution_fitness, best_solution)

# print(ga.summary())

# ga.plot_fitness()
# ga.plot_genes()
# ga.plot_new_solution_rate()

# make a plot of the cities and best path

plt.figure()
print(CITIES[0])
plt.scatter(*zip(*CITIES), c='r')
x = [CITIES[0][0]] + [CITIES[i][0] for i in best_solution] + [CITIES[0][0]]
y = [CITIES[0][1]] + [CITIES[i][1] for i in best_solution] + [CITIES[0][1]]
plt.plot(x, y, c='b')

plt.show()


"""
{
  num_parents_mating: { '30': 108, '50': 138, '100': 12 },
  crossover_probability: { '0.3': 54, '0.4': 30, '0.5': 54, '0.6': 36, '0.7': 48, '0.8': 36},
  crossover_type: { two_points: 84, single_point: 90, scattered: 42, uniform: 42 }
  mutation_probability: {
    '0.2': 43,
    '0.1': 43,
    '0.4': 43,
    '0.3': 43,
    '0.05': 43,
    '0.01': 43
  },
  mutation_type: { swap: 198, inversion: 60 },
}
"""

"""
	mutation_type="random"
	mutation_probability=None
	mutation_by_replacement=False
	mutation_percent_genes="default"

	mutation_num_genes=None: Number of genes to mutate which defaults to None meaning that no number is specified. The mutation_num_genes parameter has no action if the parameter mutation_probability exists. Starting from PyGAD 2.2.2 and higher, this parameter has no action if mutation_type is None.

	random_mutation_min_val=-1.0
	random_mutation_max_val=1.0

	on_start=None
	on_fitness=None
	on_parents=None
	on_crossover=None
	on_mutation=None
	on_generation=None
	on_stop=None

	save_best_solutions=False
	save_solutions=False
"""


"""
24860.640000000003 [92 19 42 49 96 30  8 54 44 26 71 73 16 14 97 35 98 85 78  6 81 89 70 83        
 23 18 21 66 62 82 60 74 45 38 93 86 94  7 67 33 41 56 76 36 15 37 25 77
 24  0 46 17  1 28 12 40 63 88 87  4  9 99 59 90 31 61 65 58 52 91 13 10
 53 95  3 34 55 79 47 72 22 27  5 32 29 43 80 57 48 11 50 84 69 51 75 64
 68  2 39 20]
"""

"""
	# num_genes=CITIES_QTY,
	initial_population=[initial_solution] * 4000,
	num_generations=30,
	
	# Selecciona los padres
	parent_selection_type="rank", # random, rank, tournament, rws, sss 

	num_parents_mating=100,
	keep_parents=0,
	keep_elitism=3,

	# Mete cambios aleatorios en los genes de una poblacion
	mutation_type="inversion", # random, swap, inversion, scramble, adaptive
	mutation_probability=0.3,

	# Intercambia genes entre poblaciones
	crossover_type="single_point", # single_point, two_points, uniform, scattered
	crossover_probability=0.1,
"""


"""

population_size = 5000
ga = pygad.GA(
	gene_space=range(0, CITIES_QTY),
	fitness_func=lambda solution, solution_idx: 1 / path_distance(solution),
	gene_type=int,
	
	# num_genes=CITIES_QTY,
	initial_population=[initial_solution] * population_size,
	num_generations=30,
	
	# Selecciona los padres
	parent_selection_type="rank", # random, rank, tournament, rws, sss 

	num_parents_mating=int(population_size * 0.05),
	keep_parents=0,
	keep_elitism=max(int(population_size * 0.005), 1),

	# Intercambia genes entre poblaciones
	crossover_type="single_point", # single_point, two_points, uniform, scattered
	crossover_probability=0.3,

	# Mete cambios aleatorios en los genes de una poblacion
	mutation_type="swap", # random, swap, inversion, scramble, adaptive
	mutation_probability=0.05,

	suppress_warnings=True,
	allow_duplicate_genes=False,
	random_seed=0,

	on_generation=on_generation,
)
"""