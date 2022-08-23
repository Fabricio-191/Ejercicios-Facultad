/*
Dadas dos tablas de datos de 8 bits almacenados en memoria en forma consecutiva, la primera
tabla a partir de la posición de memoria 4ABCh y la segunda tabla en la dirección de memoria
5DABh; ambas tablas con marcas de final de tabla FFh.
Desarrollar un programa en Assembler que invoque a dicha subrutina para que genere la
Concatenación (CONCAT) de las 2 tablas a partir de la dirección 7FFFh; también la tabla
generada debe poseer su marca de final de tabla en FFh y deberá proporcionar al programa
principal la cantidad de datos de la tabla en el registro B. Guardar el registro B en la posición
siguiente al final de tabla. La dirección en memoria para la carga del programa objeto es CA00h.
*/

	ORG C000h
CONCAT:
	LD B, 0d
LOOP1:
	LD A, (IX)
	CP FFh
	JP Z, LOOP2

	LD (HL), A

	INC B
	INC IX
	INC HL

	JP LOOP1
LOOP2:
	LD A, (IY)
	CP FFh
	JP NZ, ENDCONCAT

	LD (HL), A

	INC B
	INC IY
	INC HL

ENDCONCAT:
	LD (HL), FFh
	RET



	ORG CA00h
INICIO:
	LD IX, 4ABCh
	LD IY, 5DABh
	LD HL, 7FFFh
	LD SP, FFFFh

	CALL CONCAT

	INC HL
	LD (HL), B


	