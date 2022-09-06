/*
Realizar en Assembler una subrutina parametrada que genere una tabla con los datos
POSITIVOS.
La dirección de comienzo de la subrutina estará dada por la etiqueta “POSITI” y los parámetros
de la misma vendrán dados por los contenidos de los registros:
IX: dirección de comienzo de la tabla origen de datos.
HL: dirección de comienzo de la tabla de datos generada es BC34 h.
En memoria se almacena una tabla de datos de 8 bits en forma consecutiva a partir de la dirección
de memoria DCF1h; la tabla posee su marca de final de tabla en FFh.
La tabla generada deberá poseer también su marca de final de tabla en FFh.
Desarrollar un programa en Assembler que invoque a la subrutina del apartado anterior.
La dirección en memoria para la carga del programa objeto es C801h.
*/

				ORG POSITI
SUBRUTINA:		LD A, (IX)
				CP FFh
				JP Z, FINSUBRUTINA
				CP 0h
				JP M, NOPASAR

				LD (HL), A
NOPASAR:		INC IX
				INC HL

FINSUBRUTINA:	RET



				ORG C801h
INICIO:			LD IX, DCF1h
				LD HL, BC34h
				LD SP, FFFFh

				CALL SUBRUTINA

				END INICIO
