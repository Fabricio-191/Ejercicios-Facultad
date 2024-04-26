"""
Ejercicio Nº 10: Generar una muestra aleatoria de tamaño 30 de una distribución exponencial de parámetro ..., cuya semilla inicial comience en 500. Se pide.
a. Determinar estimador puntual para la media y varianza de la muestra.
b. Calcular el error cuadrático medio para los estimadores encontrados en a.
"""

import pandas as pd
import scipy.stats as st

seed=500 #Semilla para la generación
n=30 # Tamaño muestral
lambda_ = 1/140

#Generación de la muestra
muestra = st.expon.rvs(lambda_, size=n,random_state=seed)

#Determinar estimador puntual para la media y varianza de la muestra.
media = muestra.mean()
varianza = muestra.var()

#Calcular el error cuadrático medio para los estimadores encontrados en a.
ecm_media = (lambda_ - media) ** 2
ecm_varianza = (lambda_** 2 - varianza) ** 2

print("Estimador puntual para la media de la muestra: ", media)
print("Estimador puntual para la varianza de la muestra: ", varianza)
print("Error cuadrático medio para el estimador de la media: ", ecm_media)
print("Error cuadrático medio para el estimador de la varianza: ", ecm_varianza)