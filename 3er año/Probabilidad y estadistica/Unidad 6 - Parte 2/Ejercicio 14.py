"""
Ejercicio N° 14: A partir de los códigos que se encuentran en la teoría (para cálculo de IC para la media y varianza, aplicarlos en los ejercicios de la práctica y verificar los resultados obtenidos).
"""

from scipy import stats # type: ignore
import math

data = {
    # Ejercicio 1
    'x': [506, 508, 499, 503, 510, 497, 512, 514, 505, 493, 496, 506, 502, 509, 496],
    'poblational_mean': None,
    'poblational_variance': 25,
}

n = len(data['x'])
alpha = 0.05

mean = sum(data['x']) / n
variance = sum([(x - mean) ** 2 for x in data['x']]) / (n - 1)

def get_confidence_interval_for_mean(data):
	t = stats.t.ppf(1 - alpha / 2, n - 1)
	err = t * math.sqrt(variance / n)

	return (mean - err, mean + err)