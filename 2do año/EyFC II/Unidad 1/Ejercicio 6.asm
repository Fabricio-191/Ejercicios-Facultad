/*
Ejercicio 6:

A partir de la dirección de memoria 54F2h se encuentran almacenados 50 números de 1 byte.
Realizar la sumatoria de esos números y verificar si se produce overflow al calcularla, de ser así
guardar el resultado de la última suma calculada sin overflow al final de la tabla de datos e indicar
esa situación cargando el código 01h en la próxima celda de memoria; caso contrario cargar en
esas celdas el resultado de la sumatoria y el código 00h respectivamente. Cargar el programa
objeto a partir de la dirección de memoria 0450h.
*/

	ORG 0450h
	LD IX, 54F2h
	LD IY, 5524h	 ; 54F2h + 50d = 5524h   (celda despues del final de la tabla)
	LD (IY + 01h), 00h

	LD B, 50d
	LD A, 0d
	LD (IY), A

LOOP:
	LD C, (IX)
	ADD A, C
	JP PE, OVERFLOW  ; si se produce overflow, salta a OVERFLOW

	LD (IY), A
	INC IX

	DJNZ LOOP      ; decrementa el registro B y si el resultado es 0 salta a ENDING
	JP ENDING

OVERFLOW:
	LD (IY + 01h), 01h

ENDING:
	END.