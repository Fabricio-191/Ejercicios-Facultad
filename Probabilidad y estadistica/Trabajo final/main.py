import pandas as pd
import scipy.stats as st 
import matplotlib.pyplot as plt
import math 
import seaborn as sb
import os
import numpy as np

__dirname = os.path.dirname(__file__) + '/'

# cdf: cumulative distribution function (area under the curve) (number -> probability)
# ppf: percent point function (inverse of cdf — percentiles) (probability -> number)
# pdf: probability density function (not cumulative)

alpha = 0.05

key1 = 'altura'
key2 = 'peso'
dataframe = pd.read_csv(__dirname + 'PesoAltura.csv') [[key1, key2]] # .head(200) 


size = len(dataframe)
k = round(3.3 * math.log10(size) + 1)

mean = dataframe.mean()
std = dataframe.std()
var = dataframe.var()
max_value = dataframe.max()
min_value = dataframe.min()


# mostrar datos
padding_size = 15
significant_numbers = 3
def a(x, padding = True):
	if type(x) == np.float64:
		x = round(x, significant_numbers)

	return str(x).ljust(padding_size) if padding else str(x)

print()
print('Tamaño de la muestra:     ', size)
print('Cantidad de intervalos:   ', k   )
print()
print('                      ', a(key1)                             , a(key2)                             )
print('Media:                ', a(mean[key1])                       , a(mean[key2])                       )
print('Mediana:              ', a(dataframe.median()[key1])         , a(dataframe.median()[key2])         )
print('Moda:                 ', a(dataframe.mode()[key1][0])        , a(dataframe.mode()[key2][0])        )
print('Desviacion estandar:  ', a(std[key1])                        , a(std[key2])                        )
print('Maximo:               ', a(max_value[key1])                  , a(max_value[key2])                  )
print('Minimo:               ', a(min_value[key1])                  , a(min_value[key2])                  )
print('Rango:                ', a(max_value[key1] - min_value[key1]), a(max_value[key2] - min_value[key2]))
print('Coef. de variacion:   ', a(std[key1] / mean[key1])           , a(std[key2] / mean[key2])           )
print('Coef. de asimetria:   ', a(dataframe.skew()[key1])           , a(dataframe.skew()[key2])           )
print('Coef. de curtosis:    ', a(dataframe.kurtosis()[key1])       , a(dataframe.kurtosis()[key2])       )
print('P - 0.25:             ', a(dataframe.quantile(0.25)[key1])   , a(dataframe.quantile(0.25)[key2])   )
print('P - 0.50:             ', a(dataframe.quantile(0.5)[key1])    , a(dataframe.quantile(0.5)[key2])    )
print('P - 0.75:             ', a(dataframe.quantile(0.75)[key1])   , a(dataframe.quantile(0.75)[key2])   )
print()
print('Coeficiente de correlacion: ', a(dataframe.corr()[key1][key2]))
print()



# crear los intervalos
interval_size = (max_value[key1] - min_value[key1]) / k
intervals = []
for i in range(k + 1):
	left = min_value[key1] + i * interval_size
	right = left + interval_size

	intervals.append({
		'left': left,
		'right': right,
		'observed': len(dataframe[dataframe[key1].between(left, right, inclusive='left')]) # left <= num < right
	})

# agregar el valor maximo al ultimo intervalo
intervals[k - 1] = {
	'left': intervals[k - 1]['left'],
	'right': max_value[key1],
	'observed': intervals[k - 1]['observed'] + 1
}

observed = [intervals[i]['observed'] for i in range(k)]



print('Test de bondad de ajuste con distribucion normal:')
print('H0: sigue una distribucion normal')
print('H1: no sigue una distribucion normal')

normal_test = st.normaltest(dataframe[key1])

if normal_test.pvalue > alpha:
	print('No se rechaza H0')
else:
	print('Se rechaza H0')

print()



def mean_test(dataframe, mean0, direccion = 'two-sided'):
	result = st.ttest_1samp(dataframe, mean0, alternative=direccion)

	# return (result.pvalue <= alpha, result)
	if result.pvalue <= alpha: # type: ignore
		return 'Se rechaza H0'
	else:
		return 'No se rechaza H0'

print('Test de hipotesis para la media: ')
print('H0: media = 60, H1: media < 60   ', mean_test(dataframe[key1], 60, "less"))
print('H0: media = 20, H1: media > 20   ', mean_test(dataframe[key1], 20, "greater"))
print('H0: media = 45, H1: media != 45  ', mean_test(dataframe[key1], 45))

print()



