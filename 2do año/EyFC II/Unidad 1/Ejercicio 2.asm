/*
Ejercicio 2:

Desarrollar una secuencia de instrucciones para sumar los contenidos de los registros A, B, C y
D. Cargar el resultado en el registro D. Cargar el programa objeto a partir de la celda de memoria
de dirección 23CAh.
*/

ORG 23CAh
ADD A, B
ADD A, C
ADD A, D
LOAD D, A
END.
