import assert from 'assert';
import { Codification, MinASCII, Shannon, Source, Huffman, Fano } from './basicCodifications.ts';

const subdivideString = (str: string, order: number): string[] => {
	const substrings: string[] = [];
	for (let i = 0; i < str.length - order + 1; i++) {
		substrings.push(str.slice(i, i + order));
	}

	return substrings;
}

const count = (arr: string[]): { [key: string]: number } => arr.reduce((acc, curr) => {
	acc[curr] = (acc[curr] || 0) + 1;
	return acc;
}, {});

class Markov<T extends typeof Codification> {
	constructor(str: string, order = 1, codification: T) {
		this.symbols = Array.from(new Set(str.split(''))).sort();
		this.order = order;
		this.codification = codification;

		this.basicCodes = MinASCII.fromString(str);

		this._makeCodes(str);
	}
	public readonly codification: T;
	public readonly symbols: string[];
	public readonly order: number;
	public readonly basicCodes: MinASCII;
	public readonly codifications: {
		[key: string]: InstanceType<T>,
	} = {};

	private _makeCodes(str: string): void {
		const divisions = subdivideString(str, this.order + 1);
		const keys = [...new Set(divisions.map(str => str.slice(0, -1)))];

		for(const key of keys) {
			const uses = divisions.filter(str => str.startsWith(key));
			const counts = count(uses.map(str => str.slice(-1)));
			const symbols = Object.keys(counts).sort();
			const probabilities = symbols.map(symbol => counts[symbol] / uses.length);

			// @ts-expect-error
			this.codifications[key] = new this.codification(
				new Source(symbols, probabilities)
			);
		}
		
	}

	public encode(str: string): string {
		let encoded = '';
		for(let i = 0; i < this.order; i++) {
			encoded += this.basicCodes.encode(str[i]);
		}

		let prev = str.slice(0, this.order);
		for(let i = this.order; i < str.length; i++) {
			encoded += this.codifications[prev].encode(str[i]);
			prev = prev.slice(1) + str[i];
		}

		return encoded;
	}

	public decode(str: string): string {
		let decoded = '';
		while(str.length) {
			const [symbol, code] = decoded.length < this.order ?
				this.basicCodes.decodeOne(str) :
				this.codifications[decoded.slice(-this.order)].decodeOne(str);
				
			decoded += symbol;
			str = str.slice(code.length);
		}

		return decoded;
	}
}

if (require.main === module) {
	const str = 'https://www.geeknetic.es/Noticia/17666/Winrar-vs-7-Zip-vs-Winzip-Cual-es-el-mejor-descompresor-para-Windows.html';
	// const str = require('fs').readFileSync('D:\\Programacion\\Ejercicios-Facultad\\4to año\\Teoria de la informacion\\A\\basicCodifications.ts', 'utf-8');
	const markovHuffman = new Markov(str, 2, Huffman);
	const encodedHuffman = markovHuffman.encode(str);
	assert.strictEqual(str, markovHuffman.decode(encodedHuffman));

	const markovShannon = new Markov(str, 2, Shannon);
	const encodedShannon = markovShannon.encode(str);
	assert.strictEqual(str, markovShannon.decode(encodedShannon));

	const markovFano = new Markov(str, 2, Fano);
	const encodedFano = markovFano.encode(str);
	assert.strictEqual(str, markovFano.decode(encodedFano));

	console.log(encodedHuffman.length, '<', encodedFano.length, '<', encodedShannon.length);
}
