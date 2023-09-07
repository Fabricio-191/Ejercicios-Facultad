import socket

HOST = 'localhost'
PORT = 5000

def query_socket(request):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            s.sendto(request.encode('utf-8'), (HOST, PORT))
            s.settimeout(5.0)  # set a timeout of 5 seconds
            try:
                response, _ = s.recvfrom(1024)
                return response.decode('utf-8')
            except socket.timeout:
                print("Timeout occurred, retrying...")

print()

equation = '5 * x**2 + 2*x - 4'
response = query_socket(f'1;{equation};x')
print(f"The roots of '{equation}' are {response}")
print()

equation = 'x**2 - 4'
response = query_socket(f'2;{equation};x')
print(f"The derivative of '{equation}' is {response}")
print()

response = query_socket(f'2;{equation};x;7')
print(f"The derivative of '{equation}' at x=7 is {response}")
print()

response = query_socket('3;4;x;1;3')
print(f"The integral of '4' from 1 to 3 is {response}")
print()


equation = 'log(x)'
response = query_socket(f'3;{equation};y')
print(f"The integral of '{equation}' is {response}")
print()


equation = 'ln(x ** 6)'
response = query_socket(f'3;{equation};x')
print(f"The integral of '{equation}' is {response}")
print()