/*
Ejercicio 3:

En memoria se encuentran almacenados 100 datos de 1 byte a partir de la celda de memoria de
dirección C54Fh. Trasladar esta tabla de datos al bloque de memoria que comienza en la
dirección 0400h. Cargar el programa objeto a partir de la celda de memoria de dirección F55A h.
*/

		ORG F55Ah
INICIO:	LD B, 100d
		LD IX, C54Fh
		LD IY, 0400h

LOOP: 	LD HL, (IX + 00h)
		LD (IY + 00h), HL
		INC IX
		INC IY
		DJNZ, LOOP
		END INICIO