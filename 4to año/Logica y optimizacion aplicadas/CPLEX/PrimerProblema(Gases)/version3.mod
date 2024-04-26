/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Fabricio
 * Creation Date: 3 abr. 2024 at 18:35:26
 *********************************************/
{string} Productos = {"amoniaco", "cloruro_amonico"};
{string} Componentes = {"nitrogeno", "hidrogeno", "oxigeno"};

// Datos
float demanda[Productos][Componentes] = [[1, 3, 0], [1, 4, 1]];

float beneficio[Productos] = [40, 50];
float stock[Componentes] = [50, 180, 40];
// Variables de decisión
dvar float+ produccion[Productos];

// Función objetivo
maximize sum(p in Productos) beneficio[p] * produccion[p];

// Restricciones
subject to {
	forall(c in Componentes)
	  sum(p in Productos) demanda[p][c] * produccion[p] <= stock[c];
};