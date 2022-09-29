/*
Cuatro dispositivos identificados como Dispositivo Nº 1, Nº 2, Nº 3 y Nº 4 están conectados al computador a través de la PIA0-A, PIA0-B, PIA1-A y PIA1-B respectivamente. 

Los dispositivos Nº 1 y Nº 2 son dispositivos de entrada y generan sus pedidos de interrupción para ser atendidos por el uP
por medio de flancos positivos que ingresan a través de las líneas CA1 y CB1 respectivamente.

El dispositivo Nº 3 es un dispositivo de entrada que dispondrá de dos rutinas de servicio distintas para su atención y por lo tanto generará dos pedidos de interrupción a través de las líneas CA1 y CA2, ambos reconocidos por flancos negativos.

El dispositivo Nº 4 es un dispositivo de salida, no genera pedidos de interrupción al uP y utiliza la línea CB2 como salida en valor estable “0”.

Generar el programa de inicialización de las PIAs para atender a los mencionados dispositivos y el
programa de encuestas de interrupciones para localizar las rutinas de servicio de cada dispositivo.
*/
			ORG 1024h
			LD SP, 2047h

			LD A, 0d
			OUT (0d), A
			OUT (3d), A
			OUT (8d), A

			LD A, 3d
			OUT (1d), A
			OUT (4d), A
			
			LD A, 9d
			OUT (9d), A

			LD A, 48d
			OUT (12d), A

			LD A, 255d
			OUT (11d), A

			JP INICIO
			FIN


			ORG 1400h
RUTIN1  	EQU 1650d
RUTIN2  	EQU 1700d 
RUTIN3  	EQU 1750d
RUTIN4  	EQU 1800d 
			PUSH AF
			PUSH BC
			PUSH DE
			PUSH HL
			PUSH IX
			PUSH IY

			IN A, (1d)
			BIT 7, A
			JP Z, DISP2
			BIT 0, A
			JP Z, DISP2
			JP RUTIN1

DISP2		IN A, (4d)
			BIT 7, A
			JP Z, DISP3
			BIT 0, A
			JP Z, DISP3
			JP RUTIN2

DIPS3		IN A, (9d)
			BIT 7, A
			JP Z, CB
			BIT 0, A
			JP Z, CB
			JP RUTIN3
CB			BIT 6, A
			JP Z, FIN
			JP RUTIN4

FIN 		POP IY
			POP IX
			POP HL
			POP DE
			POP BC
			POP AF
			RETI ;retorno al programa que fue interrumpido
			END

