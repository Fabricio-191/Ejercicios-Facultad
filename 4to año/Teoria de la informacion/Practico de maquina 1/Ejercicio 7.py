"""
Desarrollar un programa para comparar dos cadenas, no en forma tradicional (carácter por carácter), sino que implemente un algoritmo, propuesto por Ud., que determine el parecido, por ejemplo de cadenas como: Juan Perez y Jaun Perez, Horacio López y Oracio López, cadenas que si se tratan en comparando carácter por carácter, son muy poco parecidas o incluso no se parecen en nada.
"""

class JaroWinkler: # nombre del algoritmo
    # Umbral para ajustar el coeficiente de Jaro-Winkler
    threshold = 0.7
    # Constante para dividir la fórmula de Jaro
    three = 3
    # Coeficiente de ajuste de Jaro-Winkler
    jw_coef = 0.1

    def similarity(self, s0, s1):
        # retorna Un valor de similitud entre 0 y 1
        # Si las cadenas son idénticas, la similitud es 1
        if s0 == s1: return 1
        
        # Obtiene los valores de coincidencias, transposiciones y prefijo
        mtp = self.matches(s0, s1)
        m = mtp[0]
        # Si no hay coincidencias, la similitud es 0
        if m == 0: return 0
        
        # Calcula la similitud Jaro
        j = (m / len(s0) + m / len(s1) + (m - mtp[1]) / m) / self.three
        jw = j
        
        # Ajusta la similitud usando el prefijo si es mayor al umbral
        if j > self.threshold:
            jw = j + min(self.jw_coef, 1.0 / mtp[self.three]) * mtp[2] * (1 - j)
            
        return jw

    @staticmethod
    def matches(s0, s1):
        """
        Encuentra las coincidencias y transposiciones entre dos cadenas.
        
        :param s0: Primera cadena a comparar.
        :param s1: Segunda cadena a comparar.
        :return: Una lista con el número de coincidencias, transposiciones, prefijo y longitud de la cadena más larga.
        """
        # Determina cuál cadena es más larga
        if len(s0) > len(s1):
            max_str, min_str = s0, s1
        else:
            max_str, min_str = s1, s0

        # Rango de búsqueda de coincidencias
        ran = max(int(len(max_str) / 2 - 1), 0)
        
        # Inicializa las listas de índices y banderas de coincidencias
        match_indexes = [-1] * len(min_str)
        match_flags = [False] * len(max_str)
        matches = 0
        # Encuentra las coincidencias
        for mi in range(len(min_str)):
            c1 = min_str[mi]
            for xi in range(max(mi - ran, 0), min(mi + ran + 1, len(max_str))):
                if not match_flags[xi] and c1 == max_str[xi]:
                    match_indexes[mi] = xi
                    match_flags[xi] = True
                    matches += 1
                    break

        # Crea las listas de coincidencias
        ms0, ms1 = [0] * matches, [0] * matches
        
        si = 0
        for i in range(len(min_str)):
            if match_indexes[i] != -1:
                ms0[si] = min_str[i]
                si += 1

        si = 0
        for j in range(len(max_str)):
            if match_flags[j]:
                ms1[si] = max_str[j]
                si += 1

        # Calcula las transposiciones
        transpositions = sum(ms0[mi] != ms1[mi] for mi in range(len(ms0)))

        # Calcula el prefijo común
        prefix = 0
        for mi in range(len(min_str)):
            if s0[mi] != s1[mi]: break
            prefix += 1
            
        return [matches, int(transpositions / 2), prefix, len(max_str)]

# Ejemplo de uso del algoritmo Jaro-Winkler
string1 = "Juan Perez"
string2 = "Jaun Perez"

print(string1, string2, JaroWinkler().similarity(string1, string2))

string1 = "Horacio López"
string2 = "Oracio López"

print(string1, string2, JaroWinkler().similarity(string1, string2))