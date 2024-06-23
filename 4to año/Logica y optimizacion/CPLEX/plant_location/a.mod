//Descripcion del Problema
//plant_location
// -------------------
// Una empresa de construcción naval tiene un número determinado de clientes. Cada cliente recibe
// por exactamente una planta. A su vez, una planta puede abastecer a varios clientes. El problema es
// decidir dónde instalar las plantas para poder abastecer a cada cliente minimizando
// el costo de construcción de cada planta y el costo de transporte para abastecer a los clientes.
// Para cada posible ubicación de la planta existe un costo fijo y una capacidad de producción.
// Ambos tienen en cuenta el país y las condiciones geográficas.
// Para cada cliente existe una demanda y un costo de transporte con respecto a
// ubicación de cada planta.

using CP;

int nbCustomer = ...;
int nbLocation = ...;
range Customers = 0..nbCustomer-1;
range Locations = 0..nbLocation-1;
int cost[Customers][Locations] = ...;

tuple CustomerData {
	int demand;
  	int custValue;
}
CustomerData customersData[Customers] = ...;

tuple LocationData {
	int fixedCost;
  	int capacity;
}
LocationData locationsData[Locations] = ...;

dvar int cust[Customers] in Locations;
dvar int open[Locations] in 0..1;
dvar int load[l in Locations] in 0..locationsData[l].capacity;

dexpr int obj = sum(l in Locations) locationsData[l].fixedCost * open[l]
  + sum(c in Customers) cost[c][cust[c]];

dexpr float occupancy = (sum(c in Customers) customersData[c].demand) / sum(l in Locations) open[l] * locationsData[l].capacity;

dexpr float minOccup = min(l in Locations)
	((load[l] / (locationsData[l].capacity) + (1-open[l])));

execute {
  cp.addKPI(occupancy, "Occupancy");
  cp.addKPI(minOccup, "Min occupancy");
  cp.param.timeLimit = 10;
  cp.param.logPeriod = 10000;
}

minimize obj;
subject to {
  forall(l in Locations)
    open[l] == (load[l] > 0);
  pack(all(l in Locations) load[l],
       all(c in Customers) cust[c],
       all(c in Customers) customersData[c].demand);
}

execute {
  writeln("obj = " + obj);
}
main{
	thisOplModel.generate();
	var sol=new IloOplCPSolution();
	for (var c in thisOplModel.Customers)
		sol.setValue(thisOplModel.cust[c],thisOplModel.customersData[c].custValue);
	cp.setStartingPoint(sol);
	cp.solve();
	thisOplModel.postProcess();
}


// [17, 27, 26, 1, 13, 11, 29, 28, 17, 18, 7, 22, 1, 15, 28, 27, 17, 1, 0, 14, 22, 19, 26, 20, 2, 25, 2, 7, 12, 22, 12, 20, 17, 15, 13, 11, 3, 18, 12, 27, 16, 2, 18, 0, 1, 20, 25, 14, 14, 18, 29, 8, 1, 0, 19, 12, 8, 12, 29, 16, 9, 22, 9, 0, 18, 7, 15, 23, 13, 13, 3, 11, 19, 26, 16, 18, 23, 3, 9, 23, 26, 11, 28, 18, 25, 7, 27, 27, 2, 16]
// [136, 122, 86, 125, 0, 0, 0, 157, 54, 133, 0, 119, 184, 86, 105, 111, 177, 107, 188, 93, 80, 0, 159, 123, 0, 49, 177, 177, 107, 89]
// [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
