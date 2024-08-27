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
	cuit = cuit.strip()
	if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
		return False

	tipo = int(cuit[:2])
	if(tipo not in tipos): return False
	
	cuit = [int(i) for i in cuit if i.isdigit()]
	
	aux = sum(
		cuit[i] * base[i] for i in range(10)
	)

	aux = 11 - aux % 11

	if aux == 11: aux = 0
	if aux == 10: aux = 9
	
	es_valido = aux == cuit.pop()
	return es_valido, tipo2(tipo)

print(validar_cuit("20-12345678-9")) # True
print(validar_cuit("20-43926518-4")) # True