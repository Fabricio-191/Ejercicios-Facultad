/*
Ejercicio 1: (Resuelto)

Realizar la suma de dos números de 8 bits. Los números se encuentran almacenados consecutivamente en memoria a partir de la celda de memoria de dirección 02A1h y el resultado se almacenará en la celda contigua a los sumandos. Cargar el programa objeto a partir de la celda de memoria de dirección 0505h.

Resolveremos este simple problema presentando tres soluciones alternativas que muestran distintas formas de acceder a los datos almacenados en memoria (distintos modos de direccionamiento). La siguiente figura muestra la estructura de los datos en memoria y la ubicación en memoria del programa objeto correspondiente a la solución alternativa a).
*/

ORG 0505h 		; carga el programa a partir de la dirección de memoria 0505h
LD A, (02A1h) 	; carga el acumulador con el sumando 1
LD B, A			; B <-- A, carga el registro B con el sumando 2
LD A, (02A2h) 	; carga el acumulador con el sumando 2
ADD A, B 		; A <-- A+B, realiza la suma de los datos y almacena el resultado en acumulador
LD (02A3h), A 	; almacena el resultado en la celda de memoria de dirección 02A3h
END.


ORG 0505h
LD HL, 02A1h	; carga el par registro HL con la dirección de memoria
				; donde se encuentra el sumando 1 (HL apunta a sumando 1)
LD A, (HL)  	; carga en A el contenido de la celda de memoria cuya
				; dirección está apuntada por HL (carga en A el sumando 1)
INC HL 			; incremento en 1 el contenido de HL (HL apunta a sumando2)
ADD A, (HL)		; suma el contenido de A (sumando 1) con el contenido
				; de la celda de memoria apuntada por HL (sumando2).
				; el resultado queda almacenado en A.
INC HL 			; HL apunta a la celda de memoria de dirección 02A3h
				; donde se debe almacenar el resultado de la suma
LD (HL), A 		; almacena el resultado en la celda de memoria apuntada por HL
END.


ORG 0505h
LD IX, 02A1h 	; carga el registro índice IX con la dirección de  memoria donde se encuentra el sumando 1
LD A, (IX+00) 	; carga en A el sumando 1 (IX+00 apunta a la celda de memoria que contiene el sumando 1)
ADD A, (IX+01) 	; suma el contenido de A (sumando 1) con el sumando 2 (IX+01) apunta a la celda de memoria sumando 2).
				; El resultado queda en A
LD (IX+02), A 	; almacena el resultado en la celda de memoria ubicada 2 bytes más abajo que la posición señalada por IX+00.
				; (02A3h) + A
END.