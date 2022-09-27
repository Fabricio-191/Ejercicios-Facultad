/*
Ejercicio 4:
Sobre las líneas PA0 y PA1 de la PIA1 se ingresan una combinación de valores lógicos generados por
sendas resistencias de pull-up gobernadas por las llaves L1 y L2. Sobre las líneas PA5, PA6 y PA7 de
la misma PIA1, se conectan tres diodos led D1, D2 y D3 respectivamente. Sobre la línea de entrada
CA1 de la misma PIA1 se introduce un “pulso negativo” cada vez que se acciona un pulsador P (llave
normalmente abierta) que también gobierna una resistencia de pull-up. Generar el programa de
inicialización para esta configuración y una rutina de servicio que, cada vez que se genere un flanco
positivo al despulsarse P, ejecute la siguiente tarea: los diodos led D1, D2 y D3 se deberán encender,
en función de los valores generados por las llaves L1 y L2, de acuerdo a la secuencia indicada en la
siguiente tabla

L2  L1
 0  0   Todos los leds permanecen apagados.
 0  1   Se encienden D1 y D3 simultaneamente y luego se enciende D2 repitiéndose este ciclo 10 veces y luego permanecen todos apagados.
 1  0   Se enciende primero D3, luego D2 y finalmente D1, repitiéndose este ciclo 20 veces y permaneciendo luego todos encendidos.
 1  1   Todos los leds permanecen encendidos.
*/

		ORG 1150d ; PROGRAMA DE INICIALIZACIÓN
		LD SP, 2000d
		LD A, 03d
		OUT (09d), A 		;habilitación de interrupciones y reconocimiento de interrupciones por flanco positivo sobre la línea CA1 de la PIA1.
		LD A, E0h 			; A = 11100000
		OUT (08d), A 		;PA5, PA6 y PA7 de la PIA1 definidas como salidas
		JP INICIO 			;el sistema operativo retoma el control a la espera de una orden.
		END


		ORG 1748d ; RUTINA DE SERVICIO
		;salvaguarda de los registros en memoria pila
		PUSH AF
		PUSH BC
		PUSH DE
		PUSH HL
		PUSH IX
		PUSH IY
		;lectura de las llaves L1 y L2
		IN A, (10d) 		;lectura de RDA
		AND A, 03d 			; A = 000000xx
		CP A, 0
		JP Z,CERO
		CP A, 1
		JP Z,UNO
		CP A, 2
		JP Z,DOS
		;prender todos los leds (L2 = 1 y L1 = 1)
TRES 	LD A,E0h 			; A = 11100000
		OUT (10d), A 		;los leds quedan encendidos
		JP FIN
		;apagar todos los leds (L2 = 0 y L1 = 0)
CERO 	LD A, 0
		OUT (10d), A 		;los leds quedan apagados
		JP FIN
		;los leds se encienden de acuerdo a la secuencia dada por L2 = 0 y L1 = 1
UNO 	LD C,10d 			;contador en decremento para realizar 10 veces el lazo OTRO1
OTRO1 	LD A,A0h 			; A = 10100000
		OUT (10d), A 		;se encienden los leds D1 y D3
		PUSH BC 			;salvaguarda del contenido actual del registro contador C
		CALL ESPERA 		;se invoca a una subrutina de retardo de tiempo (ESPERA)
		LD A,40h 			; A = 01000000
		OUT (10d), A 		;se enciende el led D2
		CALL ESPERA 		;se invoca a una subrutina de retardo de tiempo (ESPERA)
		POP BC 				;se recupera el contenido del registro C
		DEC C
		JP NZ,OTRO1
		LD A, 0
		OUT (10d), A 		;se apagan todos los leds
		JP FIN
		; los leds se encienden de acuerdo a la secuencia dada por L2 = 1 y L1 = 0
DOS 	LD B,20d 			;contador en decremento para realizar 20 veces el lazo OTRO2
OTRO2 	LD A,128d 			; A = 10000000
		OUT (10d), A 		;se enciende el led D3
		PUSH BC 			;salvaguarda del contenido actual del registro contador B
		CALL ESPERA 		;se invoca a una subrutina de retardo de tiempo (ESPERA)
		LD A,64d 			; A = 01000000
		OUT (10d), A 		;se enciende el led D2
		CALL ESPERA 		;se invoca a una subrutina de retardo de tiempo (ESPERA)
		LD A, 32d 			; A = 00100000
		OUT (10d), A 		;se enciende el led D1
		CALL ESPERA 		;se invoca a una subrutina de retardo de tiempo (ESPERA)
		POP BC 				;se recupera el contenido del registro B
		DEC B
		JP NZ, OTRO2
		LD A, E0h 			; A = 11100000
		OUT (10d), A 		;se encienden todos los leds
FIN 	POP IY
		POP IX
		POP HL
		POP DE
		POP BC
		POP AF
		RETI ;se retorna al programa que fue interrumpido.
		END

		ORG 1200d
ESPERA 	LD B, FFh
OTRA 	LD C, FFh
DECREC 	DEC C
		JP NZ, DECREC
		DEC B
		JP NZ, OTRA
		RET
		END