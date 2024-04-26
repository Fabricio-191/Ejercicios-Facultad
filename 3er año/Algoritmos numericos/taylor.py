import sympy
import math

var_x = sympy.symbols('x')

x = 1.75
a = 1
max_error = 3 * 10 ** -2
# fn = math.e ** var_x
# fn = sympy.ln(var_x)
# fn = sympy.ln(var_x ** 2)
fn = sympy.sqrt(var_x)
# fn = (math.e ** var_x - 1) / var_x

real_value = fn.subs(var_x, x)

padding_size = 20
significant_numbers = 10
def b(x):
	x = round(x, significant_numbers)
	return str(x).ljust(padding_size)

def taylor():
    result = 0
    n = 0
    derivative = fn

    while abs(result - real_value) > max_error:
        asd = (derivative.subs(var_x, a) / math.factorial(n)) * (x - a) ** n
        result += asd

        n += 1
        derivative = sympy.diff(derivative, var_x)
        print(n, b(real_value), b(result), b(abs(result - real_value)), b(asd))

        if n > 10: break


print()
taylor()
print()

"""
def mac_laurin():
    result = 0
    n = 0

    while abs(result - real_value) > max_error:
        result += (fn_derivative(n).subs(var_x, a) / factorial(n)) * x ** n
        n += 1
        print(n, real_value, result, abs(result - real_value))
"""