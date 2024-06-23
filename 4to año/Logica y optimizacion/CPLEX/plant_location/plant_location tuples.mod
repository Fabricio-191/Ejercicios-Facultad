using CP;

int nbCustomer = ...;
int nbLocation = ...;
range Customers = 0..nbCustomer-1;
range Locations = 0..nbLocation-1;
int cost[Customers][Locations] = ...;
int demand[Customers] = ...;
int fixedCost[Locations] = ...;
int capacity[Locations] = ...;;

int custValues[Customers] = ...;

dvar int cust[Customers] in Locations;
dvar int open[Locations] in 0..1;
dvar int load[l in Locations] in 0..capacity[l];

dexpr int obj = sum(l in Locations) fixedCost[l]*open[l]
  + sum(c in Customers) cost[c][cust[c]];

dexpr float occupancy = sum(c in Customers) demand[c]
  / sum(l in Locations) open[l]*capacity[l];

dexpr float minOccup = min(l in Locations)
  ((load[l] / (capacity[l]) + (1-open[l])));

execute {
	cp.addKPI(occupancy, "Occupancy");
	cp.addKPI(minOccup, "Min occupancy");
	cp.param.timeLimit = 30;
	cp.param.logPeriod = 10000;
}

minimize obj;

subject to {
	forall(l in Locations) open[l] == (load[l] > 0);
	pack(
		all(l in Locations) load[l],
		all(c in Customers) cust[c],
		all(c in Customers) demand[c]
	);
}

execute {
  	writeln("obj = " + obj);
}

tuple SolutionLocation {
	int load;
	int open;
}
tuple SolutionCustomer {
	int cust;
}

{SolutionCustomer} solutionCustomer = {<cust[i]> | i in Customers};
{SolutionLocation} solutionLocation = {<load[i], open[i]> | i in Locations};

main {
	thisOplModel.generate();
	var sol = new IloOplCPSolution();
	for (var c in thisOplModel.Customers)
		sol.setValue(thisOplModel.cust[c], thisOplModel.custValues[c]);

	cp.setStartingPoint(sol);
	cp.solve();
	thisOplModel.postProcess();
}
