/*********************************************
 * OPL 22.1.1.0 Model
 * Author: NotebookExo
 * Creation Date: 8 abr. 2024 at 15:56:26
 *********************************************/
{string} Productos = {"loteA", "loteB"};
{string} Componentes = {"platano", "manzana", "naranja"};

float demanda[Productos][Componentes] = [[1, 2, 1], [1, 1, 2]];

float beneficio[Productos] = [1200, 1400];
float stock[Componentes] = [500, 800, 800];

// Variables de decisión
dvar float+ produccion[Productos];

maximize sum(p in Productos) beneficio[p] * produccion[p];

// Restricciones
subject to {
    forall(c in Componentes)
        sum(p in Productos) demanda[p][c] * produccion[p] <= stock[c];
};