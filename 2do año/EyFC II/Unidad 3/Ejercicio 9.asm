/*
El valor de inicio del contador estará dado por las salidas de un periférico de 8 bits conectado a las líneas de datos PA0 a
PA7 de la PIA Nº 1 y el valor de finalización del conteo estará dado por las salidas de otro periférico de 8 bits conectado a las líneas de datos PB0 a PB7 de la misma PIA Nº 1.

El contador comienza a evolucionar a partir del valor de inicio al detectarse un flanco positivo sobre la línea CA1 de la PIA
Nº 0, lo que produce un pedido de interrupción sobre el uP que hace ejecutar la rutina de servicio correspondiente.
*/

; Inicialización de las PIAs
		ORG 1024h
		LD SP, 2047h
		LD A, FFh
		OUT (0d), A

		LD A, 00h
		OUT (8d), A
		OUT (11d), A

		LD A, 3d
		LD (1d), A

		JP INICIO
		FIN

; Rutina de servicio
		ORG 1748d
		PUSH AF
		PUSH BC
		PUSH DE
		PUSH HL
		PUSH IX
		PUSH IY

		IN A, (13d) ; fin conteo
		LD B, A
		IN A, (10d) ; inicio conteo
		
		LD C, A

FLANCO	IN A, (1d)
		BIT 7, A
		JR Z, FLANCO

		LD A, C

LOOP    OUT (2d), A
		CP B
		JP Z, FINLOOP

		PUSH AF
		PUSH BC

		LD L, 5d
		CALL DELAY

		POP BC
		POP AF

		INC A
		JP LOOP

FINLOOP POP IY
		POP IX
		POP HL
		POP DE
		POP BC
		POP AF
		RETI
		FIN