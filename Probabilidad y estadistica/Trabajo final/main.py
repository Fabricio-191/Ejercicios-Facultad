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

key = 'Height'
dataframe = pd.read_csv(__dirname + 'PesoAltura.csv') # .head(200) 

# numero de intervalos
size = len(dataframe)
k = round(3.3 * math.log10(size) + 1)

print()
print('Descripcion de los datos: ')
print(dataframe.describe())
print('Cantidad de intervalos: ', k)
print()

mean = dataframe.mean()
std = dataframe.std()
var = dataframe.var()
max_value = dataframe.max()
min_value = dataframe.min()

# crear los intervalos
interval_size = (max_value[key] - min_value[key]) / k
intervals = []
for i in range(k + 1):
	left = min_value[key] + i * interval_size
	right = left + interval_size

	intervals.append({
		'left': left,
		'right': right,
		'observed': len(dataframe[dataframe[key].between(left, right, inclusive='left')]) # left <= num < right
	})

# agregar el valor maximo al ultimo intervalo
intervals[k - 1] = {
	'left': intervals[k - 1]['left'],
	'right': max_value[key],
	'observed': intervals[k - 1]['observed'] + 1
}

observed = [intervals[i]['observed'] for i in range(k)]



print('Test de bondad de ajuste con distribucion normal:')
print('H0: sigue una distribucion normal')
print('H1: no sigue una distribucion normal')

normal_test = st.normaltest(dataframe[key])

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
print('H0: mean = 60, H1: mean < 60   ', mean_test(dataframe[key], 60, "less"))
print('H0: mean = 20, H1: mean > 20   ', mean_test(dataframe[key], 20, "greater"))
print('H0: mean = 45, H1: mean != 45  ', mean_test(dataframe[key], 45))

print()

def variance_test(var0, direccion = "two-sided"):
	vp = (size - 1) * var[key] / var0

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
err = t * std[key] / math.sqrt(size)
print('Intervalo de confianza para la media (varianza desconocida): ({:.3f}, {:.3f})'.format(mean[key] - err, mean[key] + err))

# interval = st.t.interval(1 - alpha, size - 1)
# err_left = interval[0] * std[key] / math.sqrt(size)
# err_right = interval[1] * std[key] / math.sqrt(size)
# print('Confidence interval for the mean (unknown variance): ', mean[key] + err_left, mean[key] + err_right)

interval = st.chi2.interval(1 - alpha, size - 1)
left = (size - 1) * std[key] ** 2 / interval[1]
right = (size - 1) * std[key] ** 2 / interval[0]
print('Intervalo de confianza para la varianza: ({:.3f}, {:.3f})'.format(left, right))

# chi_square_left = st.chi2.ppf(1 - alpha / 2, size - 1)
# chi_square_right = st.chi2.ppf(alpha / 2, size - 1)
# left = (size - 1) * std[key] ** 2 / chi_square_left
# right = (size - 1) * std[key] ** 2 / chi_square_right
# print('Confidence interval for the variance: ', left, right)

print()

print('Test de independencia: ')
print('H0: la altura y el peso son independientes')
print('H1: la altura y el peso no son independientes')

contingency_table = pd.crosstab(dataframe.Weight.astype(int), dataframe.Height.astype(int), margins = True)

# guardamos la tabla de contingencia en un excel
# instalar openpyxl es necesario para que funcione (pip3 install openpyxl)

if os.path.exists(__dirname + 'contingency_table.csv'):
	os.remove(__dirname + 'contingency_table.csv')

contingency_table.to_excel(__dirname + 'contingency_table.xlsx')

result = st.chi2_contingency(contingency_table)

if result.pvalue > alpha:  # type: ignore
	print('No se rechaza H0')
else:
	print('Se rechaza H0')

print()

# regresion lineal
result = st.linregress([dataframe.Height, dataframe.Weight])
y_hat = result.slope * dataframe.Height + result.intercept # type: ignore


# plot everything with subplots
fig, axs = plt.subplots(2, 2)

# plot the histogram
axs[0, 0].set_title('Histograma')
axs[0, 0].hist(dataframe[key], bins = k, color = 'blue', edgecolor = 'black', alpha = 0.5)

x = np.linspace(min_value[key], max_value[key], 1000)
y = st.norm.pdf(x, mean[key], std[key]) * size * interval_size
axs[0, 0].plot(x, y, color = 'red', label = 'Distribucion normal')


# plot lineal regression
axs[0, 1].set_title('Regresion lineal, dispersion y tabla de contingencia')
axs[0, 1].scatter(dataframe.Height, dataframe.Weight, s=0.1)
axs[0, 1].plot(dataframe.Height, y_hat, color = 'red')

# plot mean intervals in ax[1, 0]
axs[1, 0].set_title('Intervalos de confianza para la media')
axs[1, 0].scatter(dataframe.index, dataframe[key], s=0.1)
axs[1, 0].plot(dataframe.index, [mean[key]] * size, color = 'red', label = 'Media')
axs[1, 0].plot(dataframe.index, [mean[key] + err] * size, color = 'green', label = 'Media + error')
axs[1, 0].plot(dataframe.index, [mean[key] - err] * size, color = 'green', label = 'Media - error')

plt.show()
