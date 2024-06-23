/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Fabricio
 * Creation Date: 7 may. 2024 at 10:25:22
 *********************************************/

/*
Una empresa elabora tres tipos de bebidas utilizando zumo de piña y zumo de melocotón.
El  dueño de la empresa ha comprado 1.500 litros de zumo de piña y 2.000 de zumo de  melocotón.
Los litros de zumo requeridos en la fabricación de cada bebida vienen dados en la  siguiente tabla.  

					Bebida 1	Bebida 2	Bebida 3
Zumo de piña		6			3			3
Zumo de melocotón 	2 			3 			4


El precio de venta de cada bebida es 15 euros el litro.
El coste del zumo de piña es de 1 euro el  litro y 2 euros el litro de zumo de melocotón.
Se conoce que la demanda de bebidas asciende a  400 litros.  
Se pide maximizar el beneficio de la venta de bebidas.

valor de venta b1 = valor de venta b2 = valor de venta b3 =15
*/

// Definir las variables
dvar float+ x1; // cantidad de litros de bebida 1
dvar float+ x2; // cantidad de litros de bebida 2
dvar float+ x3; // cantidad de litros de bebida 3

maximize 15*x1 + 15*x2 + 15*x3;

subject to {
	x1 + x2 + x3 >= 400;
	6*x1 + 3*x2 + 3*x3 <= 1500;
	2*x1 + 3*x2 + 4*x3 <= 2000;
}