import assert from "assert";
import * as MathJS from "mathjs";
import Polynomial from "polynomial";

function polyAbs(p: Polynomial | string): Polynomial {
	if(typeof p === 'string'){
		return polyAbs(new Polynomial(p));
	}

	const p1 = p.clone();

	for (const i in p1.coeff){
		p1.coeff[i] = Math.abs(p1.coeff[i]);
	}

	return p1;
}

// @ts-expect-error
Polynomial.prototype[Symbol.for('nodejs.util.inspect.custom')] = function() {
	return this.toString();
}

const logDivisions = false;

function divide(dividend: Polynomial, baseDivisor: Polynomial, warn = false): {
	result: Polynomial,
	remainder: Polynomial,
	dividendsTrace: Polynomial[],
	divisorsTrace: Polynomial[]
} {
	const r: Record<number, number> = {};

	let i = dividend.degree();
	const j = baseDivisor.degree();

	const dividendsTrace = [];
	const divisorsTrace = [];

	while(i >= j){
		dividendsTrace.push(dividend.clone());

		const tmp = r[i - j] = dividend.coeff[i] / baseDivisor.coeff[j];
		const divisor = baseDivisor.mul(`x^${i - j}`);

		dividend = polyAbs(dividend.sub(divisor.mul(tmp.toString())));

		divisorsTrace.push(divisor);

		i = dividend.degree();
	}

	if(warn && dividend.toString() !== '0'){
		console.warn('Warning: Division remainder is not 0');
	}

	if(logDivisions){
		console.log({
			result: new Polynomial(r),
			remainder: dividend,
			dividendsTrace,
			divisorsTrace
		})

		for(let i = 0; i < dividendsTrace.length; i++){
			console.log(
				dividendsTrace[i]!.toString(), ' - ',
				divisorsTrace[i]!.toString(), ' = ',
				dividendsTrace[i + 1] ?? dividend);
		}
	}

	return {
		result: new Polynomial(r),
		remainder: dividend,
		dividendsTrace,
		divisorsTrace
	};
}

function bin(a: Polynomial): Polynomial {
	const r: Record<number, number> = {};

	for(const i in a.coeff){
		// @ts-expect-error
		r[i] = a.coeff[i] % 2; // cut the number to 1 bit
	}

	return new Polynomial(r);
}

function binStrToPol(data: string): Polynomial {
	const pol = data.split('').reverse().map((bit, i) => {
		if(bit !== '0' && bit !== '1'){
			throw new Error('Los datos deben ser 0 o 1');
		}

		return bit === '0' ? '' : `x^${i}`;
	}).join('+');

	return new Polynomial(pol)
}

function polToBinStr(a: Polynomial): string {
	if(a.toString() === '0') return '0';
	const arr = Array(a.degree() + 1).fill('0');
	
	for(const i in a.coeff){
		// @ts-expect-error
		arr[a.degree() - i] = a.coeff[i] % 2;
	}

	return arr.join('');
}

class CiclicCode {
	constructor(
		N: number,
		K: number,
		G: Polynomial | null = null,
		H: Polynomial | null = null
	){
		this.N = N;
		this.K = K;
		console.log(G, H, N - K);

		const BASE = new Polynomial(`x^${N}+1`);
		if(G === null && H === null){
			throw new Error('G o H deben ser provistos');
		}
		if(H === null) H = divide(BASE, G!, true).result
		if(G === null) G = divide(BASE, H , true).result

		this.G = G!;
		this.H = H!;

		if(G.degree() !== (N - K)){
			throw new Error('G debe ser de grado N - K');
		}else if(H.degree() !== this.K){
			throw new Error('H debe ser de grado K');
		}
	}

	public readonly N: number;
	public readonly K: number;
	public G: Polynomial;
	public H: Polynomial;

	public encode(data: Polynomial): Polynomial {
		if(data.degree() > this.K){
			throw new Error(`Se esperaban como mucho ${this.K} bits de datos`);
		}

		return bin(data.mul(this.G));
	}

	public encodeSistematic(data: Polynomial): Polynomial {
		const T = data.mul(`x^${this.N - this.K}`);

		const result = divide(T, this.G);

		return T.add(result.remainder);
	}

	public decode(data: Polynomial): Polynomial {
		if(data.degree() > this.N){
			throw new Error(`Se esperaban como mucho ${this.N} bits de datos`);
		}

		const division = divide(data, this.G);
		if(division.remainder.degree() === 0){
			return division.result;
		}

		console.log('division', division)

		console.warn('Palabra recibida con error');
		// correct data
		const syndrome = division.remainder;
		const correctedData = data.sub(syndrome);

		const correctedDivision = divide(correctedData, this.G);

		if(correctedDivision.remainder.degree() !== 0){
			throw new Error('No se pudo corregir el error');
		}

		return correctedDivision.result;
	}

