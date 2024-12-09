import assert from 'assert';
import { reverse } from 'dns';
import * as MathJS from 'mathjs'

// Nota: arma la matriz G de la forma [I, P]

function binaryMultiply(a: MathJS.Matrix, b: MathJS.Matrix): MathJS.Matrix {
	return MathJS.map(
		MathJS.multiply(a, b),
		x => x % 2
	);
}

function isZeroes(a: MathJS.Matrix): boolean {
	return a.toArray().flat().every(x => x === 0);
}

function binaryXor(a: MathJS.Matrix, b: MathJS.Matrix): MathJS.Matrix {
	return (MathJS.xor(a, b) as MathJS.Matrix).map(Number)
}

MathJS.Matrix.prototype[Symbol.for('nodejs.util.inspect.custom')] = function() {
	const [rows, columns] = this.size();
	const arr = this.toArray();

	if(rows === 1) return '\n' + arr.join('');
	else if(columns === 1 || !columns) return '\n' + arr.join('');
	else return '\n  ' + arr.map((x: number[]) => x.join('')).join('\n  ');
}

class MatrixCoding {
	constructor(P: MathJS.Matrix, reverse = false){
		const [rows, cols] = P.size() as [number, number];

		this.K = rows;
		this.N = cols + rows;
		this.Q = cols;

		this.P = P;

		if(reverse){
			this.G = MathJS.concat(this.P, MathJS.identity(this.K)) as MathJS.Matrix;
			this.H = MathJS.concat(MathJS.identity(this.N - this.K), MathJS.transpose(this.P)) as MathJS.Matrix;
		}else{
			this.G = MathJS.concat(MathJS.identity(this.K), this.P) as MathJS.Matrix;	
			this.H = MathJS.concat(MathJS.transpose(this.P), MathJS.identity(this.N - this.K)) as MathJS.Matrix;
		}

		this.Ht = MathJS.transpose(this.H);

		if(!isZeroes(binaryMultiply(this.G, this.Ht))) {
			throw new Error('La matriz G no es ortogonal a la matriz H');
		}
	}
	public readonly N: number; // Cantidad de bits totales
	public readonly K: number; // Cantidad de bits de datos
	public readonly Q: number; // Cantidad de bits de control

	public readonly P: MathJS.Matrix; // Matriz de chequeo de paridad
	public readonly G: MathJS.Matrix; // Matriz generadora
	public readonly H: MathJS.Matrix; // Matriz de chequeo de error
	public readonly Ht: MathJS.Matrix; // Matriz transpuesta de H

	public encode(data: number[]): number[] {
		if(data.some(x => x !== 0 && x !== 1)){
			throw new Error('Los datos deben ser 0 o 1');
		}

		if(data.length !== this.K){
			throw new Error(`Se esperaban ${this.K} bits de datos`);
		}

		const x = MathJS.matrix(data);

		return binaryMultiply(x, this.G).toArray() as number[];
	}

	public encodeString(data: string): string {
		return this.encode(data.split('').map(Number)).join('');
	}

	private findErrorPattern(syndrome: MathJS.Matrix): MathJS.Matrix {
		// return MathJS.multiply(syndrome, MathJS.pinv(this.Ht)).map(x => Math.abs(Math.round(x as number))) as MathJS.Matrix; // (inverse aproximation)

		const errorPattern = MathJS.zeros(this.N) as MathJS.Matrix;

		for(let i = 0; i < this.N; i++){
			const row = MathJS.reshape(MathJS.row(this.Ht, i), [this.Q]) as MathJS.Matrix;

			if(MathJS.deepEqual(row, syndrome)){
				errorPattern.set([i], 1);
				return errorPattern;
			}
		}

		for(let i = 0; i < this.N; i++){
			const row1 = MathJS.reshape(MathJS.row(this.Ht, i), [this.Q]) as MathJS.Matrix;

			for(let j = i + 1; j < this.N; j++){
				const row2 = MathJS.reshape(MathJS.row(this.Ht, j), [this.Q]) as MathJS.Matrix;

				const row = binaryXor(row1, row2);

				if(MathJS.deepEqual(row, syndrome)){
					errorPattern.set([i], 1);
					errorPattern.set([j], 1);
					return errorPattern;
				}
			}
		}

		throw new Error('No se pudo encontrar el patrón de error');
	}

	public correct(data: number[]): number[] {
		const dataMatrix = MathJS.matrix(data);
		const syndrome = binaryMultiply(dataMatrix, this.Ht);

		if(isZeroes(syndrome)) return data;

		const errorPattern = this.findErrorPattern(syndrome);

		return binaryXor(dataMatrix, errorPattern).toArray() as number[];
	}

	public decode(data: number[]): number[] {
		return this.correct(data).slice(0, this.K);
	}

	public decodeString(data: string): string {
		return this.decode(data.split('').map(Number)).join('');
	}

