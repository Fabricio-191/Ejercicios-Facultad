/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Fabricio
 * Creation Date: 3 abr. 2024 at 18:30:01
 *********************************************/
{string} Productos = {"amoniaco","cloruro_amonico"};
// Variables de decisión
dvar float+ produccion[Productos];

// Función objetivo
maximize 40 * produccion["amoniaco"] + 50 * produccion["cloruro_amonico"];

// Restricciones
subject to {
	produccion["amoniaco"] + produccion["cloruro_amonico"] <= 50;
	3 * produccion["amoniaco"] + 4 * produccion["cloruro_amonico"] <= 180;
	produccion["cloruro_amonico"] <= 40;
};