# calculate entropy of information of a file
import math

max_entropy = math.log2(256)

def calc_entropy(file_path):
    # read file
    with open(file_path, "rb") as f:
        data = f.read()

    # calculate probability of each byte
    probabilities = {}
    for byte in data:
        if byte not in probabilities:
            probabilities[byte] = 0
        probabilities[byte] += 1

    # calculate entropy
    entropy = 0
    total_bytes = len(data)
    for byte in probabilities:
        prob = probabilities[byte] / total_bytes
        entropy += prob * math.log2(prob)

    entropy *= -1
    relative_entropy = entropy / max_entropy
    return entropy, relative_entropy


print(calc_entropy("D:\\Programacion\\Ejercicios-Facultad\\4to año\\Teoria de la informacion\\Practico de maquina 1\\asd\\Ejercicio 4.py"))
print(calc_entropy("D:\\Universidad\\Fabricio Rubio - Curriculum.pdf"))