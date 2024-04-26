"""
Actividad 5

Ejercicio Nº 5

Los vértices del siguiente Dígrafo representan ciudades (Almafuerte, Belén, Córdoba, Dar-el-Salam, Estambul y Finisterre) y las aristas indican si existe una ruta aérea entre ellas.

Implemente un algoritmo para averiguar cuál sería la forma en la que una persona podría viajar de una a otra pasando por la menor cantidad de ciudades intermedias posibles.
"""
from DiGrafoSecuencial import DiGrafoSecuencial

ciudades = {
    'A': 'Almafuerte',
    'B': 'Belén',
    'C': 'Córdoba',
    'D': 'Dar-el-Salam',
    'E': 'Estambul',
    'F': 'Finisterre'
}

if __name__ == '__main__':
    nodos = ['A', 'B', 'C', 'D', 'E', 'F']
    adyacencias = [('A', 'D'), ('B', 'C'), ('B', 'D'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]

    grafo = DiGrafoSecuencial(nodos, adyacencias)

    def getCamino(inicio, fin):
        try:
            camino = grafo.caminoMinimo(inicio, fin)

            return ' -> '.join([ciudades[ciudad] for ciudad in camino])
        except:
            return 'No existe camino'

    for nodo1 in nodos:
        print()
        for nodo2 in nodos:
            if nodo1 != nodo2:
                print(f'El camino más corto de {ciudades[nodo1]} a {ciudades[nodo2]} es: {getCamino(nodo1, nodo2)}')

    grafo.graficar(nodos, adyacencias)
