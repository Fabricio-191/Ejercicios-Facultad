/*********************************************
 * OPL 22.1.1.0 Model
 * Author: NotebookExo
 * Creation Date: 8 abr. 2024 at 16:10:25
 *********************************************/
/*********************************************
 * OPL 22.1.1.0 Model
 * Author: NotebookExo
 * Creation Date: 8 abr. 2024 at 15:56:26
 *********************************************/
{string} Productos = ...;
{string} Componentes = ...;

float costo[Productos] = ...;
float porcentaje[Productos][Componentes] = ...;
float cantidad[Componentes] = ...;

dvar float+ produccion[Productos];

minimize sum(p in Productos) costo[p] * produccion[p];

// Restricciones
subject to {
	forall(c in Componentes)
		sum(p in Productos) produccion[p] * porcentaje[p][c] >= cantidad[c];
};