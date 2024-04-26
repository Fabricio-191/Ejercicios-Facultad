/*
Ejercicio 5:
Realizar un programa de inicialización de interfases para obtener las siguientes configuraciones de las
PIAs del sistema:
· Líneas PA0 a PA5 de la PIA0 salidas y PA6 y PA7 entradas.
· Interrupciones provenientes de la línea CA1 de la PIA0 reconocidas por flanco negativo y deshabilitadas para interrumpir al uP.
· Línea CA2 de la PIA0 definida como salida y en estado “1”

· Líneas PB0 a PB7 de la PIA0: salidas.
· Línea CB2 de la PIA0 definida como salida y en estado “0”
*/

		ORG 1024d
		LD A, 63d ;00111111b
		OUT (0d), A
		LD A, 56d ; 00111000b
		OUT (1d), A

		LD A, 255d ;11111111b
		OUT (3d), A
		LD A, 48d ;00110000b
		OUT (4d), A

		JP INICIO
		FIN