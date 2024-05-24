import pygad # pip3 install pygad==2.19.2
import random
import math
import matplotlib.pyplot as plt
import csv

dirname = 'D:/Programacion/Ejercicios-Facultad/4to año/IA/Practico/Ejercicio 4'

CITIES_QTY = 100
distances = {}

with open(f'{dirname}/DIST100.TXT', 'r') as file:
	data = file.read().strip().split('\n')
	for line in data:
		line = line.strip().split()[1:]
		ciudadA = int(line[0])
		ciudadB = int(line[1])
		distancia = float(line[2])
		distances[(ciudadA - 1, ciudadB - 1)] = distancia
		distances[(ciudadB - 1, ciudadA - 1)] = distancia


def path_distance(path):
	# if len(set(path)) != len(path): raise ValueError("Path has repeated cities")

	distance = 0
	for i in range(CITIES_QTY - 1):
		distance += distances[(path[i], path[i+1])]
	distance += distances[(path[-1], path[0])]

	return distance

def path_of_nearest_cities():
	path = [0]
	not_visited = list(range(1, CITIES_QTY))
	
	for _ in range(CITIES_QTY - 1):
		not_visited.sort(key=lambda x: distances[(path[-1], x)])
		path.append(not_visited.pop(0))

	return path

initial_solution = list(range(CITIES_QTY))
# initial_solution = path_of_nearest_cities()

print(initial_solution)

def on_generation(ga_instance):
	# This function is called after each generation of the genetic algorithm
	# You can use it to track progress or print debug information
	# if istance has repeated genes then raise an exception

	try: 
		# Get the best solution from the current generation
		best_solution, best_solution_fitness, best_solution_idx = ga_instance.best_solution()

		# Print the generation number, best fitness score, and best solution
		print(f"Generation: {ga_instance.generations_completed}, Best fitness: {int(1 / best_solution_fitness)}")
	except Exception as e:
		print(f"Error in on_generation function: {e}")
		raise e

"""
num_parents_mating, crossover_probability, mutation_probability, mutation_type, crossover_type
59581.33999999999,1.678377827689005e-05,30,0.3,0.01,inversion,single_point
59581.33999999999,1.678377827689005e-05,30,0.3,0.2,inversion,single_point
59581.33999999999,1.678377827689005e-05,30,0.3,0.4,inversion,single_point
59581.33999999999,1.678377827689005e-05,30,0.3,0.3,inversion,single_point
59581.33999999999,1.678377827689005e-05,30,0.3,0.1,inversion,single_point
59581.33999999999,1.678377827689005e-05,30,0.3,0.05,inversion,single_point
"""

population_size = 300
ga = pygad.GA(
	gene_space=range(0, CITIES_QTY),
	fitness_func=lambda solution, solution_idx: 1 / path_distance(solution),
	gene_type=int,
	
	# num_genes=CITIES_QTY,
	initial_population=[initial_solution] * population_size,
	num_generations=300,
	
	# Selecciona los padres
	parent_selection_type="sss", # random, rank, tournament, rws, sss 

	num_parents_mating=int(population_size * 0.05),
	keep_parents=0,
	keep_elitism=max(int(population_size * 0.005), 1),

	# Intercambia genes entre poblaciones
	crossover_type="single_point", # single_point, two_points, uniform, scattered
	crossover_probability=0.5,

	# Mete cambios aleatorios en los genes de una poblacion
	mutation_type="swap", # random, swap, inversion, scramble, adaptive
	mutation_probability=0.1,

	suppress_warnings=True,
	allow_duplicate_genes=False,
	random_seed=0,

	on_generation=on_generation,
)

ga.run()

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

# print(ga.summary())

# ga.plot_fitness()
# ga.plot_genes()
# ga.plot_new_solution_rate()

"""
	num_generations: Number of generations.
	num_parents_mating: Number of solutions to be selected as parents.

	initial_population
	sol_per_pop: Number of solutions (i.e. chromosomes) within the population. This parameter has no action if initial_population parameter exists.

	init_range_low=-4
	init_range_high=4

	parent_selection_type="sss"

	keep_parents=-1
	keep_elitism=1
	K_tournament=3
	
	crossover_type="single_point"
	crossover_probability=None

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

	stop_criteria=None
"""


"""
[ 0 24 77  1 17 46 40 12 28 25 37 15 36 76 56 41 33 67  7 94 86 93 38 45
 74 60 82 62 66 21 18 23 83 70 89 81  6 78 85 98 35 97 14 16 73 71 26 44
 54  8 30 96 49  1 17 46 40 12 87  4  9 99 59 31 90 61 65 58 52 91 13 10
 53 95  3 34 55 79 47 72 22 27  5 32 29 43 80 57 48 11 50 84 69 51 73 71
 26 44 54  8] 4.5875810510882196e-05 0
21797.980000000003
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