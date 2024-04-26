# create a socket that recieves an string that is an math ecuation and returns it's integral using sympy
# if there are limits, it returns the definite integral, if not, it returns the indefinite integral
# also it recieves the variable to integrate
# the socket recieves a byte array with the following format: [number of service, ...data]

# number of service 1 = equation solve
# recieved: 1, ecuation, variable
# number of service 2 = derivative solving
# recieved: [2, ecuation, variable, point?]
# number of service 3 = integral definite or indefinite
# recieved: [3, ecuation, variable, (limit1, limit2)?

import socket
import sympy

HOST = 'localhost'
PORT = 5000

def handle_request(data, addr, s):
    service, equation, variable, *limits = data.decode('utf-8').split(';')
    variable = sympy.Symbol(variable)
    equation = sympy.sympify(equation)
    
    if service == '1':
        result = sympy.solve(equation, variable)
    elif service == '2':
        result = sympy.diff(equation, variable)
        if len(limits) > 0: result = result.subs(variable, float(limits[0]))
    elif service == '3':
        if len(limits) >= 2:
            result = sympy.integrate(equation, (variable, float(limits[0]), float(limits[1])))
        else:
            result = sympy.integrate(equation, variable)
    else:
        result = 'Invalid service number'

    response = str(result).encode('utf-8')
    s.sendto(response, addr)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        handle_request(data, addr, s)
