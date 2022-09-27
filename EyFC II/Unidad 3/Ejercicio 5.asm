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

		ORG 1000h
INICIO  NOP

		OUT (0d), 63d ;00111111b
		OUT (1d), 56d ;00111000b

		OUT (3d), 255d ;11111111b
		OUT (4d), 48d ;00110000b
		FIN