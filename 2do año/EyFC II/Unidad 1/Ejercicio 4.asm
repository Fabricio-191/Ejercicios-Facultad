/*
Ejercicio 4:

Sobre un conjunto de 15 valores numéricos de 8 bits almacenados consecutivamente en memoria
a partir de la dirección etiquetada como DATOS, contar los negativos. Guardar el conteo
obtenido en la celda de memoria anterior al inicio de la tabla de datos y cargar el programa a
partir de la dirección de memoria FFB5h.
*/

		ORG FFB5h
INICIO:	LD B, 15
		LD C, 0
		LD IX, DATOS

LOOP:	LD A, (IX + 00h)
		CP A, 0

		JP P, SEGUIR
		INC C
SEGUIR:	INC IX
		DEC B
		JP NZ, LOOP
		END INICIO