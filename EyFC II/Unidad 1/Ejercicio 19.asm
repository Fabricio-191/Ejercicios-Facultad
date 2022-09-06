/*
Realizar en Assembler una subrutina parametrada que realice la sumatoria de un conjunto de
datos. Los datos se encuentran almacenados a partir de la dirección de memoria B34Ah, la tabla
tiene 30 datos de 8 bits almacenados en forma consecutiva en memoria. La dirección de
comienzo de la subrutina estará dada por la etiqueta “SUMAR” y los parámetros de la misma
vendrán dados por los contenidos de los registros:
• HL: dirección de comienzo de la tabla.
• B: Contiene la cantidad de datos de la tabla.
• E: Contiene la sumatoria del conjunto de datos.
Desarrollar un programa en Assembler que invoque a la subrutina del apartado anterior y luego
analice el resultado obtenido de la sumatoria. Si el resultado obtenido es menor a 100 cargar la
tabla de datos con los valores 1, 2, 3,…, 30 (cargar la tabla de datos desde 1 hasta 30), caso
contrario almacenar el resultado de la sumatoria en la dirección de memoria 4731h.
La dirección en memoria para la carga del programa objeto es B4A0h.
*/

			ORG SUMAR
SUBRUTINA:	LD E, 0d
LOOP:		LD A, (HL)

			ADD A, E
			LD E, A
			INC HL

			DJNZ LOOP
			RET

			ORG B4A0h
INICIO: 	LD HL, B34Ah
			LD B, 30d

			PUSH HL
			PUSH BC
			CALL SUBRUTINA
			POP BC
			POP HL

			CP 100d
			JP M, ABC
		
			LD (4731h), E
END:		END INICIO


			ORG C412H
ABC:		LD SP, FFFFh
			LD C, 1d
LOOP:		LD (HL), C
			INC HL
			INC C

			DJNZ LOOP

			JP END
