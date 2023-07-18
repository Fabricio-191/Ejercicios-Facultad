import pandas as pd
import scipy.stats as st 
import matplotlib.pyplot as plt
import numpy as np
import math 

def calcChiSquare(expected, observed, degreesOfFreedom):
	if(len(expected) != len(observed)):
		raise Exception('The expected and observed values must have the same length')
	
	chi_square = 0
	for i in range(k):
		if expected[i] == 0:
			chi_square += math.inf
		else:
			chi_square += ((observed[i] - expected[i]) ** 2) / expected[i]


	# calculate the critical value
	critical_value = st.chi2.ppf(1 - alpha, degreesOfFreedom)

	# calculate the p-value
	p_value = 1 - st.chi2.cdf(chi_square, degreesOfFreedom)

	return chi_square, critical_value, p_value

# set the significance level
alpha = 0.05

# read csv games.csv as list of dictionaries
# data = pd.read_csv('C:/Users/Fabricio/Desktop/Programacion/Ejercicios-Facultad/Probabilidad y estadistica/Trabajo final/games.csv')
data = pd.read_csv('C:/Users/Fabricio/Desktop/Programacion/Ejercicios-Facultad/Probabilidad y estadistica/Trabajo final/fly.csv')
# data = pd.DataFrame({ 'length': st.norm.rvs(5, 0.75, size=300000) })
#data = pd.DataFrame({ 'length': st.poisson.rvs(5, size=300000) })

# set the number of intervals
size = len(data)
k = round(1 + 3.3 * math.log10(size))

print(data.describe())
print('  k        ', k)
print()

# plot the histogram
plt.hist(data, k, density=True, color='lightblue', edgecolor='black', linewidth=1.2)

mean = data.mean()
std = data.std()
max_value = data.max()
min_value = data.min()

# create the intervals
intervalsize = (max_value.length - min_value.length) / k
intervals = []
for i in range(k + 1):
	left = min_value.length + i * intervalsize
	right = left + intervalsize

	intervals.append({
		'left': left,
		'right': right,
		'observed': len(data[data.length.between(left, right, inclusive='left')]) # left <= num < right
	})

# add the max value to the last interval
intervals[k - 1] = {
	'left': intervals[k - 1]['left'],
	'right': max_value.length,
	'observed': intervals[k - 1]['observed'] + 1
}

observed = [intervals[i]['observed'] for i in range(k)]




# check if the length follows a normal distribution using chi-square test
# calculate the expected values
expected = []
for i in range(k):
	expected.append(size * (
		st.norm.cdf(intervals[i]['right'], mean.length, std.length) - st.norm.cdf(intervals[i]['left'], mean.length, std.length)
	))

# calculate the chi-square statistic
chi_square, critical_value, p_value = calcChiSquare(expected, observed, k - 3)

print('Chi-square statistic: ', chi_square)
print('Critical value: ', critical_value)
print('P-value: ', p_value)

if chi_square < critical_value:
	print('The length follows a normal distribution')
else:
	print('The length does not follow a normal distribution')

if p_value > alpha:
	print('The length follows a normal distribution')
else:
	print('The length does not follow a normal distribution')

# using scipy.stats.normaltest
statistic, p_value = st.normaltest(data.length)

print('Statistic: ', statistic)
print('P-value: ', p_value)

print()


"""
# check if the length follows a poisson distribution using chi-square test
# calculate the expected values
expected = []
for i in range(k):
	expected.append(size * (
		st.poisson.cdf(intervals[i]['right'], mean.length) - st.poisson.cdf(intervals[i]['left'], mean.length)
	))

# calculate the chi-square statistic
chi_square, critical_value, p_value = calcChiSquare(expected, observed, k - 3)

print('Chi-square statistic: ', chi_square)
print('Critical value: ', critical_value)
print('P-value: ', p_value)

if chi_square < critical_value:
	print('The length follows a poisson distribution')
else:
	print('The length does not follow a poisson distribution')

if p_value > alpha:
	print('The length follows a poisson distribution')
else:
	print('The length does not follow a poisson distribution')
"""



x = [intervals[i]['left'] + (intervals[i]['right'] - intervals[i]['left']) / 2 for i in range(k)]

# plot the normal distribution
y = [st.norm.pdf(x[i], mean.length, std.length) for i in range(k)]
plt.plot(x, y, color='green', linewidth=3)

# plot the poisson distribution
# y = [st.poisson.pmf(x[i], mean.length) for i in range(k)]
# plt.plot(x, y, color='red', linewidth=3)


# show the plot
#plt.show()


# test for mean with var unknown
# H0: mean = 3
# H1: mean > 3

vp = st.t.cdf((mean.length-3)/(std.length/math.sqrt(size)),size-1)
ec = st.t.ppf(1-alpha,size-1)
p_value = 1 - st.t.cdf(vp,size-1) 

print("P value:",p_value)
if vp > ec:
	print('Rechazo H0')
else:
	print('No rechazo H0, u1')

#H0: mean = 7
#H1: mean < 7
vp = st.t.cdf((mean.length-7)/(std.length/math.sqrt(size)),size-1)
ec = st.t.ppf(alpha,size-1)
p_value = st.t.cdf(vp,size-1) 

print("P value:",p_value)
if vp < ec:
	print('Rechazo H0')
else:
	print('No rechazo H0,u2')

#H0: mean = 5
#H1: mean != 5
vp = st.t.cdf((mean.length-7)/(std.length/math.sqrt(size)),size-1)

ec_left = st.t.ppf(alpha/2,size-1)
ec_right = st.t.ppf(1-(alpha/2),size-1)

pder = p_value = 1 - st.t.cdf(vp,size-1) 
pizq = p_value = st.t.cdf(vp,size-1) 
p_value = 2 * min(pder,pizq)

print("P value:",p_value)
if vp < ec_left or vp > ec_right:
	print("Rechazo H0")
else:
	print("No rechazo H0,u3")

#H0: var = 0.5
#H1: var > 0.5
vp = st.chi2.cdf((((size-1)*(std.length**2))/0.5),size-1)
ec = st.chi2.ppf(1-alpha,size-1)
p_value = 1 - st.chi2.cdf(vp,size-1)

print(p_value)
if vp > ec:
	print('Rechazo H0')
else:
	print("No rechazo H0,o1")

#H0: var = 1
#H1: var < 1
vp = st.chi2.cdf((((size-1)*(std.length**2))),size-1)
ec = st.chi2.ppf(alpha,size-1)
p_value = st.chi2.cdf(vp,size-1)

print(p_value)
if vp < ec:
	print('Rechazo H0')
else:
	print("No rechazo H0,o2")

#H0: var = 0.75
#H1: var != 0.75
vp = st.chi2.cdf((((size-1)*(std.length**2))/0.75),size-1)

ec_left = st.chi2.ppf(alpha/2,size-1)
ec_right = st.chi2.ppf(1-(alpha/2),size-1)

pder = p_value = 1 - st.chi2.cdf(vp,size-1) 
pizq = p_value = st.chi2.cdf(vp,size-1) 
p_value = 2 * min(pder, pizq)

print("P value:",p_value)
if vp < ec_left or vp > ec_right:
	print("Rechazo H0")
else:
	print("No rechazo H0,o3")