"""
Ejercicio Nº 3

Dada la siguiente Narrativa:

a) Elija el TAD adecuado
b) Construya un algoritmo que resuelva la problemática planteada

La Compañía de Líneas Telefónicas (CLT) está por instalar un cableado telefónico nuevo.

Están conectando varios sitios, los cuales están numerados de 1 a n. Dos sitios nunca comparten un mismo número. Las líneas son bidireccionales, y cada línea une a dos sitios.

En cada sitio, al final de la línea hay un solo teléfono. Siempre es posible marcar de un teléfono a otro, aunque no siempre a través de una conexión directa (puede pasar por varios sitios). En ocasiones, a un sitio le falla el suministro eléctrico y ya no puede conectar.

Los directivos de CLT se han dado cuenta que puede pasar que no solo ese sitio quede inalcanzable, sino que puede causar que otros sitios también lo sean. En estos casos, decimos que el sitio (donde ocurrió el fallo) es crítico. Ahora los directivos quieren contar con un programa que encuentre la cantidad de sitios críticos.
"""

from GrafoSecuencial import GrafoSecuencial


if __name__ == '__main__':
    """
    N = int(input('Ingrese la cantidad de sitios: '))
    nodos = [str(i) for i in range(1, N + 1)]
    adyacencias = []

    print('Ingrese las conexiones entre los sitios formato "1 2": ')
    while True:
        linea = input('Ingrese una línea (o ingrese "fin" para terminar): ')
        if linea == 'fin':
            break

        adyacencias.append(tuple(linea.split()))
    """
    nodos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    adyacencias = [('1', '2'), ('1', '3'), ('1', '4'), ('2', '5'), ('2', '6'), ('3', '7'), ('3', '8'), ('4', '9'), ('4', '10')]

    grafo = GrafoSecuencial(nodos, adyacencias)
    print(grafo.esConexo())

    sitiosCriticos = []
    for nodo in nodos:
        nuevosNodos = nodos.copy()
        nuevosNodos.remove(nodo)

        nuevosAdyacencias = [adyacencia for adyacencia in adyacencias if nodo not in adyacencia]

        subGrafo = GrafoSecuencial(nuevosNodos, nuevosAdyacencias)
        if not subGrafo.esConexo():
            sitiosCriticos.append(nodo)

    print('Sitios críticos: ')
    print(sitiosCriticos)
    print(f'Cantidad de sitios críticos: {len(sitiosCriticos)}')

    grafo.graficar(nodos, adyacencias)
    
