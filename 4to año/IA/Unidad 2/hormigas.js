// @ts-nocheck
const ciudades = 'ABCDEF'.split('')
const n = ciudades.length;

const mostarMatriz = (matriz) => console.log(matriz.map(x => x.map(x => x.toFixed(5)).join(' ')).join('\n'));

const matrizDistancias = [
	[0, 5, 6, 7, 2, 3],
	[5, 0, 3, 6, 5, 2],
	[6, 3, 0, 3, 4, 2],
	[7, 6, 3, 0, 4, 5],
	[2, 5, 4, 4, 0, 3],
	[3, 2, 2, 5, 3, 0]
];

const deltaFeromonas = [
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0]
];

const matrizFeromonas = [
	[0, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 1, 1],
	[1, 1, 0, 1, 1, 1],
	[1, 1, 1, 0, 1, 1],
	[1, 1, 1, 1, 0, 1],
	[1, 1, 1, 1, 1, 0]
];

const matrizProbabilidades = [
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0]
];

const RHO = 0.7, BETA = 1, ALFA = 2;
const k = 1;

const caminosHormigas = [
	'FAECDBF',
	'CEFDABC',
	'EABDFCE'
].map(camino => {
	let cost = 0;
	for(let i = 0; i < camino.length - 1; i++){
		const A = ciudades.indexOf(camino[i]);
		const B = ciudades.indexOf(camino[i + 1]);
		cost += matrizDistancias[A][B];
	}

	return [camino, k / cost];
})

for(let i = 0; i < n; i++){
	for(let j = i + 1; j < n; j++){
		const A = ciudades[i], B = ciudades[j];
		const str1 = A + B;
		const str2 = B + A;
		let acc = 0;
		
		// ARREGLAR
		for(const [camino, z] of caminosHormigas){
			if(camino.includes(str1) || camino.includes(str2)) acc += z;
		}

		deltaFeromonas[i][j] = deltaFeromonas[j][i] = acc;
	}
}

console.log('Delta feromonas')
mostarMatriz(deltaFeromonas);

function iter(cb){
	for(let i = 0; i < n; i++){
		for(let j = 0; j < n; j++){
			cb(i, j);
		}
	}
}

for(let i = 0; i < 1; i++){
	iter((i, j) => {
		const anterior = matrizFeromonas[i][j];
		const nuevo = (1 - RHO) * anterior + deltaFeromonas[i][j];
		matrizFeromonas[i][j] = nuevo;
	});
	
	console.log();
	console.log('Matriz feromonas');
	mostarMatriz(matrizFeromonas);

	// let sum = 0;
	// iter((i, j) => {
	// 	if(i === j) return;
	// 	sum += Math.pow(matrizFeromonas[i][j], ALFA) *
	// 			Math.pow(1 / matrizDistancias[i][j], BETA)
	// });
	
	// iter((i, j) => {
	// 	if(i === j) return;
	// 	const numerador = Math.pow(matrizFeromonas[i][j], ALFA) *
	// 		Math.pow(1 / matrizDistancias[i][j], BETA);
	// 	matrizProbabilidades[i][j] = numerador / sum;
	// });

	for(let i = 0; i < n; i++){
		let denominador = 0;
		for(let j = 0; j < n; j++){
			if(i === j) continue;
			denominador += Math.pow(matrizFeromonas[i][j], ALFA) *
				Math.pow(1 / matrizDistancias[i][j], BETA);
		}

		for(let j = 0; j < n; j++){
			if(i === j) continue;
			const numerador = Math.pow(matrizFeromonas[i][j], ALFA) *
				Math.pow(1 / matrizDistancias[i][j], BETA);

			matrizProbabilidades[i][j] = numerador / denominador;
		}
	}

	console.log();
	console.log('Matriz probabilidades');
	mostarMatriz(matrizProbabilidades);
}




/*
0,00000 0,16165 0,08453 0,09145 0,43225 0,23012
0,16738 0,00000 0,22096 0,14920 0,10504 0,35742
0,07575 0,19122 0,00000 0,20622 0,23204 0,29477
0,12127 0,19107 0,30516 0,00000 0,16815 0,21436
0,38157 0,08955 0,22858 0,11193 0,00000 0,18837
0,17988 0,26982 0,25713 0,12636 0,16681 0,00000
*/


/*
= (POW(C23, J2) + POW(C2, J3)) / (
	POW(C23, J2) + C2 ** J3 +
	POW(D23, J2) + D3 ** J3 +
	POW(E23, J2) + E3 ** J3 +
	POW(F23, J2) + F3 ** J3 +
	POW(G23, J2) + G3 ** J3
) 
*/