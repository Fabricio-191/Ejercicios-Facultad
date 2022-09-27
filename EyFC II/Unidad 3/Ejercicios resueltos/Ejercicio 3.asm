/*
Se pretende cargar en la memoria del computador una serie de datos de 8 bits provenientes de un
periférico conectado al lado A de la PIA Nº 0. Los datos comenzarán a ser transferidos a partir del
momento en que el periférico realice un pedido de interrupción generando un flanco positivo sobre la
línea CA1. El periférico genera un “pulso negativo” cada vez que un dato está listo en su salida para
ser leído por el computador; el flanco negativo de este pulso será leído a través de la línea CA2
(definida como entrada). El ingreso de datos finaliza al ingresarse el dato FFh. Esto debe indicarse al
exterior mediante el encendido de 3 diodos led D1, D2 y D3 conectados a las salidas de datos PB0,
PB1 y PB2 respectivamente; los mismos serán encendidos en la siguiente secuencia: D1, D2, D3.
Realizar el programa de inicialización de la PIA0 y la rutina de servicio capaz de efectuar esta tarea
almacenando dichos datos a partir de la dirección de memoria 1050d.
*/


			; PROGRAMA DE INICIALIZACIÓN
			ORG 1024d
			LD SP, 2047d
			LD A, 03d
			OUT (01), A 	; habilitación de interrupciones y reconocimiento de interrupciones por flanco positivo sobre la línea CA1.
			LD A, 07d
			OUT (03d), A 	; PB0 a PB2 de la PIA0 definidas como salidas
			JP INICIO
			END



			; RUTINA DE SERVICIO
			ORG 1748d
			;salvaguarda de los registros en memoria pila
			PUSH AF
			PUSH BC
			PUSH DE
			PUSH HL
			PUSH IX
			PUSH IY
			LD IX, 1050d 	;el registro IX apunta al comienzo de la tabla de datos a cargar
			;detección del flanco negativo de la línea de entrada CA2
LEER1 		IN A,	(01d)
			BIT 6, A
			JP Z, LEER1
			;lectura del dato del periférico y almacenamiento en memoria
			IN A, (02d) 	;al leerse el registro RDA, el bit 6 del registro RCA (bandera IRQA2) se pone en “0”.
			LD (IX+00), A 	;almacenamiento en memoria
			INC IX 			;IX apunta a la próxima celda de memoria para almacenar el próximo dato
			CP FFh
			JP Z, FIN 		;si es el último dato salgo del lazo y salto a encender los leds
			JP LEER1 		;salta a leer el próximo dato
FIN 		LD C, 03d 		;contador en decremento para realizar 3 veces el lazo OTRO
			LD A, 01d
OTRO 		OUT (05d), A 	;se enciende el led correspondiente (D1 en la primer pasada, D2 en la segunda y D3 en la tercera) y permanece encendido hasta que se actualice el valor del registro RDB
			;retardo de tiempo durante el cual el led correspondiente se mantendrá encendido
			LD D, FFh
ESPERA 		LD B, FFh
DECRE 		DEC B
			JP NZ, DECRE
			DEC D
			JP NZ, ESPERA
			SLA A 			;desplazamiento a la izquierda del acumulador
			DEC C
			JP NZ,OTRO
			LD A,00
			OUT (05d),A 	;se mantienen apagados todos los leds
			;recuperación de los contenidos de los registros salvaguardados en memoria pila
			POP IY
			POP IX
			POP HL
			POP DE
			POP BC
			POP AF
			RETI 			;retorno al programa que fue interrumpido
			END