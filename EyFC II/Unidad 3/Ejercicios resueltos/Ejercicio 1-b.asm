/*
Realizar programas de inicialización de interfases para obtener las siguientes configuraciones de las PIAs del sistema:

PIA Nº 1 Lado A:
· Líneas de datos PA0 a PA3: entradas
· Líneas de datos PA4 a PA7: salidas
· Interrupciones provenientes de la línea CA1 reconocidas por flanco negativo y habilitadas para interumpir al uP.
· Línea CA2 definida como salida con estado estable en “0”

PIA Nº 1 Lado B:
· Líneas de datos PB0 a PB7: salidas

PIA Nº 0: no usada
*/

			ORG 1060d 		; carga del programa a partir de la dirección 1060
INICIO		LD A, F0h 		; A = 11110000
			OUT (08d), A	; PA0 a PA3: entradas y PA4 a PA7: salidas para la PIA1
			LD A, 31h 		; A = 00110001
			OUT (09d), A 	; interrupciones provenientes de la línea CA1 reconocidas por flanco negativo y habilitadas para interumpir al uP y línea CB2 definida como salida con estado estable en “0”
			LD A, FFh 		; A = 11111111
			OUT (11d), A 	; PB0 a PB7: salidas para la PIA1
			JP INICIO 		; el sistema operativo retoma el control a la espera de una orden.
			END 			; fin del ensamblado