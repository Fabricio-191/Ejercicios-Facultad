import pandas
import scipy.stats as st 
import matplotlib.pyplot as plt
import seaborn
import os
import math 
import numpy

# cdf: cumulative distribution function (area under the curve) (number -> cumulative probability)
# ppf: percent point function (inverse of cdf — percentiles) (cumulative probability -> number)

alpha = 0.00000000000001 # 99.99999999999999% de confianza
alpha = 0.01
dataframe = pandas.read_csv(os.path.dirname(__file__) + '/PesoAltura.csv') # .head(200) 


size = len(dataframe)
mean = dataframe.mean()
std = dataframe.std()
var = dataframe.var()
max_value = dataframe.max()
min_value = dataframe.min()
k = round(3.3 * math.log10(size) + 1)

# mostrar datos
print()
print('Tamaño de la muestra:     ', size)
print('Cantidad de intervalos:   ', k   )
print()
print('                      ', 'altura')
print('Media:                ', mean.altura)
print('Mediana:              ', dataframe.altura.median())
print('Moda/s:               ', ', '.join([str(i) for i in dataframe.altura.mode()]))
print('Varianza:             ', var.altura)
print('Desviacion estandar:  ', std.altura)
print('Coef. de variacion:   ', std.altura / mean.altura)
print('Maximo:               ', max_value.altura)
print('Minimo:               ', min_value.altura)
print('Rango:                ', max_value.altura - min_value.altura)
print('Coef. de asimetria:   ', dataframe.altura.skew())
print('Coef. de curtosis:    ', dataframe.altura.kurtosis())
print('P - 0.25:             ', dataframe.altura.quantile(0.25))
print('P - 0.50:             ', dataframe.altura.quantile(0.5))
print('P - 0.75:             ', dataframe.altura.quantile(0.75))
print()
print('Coeficiente de correlacion: ', dataframe.corr().altura.peso)
print()

print('Test de bondad de ajuste con distribucion normal:')
print('H0: la altura sigue una distribucion normal')
print('H1: la altura no sigue una distribucion normal')
normal_test = st.normaltest(dataframe.altura) # Averiguar que hace
print('No se rechaza H0' if normal_test.pvalue > alpha else 'Se rechaza H0')
print()

print('Intervalos de confianza para la altura: ')
interval = st.t.interval(1 - alpha, size - 1, mean.altura, std.altura / math.sqrt(size))
print('Intervalo de confianza para la media:  ({:.3f}, {:.3f})'.format(interval[0], interval[1]))

interval = st.chi2.interval(1 - alpha, size - 1)
left = ((size - 1) * var.altura) / interval[1]
right = ((size - 1) * var.altura) / interval[0]
print('Intervalo de confianza para la varianza: ({:.3f}, {:.3f})'.format(left, right))
print('Intervalo de confianza para la desviacion estandar:  ({:.3f}, {:.3f})'.format(math.sqrt(left), math.sqrt(right)))
print()


def mean_test(dataframe, mean0, direccion):
	result = st.ttest_1samp(dataframe, mean0, alternative=direccion)
	
	return 'No se rechaza H0' if result.pvalue > alpha else 'Se rechaza H0' # type: ignore

print('Test de hipotesis para la media de la altura: ')
print('H0: media = 160, H1: media < 160   ', mean_test(dataframe.altura, 60, 'less'))
print('H0: media = 170, H1: media > 170   ', mean_test(dataframe.altura, 20, 'greater'))
print('H0: media = 180, H1: media != 180  ', mean_test(dataframe.altura, 45, 'two-sided'))
print()


def variance_test(var0, direccion):
	vp = ((size - 1) * var.altura) / var0

	if direccion == 'greater':
		result = st.chi2.ppf(1 - alpha, size - 1)
		return 'Se rechaza H0' if vp > result else 'No se rechaza H0'
	elif direccion == 'less':
		result = st.chi2.ppf(alpha, size - 1)
		return 'Se rechaza H0' if vp < result else 'No se rechaza H0'
	elif direccion == 'two-sided':
		result_left = st.chi2.ppf(alpha / 2, size - 1)
		result_right = st.chi2.ppf(1 - alpha / 2, size - 1)
		return 'Se rechaza H0' if vp < result_left or vp > result_right else 'No se rechaza H0'

	vp = ((size - 1) * var.altura) / var0
	p_value = st.chi2.cdf(vp, size - 1)

	if direccion == 'greater' or (direccion == 'two-sided' and p_value > 0.5):
		p_value = 1 - p_value
		
	return 'No se rechaza H0' if p_value > alpha else 'Se rechaza H0'

