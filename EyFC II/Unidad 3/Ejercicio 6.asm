/*
Cuatro dispositivos identificados como Dispositivo Nº 1, Nº 2, Nº 3 y Nº 4 están conectados al computador a través de la PIA0-A, PIA0-B, PIA1-A y PIA1-B respectivamente. 

Los dispositivos Nº 1 y Nº 2 son dispositivos de entrada y generan sus pedidos de interrupción para ser atendidos por el uP
por medio de flancos positivos que ingresan a través de las líneas CA1 y CB1 respectivamente.

El dispositivo Nº 3 es un dispositivo de entrada que dispondrá de dos rutinas de servicio distintas para su atención y por lo tanto generará dos pedidos de interrupción a través de las líneas CA1 y CA2, ambos reconocidos por flancos negativos.

El dispositivo Nº 4 es un dispositivo de salida, no genera pedidos de interrupción al uP y utiliza la línea CB2 como salida en valor estable “0”.

Generar el programa de inicialización de las PIAs para atender a los mencionados dispositivos y el
programa de encuestas de interrupciones para localizar las rutinas de servicio de cada dispositivo.
*/
			ORG 1000h
INICIO		OUT (0d), 00000000b
			OUT (1d), 00000011b

			OUT (3d), 00000000b
			OUT (4d), 00000011b
			
			OUT (8d), 00000000b
			OUT (9d), 00001001b

			OUT (11d), 11111111b
			OUT (12d), 00110000b
			; FALTA ALGO

			FIN


			ORG 2000h
RUTIN1  	EQU 2250d
RUTIN2  	EQU 2300d 
RUTIN2  	EQU 2350d
RUTIN3  	EQU 2400d 
RUTIN4  	EQU 2450d 
			PUSH AF
			PUSH BC
			PUSH DE
			PUSH HL
			PUSH IX
			PUSH IY

			
			;


FIN 		POP IY
			POP IX
			POP HL
			POP DE
			POP BC
			POP AF
			RETI ;retorno al programa que fue interrumpido
			END

