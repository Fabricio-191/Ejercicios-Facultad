import pandas
import scipy.stats as st 
import matplotlib.pyplot as plt
import seaborn
import os
import numpy



alpha = 0.01
fig, axs = plt.subplots(2, 2)


dataframe = pandas.read_csv(os.path.dirname(__file__) + '/PesoAltura.csv') # .head(200)


print()
print('Test de independencia: ')
print('H0: la altura y el peso son independientes')
print('H1: la altura y el peso no son independientes')

# test de independencia usando el coeficiente de correlacion de Spearman usando 5 intervalos de igual tamaño
contingency_table = pandas.crosstab(
	pandas.cut(dataframe.altura, bins = 5, labels = ['Muy bajo', 'Bajo', 'Normal', 'Alto', 'Muy alto']),
	pandas.cut(dataframe.peso, bins = 5, labels = ['Muy bajo', 'Bajo', 'Normal', 'Alto', 'Muy alto'])
)
result = st.chi2_contingency(contingency_table)
print( 'No se rechaza H0' if result[1] > alpha else 'Se rechaza H0') # type: ignore

# test de independencia usando el coeficiente de correlacion de Pearson
result = st.pearsonr(dataframe.altura, dataframe.peso) # Averiguar que hace
print("Pearson's: " + 'No se rechaza H0' if result[1] > alpha else 'Se rechaza H0') # type: ignore

# test de independencia usando el coeficiente de correlacion de Spearman usando intervalos de 1 en 1
contingency_table = pandas.crosstab(dataframe.altura.astype(int), dataframe.peso.astype(int))
result = st.chi2_contingency(contingency_table)
print('No se rechaza H0' if result[1] > alpha else 'Se rechaza H0') # type: ignore
print()

contingency_table = pandas.crosstab(
	pandas.cut(dataframe.altura, bins = 5, labels = ['Muy bajo', 'Bajo', 'Normal', 'Alto', 'Muy alto']),
	pandas.cut(dataframe.peso,   bins = 5, labels = ['Muy bajo', 'Bajo', 'Normal', 'Alto', 'Muy alto'])
)
seaborn.heatmap(contingency_table, ax=axs[0, 0], robust=True).invert_yaxis()

contingency_table = pandas.crosstab(
	dataframe.altura.astype(int),
	dataframe.peso.astype(int)
)
seaborn.heatmap(contingency_table, ax=axs[0, 1], robust=True).invert_yaxis()


dataframe = pandas.DataFrame({
	# round to two decimals
	'altura': numpy.round_(st.norm.rvs(172.7, 4.83, 25000), 2), # type: ignore
	'peso': numpy.round_(st.norm.rvs(57.64, 5.3, 25000), 2) # type: ignore
})


contingency_table = pandas.crosstab(
	pandas.cut(dataframe.altura, bins = 5, labels = ['Muy bajo', 'Bajo', 'Normal', 'Alto', 'Muy alto']),
	pandas.cut(dataframe.peso,   bins = 5, labels = ['Muy bajo', 'Bajo', 'Normal', 'Alto', 'Muy alto'])
)
seaborn.heatmap(contingency_table, ax=axs[1, 0], robust=True).invert_yaxis()

contingency_table = pandas.crosstab(
	dataframe.altura.astype(int),
	dataframe.peso.astype(int)
)
seaborn.heatmap(contingency_table, ax=axs[1, 1], robust=True).invert_yaxis()

plt.show()
