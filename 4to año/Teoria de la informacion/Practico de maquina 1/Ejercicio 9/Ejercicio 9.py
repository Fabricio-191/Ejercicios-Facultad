"""
En la actualidad, muchos de los procesos que se ejecutan en una computadora requiere obtener o enviar información a otros procesos que se localizan en una computadora diferente, o en la misma. Para lograr esta comunicación se utilizan los protocolos de comunicación TCP y UDP. Una implementación de comunicación entre procesos, se puede realizar utilizando sockets.
Los sockets son una forma de comunicación entre procesos que se encuentran en diferentes máquinas de una red, los sockets proporcionan un punto de comunicación por el cual se puede enviar o recibir información entre procesos.
Los sockets tienen un ciclo de vida dependiendo si son sockets de servidor, que esperan a un cliente para establecer una comunicación, o socket cliente que busca a un socket de servidor para establecer la comunicación.

Haciendo uso de sockets, implemente un servidor y un cliente (a modo de ejemplo, se proveen un servidor y un cliente en lenguaje Python), que permita desde el cliente, enviar un archivo comprimido utilizando el alfabeto ABCDEFGH, y en el servidor, descomprimir el archivo.
"""

