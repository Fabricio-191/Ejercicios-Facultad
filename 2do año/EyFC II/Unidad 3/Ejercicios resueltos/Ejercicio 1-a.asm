/*
Realizar programas de inicialización de interfases para obtener las siguientes configuraciones de las PIAs del sistema:

PIA Nº 0 Lado A:
· Líneas de datos PA0 a PA7: entradas
· Interrupciones provenientes de la línea CA1 reconocidas por flanco positivo y habilitadas para interumpir al uP.

PIA Nº 0 Lado B:
· Líneas de datos PB0 a PB7: salidas
· Línea CB2 definida como salida con estado estable en “1” PIA Nº 1: no usada
*/

			ORG 1024d 		; carga del programa a partir de la dirección 1024
			LD A, 03d
			OUT (01d), A 	; carga “1” en el bit 0 de RCA-PIA0 (habilitación de interrupciones) y “1” en el bit 1 de RCA-PIA0 (reconocimiento de interrupciones por flanco positivo).
			LD A, FFh
			OUT (03d), A 	; carga todos unos sobre el RSTDB-PIA0 (define PB0 a PB7 como salidas)
			LD A, 38h 		; A = 00111000
			OUT (04d), A 	; carga con “unos” los bits 3, 4 y 5 del RCB-PIA0 (línea CB2 definida como salida en estado “1”)
			JP INICIO 		; el sistema operativo retoma el control a la espera de una orden.
			END 			; fin del ensamblado