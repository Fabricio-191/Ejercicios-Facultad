# Implementar un programa que valide un CUIT/CUIL ingresado por teclado.

base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2] # cuit[i] * (2 + ((9 - i) % 6)) for i in range(10)
tipos_cuil = [20, 23, 24, 27]
tipos_cuit = [30, 33, 34]
tipos = tipos_cuil + tipos_cuit

def tipo2(tipo):
	if tipo in tipos_cuil: return "CUIL"
	if tipo in tipos_cuit: return "CUIT"
	raise ValueError("Tipo de CUIL/CUIT no valido")

def validar_cuit(cuit):
     # Elimina espacios en blanco al inicio y al final
	cuit = cuit.strip()
 
    # Verifica el formato del CUIT/CUIL
	if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
		return False

    # Obtiene el tipo (los primeros dos dígitos)
	tipo = int(cuit[:2])
	if(tipo not in tipos): return False
 
	# Convierte los caracteres numéricos a una lista de enteros
	cuit = [int(i) for i in cuit if i.isdigit()]
 
	# Calcula una parte del valor del dígito verificador
	aux = sum(
		cuit[i] * base[i] for i in range(10)
	)
 
    # Calcula el dígito verificador
	aux = 11 - aux % 11

	if aux == 11: aux = 0
	if aux == 10: aux = 9
	
 	# Verifica si el dígito verificador es correcto y retorna el tipo
	return aux == cuit.pop(), tipo2(tipo)


# print(validar_cuit("20-12345678-9")) # True
# print(validar_cuit("20-43926518-4")) # True

if __name__ == "__main__":
	cuit = input("Ingrese un CUIT/CUIL (con guiones): ")
	es_valido, tipo = validar_cuit(cuit)
	if es_valido:
		print(f"El {tipo} ingresado es valido")
	else:
		print(f"El {tipo} ingresado no es valido")