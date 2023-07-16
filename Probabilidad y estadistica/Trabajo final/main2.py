import pandas as pd
import scipy.stats as st 
import matplotlib.pyplot as plt
import math 

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
alpha = 0.05

# read csv games.csv as list of dictionaries
# data = pd.read_csv('C:/Users/Fabricio/Desktop/Programacion/Ejercicios-Facultad/Probabilidad y estadistica/Trabajo final/games.csv')
data = pd.DataFrame({ 'price': st.norm.rvs(5, math.sqrt(3), size=300) })
# data = pd.DataFrame({ 'price': st.poisson.rvs(5, size=300000) })

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
max = data.max()
min = data.min()

# create the intervals
intervalsize = (max.price - min.price) / k
intervals = []
for i in range(k + 1):
	left = min.price + i * intervalsize
	right = left + intervalsize

	intervals.append({
		'left': left,
		'right': right,
		'observed': len(data[data.price.between(left, right, inclusive='left')]) # left <= num < right
	})

# add the max value to the last interval
intervals[k - 1] = {
	'left': intervals[k - 1]['left'],
	'right': max.price,
	'observed': intervals[k - 1]['observed'] + 1
}

observed = [intervals[i]['observed'] for i in range(k)]

x = [intervals[i]['left'] + (intervals[i]['right'] - intervals[i]['left']) / 2 for i in range(k)]




# check if the price follows a normal distribution using chi-square test
# calculate the expected values
expected = []
for i in range(k):
	expected.append(size * (
		st.norm.cdf(intervals[i]['right'], mean.price, std.price) - st.norm.cdf(intervals[i]['left'], mean.price, std.price)
	))

# calculate the chi-square statistic
chi_square, critical_value, p_value = calcChiSquare(expected, observed, k - 3)

print('Chi-square statistic: ', chi_square)
print('Critical value: ', critical_value)
print('P-value: ', p_value)

if chi_square < critical_value:
	print('The price follows a normal distribution')
else:
	print('The price does not follow a normal distribution')

if p_value > alpha:
	print('The price follows a normal distribution')
else:
	print('The price does not follow a normal distribution')

# plot the normal distribution
y = [st.norm.pdf(x[i], mean.price, std.price) for i in range(k)]
plt.plot(x, y, color='green', linewidth=3)


print()

# interval estimation
# calculate the confidence interval for the mean (unknown variance)
t = st.t.ppf(1 - alpha / 2, size - 1)
err = t * std.price / math.sqrt(size)
print('Confidence interval for the mean (unknown variance): ', mean.price - err, mean.price + err)

interval = st.t.interval(1 - alpha, size - 1)
err_left = interval[0] * std.price / math.sqrt(size)
err_right = interval[1] * std.price / math.sqrt(size)
print('Confidence interval for the mean (unknown variance): ', mean.price + err_left, mean.price + err_right)

# calculate the confidence interval for the variance
chi_square_left = st.chi2.ppf(1 - alpha / 2, size - 1)
chi_square_right = st.chi2.ppf(alpha / 2, size - 1)
left = (size - 1) * std.price ** 2 / chi_square_left
right = (size - 1) * std.price ** 2 / chi_square_right
print('Confidence interval for the variance: ', left, right)

interval = st.chi2.interval(1 - alpha, size - 1)
left = (size - 1) * std.price ** 2 / interval[1]
right = (size - 1) * std.price ** 2 / interval[0]
print('Confidence interval for the variance: ', left, right)

print()


"""
# check if the price follows a poisson distribution using chi-square test
# calculate the expected values
expected = []
for i in range(k):
	expected.append(size * (
		st.poisson.cdf(intervals[i]['right'], mean.price) - st.poisson.cdf(intervals[i]['left'], mean.price)
	))

# calculate the chi-square statistic
chi_square, critical_value, p_value = calcChiSquare(expected, observed, k - 3)

print('Chi-square statistic: ', chi_square)
print('Critical value: ', critical_value)
print('P-value: ', p_value)

if chi_square < critical_value:
	print('The price follows a poisson distribution')
else:
	print('The price does not follow a poisson distribution')

if p_value > alpha:
	print('The price follows a poisson distribution')
else:
	print('The price does not follow a poisson distribution')

# plot the poisson distribution
y = [st.poisson.pmf(x[i], mean.price) for i in range(k)]
plt.plot(x, y, color='red', linewidth=3)
"""

# show the plot
plt.show()
