/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Fabricio Rubio
 * Creation Date: 8 may. 2024 at 16:25:46
 *********************************************/
/*
Una empresa está estudiando llevar a cabo una campaña publicitaria, para ello dispone de  1.000.000 de euros.
Puede difundir sus anuncios en dos canales publicitarios distintos,
el primero de  ellos cobra 15.000 euros cada vez que emite un anuncio,
mientras que el segundo cobra el doble.

La probabilidad de que un anuncio del primer canal sea visto es del 30 %,
mientras que del segundo es  del 70 %.

Como mínimo deben emitirse 26 anuncios en el primer canal y 13 en el segundo.  
*/

dvar float+ x1;
dvar float+ x2;

maximize x1 * 0.3 + x2 * 0.7;

subject to {
	C1: x1 * 15000 + x2 * 30000 <= 1000000;
	C2: x1 >= 26;
	C3: x2 >= 13;
};
// 22.0333333
// 21.8333333

execute {
	if(cplex.getCplexStatus() == 1){
		writeln("precio sombra de C1: ", C1.dual);
		writeln("precio sombra de C2: ", C2.dual);
		writeln("precio sombra de C3: ", C3.dual);

		writeln("slack de C1: ", C1.slack);
		writeln("slack de C2: ", C2.slack);
		writeln("slack de C3: ", C3.slack);
		
		writeln("costo reducido x1: ", x1.reducedCost);
		writeln("costo reducido x2: ", x2.reducedCost);
	}
};