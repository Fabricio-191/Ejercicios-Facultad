// @ts-nocheck
import prisma from "./prisma";
  
import { readFileSync } from "fs";

const str = readFileSync("./db/data.dat", "utf-8");

function encodeDat(clients: Client[], locations: LocationA[], locationClients: LocationClient[]): string {
	const cost: number[][] = [];

	for(let i = 0; i < clients.length; i++){
		cost.push([]);
		for(let j = 0; j < locations.length; j++){
			const lc = locationClients.find(lc => lc.clientId === clients[i].id && lc.locationId === locations[j].id);
			cost[i].push(lc ? lc.cost : 0);
		}
	}

	return `
nbCustomer = ${clients.length};
nbLocation = ${locations.length};
demand = [${clients.map(c => c.demand).join(', ')}];
custValues = [${clients.map(c => c.custValue).join(', ')}];
fixedCost = [${locations.map(l => l.fixedCost).join(', ')}];
capacity = [${locations.map(l => l.capacity).join(', ')}];
cost = [${
	cost.map(x => `[${x.join(', ')}]`).join(', ')
}];`;
}

function decodeDat(str: string): object {
	const obj: Record<string, unknown> = {};

	const variables = str.split(';');
	variables.pop();

	for(const variable of variables) {
		const [name, value] = variable.split('=') as [string, string];
		obj[name.trim()] = JSON.parse(value);
	}

	return obj;
}

async function main(){
	const data = decodeDat(str);

	console.log(data);

	const clientsN = data.nbCustomer as number;
	const locationsN = data.nbLocation as number;

	await prisma.client.deleteMany();
	await prisma.location.deleteMany();
	await prisma.locationClient.deleteMany();

	const clientPromises = [];
	for(let i = 0; i < clientsN; i++){
		clientPromises.push(prisma.client.create({
			data: {
				demand: data.demand[i] as number,
				custValue: data.custValues[i] as number,
			}
		}));
	}

	await prisma.$transaction(clientPromises);

	const locationPromises = [];
	for(let i = 0; i < locationsN; i++){
		locationPromises.push(prisma.location.create({
			data: {
				fixedCost: data.fixedCost[i] as number,
				capacity: data.capacity[i] as number,
			}
		}));
	}

	await prisma.$transaction(locationPromises);

	const clients = await prisma.client.findMany();
	const locations = await prisma.location.findMany();
	const locationClientsPromises = [];
	for(const client of clients){
		for(const location of locations){
			locationClientsPromises.push(prisma.locationClient.create({
				data: {
					clientId: client.id,
					locationId: location.id,
					cost: data.cost[client.id - 1][location.id - 1] as number,
				}
			}))
		}
	}

	await prisma.$transaction(locationClientsPromises);
}

main()
	.then(() => prisma.$disconnect())
	.then(() => {
		console.log("Base de datos cargada correctamente");
		process.exit(0);
	})
	.catch(async (e) => {
		console.log("Troleaste, la base de datos no se cargo correctamente")
		console.error(e);
		await prisma.$disconnect();
		process.exit(1);
	});