def variance_test(var0, direccion = "two-sided"):
	vp = (size - 1) * var[key1] / var0

	if direccion == "less":
		ec = st.chi2.ppf(alpha, size - 1)
		p_value = st.chi2.cdf(vp, size - 1)
	
		# return (vp < ec, { 'vp': vp, 'ec': ec, 'p_value': p_value })
		if vp < ec:
			return 'Se rechaza H0'
	elif direccion == "greater":
		ec = st.chi2.ppf(1 - alpha, size - 1)
		p_value = 1 - st.chi2.cdf(vp, size - 1)
		
		# return (vp > ec, { 'vp': vp, 'ec': ec, 'p_value': p_value })
		if vp > ec:
			return 'Se rechaza H0'
	elif direccion == "two-sided":
		ec_left = st.chi2.ppf(alpha / 2, size - 1)
		ec_right = st.chi2.ppf(1 - (alpha / 2), size - 1)
		p_izq = st.chi2.cdf(vp, size - 1)
		p_der = 1 - st.chi2.cdf(vp, size - 1)
		p_value = 2 * min(p_der, p_izq) # type: ignore
		
		# return (vp < ec_left or vp > ec_right, { 'vp': vp, 'ec_left': ec_left, 'ec_right': ec_right, 'p_value': p_value })
		if vp < ec_left or vp > ec_right:
			return 'Se rechaza H0'
	else:
		raise Exception("Direccion no valida")
	
	return 'No se rechaza H0'

print('Test de hipotesis para la varianza: ')
print('H0: var = 20, H1: var < 20     ', variance_test(20, "less"))
print('H0: var = 10, H1: var > 10     ', variance_test(10, "greater"))
print('H0: var = 15, H1: var != 15    ', variance_test(15))

print()



print('Intervalos de confianza: ')
t = st.t.ppf(1 - alpha / 2, size - 1)
err = t * std[key1] / math.sqrt(size)
print(
	'Intervalo de confianza para la media (varianza desconocida): ({}, {})'
    .format(a(mean[key1] - err, False), a(mean[key1] + err, False))
)

# interval = st.t.interval(1 - alpha, size - 1)
# err_left = interval[0] * std[key1] / math.sqrt(size)
# err_right = interval[1] * std[key1] / math.sqrt(size)
# print('Confidence interval for the mean (unknown variance): ', mean[key1] + err_left, mean[key1] + err_right)

interval = st.chi2.interval(1 - alpha, size - 1)
left = (size - 1) * std[key1] ** 2 / interval[1]
right = (size - 1) * std[key1] ** 2 / interval[0]
print('Intervalo de confianza para la varianza: ({}, {})'.format(a(left, False), a(right, False)))

# chi_square_left = st.chi2.ppf(1 - alpha / 2, size - 1)
# chi_square_right = st.chi2.ppf(alpha / 2, size - 1)
# left = (size - 1) * std[key1] ** 2 / chi_square_left
# right = (size - 1) * std[key1] ** 2 / chi_square_right
# print('Confidence interval for the variance: ', left, right)

print()



print('Test de independencia: ')
print('H0: la altura y el peso son independientes')
print('H1: la altura y el peso no son independientes')


if os.path.exists(__dirname + 'contingency_table.xlsx'):
	os.remove(__dirname + 'contingency_table.xlsx')

contingency_table = pd.crosstab(dataframe[key2].astype(int), dataframe[key1].astype(int))
contingency_table.to_excel(__dirname + 'contingency_table.xlsx')

result = st.chi2_contingency(contingency_table)

if result.pvalue > alpha:  # type: ignore
	print('No se rechaza H0')
else:
	print('Se rechaza H0')



print()

# regresion lineal
result = st.linregress([dataframe[key1], dataframe[key2]])
y_hat = result.slope * dataframe[key1] + result.intercept # type: ignore



# plot everything with subplots
fig, axs = plt.subplots(2, 2)


axs[0, 0].set_title('Histograma')
axs[0, 0].hist(dataframe[key1], bins = k, color = 'blue', edgecolor = 'black', alpha = 0.5)

x = np.linspace(min_value[key1], max_value[key1], 1000)
y = st.norm.pdf(x, mean[key1], std[key1]) * size * interval_size
axs[0, 0].plot(x, y, color = 'red', label = 'Distribucion normal')


axs[0, 1].set_title('Regresion lineal')
axs[0, 1].scatter(dataframe[key1], dataframe[key2], s = 0.1)
axs[0, 1].plot(dataframe[key1], y_hat, color = 'red')


axs[1, 0].set_title('Intervalos de confianza para la media (hacer zoom)')
axs[1, 0].scatter(dataframe.index, dataframe[key1], s = 0.1)
axs[1, 0].plot(dataframe.index, [mean[key1]] * size, color = 'red', label = 'Media')
axs[1, 0].plot(dataframe.index, [mean[key1] + err] * size, color = 'green', label = 'Media + error')
axs[1, 0].plot(dataframe.index, [mean[key1] - err] * size, color = 'green', label = 'Media - error')


axs[1, 1].set_title('Test de independencia')
sb.heatmap(contingency_table, ax=axs[1, 1], robust=True).invert_yaxis()


plt.show()