	public encodeAllPosibleWords(): void {
		console.log('=============================');
		console.log('=============================');
		console.log('=============================');
		console.log('Iniciando codificacion de todas las palabras posibles');
		
		const decoded = [];
		const encoded = [];

		for(let i = 0; i < 2 ** this.K; i++){
			const data = i.toString(2).padStart(this.K, '0');
			const encodedData = this.encodeString(data);

			decoded.push(data);
			encoded.push(encodedData);
		}

		console.log('=============================');

		for(let i = 0; i < 2 ** this.K; i++){
			console.log(decoded[i], encoded[i]);
		}

		console.log('=============================');
		console.log('=============================');
		console.log('=============================');
	}

	public calcDminByForce(): number {
		const wordsAmount = 2 ** this.K;
		const encodedWords = [];

		for(let i = 0; i < wordsAmount - 1; i++){
			const word = i.toString(2).padStart(this.K, '0');
			encodedWords.push(this.encodeString(word));
		}

		let minDistance = Infinity;

		const hammingDistance = (a: number[], b: number[]) => a.reduce((acc, x, i) => acc + (x !== b[i] ? 1 : 0), 0);

		for(const w1 of encodedWords){
			for(const w2 of encodedWords){
				if(w1 === w2) continue;

				minDistance = Math.min(minDistance, hammingDistance(w1, w2));
			}
		}

		return minDistance;
	}
}


// if(require.main === module){
// 	const P = MathJS.matrix([ // matriz de chequeo de paridad
// 		[1, 0, 1, 0, 1, 1],
// 		[0, 1, 0, 1, 1, 1],
// 	]);
// 
// 	const coder = new MatrixCoding(P);
// 	
// 	console.log(coder)
// 	// console.log(coder.calcDminByForce())
// 
// 	for(let i = 0; i < 4; i++){
// 		const data = i.toString(2).padStart(2, '0');
// 	
// 		const encoded = coder.encodeString(data);
// 		const decoded = coder.decodeString(encoded);
// 	
// 		assert(data === decoded, `Error en ${data} -> ${encoded} -> ${decoded}`);
// 	
// 		for(let j = 0; j < 4; j++){
// 			const corrupted = encoded.slice().split('').map(Number);
// 			corrupted[j]! ^= 1;
// 	
// 			const decoded = coder.decode(corrupted).join('');
// 	
// 			assert(data === decoded, `Error en ${data} -> ${corrupted.join('')} -> ${decoded}`);
// 	
// 			for(let k = 0; k < 4; k++){
// 				const corrupted2 = corrupted.slice();
// 				corrupted2[k]! ^= 1;
// 	
// 				const decoded = coder.decode(corrupted2).join('');
// 	
// 				assert(data === decoded, `Error en ${data} -> ${corrupted2.join('')} -> ${decoded}`);
// 			}
// 		}
// 	}
// }

// (I1, I2, I3, I4, U5, U6, U7)
// const P = MathJS.matrix([ // matriz de chequeo de paridad
// 	[1, 1, 0, 1], // U5 = I1 + I2 + I4
// 	[1, 0, 1, 1], // U6 = I1 + I3 + I4
// 	[1, 1, 1, 0], // U7 = I1 + I2 + I3	
// ]);

const P = MathJS.matrix([ // matriz de chequeo de paridad
 	[1, 1, 0],
 	[0, 1, 1],
 	[1, 1, 1],
	[1, 0, 1],
]);

const coder = new MatrixCoding(P);

console.log(coder)
console.log()
coder.encodeAllPosibleWords()
// console.log(coder.H)
// console.log()
// console.log(coder.Ht)
// 
// console.log(coder.calcDminByForce())
// console.log(coder.calcDminByMatrix())

/*
0000 0000000 = 0
0001 0001101 = x^3+x+1
0010 0010111 - x^4+x^2+x
0011 0011010 - x^4+x^3+x^2+1
0100 0100011 - x^5+x^2+x+1
0101 0101110 - x^5+x^3+x^2
0110 0110100 - x^5+x^4+1
0111 0111001 = x^5+x^4+x^3+x
1000 1000110 - x^6+x^2+1
1001 1001011 = x^6+x^3+x^2+x
1010 1010001 = x^6+x^4+x+1
1011 1011100 = x^6+x^4+x^3
1100 1100101 = x^6+x^5+x
1101 1101000 = x^6+x^5+x^3+1
1110 1110010 = x^6+x^5+x^4+x^2
1111 1111111 = x^6+x^5+x^4+x^3+x^2+x+1
*/

// 
// const coder = new MatrixCoding(P);
// 
// console.log(coder.G)
// 
// console.log(coder.encodeString('1101'))

//
// x^14+x^12+x^8+x^5+x+1
// console.log(coder.decode([1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1]).join(''))
// console.log(coder.decode([1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1].reverse()).join(''))