	public decodeSistematic(data: Polynomial): Polynomial {
		if(data.degree() > this.N){
			throw new Error(`Se esperaban como mucho ${this.N} bits de datos`);
		}

		const result = divide(data, this.G);

		return result.result;
	}
	
	public getMatrixes(): {
		P: MathJS.Matrix,
		G: MathJS.Matrix,
		H: MathJS.Matrix
	} { // De la forma [I, P] (el profe en el ppt lo al reves a nivel de bit)
		const P = [];

		for(let i = 0; i < this.K; i++){
			const A = new Polynomial(`x^${this.N - this.K + i}`);

			const result = divide(A, this.G);

			P.push(
				polToBinStr(result.remainder).padStart(this.N - this.K, '0').split('').map(Number)
			);
		}

		const matrixP = MathJS.matrix(P);


		const G = MathJS.concat(MathJS.identity(this.K), matrixP) as MathJS.Matrix;	
		const H = MathJS.concat(MathJS.transpose(matrixP), MathJS.identity(this.N - this.K)) as MathJS.Matrix;

		return {
			P: matrixP,
			G,
			H
		};
	}

	public calcDmin(): number {
		let min = Infinity;

		for(let i = 0; i < 2 ** this.K; i++){
			const word = binStrToPol(i.toString(2).padStart(this.K, '0'));
			const encoded = this.encode(word);

			const d = this.decode(encoded).degree();

			if(d < min){
				min = d;
			}
		}

		return min;
	}
}

if(false && require.main === module){
	const codes = [
		new CiclicCode(7, 4, new Polynomial('x^3+x+1')),
		// new CiclicCode(15, 5, new Polynomial('1+x+x^2+x^4+x^5+x^8+x^10'))
	];

	for(const code of codes){
		for(let i = 0; i < 2 ** code.K; i++){
			const str = i.toString(2).padStart(4, '0');
			const word = binStrToPol(str);
			const encoded = code.encode(word);
			// const encodedSistematic = code1.encodeSistematic(word);
		
			// assert(encoded.toString() === encodedSistematic.toString(), `Error en ${word} -> ${encoded} -> ${encodedSistematic}`);
		
			const decoded = code.decode(encoded);
			// const decodedSistematic = code1.decodeSistematic(encodedSistematic);
		
			assert(word.toString() === decoded.toString(), `Error en ${word} -> ${encoded} -> ${decoded}`);
			 // assert(word.toString() === decodedSistematic.toString(), `Error en ${word} -> ${encodedSistematic} -> ${decodedSistematic}`);


			// const encodedStr = polToBinStr(encoded).padStart(code.N, '0');
			// for(let j = 0; j < code.N; j++){
			// 	const corrupted = encodedStr.split('');
			// 	corrupted[j] = corrupted[j] === '0' ? '1' : '0';
			// 	const corruptedPol = binStrToPol(corrupted.join(''));
// 
			// 	console.log(word, corruptedPol);
// 
			// 	const decodedError = code.decode(corruptedPol);
// 
			// 	assert(word.toString() === decodedError.toString(), `Error en ${word} -> ${corruptedPol} -> ${decodedError}`);
			// }
		}
	}
}

// const code = new CiclicCode(12, 3, null, new Polynomial('x^3+x^2+x+1'));
// const code = new CiclicCode(7, 4, new Polynomial('x^3+x+1'));
// 
// console.log(code.getMatrixes().H.toArray().map(row => row.join('')).join('\n'));
// 
// console.log(code.G);


const code = new CiclicCode(15, 5, new Polynomial('x^10+x^8+x^5+x^4+x^2+x+1'));

console.log(code)
console.log(code.H)
console.log()
console.log(code.encodeSistematic(new Polynomial('x^4+x+1')))

const matrixes = code.getMatrixes();

console.log(matrixes.P.toArray().map(row => row.join('')).join('\n'));
console.log()
console.log(matrixes.G.toArray().map(row => row.join('')).join('\n'));
console.log()
console.log(matrixes.H.toArray().map(row => row.join('')).join('\n'));

// console.log(code.calcDmin());

/*
syn: 0100011100
err 000000100001010
11000
syn: 0111111111
err 000000000000000
10100
*/

// console.log(code.decode(new Polynomial('x^14+x^12+x^8+x^5+x+1')));

for(let i = 0; i < 32; i++){
	const data = i.toString(2).padStart(5, '0');
	const encoded = code.encode(binStrToPol(data));

	console.log(data, encoded);
}