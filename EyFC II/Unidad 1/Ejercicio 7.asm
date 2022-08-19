/*
Ejercicio 7:

Realizar la sumatoria de los números negativos y el conteo de los números positivos e iguales a
cero de una tabla de 18 datos numéricos de 1 byte almacenados en memoria a partir de la
dirección 4FFFh. Guardar los resultados de la sumatoria y el conteo a partir de las celdas de
memoria ubicadas 10 lugares por encima de la tabla de datos y cargar el programa a partir de la
dirección ABFFh.
*/

	ORG ABFFh
	LD IX, 4FFFh
	LD IY, 4FF5h	; 4FFFh - 10d = 4FF5h   (celda despues del final de la tabla)

	LD B, 18d
	LD C, 0d 		; conteo
	LD D, 0d 		; sumatoria

LOOP:
	LD A, (IX)
	CP 0d

	JP P, POSITIVE
	JP NEGATIVE

CONTINUE_LOOP:
	INC IX

	DJNZ ENDING      ; decrementa el registro B y si el resultado es 0 salta a ENDING
	JP LOOP

POSITIVE:
	INC C
	JP CONTINUE_LOOP

NEGATIVE:
	ADD D, A
	JP CONTINUE_LOOP

ENDING:
	LD (IY), C
	LD (IY + 01h), D
	END.