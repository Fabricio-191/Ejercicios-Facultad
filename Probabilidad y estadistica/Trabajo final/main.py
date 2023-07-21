import pandas as pd
import scipy.stats as st 
import matplotlib.pyplot as plt
import numpy as np
import math 
import seaborn as sb

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

def var_test(data,var,direccion="diff",alpha=0.05):
	rejected = False
	n = len(data)
	vp = (n-1) * np.var(data) / var
	if direccion == "less":
		ec = st.chi2.ppf(alpha,n-1)
		p_value = st.chi2.cdf(vp,n-1)
	
		if vp < ec:
			rejected = True
	elif direccion == "greater":
		ec = st.chi2.ppf(1-alpha,n-1)
		p_value = 1-st.chi2.cdf(vp,n-1)
		
		if vp > ec:
			rejected = True
	else:
		ec_left = st.chi2.ppf(alpha/2,n-1)
		ec_right =st.chi2.ppf(1-(alpha/2),n-1)
		p_izq = st.chi2.cdf(vp,n-1)
		p_der = 1-st.chi2.cdf(vp,n-1)
		p_value = 2*min(p_der,p_izq)
		
		if vp < ec_left or vp > ec_right:
			rejected = True
	print("Var test: vp:",vp,"p_value:",p_value)
	if rejected:
		return("H0 rejected")
	else:
		return("H0 not rejected")

def mean_test(data,mean0,direccion='two-sided',alpha = 0.05):
	rejected = False
	result=st.ttest_1samp(data,mean0,alternative=direccion)
	print(result)
	if result.pvalue <= alpha:
		rejected = True
	if rejected == True:
		print("H0 rejected")
	else:
		print("H0 not rejected")

# set the significance level
alpha = 0.05

key = 'length'

# read csv fly.csv as list of dictionaries
data = pd.read_csv('C:/Users/Fabricio/Desktop/Programacion/Ejercicios-Facultad/Probabilidad y estadistica/Trabajo final/fly.csv')
#data = pd.DataFrame({ 'price': st.norm.rvs(5, 0.75, size=300000) })
#data = pd.DataFrame({ 'price': st.poisson.rvs(5, size=300000) })

# set the number of intervals
size = len(data)
k = round(3.3 * math.log10(size) + 1)

print(data.describe())
print('k', k)
print()

# plot the histogram
plt.hist(data, k, density=True, color='lightblue', edgecolor='black', linewidth=1.2)
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



# check if the length follows a normal distribution using chi-square test
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
	print('The price follows a normal distribution')
elif chi_square > critical_value and p_value <= alpha:
	print('The price does not follow a normal distribution')
else:
	print('???')

print()

# check if the length follows a poisson distribution using chi-square test
# calculate the expected values
expected = []
for i in range(k):
	expected.append(size * (
		st.poisson.cdf(intervals[i]['right'], mean[key]) -
		st.poisson.cdf(intervals[i]['left'], mean[key])
	))

# calculate the chi-square statistic
chi_square, critical_value, p_value = calcChiSquare(expected, observed, k - 2)

print('Chi-square statistic: ', chi_square)
print('Critical value: ', critical_value)
print('P-value: ', p_value)

if chi_square < critical_value and p_value > alpha:
	print('The price follows a poisson distribution')
elif chi_square > critical_value and p_value <= alpha:
	print('The price does not follow a poisson distribution')
else:
	print('???')

print()

#another way trought function
result = st.normaltest(data[key])
print(result)
if result.pvalue > alpha:
	print("It follows a normal distribution")
else:
	print("It does not follows a normal distribution")


x = [intervals[i]['left'] + (intervals[i]['right'] - intervals[i]['left']) / 2 for i in range(k)]

# plot the normal distribution
y = [st.norm.pdf(x[i], mean[key], std[key]) for i in range(k)]
plt.plot(x, y, color='green', linewidth=3)

# plot the poisson distribution
y = [st.poisson.pmf(x[i], mean[key]) for i in range(k)]
plt.plot(x, y, color='red', linewidth=3)


# show the plot
plt.show()
plt.figure().clear()
plt.cla()
plt.clf()

#Hyphtoesis test for mean
mean_test(data[key], 60, "less", alpha) # H0: mean = 60, H1: mean < 60
mean_test(data[key], 20, "greater", alpha) # H0: mean = 20, H1: mean > 20
mean_test(data[key], 45, alpha=alpha) # H0: mean = 45, H1: mean != 45


#Hyphtoesis test for var
print(var_test(data[key], 20, "less")) # H0: var = 20, H1: var < 20
print(var_test(data[key], 10, "greater")) # H0: var = 10, H1: var > 10
print(var_test(data[key], 15, "diff")) # H0: var = 15, H1: var != 15

# interval estimation
# calculate the confidence interval for the mean (unknown variance)
t = st.t.ppf(1 - alpha / 2, size - 1)
err = t * std[key] / math.sqrt(size)
print('Confidence interval for the mean (unknown variance): ', mean[key] - err, mean[key] + err)

# interval = st.t.interval(1 - alpha, size - 1)
# err_left = interval[0] * std[key] / math.sqrt(size)
# err_right = interval[1] * std[key] / math.sqrt(size)
# print('Confidence interval for the mean (unknown variance): ', mean[key] + err_left, mean[key] + err_right)

# calculate the confidence interval for the variance

interval = st.chi2.interval(1 - alpha, size - 1)
left = (size - 1) * std[key] ** 2 / interval[1]
right = (size - 1) * std[key] ** 2 / interval[0]
print('Confidence interval for the variance: ', left, right)

# chi_square_left = st.chi2.ppf(1 - alpha / 2, size - 1)
# chi_square_right = st.chi2.ppf(alpha / 2, size - 1)
# left = (size - 1) * std[key] ** 2 / chi_square_left
# right = (size - 1) * std[key] ** 2 / chi_square_right
# print('Confidence interval for the variance: ', left, right)

print()

#Indenpendance test
# H0: sex and smoker are independent, sex and smoker are not independent
tips = sb.load_dataset("tips")
tips = pd.crosstab(tips.sex, tips.smoker)

print(tips)

result = st.chi2_contingency(tips)

print(result)

if result.pvalue > alpha:
	print("H0 not rejected")
else:
	print("H0 rejected")

# regresion lineal
data = pd.read_csv('C:/Users/Fabricio/Desktop/Programacion/Ejercicios-Facultad/Probabilidad y estadistica/Trabajo final/SOCR-HeightWeight.csv')
x=[data["Height"], data["Weight"]]


result = st.linregress(x)
y_hat = result.slope * x[0] + result.intercept

plt.scatter(x[0], x[1], color="green", s =0.5)
plt.plot(x[0], y_hat, color="red")
plt.xlabel("x [0]")
plt.ylabel("x [1]")
plt.title("Linear Regression")
plt.show()
