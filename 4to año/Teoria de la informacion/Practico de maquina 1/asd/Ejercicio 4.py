"""
4) Mediante un programa en el lenguaje que usted prefiera, calcule la capacidad de canal teniendo en cuenta los siguientes requisitos:
a) Canales Binarios, Ternarios y Cuaternarios (Uniformes y No Uniformes) y donde la dimensión del canal (entradas) se puedan ingresar por teclado
b) Que se permitan ingresar por teclado los valores de las probabilidades hacia adelante representativas del canal.
c) Que como salida se brinde el valor de C, y el de las probabilidades de los símbolos de entrada.
"""

import math

# dimension = int(input("Ingrese la dimensión del canal: "))
# probabilidades = []
# 
# for i in range(dimension):
#     probabilidades.append([])
#     for j in range(dimension - 1):
#         prob = float(input(f"Ingrese la probabilidad del símbolo {i+1} hacia el símbolo {j+1}: "))
#         probabilidades[i].append(prob)
#     probabilidades[i].append(1 - sum(probabilidades[i]))

dimension = 3
probabilidades = [
    [0.8, 0.1, 0.1],
    [0.1, 0.8, 0.1],
    [0.1, 0.1, 0.8]
]

print(f"Las probabilidades de los símbolos de entrada son: {probabilidades}")

capacidad = 0
for i in range(dimension):
    for j in range(dimension):
        if probabilidades[i][j] != 0:
            capacidad += probabilidades[i][j] * math.log2(probabilidades[i][j])

print(f"La capacidad del canal es: {-capacidad}")

def probabilidad_simbolo(probabilidades, simbolo):
    prob = 0
    for i in range(len(probabilidades)):
        prob += probabilidades[simbolo][i]
    return prob

probabilidades_simbolos = []
for i in range(dimension):
    prob = 0
    for j in range(dimension):
        prob += probabilidades[j][i]

    probabilidades_simbolos.append(prob)

# normalizar
suma = sum(probabilidades_simbolos)
for i in range(dimension):
    probabilidades_simbolos[i] /= suma

print(f"Las probabilidades de los símbolos de entrada son: {probabilidades_simbolos}")

"""
3
0.1
0.8
0.1
0.8
0.1
0.1
"""