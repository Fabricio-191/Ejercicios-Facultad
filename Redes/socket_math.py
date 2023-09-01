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

def handle_request(conn):
	data = conn.recv(1024).decode('utf-8')
	service, equation, variable, *data = data.split(';')
	variable = sympy.Symbol(variable)
	equation = sympy.sympify(equation)
	
	if service == '1':
		result = sympy.solve(equation, variable)
	elif service == '2':
		result = sympy.diff(equation, variable)
		if len(data) > 0: result = result.subs(variable, data[0])
	elif service == '3':
		if len(data) >= 2:
			result = sympy.integrate(equation, (variable, data[0], data[1]))
		else:
			result = sympy.integrate(equation, variable)
	else:
		result = 'Invalid service number'

	conn.sendall(str(result).encode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	while True:
		conn, addr = s.accept()
		with conn:
			try:
				handle_request(conn)
			except Exception as e:
				conn.sendall('Invalid request'.encode('utf-8'))
				conn.close()

	# s.close()

