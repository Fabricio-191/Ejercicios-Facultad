/*********************************************
 * OPL 22.1.1.0 Model
 * Author: NotebookExo
 * Creation Date: 8 abr. 2024 at 16:35:34
 *********************************************/

dvar int ViajesA;
dvar int ViajesB;

maximize ViajesA * 30000 + ViajesB * 20000;

subject to {
	ViajesA - ViajesB >= 1;
	ViajesA <= 120;
	ViajesA + ViajesB <= 200;
	ViajesA + ViajesB >= 60;
};