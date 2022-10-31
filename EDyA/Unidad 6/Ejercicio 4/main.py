"""
Actividad 4

Ejercicio Nº 4

Los vértices del siguiente Dígrafo representan personas (Ana, Belén, Cecilia, Daniel, Ezequiel y Federico) y las aristas indican si una persona tiene el número de móvil de otra. El peso de una arista es el costo de enviar un SMS (por ejemplo, Ana puede enviar un SMS a Belén por 3 centavos).

Implemente un algoritmo para averiguar cuál sería la forma más barata de que una persona le haga llegar un SMS a cualquier otra.
"""

nodos = ['A', 'B', 'C', 'D', 'E', 'F']
adyacencias = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]
pesos = [('A', 'B', 3), ('A', 'D', 6), ('B', 'C', 1), ('B', 'E', 2), ('B', 'F', 1), ('C', 'D', 2), ('D', 'B', 3), ('E', 'D', 3), ('E', 'F', 2), ('F', 'D', 1), ('F', 'A', 5)]