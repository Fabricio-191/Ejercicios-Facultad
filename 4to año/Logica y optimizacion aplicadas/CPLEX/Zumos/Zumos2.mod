/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Fabricio
 * Creation Date: 7 may. 2024 at 10:25:22
 *********************************************/

/*
Una empresa elabora tres tipos de bebidas utilizando zumo de pina y zumo de melocoton.
El  dueño de la empresa ha comprado 1.500 litros de zumo de pina y 2.000 de zumo de  melocoton.
Los litros de zumo requeridos en la fabricación de cada bebida vienen dados en la  siguiente tabla.  

					Bebida 1	Bebida 2	Bebida 3
Zumo de pina		6			3			3
Zumo de melocoton 	2 			3 			4


El precio de venta de cada bebida es 15 euros el litro.
El coste del zumo de pina es de 1 euro el  litro y 2 euros el litro de zumo de melocoton.
Se conoce que la demanda de bebidas asciende a  400 litros.  
Se pide maximizar el beneficio de la venta de bebidas.

valor de venta b1 = valor de venta b2 = valor de venta b3 =15
*/

// Definir las variables

tuple Bebida {
	string nom;
	float venta;
};

tuple Zumo {
	string nom;
	float stock;
};

tuple Demanda {
	string nomBebida;
	string nomZumo;
	float cant;
};

{Bebida} Bebidas = {
	<"b1", 15>,
	<"b2", 15>,
	<"b3", 15>
};

{Zumo} Zumos = {
	<"pina", 1500>,
	<"melocoton", 2000>
};

{Demanda} Demandas = {
	<"b1", "pina", 6>,  
	<"b1", "melocoton", 2>,  
	<"b2", "pina", 3>,  
	<"b2", "melocoton", 3>,  
	<"b3", "pina", 3>,  
	<"b3", "melocoton", 4>
};

dvar float+ produccion[Bebidas];

maximize sum(b in Bebidas) b.venta * produccion[b];

subject to {
	sum(b in Bebidas) produccion[b] >= 400;
	forall(z in Zumos)
		sum(b in Bebidas)
			sum(<b.nom, z.nom, cant> in Demandas) cant * produccion[b]
	<= z.stock;
};