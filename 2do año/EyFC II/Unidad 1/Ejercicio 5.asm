/*
Ejercicio 5 (Resuelto):

Realizar la suma de dos números de 3 bytes (a23, a22,…… a1, a0) y (b23, b22,….. b1, b0) que
se encuentran almacenados en distintos lugares de memoria, uno a partir de la dirección 0300h
y el otro a partir de la dirección 3FF0h. Almacenar el resultado en memoria a partir de la
dirección 4731h.

Tener en cuenta que la suma de los bytes menos significativos (a0… a7) y (b0…. b7) debe
realizarse sin acarreo (con una instrucción ADD o bien con una ADC habiendo colocado
previamente el bit de acarreo del registro de estado a cero, C=0) y los bytes restantes se deben
sumar con acarreo, es decir, con una instrucción ADC.
*/