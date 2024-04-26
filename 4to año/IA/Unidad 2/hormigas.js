// @ts-nocheck
const ciudades = 'ABCDEF'.split('')
const n = ciudades.length;

const matrizDistancias = [
	[0, 5, 6, 7, 2, 3],
	[5, 0, 3, 6, 5, 2],
	[6, 3, 0, 3, 4, 2],
	[7, 6, 3, 0, 4, 5],
	[2, 5, 4, 4, 0, 3],
	[3, 2, 2, 5, 3, 0]
]

const matrizFeromonas = [
	[0, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 1, 1],
	[1, 1, 0, 1, 1, 1],
	[1, 1, 1, 0, 1, 1],
	[1, 1, 1, 1, 0, 1],
	[1, 1, 1, 1, 1, 0]
]

const RHO = 0.7, BETA = 1, ALFA = 2;

const k = 1;
const hormigas = [
	['FAECDBF', k/21],
	['CEFDABC', k/26],
	['EABDFCE', k/20]
];

function delta(i, j){
	const A = ciudades[i], B = ciudades[j];
	const str1 = A + B;
	const str2 = B + A;
	let acc = 0;

	for(const [camino, z] of hormigas){
		if(camino.includes(str1) || camino.includes(str2)) acc += z;
	}

	return acc;
}

function iter(cb, cant = 1){
	for(let c = 0; c < cant; c++){
		for(let i = 0; i < n; i++){
			for(let j = 0; j < n; j++){
				cb(i, j);
			}
		}
	}
}

iter((i, j) => {
	const anterior = matrizFeromonas[i][j];
	const nuevo = (1 - RHO) * anterior + delta(i, j);
	matrizFeromonas[i][j] = nuevo;
});

console.log(matrizFeromonas.map(x => x.map(x => x.toFixed(3)).join(' ')).join('\n'));

iter((i, j) => {
	const anterior = matrizFeromonas[i][j];
	const nuevo = (1 - RHO) * anterior + delta(i, j);
	matrizFeromonas[i][j] = nuevo;
});

console.log()
console.log(matrizFeromonas.map(x => x.map(x => x.toFixed(3)).join(' ')).join('\n'));

iter((i, j) => {
	const anterior = matrizFeromonas[i][j];
	const nuevo = (1 - RHO) * anterior + delta(i, j);
	matrizFeromonas[i][j] = nuevo;
});

console.log()
console.log(matrizFeromonas.map(x => x.map(x => x.toFixed(3)).join(' ')).join('\n'));

/*
0.000 0.388 0.300 0.338 0.398 0.348
0.388 0.000 0.338 0.398 0.300 0.348
0.300 0.338 0.000 0.348 0.436 0.350
0.338 0.398 0.348 0.000 0.300 0.388
0.398 0.300 0.436 0.300 0.000 0.338
0.348 0.348 0.350 0.388 0.338 0.000

0.000 0.205 0.090 0.140 0.217 0.152
0.205 0.000 0.140 0.217 0.090 0.152
0.090 0.140 0.000 0.152 0.267 0.155
0.140 0.217 0.152 0.000 0.090 0.205
0.217 0.090 0.267 0.090 0.000 0.140
0.152 0.152 0.155 0.205 0.140 0.000

0.000 0.150 0.027 0.080 0.163 0.093
0.150 0.000 0.080 0.163 0.027 0.093
0.027 0.080 0.000 0.093 0.216 0.097
0.080 0.163 0.093 0.000 0.027 0.150
0.163 0.027 0.216 0.027 0.000 0.080
0.093 0.093 0.097 0.150 0.080 0.000
*/