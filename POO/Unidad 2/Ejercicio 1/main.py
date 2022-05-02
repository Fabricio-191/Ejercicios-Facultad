from Email import Email
from os import path
import re
import csv

def EmailfromStr(string: str) -> Email:
	matches = re.search(r"(.+)@(.+)\.(.+)", string)
	if(matches == None):
		raise Exception("Email is not valid")
		
	return Email(matches.group(1), matches.group(2), matches.group(3))

def leerArchivo(filePath: str) -> list[Email]:
	with open(filePath, "r") as file:
		reader = csv.reader(file, delimiter=',')
		next(reader, None)
		emails: list[Email] = []

		for line in reader:
			emails.append(EmailfromStr(line[0]))

		return emails

def test():
	email = Email("alumnopoo", "gmail", "com")

	assert email.getDominio() == "gmail"
	assert email.getIDCuenta() == "alumnopoo"

if __name__ == "__main__":
	test()

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

	EmailfromStr(input("email: "))
	
	print()

	"""
	4- Leer de un archivo separado por comas 10 direcciones de e-mail, crear instancias de la clase Email; luego ingresar un identificador de cuenta e indicar si está repetido o no.
	"""
	emailsDelArchivo = leerArchivo(path.dirname(__file__) + "/emails.csv")
	identificador = input("Ingresar identificador de cuenta: ")
	contador = 0

	for email in emailsDelArchivo:
		if email.getIDCuenta() == identificador:
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