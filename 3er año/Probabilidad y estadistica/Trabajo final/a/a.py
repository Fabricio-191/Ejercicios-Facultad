import pandas
import scipy.stats as st 
import matplotlib.pyplot as plt
import seaborn
import os
import math 
import numpy

print(os.path.dirname(__file__))

# read all files in the directory
for file in os.listdir(os.path.dirname(__file__) + '\\csvs'):
	if not file.endswith('.csv'): continue
	print(file)

	dataframe = pandas.read_csv(os.path.dirname(__file__) + '\\csvs\\' + file)
	dataframe = dataframe.dropna()

	# Eliminar columnas no numericas
	for i in dataframe.columns:
		if not numpy.issubdtype(dataframe[i].dtype, numpy.number):
			dataframe = dataframe.drop(i, axis=1)

	# print(dataframe.head())

	# Test de normalidad
	variables_normales = []
	for i in dataframe.columns:
		result = st.shapiro(dataframe[i])
		if result.pvalue > 0.001:
			variables_normales.append((i, "%.3f" % result.pvalue))

	variables_con_regresion = []
	# Test de independencia
	for i in dataframe.columns:
		for j in dataframe.columns:
			if i == j: continue
			
			result = st.linregress(dataframe[i], dataframe[j])
			if result.pvalue > 0.1: 
				variables_con_regresion.append((i, j, "%.3f" % result.pvalue))
    
    
    
	print('Variables normales:', variables_normales)
	print('Variables con regresion:', variables_con_regresion)
	print('')