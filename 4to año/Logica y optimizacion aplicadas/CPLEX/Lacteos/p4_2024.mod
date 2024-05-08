/*********************************************
 * OPL 22.1.1.0 Model
 * Author: NotebookExo
 * Creation Date: 17 abr. 2024 at 18:53:18
 *********************************************/

dvar float+ X1;
dvar float+ X2;
dvar float+ X3;

maximize 5 * X1 + 7 * X2 + 3 * X3;

subject to {
	C1: 4 * X1 + 3 * X2 + 2 * X3 <= 75;  // consumo leche
	C2:     X1 + 2 * X2 + 3 * X3 <= 100; // consumo nata
	C3:     X1 +     X2 +     X3 >= 20;  // cantidad general
	// C3:     X1 + 2 * X2 + 4 * X3 <= 30
}

/*
Con estos datos determine:  
1. El plan de producción si en lugar de disponer de 75 unidades de leche dispone únicamente de 50.  
2. Calcule los precios sombra.  
3. Cómo se verá afectado el plan de producción si un convenio firmado con los 
 productores de leche obliga a utilizar las 75 unidades de leche disponibles. 
4. A qué precio resulta interesante vender helados del tipo 1.  
5. A qué precio resulta interesante vender helados del tipo 3.  
6. El precio a partir del cual no resulta interesante producir 25 helados del tipo 2.
7. La dirección está estudiando la posibilidad de dedicar un empleado a realizar tareas de  control de calidad.
Preguntado por el tiempo necesario para realizarlo ha contestado  que si todos los helados fuesen del tipo 1 podría examinar hasta 30,
mientras que los  helados del tipo 2 necesitan el doble que los de tipo 1, y los del tipo 3 el doble que los  del tipo 2.
Si realiza el control de calidad la dirección no considera necesario mantener  la producción mínima de 20 helados.
Que restricción debería cambiar y como quedaría  el modelo. si la nueva solución alcanza un beneficio 123 euros. 

 X1 +    2 * X2 +    4 * X3 <= 30
*/

// X1 = 0; X2 = 25; X3 = 0; 175

// Las ganancias se reducen en 58.33333$

// precio sombra X1 = 5 + 4.33333 = 9.3333
// precio sombra X2 = 7 + 0
// precio sombra X3 = 3 + 1.66667 = 4.6667

// No cambia nada por que se utilizan siempre 75 unidades de leche

// A 9.3333$

// A 4.6667$

// A partir de 4.5$





