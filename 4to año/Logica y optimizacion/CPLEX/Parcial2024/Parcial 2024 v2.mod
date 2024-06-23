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

tuple Anuncio {
  	float costo;
  	float probabilidad;
  	float minimo;
};

tuple DineroMaximo {
	float valor;  
};

{Anuncio} Anuncios = {
	<15000, 0.3, 26>,
	<30000, 0.7, 13>  
};

{DineroMaximo} DinerosMaximos = { <1000000> };

dvar float+ valores[Anuncios];

maximize sum(a in Anuncios) valores[a] * a.probabilidad;

subject to {
  	C1: forall(<maximo> in DinerosMaximos) 
  			sum(a in Anuncios) valores[a] * a.costo
  		<= maximo;
	C2: forall(a in Anuncios) valores[a] >= a.minimo;
};