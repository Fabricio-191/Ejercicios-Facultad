/*
Tengo un sistema de ecuaciones simultaneo:

v1+v2+v3+v4+v5=100
v1+v6+v7+v8+v9=100
v1+v10+v11+v12+v13=100
v1+v14+v15+v16+v17=100
v1+v18+v19+v20+v21=100

v2+v6+v10+v14+v18=100
v3+v7+v11+v15+v19=100
v4+v8+v12+v16+v20=100
v5+v9+v13+v17+v21=100

Tengo 21 numeros, los cuales puedo asignar a esas 21 variables, sin repetir numeros, solo hay 5 numeros pares
Ademas se que v1 tiene que ser par y que en las primeras 5 ecuaciones, habra dos ecuaciones con 3 numeros pares y 2 impares, y 3 ecuaciones con 1 numero par y 4 impares

Crear un codigo que me de las soluciones posibles
*/

const nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 20, 32, 34, 38, 40].sort((a, b) => a - b);
const even = nums.filter(a => a % 2 === 0);
const odd = nums.filter(a => a % 2 === 1);

const differentValues = (...values) => new Set(values).size === values.length;
const add = (arr) => arr.reduce((a, b) => a + b, 0);

const eqArray = (xs, ys) =>
	xs.length === ys.length &&
	xs.every(x => ys.includes(x));

for(let i = 0; i < 5; i++){
	for(const range1 of range(0, 1, 5)){
		// select v1
		const v1 = even[range1[0]];

		
	}
}


function* range(start, end, size, triangular = false){
	const range = Array(size).fill(start);

	if(triangular){
		while(range[0] <= end){
			yield range.slice();
			range[size - 1]++;
			
			for(let i = size - 1; i > 0; i--){
				if(range[i] > end) range[i - 1]++;
			}

			for(let i = 0; i < size; i++){
				if(range[i] > end) range[i] = range[i - 1];
			}
		}
	}else while(range[0] <= end){
		yield range.slice();
		range[size - 1]++;
		for(let i = size - 1; i > 0; i--){
			if(range[i] > end){
				range[i] = start;
				range[i - 1]++;
			}
		}
	}
}

