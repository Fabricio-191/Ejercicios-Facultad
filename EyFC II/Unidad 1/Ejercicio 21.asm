/*
Desarrollar en Assembler una subrutina parametrada cuyo propósito sea generar en memoria una
tabla de datos de 8 bits, a partir de otra tabla de datos de 8 bits almacenados consecutivamente
en memoria. La tabla generada deberá contener todos los bytes de la tabla existente en memoria,
excepto los bytes que representen datos iguales a cero. La subrutina debe retornar al programa
principal como resultado el número de ceros detectados en la tabla.
Los parámetros de la subrutina son:
• IX: dirección de comienzo de la tabla origen (DC10 h).
• B: Cantidad de datos de la tabla origen (25 datos).
• HL: dirección de comienzo de la tabla a generar (AB89 h).
• C: cantidad de veces que se presenta el valor cero en la tabla de datos.
Desarrollar un programa en Assembler que invoque a la subrutina del apartado anterior; el
resultado proporcionado por la subrutina deberá ser almacenarlo en la posición de memoria
previa al inicio de la tabla de datos obtenida en la subrutina. La dirección en memoria para la
carga del programa objeto es A49Fh.
*/

	ORG A100h
SUBRUTINA:
	LD A, (IX)
	CP 0d

	JP Z, CONTAR
	JP NOCONTAR
CONTAR:
	INC C
	JP DESPUESDECONTAR
NOCONTAR:
	LD (HL), A
DESPUESDECONTAR:
	INC IX
	INC HL
	DJNZ SUBRUTINA
	RET


	ORG A49Fh
INICIO:
	LD IX, DC10h
	LD B, 25d
	LD HL, AB89h
	LD C, 0d
	LD SP, FFFFh
	
	CALL SUBRUTINA