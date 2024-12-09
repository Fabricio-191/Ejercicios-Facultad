import assert = require("assert");
import * as MathJS from "mathjs";
import Polynomial from "polynomial";
const logFile = require('fs').createWriteStream('./node.access.log')

const consoleLog2 = (...args: unknown[]) => {
	console.log(...args);

	args = args.map(x => x instanceof MathJS.Matrix ? x : x);

	logFile.write(args.join(' ') + '\n');
}

// @ts-expect-error
Polynomial.prototype[Symbol.for('nodejs.util.inspect.custom')] = function() {
	return this.toString();
}

MathJS.Matrix.prototype[Symbol.for('nodejs.util.inspect.custom')] = function() {
	const [rows, columns] = this.size();
	const arr = this.toArray();

	if(rows === 1) return arr.join('');
	else if(columns === 1 || !columns) return arr.join('');
	else return arr.map((x: number[]) => x.join('')).join('\n');
}

function bin(a: Polynomial): Polynomial {
	const r: Record<number, number> = {};

	for(const i in a.coeff){
		// @ts-expect-error
		r[i] = a.coeff[i] % 2; // cut the number to 1 bit
	}

	return new Polynomial(r);
}

function divide(baseDividend: Polynomial, baseDivisor: Polynomial, warn = false): {
	result: Polynomial,
	remainder: Polynomial,
} {
	const r: Record<number, number> = {};

	consoleLog2('--------- Inicio division ---------');
	consoleLog2('Dividimos:', baseDividend, '/', baseDivisor)
	consoleLog2()

	let dividend = baseDividend.clone();
	let i = dividend.degree();
	const j = baseDivisor.degree();

	while(i >= j){
		consoleLog2('  ', dividend.toString())

		const tmp = r[i - j] = dividend.coeff[i] / baseDivisor.coeff[j];
		const divisor = baseDivisor.mul(`x^${i - j}`);

		dividend = dividend.sub(divisor.mul(tmp.toString()));
		
		for (const i in dividend.coeff){
			dividend.coeff[i] = Math.abs(dividend.coeff[i]);
		}

		consoleLog2('- ', divisor.toString())
		consoleLog2('__________________________________');

		i = dividend.degree();
	}
	consoleLog2('  ', dividend);

	if(warn && dividend.toString() !== '0'){
		console.warn('Warning: Division remainder is not 0');
	}

	consoleLog2('Resultado division:', baseDividend, '/', baseDivisor, '=', new Polynomial(r));
	consoleLog2('Resto:', dividend.toString());
	consoleLog2('--------- Fin division ---------');

	return {
		result: new Polynomial(r),
		remainder: dividend,
	};
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

function polToNumberArray(a: Polynomial, N: number): number[] {
	return polToBinStr(a).padStart(N, '0').split('').map(Number);
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

		consoleLog2('Armamos el codigo cilico con N:', N, 'K:', K);

		const BASE = new Polynomial(`x^${N}+1`);
		if(G === null && H === null){
			throw new Error('G o H deben ser provistos');
		}
		if(H === null){
			consoleLog2('Como tenemos G, despejamos H');
			consoleLog2('Dividimos x^N+1 en G\n');

			H = divide(BASE, G!, true).result

			consoleLog2('Nota: el resto debe dar 0');
			consoleLog2('H:', H.toString());
		}
		if(G === null){
			consoleLog2('Como tenemos H, despejamos G');
			consoleLog2('Dividimos x^N+1 en H\n');

			G = divide(BASE, H , true).result
			consoleLog2('Nota: el resto debe dar 0');
			consoleLog2('G:', G.toString());
		}
		consoleLog2('=============================');

		this.G = G!;
		this.H = H!;

		consoleLog2('La distancia minima es:', G.toString().split('+').length);
		consoleLog2('En base a la cantidad de terminos no nulos del polinomio G');
		consoleLog2('=============================');
		consoleLog2('=============================');

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
		if(data.degree() >= this.K){
			throw new Error(`Se esperaban como mucho ${this.K} bits de datos`);
		}
		consoleLog2('=============================');
		consoleLog2('=============================');

		consoleLog2('Codificando');
		consoleLog2('Datos entrada:', data.toString());
		consoleLog2('Multiplicamos los datos por G');

		const result = bin(data.mul(this.G));

		consoleLog2('Resultado:', result.toString());

		consoleLog2('=============================');
		consoleLog2('=============================');
		return result;
	}

	public encodeSistematic(data: Polynomial): Polynomial {
		if(data.degree() >= this.K){
			throw new Error(`Se esperaban como mucho ${this.K} bits de datos`);
		}
		consoleLog2('=============================');
		consoleLog2('=============================');
		consoleLog2('Codificando de manera sistematica');
		const T = data.mul(`x^${this.N - this.K}`);

		consoleLog2('Datos entrada:', data.toString());
		consoleLog2('Bin:', polToBinStr(data));

		consoleLog2('Multiplicamos los datos por x^(N - K)');
		consoleLog2('T:', T.toString());

		consoleLog2('Dividimos T en G');
		const result = divide(T, this.G);
		
		consoleLog2('Agregamos el resto de la division a T');
		consoleLog2('Basicamente el resto son los bits');
		const r = T.add(result.remainder);

		consoleLog2('Resultado codificado:', r.toString());

		consoleLog2('=============================');
		consoleLog2('=============================');
		return r;
	}

	public decode(data: Polynomial): Polynomial {
		if(data.degree() > this.N){
			throw new Error(`Se esperaban como mucho ${this.N} bits de datos`);
		}
		consoleLog2('=============================');
		consoleLog2('=============================');
		consoleLog2(`Decodificamos ${data.toString()}`);
		consoleLog2('Dividimos los datos en G');

		const division = divide(data, this.G);

		consoleLog2('Decodificado:', division.result.toString());
		if(division.remainder.toString() === '0'){
			consoleLog2('El resto de la division es 0, lo que indica una palabra valida');

			consoleLog2('=============================');
			consoleLog2('=============================');
			return division.result;
		}

		throw new Error('No se pudo decodificar');
	}

	public decodeSistematic(data: Polynomial): Polynomial {
		if(data.degree() > this.N){
			throw new Error(`Se esperaban como mucho ${this.N} bits de datos`);
		}
		consoleLog2('=============================');
		consoleLog2('=============================');

		consoleLog2('Decodificando de manera sistematica');
		consoleLog2('Datos entrada:', data.toString());
		consoleLog2('Dividimos los datos en G');

		const result = divide(data, this.G);

		if(result.remainder.toString() === '0'){
			consoleLog2('El resto de la division es 0, lo que indica una palabra valida');
		}else{
			console.warn('El resto de la division no es 0, lo que indica una palabra con error');
		}

		consoleLog2('Luego para decodificar dividimos los datos en x^(N - K)');

		const division = divide(data, new Polynomial(`x^${this.N - this.K}`));

		consoleLog2('Decodificado:', division.result.toString());
		consoleLog2('=============================');
		consoleLog2('=============================');
		return division.result;
	}
	
	public getMatrixes(): {
		P: MathJS.Matrix,
		G: MathJS.Matrix,
		H: MathJS.Matrix
	} { // De la forma [I, P] (el profe en el ppt lo al reves a nivel de bit)
		consoleLog2('=============================');
		consoleLog2('=============================');
		consoleLog2('=============================');
		consoleLog2('Calculando matrices G, H y P');
		consoleLog2('Obtenemos la matriz P');
		const P = [];

		for(let i = 0; i < this.K; i++){
			consoleLog2('=============================');
			consoleLog2(`Para obtener la fila ${i + 1} de P`);
			const A = new Polynomial(`x^${this.N - this.K + i}`);

			consoleLog2(`Dividimos ${A} en G`);

			const result = divide(A, this.G);
			const row = result.remainder;

			consoleLog2('Resultado:', row);
			consoleLog2('Resultado:', A.add(result.remainder));

			P.push(polToNumberArray(row, this.N - this.K));
		}

		const matrixP = MathJS.matrix(P);

		consoleLog2('=============================');
		consoleLog2('=============================');

		consoleLog2('La matriz P obtenida fue: ');

		consoleLog2(matrixP);

		const G = MathJS.concat(MathJS.identity(this.K), matrixP) as MathJS.Matrix;	
		const H = MathJS.concat(MathJS.transpose(matrixP), MathJS.identity(this.N - this.K)) as MathJS.Matrix;

		consoleLog2('Obtenemos la matriz G de la manera [I, P]');
		consoleLog2(G);
		consoleLog2('Obtenemos la matriz H de la manera [P^t, I]');
		consoleLog2(H);

		consoleLog2('=============================');
		consoleLog2('=============================');
		consoleLog2('=============================');
		return {
			P: matrixP,
			G,
			H
		};
	}

	public encodeAllPosibleWords(): Polynomial[] {
		console.log('=============================');
		console.log('=============================');
		console.log('=============================');
		console.log('=============================');
		console.log('Iniciando codificacion de todas las palabras posibles');
		const words: string[] = [];
		const pols: Polynomial[] = [];

		for(let i = 0; i < 2 ** this.K; i++){
			const binStr = i.toString(2).padStart(this.K, '0');
			const word = binStrToPol(binStr);
			const encoded = this.encode(word);

			words.push(binStr);
			pols.push(encoded);
		}

		for(let i = 0; i < words.length; i++){
			console.log(words[i], pols[i]!.toString());
		}

		console.log('=============================');
		console.log('=============================');
		console.log('=============================');
		console.log('=============================');

		return pols;
	}

	public encodeSystematicAllPosibleWords(): Polynomial[] {
		console.log('=============================');
		console.log('=============================');
		console.log('=============================');
		console.log('=============================');
		console.log('Iniciando codificacion de todas las palabras posibles');
		const words: string[] = [];
		const pols: Polynomial[] = [];

		for(let i = 0; i < 2 ** this.K; i++){
			const binStr = i.toString(2).padStart(this.K, '0');
			const word = binStrToPol(binStr);
			const encoded = this.encodeSistematic(word);

			words.push(binStr);
			pols.push(encoded);
		}

		for(let i = 0; i < words.length; i++){
			console.log(words[i], pols[i]!.toString());
		}

		console.log('=============================');
		console.log('=============================');
		console.log('=============================');
		console.log('=============================');

		return pols;
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
		new CiclicCode(15, 5, new Polynomial('1+x+x^2+x^4+x^5+x^8+x^10')),
		new CiclicCode(9, 2, new Polynomial('x^7+x^6+x^4+x^3+x+1'))
	];

	for(const code of codes){
		for(let i = 0; i < 2 ** code.K; i++){
			const str = i.toString(2).padStart(4, '0');
			const word = binStrToPol(str);
			const encoded = code.encode(word);
			const encodedSistematic = code.encodeSistematic(word);
		
			const decoded = code.decode(encoded);
			const decodedSistematic = code.decodeSistematic(encodedSistematic);
		
			assert(word.toString() === decoded.toString(), `Error en ${word} -> ${encoded} -> ${decoded}`);
			assert(word.toString() === decodedSistematic.toString(), `Error en ${word} -> ${encodedSistematic} -> ${decodedSistematic}`);


			// const encodedStr = polToBinStr(encoded).padStart(code.N, '0');
			// for(let j = 0; j < code.N; j++){
			// 	const corrupted = encodedStr.split('');
			// 	corrupted[j] = corrupted[j] === '0' ? '1' : '0';
			// 	const corruptedPol = binStrToPol(corrupted.join(''));
// 
			// 	consoleLog2(word, corruptedPol);
// 
			// 	const decodedError = code.decode(corruptedPol);
// 
			// 	assert(word.toString() === decodedError.toString(), `Error en ${word} -> ${corruptedPol} -> ${decodedError}`);
			// }
		}
	}
}

// const code = new CiclicCode(7, 4, new Polynomial('x^3+x+1'));
// code.encodeAllPosibleWords();

// const code = new CiclicCode(15, 5, new Polynomial('x^10+x^8+x^5+x^4+x^2+x+1'));
// 
// consoleLog2()
// consoleLog2(code.encodeSistematic(new Polynomial('x^4+x+1')))
// 
// const matrixes = code.getMatrixes();

// consoleLog2(code.calcDmin());


// const code = new CiclicCode(12, 3, null, new Polynomial('x^3+x^2+x+1'));

const code = new CiclicCode(7, 4, new Polynomial('x^3+x+1'));

code.getMatrixes()

code.encodeSystematicAllPosibleWords();