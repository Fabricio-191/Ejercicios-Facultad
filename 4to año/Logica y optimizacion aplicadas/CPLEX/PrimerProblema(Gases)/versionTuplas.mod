tuple Producto {
	string nombre;
	float beneficio;
};

tuple Componente {
	string nombre;
	float stock;
};

tuple Demanda {
  	key string nomProd;
  	key string nomComp;
  	float cant;
};

{Producto} Productos = {
	<"amoniaco", 40>,
	<"cloruro_amonico", 50>
};
 
{Componente} Componentes = {
	<"nitrogeno", 50>,
	<"hidrogeno", 180>,
	<"oxigeno", 40>
};

{Demanda} Demandas = {
	<"amoniaco", "nitrogeno", 1>,  
	<"amoniaco", "hidrogeno", 3>,  
	<"amoniaco", "oxigeno", 0>,  
	<"cloruro_amonico", "nitrogeno", 1>,  
	<"cloruro_amonico", "hidrogeno", 4>,  
	<"cloruro_amonico", "oxigeno", 1>
};

dvar float+ produccion[Productos];


// Función objetivo
maximize sum(p in Productos) p.beneficio * produccion[p];
// [20, 30]

subject to {
  forall(c in Componentes)
    sum(p in Productos)
      sum(<p.nombre, c.nombre, cant> in Demandas) cant * produccion[p] <= c.stock;
};