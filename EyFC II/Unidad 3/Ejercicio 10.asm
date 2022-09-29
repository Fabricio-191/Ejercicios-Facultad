/*
Un periférico vuelca sobre sus salidas un valor de 16 bits que conforma la dirección de memoria RAM
a partir de la cual está cargada una tabla de datos con final de tabla FFh. La parte baja de dicha
dirección es introducida al computador a través de las líneas de datos PB0 a PB7 de la PIA Nº 0 y la
parte alta a través de las líneas de datos PA0 a PA7 de la misma PIA, correspondiéndose PB0 con el
bit menos significativo y PA7 con el más significativo de la dirección.

Sobre las líneas de datos PA1, PA3 y PA7 de la PIA Nº 1 se conectan tres diodos led D1, D2 y D3
respectivamente, de manera que enciendan cuando se presente un “1” sobre la línea de datos
corrrespondiente.
Cuando una línea de control de salida del periférico genera un flanco positivo sobre la línea CA1 de la
PIA Nº 0 se 

debe interrumpir al uP para que ejecute una rutina de servicio que calcule el promedio de
la tabla de datos y si el promedio calculado es > 0, encender el diodo led D1; si el promedio es = 0,
encender el diodo led D2; si el promedio es < 0, encender el diodo led D3.
.Escribir el programa de inicialización de las PIAs y la rutina de servicio requerida. Para calcular el
promedio se debe invocar a la subrutina “PROMED” que calcula el promedio de una determinada
cantidad de datos almacenados consecutivamente en memoria y cuyos parámetros son:
Registro B: Contiene la cantidad de datos a ser promediados (parámetro de entrada).
Par registro HL: Contiene la dirección de inicio de la tabla de datos a ser promediada (parámetro de
entrada).
Registro C: Contiene el resultado del promedio calculado (parámetro de salida).
*/

		ORG 1024h
		LD SP, 2047h
		LD A, 0d ; registros de direccion de transferencia de datos
		OUT (0d), A
		OUT (3d), A

		LD A, 255d
		OUT (8d), A

		; registros de control
		LD A, 2d ; 00000010b (flanco positivo)
		OUT (1d), A
		LD A, 0d
		OUT (4d), A
		OUT (9d), A
		JP INICIO
		FIN



		ORG 1400h
SUBR	PUSH AF
		PUSH BC
		PUSH DE
		PUSH HL
		PUSH IX
		PUSH IY
		IN A, (2d)
		LD H, A
		IN A, (5d)
		LD L, A

		LD D, H
		LD E, L

		LD B, 0d
LOOP	LD A, (HL)
		CP FFh
		JP Z, FIN
		INC B
		INC HL
		JP LOOP
		
FIN		LD H, D
		LD L, E

		CALL PROMED
		LD A, C
		CP 0d

		JP Z, D2
		JP P, D1

D3		LD A, 128d ; 1000 0000
		OUT (10d), A
		JP FINAL

D2		LD A, 8d ; 0000 1000
		OUT (10d), A
		JP FINAL

D1		LD A, 2d ; 0000 0010
		OUT (10d), A

FINAL 	POP IY
		POP IX
		POP HL
		POP DE
		POP BC
		POP AF
		RETI
		FIN SUBR