print('Test de hipotesis para la varianza de la altura: ')
print('H0: var = 25,   H1: var > 25      ', variance_test(25, 'greater'))
print('H0: var = 25,   H1: var < 25      ', variance_test(25, 'less'))
print('H0: var = 23.5, H1: var != 23.5   ', variance_test(23.5, 'two-sided'))
print()


print('Test de independencia: ')
print('H0: la altura y el peso son independientes')
print('H1: la altura y el peso no son independientes')
contingency_table = pandas.crosstab(
	pandas.cut(dataframe.altura, bins = 5, labels = ['Muy bajo', 'Bajo', 'Normal', 'Alto', 'Muy alto']),
	pandas.cut(dataframe.peso, bins = 5, labels = ['Muy bajo', 'Bajo', 'Normal', 'Alto', 'Muy alto'])
)
result = st.chi2_contingency(contingency_table)
print('No se rechaza H0' if result.pvalue > alpha else 'Se rechaza H0') # type: ignore
print()


print('Regresion lineal: ')
result = st.linregress([dataframe.altura, dataframe.peso], alternative='greater')
print('peso = ({:.3f} ± {:.3f}) * altura + ({:.3f} ± {:.3f})'.format(
	result.slope, result.stderr, result.intercept, result.intercept_stderr # type: ignore
))
print()

y_hat = result.slope * dataframe.altura + result.intercept # type: ignore
y_hat_max = (result.slope + result.stderr) * dataframe.altura + result.intercept + result.intercept_stderr # type: ignore
y_hat_min = (result.slope - result.stderr) * dataframe.altura + result.intercept - result.intercept_stderr # type: ignore




fig, axs = plt.subplots(2, 3)


axs[0, 0].set_title('Histograma de la altura')
axs[0, 0].hist(dataframe.altura, bins = k, color = 'blue', edgecolor = 'black', alpha = 0.5)

x = numpy.linspace(min_value.altura, max_value.altura, 500)
y = st.norm.pdf(x, mean.altura, std.altura) * size * (max_value.altura - min_value.altura) / k
axs[0, 0].plot(x, y, color = 'red', label = 'Distribucion normal')


st.probplot(dataframe.altura, dist='norm', plot=axs[0, 1])
axs[0, 1].set_title('QQ plot')
axs[0, 1].set_xlabel('')
axs[0, 1].set_ylabel('')


axs[0, 2].set_title('Regresion lineal de la altura')
axs[0, 2].scatter(dataframe.altura, dataframe.peso, s = 0.1)
axs[0, 2].plot(dataframe.altura, y_hat, color = 'red')
axs[0, 2].plot(dataframe.altura, y_hat_max, color = 'green', linestyle = 'dashed')
axs[0, 2].plot(dataframe.altura, y_hat_min, color = 'green', linestyle = 'dashed')


axs[1, 0].set_title('Intervalos de confianza para la media (hacer zoom)')
axs[1, 0].scatter(dataframe.index, dataframe.altura, s = 0.1)
interval = st.t.interval(1 - alpha, size - 1, mean.altura, std.altura / math.sqrt(size))
axs[1, 0].plot(dataframe.index, [mean.altura] * size, color = 'red', label = 'Media')
axs[1, 0].plot(dataframe.index, [interval[0]] * size, color = 'green', label = 'Intervalo de confianza')
axs[1, 0].plot(dataframe.index, [interval[1]] * size, color = 'green')

# draw line for outliers
IQR = dataframe.altura.quantile(0.75) - dataframe.altura.quantile(0.25)
axs[1, 0].plot(dataframe.index, [dataframe.altura.quantile(0.25) - 1.5 * IQR] * size, color = 'orange', linestyle = 'dashed', label = 'Outliers')
axs[1, 0].plot(dataframe.index, [dataframe.altura.quantile(0.75) + 1.5 * IQR] * size, color = 'orange', linestyle = 'dashed')

# draw line for IQR
axs[1, 0].plot(dataframe.index, [dataframe.altura.quantile(0.25)] * size, color = 'blue', linestyle = 'dashed', label = 'IQR')
axs[1, 0].plot(dataframe.index, [dataframe.altura.quantile(0.75)] * size, color = 'blue', linestyle = 'dashed')


axs[1, 1].set_title('Altura')
axs[1, 1].boxplot([dataframe.altura], vert=True, labels=[''])

from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(axs[1, 1])
extraAx = divider.append_axes('right', size='100%', pad=0.55)

extraAx.set_title('Peso')
extraAx.boxplot([dataframe.peso], vert=True, labels=[''])

axs[1, 2].set_title('Test de independencia')
seaborn.heatmap(contingency_table, ax=axs[1, 2], robust=True).invert_yaxis()


plt.show()
