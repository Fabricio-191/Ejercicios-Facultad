"""
Haciendo uso de sockets, implemente un servidor y un cliente (a modo de ejemplo, se proveen un servidor y un cliente en lenguaje Python), que permita desde el cliente, enviar un archivo comprimido utilizando el alfabeto ABCDEFGH, y en el servidor, descomprimir el archivo.
"""
import Compresor
import socket

class __Base:
    _socket = None
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, string):
        self._socket.send(Compresor.compress(string))

    def receive(self):
        return Compresor.decompress(self._socket.recv(1024))

    def close(self):
        self._socket.close()

class Client(__Base):
    def __init__(self, ip = 'localhost', port = 27015):
        super().__init__()
        self._socket.connect((ip, port))
        
class Server(__Base):
    def __init__(self, ip = 'localhost', port = 27015):
        super().__init__()
        self._socket.bind((ip, port))
        self._socket.listen(1)
        self._socket, addr = self._socket.accept()

if __name__ == "__main__":
    import threading
    
    def make_server():
        server = Server()
        recibido = server.receive()
        server.send("ABCDE")
        server.send("AAAA" + recibido)
        server.close()
        
    # Crear y ejecutar el servidor en un hilo separado
    thread = threading.Thread(target=make_server)
    thread.start()
    
    # Crear el cliente y enviar datos al servidor
    client = Client()
    client.send("BDAEB")
    
    # Recibir y mostrar las respuestas del servidor
    print(client.receive())
    print(client.receive())
    
    # Cerrar la conexión del cliente y esperar a que el hilo del servidor termine
    client.close()
    thread.join()
    
