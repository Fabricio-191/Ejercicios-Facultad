import pandas as pd
import scipy.stats as st 
import numpy as np
import math
import seaborn as sns 
import matplotlib.pyplot as plt
sns.get_dataset_names()

def calcChiSquare(expected, observed, degreesOfFreedom):
	if(len(expected) != len(observed)):
		raise Exception('The expected and observed values must have the same length')
	
	chi_square = 0
	for i in range(k):
		if expected[i] != 0:
			chi_square += ((observed[i] - expected[i]) ** 2) / expected[i]
		# else: print('Expected value is 0')

	# calculate the critical value
	critical_value = st.chi2.ppf(1 - alpha, degreesOfFreedom)

	# calculate the p-value
	p_value = 1 - st.chi2.cdf(chi_square, degreesOfFreedom)

	return chi_square, critical_value, p_value

# set the significance level
alpha = 0.1

# data = pd.read_csv('C:/Users/Fabricio/Desktop/Programacion/Ejercicios-Facultad/Probabilidad y estadistica/Trabajo final/games.csv')
# data = pd.DataFrame({ 'price': st.norm.rvs(5, 0.75, size=300000) })
#data = pd.DataFrame({ 'price': st.poisson.rvs(5, size=300000) })

key = 'Weight'
file = 'SOCR-HeightWeight.csv'
# data = sns.load_dataset('exercise') [[key]]
data = pd.read_csv(f'C:/Users/Fabricio/Desktop/Programacion/Ejercicios-Facultad/Probabilidad y estadistica/Trabajo final/{file}') [[key]]

# set the number of intervals
size = len(data)
k = round(1 + 3.3 * math.log10(size))

print(data.describe())
print('k', k)
print()

mean = data.mean()
std = data.std()
var = data.var()
max_value = data.max()
min_value = data.min()

# create the intervals
intervalsize = (max_value[key] - min_value[key]) / k
intervals = []
for i in range(k + 1):
	left = min_value[key] + i * intervalsize
	right = left + intervalsize

	intervals.append({
		'left': left,
		'right': right,
		'observed': len(data[data[key].between(left, right, inclusive='left')]) # left <= num < right
	})

# add the max value to the last interval
intervals[k - 1] = {
	'left': intervals[k - 1]['left'],
	'right': max_value[key],
	'observed': intervals[k - 1]['observed'] + 1
}

observed = [intervals[i]['observed'] for i in range(k)]




# check if the ... follows a normal distribution using chi-square test
# calculate the expected values
expected = []
for i in range(k):
	expected.append(size * (
		st.norm.cdf(intervals[i]['right'], mean[key], std[key]) -
		st.norm.cdf(intervals[i]['left'],  mean[key], std[key])
	))

# calculate the chi-square statistic
chi_square, critical_value, p_value = calcChiSquare(expected, observed, k - 3)

print('Chi-square statistic: ', chi_square)
print('Critical value: ', critical_value)
print('P-value: ', p_value)

if chi_square < critical_value and p_value > alpha:
	print('The ... follows a normal distribution')
elif chi_square > critical_value and p_value < alpha:
	print('The ... does not follow a normal distribution')
else:
	print('The test is inconclusive')


print()


# check if the ... follows a poisson distribution using chi-square test
# calculate the expected values
expected = []
for i in range(k):
	expected.append(size * (
		st.poisson.cdf(intervals[i]['right'], mean[key]) -
		st.poisson.cdf(intervals[i]['left'],  mean[key])
	))

# calculate the chi-square statistic
chi_square, critical_value, p_value = calcChiSquare(expected, observed, k - 2)

print('Chi-square statistic: ', chi_square)
print('Critical value: ', critical_value)
print('P-value: ', p_value)

if chi_square < critical_value and p_value > alpha:
	print('The ... follows a poisson distribution')
elif chi_square > critical_value and p_value < alpha:
	print('The ... does not follow a poisson distribution')
else:
	print('The test is inconclusive')

print(st.normaltest(data[key]))


print(st.ttest_1samp(data[key], 7, alternative="less")) # H0: mean = 7, H1: mean < 7
print(st.ttest_1samp(data[key], 3, alternative="greater")) # H0: mean = 3, H1: mean > 3
print(st.ttest_1samp(data[key], 5)) # H0: mean = 5, H1: mean != 5

def var_test(data, var, direccion = "diff", alpha = 0.05):
	rejected = False
	n = len(data)
	vp = (n - 1) * np.var(data) / var
	if direccion == "less":
		ec = st.chi2.ppf(alpha, n - 1)
		p_value = st.chi2.cdf(vp, n - 1)
	
		if vp < ec:
			rejected = True
	elif direccion == "greater":
		ec = st.chi2.ppf(1 - alpha, n - 1)
		p_value = 1-st.chi2.cdf(vp, n - 1)
		
		if vp > ec:
			rejected = True
	else:
		ec_left = st.chi2.ppf(alpha / 2, n - 1)
		ec_right =st.chi2.ppf(1 - (alpha / 2), n - 1)
		p_izq = st.chi2.cdf(vp, n - 1)
		p_der = 1 - st.chi2.cdf(vp, n - 1)
		p_value = 2 * min(p_der, p_izq)
		
		if vp < ec_left or vp > ec_right:
			rejected = True
	
	if rejected:
		return("H0 rejected")
	else:
		return("H0 not rejected")



print(var_test(data[key], 1, "less"))
print(var_test(data[key], 0.5, "greater"))
print(var_test(data[key], 0.75, "diff"))

# linear regression

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

x = np.array([[-3.0, -2.2, -1.4, -0.6, 0.2 , 1.0, 1.8 , 2.6 , 3.4 , 4.2 , 5.0],
              [-10.77, -10.12,  -5.90, -4.8,  -0.61, 2.67, 3.34, 6.25, 11.16, 12.12, 12.19]])


result = linregress(x)
slope = result.slope
intercept = result.intercept
y_hat = slope*x[0] + intercept

plt.scatter(x[0],x[1],color="green")
plt.plot(x[0],y_hat,color="red")
plt.xlabel("x [0]")
plt.ylabel("x [1]")
plt.title("Linear Regression")
plt.show()
"""

# plot everything

# plot histogram
sns.histplot(data[key], bins=k, stat='density', color='blue', edgecolor='black', alpha=0.5)

# plot the normal distribution
x = np.linspace(min_value[key], max_value[key], 1000)
y = st.norm.pdf(x, mean[key], std[key])
plt.plot(x, y, color='red', label='Normal distribution')

# plot the poisson distribution
x = np.linspace(min_value[key], max_value[key], 1000)
y = st.poisson.pmf(x, mean[key])
plt.plot(x, y, color='green', label='Poisson distribution')

plt.legend()
plt.show()