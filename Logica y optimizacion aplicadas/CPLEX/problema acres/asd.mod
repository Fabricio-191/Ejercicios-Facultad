/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Fabricio
 * Creation Date: 10 abr. 2024 at 17:07:44
 *********************************************/
/*
El problema de los Tomates, Pimientos y Espinacas
Un granjero tiene 600 acres de terreno y desea determinar el número de acres que asignará a cada una
de las tres cosechas siguientes: tomates, pimientos y espinacas. Los días hombre, el coste de
preparación y la ganancia por acre de cada una de las cosechas se muestran en la tabla siguiente:

Cosecha Días hombre Coste preparación Beneficio
Tomates 5 12 6
Pimientos 8 18 12
Espinacas 13 14 10

Suponga que el número de días hombre disponibles es de 4.000, y que el granjero tiene 6.000 euros
para preparación.

1. Determinar que cantidad acres de tomates, que cantidad de acres pimientos y que cantidad de
acres de espinacas se deben producir para obtener el máximo beneficio
2. Determine si conviene contratar ayuda adicional a 6 euros por hora. Suponga una jornada
laboral de 8 horas.
3. Según la solución obtenida cual es la incidencia de producir un acre de tomate, ¿ se incrementa
o se reduce el beneficio, en cuanto ?
4. Suponga que el granjero tiene un contrato para entregar al menos el equivalente a 200 acres
de tomate, cuál sería la nueva solución óptima.
5. Determinar a partir de que precio del acre de tomate, combiene comenzar a producir, y cual
es la solución que arroja al insertar en el modelo dicho precio,
*/
{string} cultivos = {"Tomates", "Pimientos", "Espinacas"};
int diasHombre[cultivos] = [5, 8, 13];
int costePreparacion[cultivos] = [12, 18, 14];
int beneficio[cultivos] = [6, 12, 10];

dvar float+ acres[cultivos];
// dvar boolean contratarAyuda;

maximize sum(i in cultivos) beneficio[i] * acres[i];

subject to {
  C1: sum(i in cultivos) diasHombre[i] * acres[i] <= 4000;
  C2: sum(i in cultivos) costePreparacion[i] * acres[i] <= 6000;
  C3: sum(i in cultivos) acres[i] <= 600;
  // C4: acres["Tomates"] >= 200;
}

// Performing sensitivity analysis
execute {
	if(cplex.getCplexStatus() == 1){
	  	
	  	writeln("constraints")
		writeln("        dual    slack     upper bound    lower bound")
		writeln("C1: ", C1.dual, '  ', C1.slack, '  ', C1.UB, '  ', C1.LB);
		writeln("C2: ", C2.dual, '  ', C2.slack, '  ', C2.UB, '  ', C2.LB);
		writeln("C3: ", C3.dual, '  ', C3.slack, '  ', C3.UB, '  ', C3.LB);
		
		// for all constraint in the model write the dual value, slack, upper bound and lower bound
		
	  	writeln("dvars")
		writeln("        priority    reduced cost    solution value     upper bound    lower bound")
		writeln("costos oportunidad de X1: ", acres['Tomates'].reducedCost);
		writeln("costos oportunidad de X2: ", acres['Pimientos'].reducedCost);
		writeln("costos oportunidad de X3: ", acres['Espinacas'].reducedCost);
		
		writeln("si produzo un acre de tomates el beneficio deberia ser: ", cplex.getObjValue() + acres['Tomates'].reducedCost);
		writeln("Para producir tomates el precio debe ser superior a: ", 6 - acres['Tomates'].reducedCost);
	}
}

