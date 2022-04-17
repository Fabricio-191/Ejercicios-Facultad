"""
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos se ingresan por teclado). Y los siguientes métodos:

a- El constructor.
b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:
idCuenta.: alumnopoo
dominio: gmail
tipoDominio: com

Resultado devuelto por retornaEmail: alumnopoo@gmail.com

c- Método “getDominio()”, que retorna el dominio.
d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.

Implemente un programa que permita:

1- Ingresar el nombre de una persona y de su cuenta de correo, el identificador de cuenta, dominio y tipo de dominio (crear una instancia de la clase Email) y luego imprima el siguiente mensaje:

Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.

2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.

3- Crear un objeto de clase Email, a partir de una dirección de correo, por ejemplo: informatica.fcefn@gmail.com, juanLiendro1957@yahoo.com, etc.

4- Leer de un archivo separado por comas 10 direcciones de e-mail, crear instancias de la clase Email; luego ingresar un identificador de cuenta e indicar si está repetido o no.
"""
import re
from os import path

class Email:
	def __init__(self, idCuenta, dominio, tipoDominio, contraseña = None):
		self.idCuenta = idCuenta
		self.dominio = dominio
		self.tipoDominio = tipoDominio
		self.__contraseña = contraseña

	def retornaEmail(self):
		return self.idCuenta + "@" + self.dominio + "." + self.tipoDominio

	def getDominio(self):
		return self.dominio

	def modificarContraseña(self, contraseñaActual, nuevaContraseña):
		if self.__contraseña == contraseñaActual:
			self.__contraseña = nuevaContraseña
			print("La contraseña ha sido modificada")
		else:
			print("La contraseña actual no es correcta")
	
	def __str__(self):
		return self.idCuenta + "@" + self.dominio + "." + self.tipoDominio

	@staticmethod
	def fromStr(string):
		matches = re.search(r"(.+)@(.+)\.(.+)", string)

		return Email(matches.group(1), matches.group(2), matches.group(3))

def leerArchivo(file):
	with open(file, "r") as f:
		direccionesMail = f.readline().split(',')
	
		return map(lambda email: Email.fromStr(email), direccionesMail)

if __name__ == "__main__":
	"""
	1- Ingresar el nombre de una persona y de su cuenta de correo, el identificador de cuenta, dominio y tipo de dominio (crear una instancia de la clase Email) y luego imprima el siguiente mensaje:
	
	Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.
	"""

	nombre = input("Nombre: ")
	email = Email(
		input("Nombre de usuario: "), 
		input("Dominio: "),
		input("Tipo de dominio: "),
		input("Contraseña: ")
	)

	"""
	2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.
	"""

	print()
	print("Estimado " + nombre + " te enviaremos tus mensajes a la dirección " + email.retornaEmail())

	print()
	email.modificarContraseña(input("Contraseña vieja: "), input("Contraseña nueva: "))
	print()

	"""
	3- Crear un objeto de clase Email, a partir de una dirección de correo, por ejemplo: informatica.fcefn@gmail.com, juanLiendro1957@yahoo.com, etc.
	"""

	Email.fromStr(input("email: "))
	
	print()

	"""
	4- Leer de un archivo separado por comas 10 direcciones de e-mail, crear instancias de la clase Email; luego ingresar un identificador de cuenta e indicar si está repetido o no.
	"""

	emailsDelArchivo = leerArchivo(path.dirname(__file__) + "/emails.txt")
	identificador = input("Ingresar identificador de cuenta: ")
	contador = 0

	for email in emailsDelArchivo:
		if email.idCuenta == identificador:
			contador += 1
	
	if contador == 0:
		print("El email con ese identificador no existe")
	elif contador == 1:
		print("El email con ese identificador es unico")
	else:
		print("El email con ese identificador esta repetido") # Fabricio1 es el unico repetido

""" Lote de prueba
Fabricio
Fabricio
gmail
com
1
1
2
Fabricio@gmail.com
Fabricio1

"""
	