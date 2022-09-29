/*
Con este propósito, las salidas A0, A1, A2 y A3 del periférico, que conforman la salida BCD natural multiplexada en el tiempo para los tres dígitos, son ingresadas por las líneas PA0, PA1, PA2 y PA3 respectivamente de la PIA N° 0.

Con el objeto de identificar a qué dígito decimal corresponde la salida BCD del periférico en un determinado momento, el periférico dispone de dos salidas de control M1 y M2 que de acuerdo a la combinación de sus valores indican lo siguiente:

Estas líneas M1 y M2 son ingresadas por las líneas PA5 y PA6 respectivamente de la misma PIA Nº 0.
Cuando el periférico vuelca un nuevo valor sobre sus salidas de datos lo indica al exterior generando un pulso negativo sobre una línea de control que es ingresada a la línea CA1 de la PIA N° 0 para que al detectarse un flanco negativo se interrumpa al uP para que se ejecute la rutina de servicio que debe atender al periférico.

La conversión de BCD natural a 7 segmentos para cada dígito decimal será realizada invocando a la
subrutina “BCD7SE” usada en el ejercicio 11.
Entrada B
Salida C
*/

			ORG 1024h
			LD A, 255d
			OUT (3d), A
			OUT (8d), A
			OUT (11d), A

			LD A, 0d
			LD (0d), A
			LD A, 1d; 00000001b
			LD (1d), A

			JP INICIO
			FIN 

			ORG 1400h
SUBR		PUSH IY
			PUSH IX
			PUSH HL
			PUSH DE
			PUSH BC
			PUSH AF
			IN A, (02d)
			PUSH AF

			AND 15d
			LD B, A

			CALL BCD7SE

			POP AF
			AND 60h

			CP 0d
			JP Z, UNIDADES
			CP 20h
			JP Z, DECENAS
			CP 40h
			JP Z, CENTENAS
			JP FIN

UNIDADES	LD A, C
			OUT (11d), A
			JP FIN

DECENAS		LD A, C
			OUT (8d), A
			JP FIN

CENTENAS	LD A, C
			OUT (3d), A

FIN			POP AF
			POP BC
			POP DE
			POP HL
			POP IX
  			POP IY
			RETI
