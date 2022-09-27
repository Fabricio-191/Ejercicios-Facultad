/*
Realizar una rutina de encuesta de interrupciones para determinar cuál de dos periféricos de entrada
conectados al computador ha generado el pedido. El 1º de los periféricos está conectado a la PIA0 lado
A y el 2º a la PIA1 lado B; estos periféricos ingresan los pedidos de interrupciones por las líneas CA1
y CB1 respectivamente. Las rutinas de servicio para el 1º y 2º periférico están cargadas en memoria
RAM a partir de las direcciones de memoria 1850d y 1900d respectivamente
*/

			ORG 1748d ;carga del programa a partir de la dirección 1748d
RUTIN1  	EQU 1850d
RUTIN2  	EQU 1900d 
			PUSH AF ;salvaguarda de los registros en memoria pila
			PUSH BC
			PUSH DE
			PUSH HL
			PUSH IX
			PUSH IY
			;testeo del bit 7 del Registro de Control del lado A de la PIA0 (bandera de interrupción IRQA1)
			IN A, (01d)
			BIT 7, A ;Testeo de IRQA1
			; ********
			JP Z, ENC2
			BIT 0, A ;Testeo de la máscara de interrupción
			JP NZ, RUTIN1 ;salta a la rutina de servicio del 1º periférico si la bandera IRQA1 está activada y la interrupción está habilitada (no enmascarada)

			;testeo del bit 7 del Registro de Control del lado B de la PIA1 (bandera de interrupción IRQB1)
ENC2    	IN A, (12d)
			BIT 7, A
			JP Z, FIN
			BIT 0, A
			JP NZ, RUTIN2 ;salta a la rutina de servicio del 2º periférico si la bandera IRQB1 está activada y la interrupción está habilitada (no enmascarada)
			
			;recuperación de los contenidos de los registros salvaguardados en memoria pila.
FIN 		POP IY
			POP IX
			POP HL
			POP DE
			POP BC
			POP AF
			RETI ;retorno al programa que fue interrumpido
			END

			ORG 1850d
RUTIN1 		


			POP IY
			POP IX
			POP HL
			POP DE
			POP BC
			POP AF
			RETI
			END



			ORG 1900d
RUTIN2  	

			POP IY
			POP IX
			POP HL
			POP DE
			POP BC
			POP AF
			RETI
			END