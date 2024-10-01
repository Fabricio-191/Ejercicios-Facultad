import assert from 'assert';
import { Codification, Source } from './core/base';
import { Shannon, Huffman, Fano } from './estaticas/estaticas';
import { MinASCII } from './estaticas/ASCII';
import Fraction from './core/fraction';

const subdivideString = (str: string, order: number): string[] => {
	const substrings: string[] = [];
	for (let i = 0; i < str.length - order + 1; i++) {
		substrings.push(str.slice(i, i + order));
	}

	return substrings;
}

type Constructor<T> = new (...args: any[]) => T;

interface CodificationWithDecodeOne extends Codification<string> {
	decodeOne(str: string): [string, string];
}

class Markov implements Codification<string> {
	constructor(str: string, order = 1, codification: Constructor<CodificationWithDecodeOne>) {
		this.symbols = Array.from(new Set(str.split(''))).sort();
		this.order = order;
		this.codification = codification;

		this.basicCodes = MinASCII.fromString(str);

		this._makeCodes(str);
	}
	public readonly codification: Constructor<CodificationWithDecodeOne>;
	public readonly symbols: string[];
	public readonly order: number;
	public readonly basicCodes: MinASCII;
	public readonly codifications: {
		[key: string]: CodificationWithDecodeOne,
	} = {};

	private _makeCodes(str: string): void {
		const divisions = subdivideString(str, this.order + 1);
		const keys = [...new Set(divisions.map(str => str.slice(0, -1)))];

		for(const key of keys) {
			const uses = divisions.filter(str => str.startsWith(key));
			const probabilities: Record<string, Fraction> = {};

			for(const use of uses) {
				const symbol = use.slice(-1);
				probabilities[symbol] = (probabilities[symbol] || Fraction.zero).add(1);
			}

			for(const symbol in probabilities) {
				probabilities[symbol] = probabilities[symbol]!.divide(uses.length);
			}

			this.codifications[key] = new this.codification(
				new Source(probabilities)
			);
		}
		
	}

	public encode(str: string): string {
		let encoded = '';
		for(let i = 0; i < this.order; i++) {
			encoded += this.basicCodes.encode(str[i]!);
		}

		let prev = str.slice(0, this.order);
		for(let i = this.order; i < str.length; i++) {
			encoded += this.codifications[prev]!.encode(str[i]!);
			prev = prev.slice(1) + str[i];
		}

		return encoded;
	}

	public decode(str: string): string {
		let decoded = '';

		while(str.length) {
			const [symbol, code] = decoded.length < this.order ?
				this.basicCodes.decodeOne(str) :
				this.codifications[decoded.slice(-this.order)]!.decodeOne(str);
				
			decoded += symbol;
			str = str.slice(code.length);
		}

		return decoded;
	}
}

if (require.main === module) {
	// const str = 'https://www.geeknetic.es/Noticia/17666/Winrar-vs-7-Zip-vs-Winzip-Cual-es-el-mejor-descompresor-para-Windows.html';
	const str = 'aeiouaaaeouaiaaoeoua';
	const grado = 2;

	const markovHuffman = new Markov(str, grado, Huffman);
	const encodedHuffman = markovHuffman.encode(str);
	assert.strictEqual(str, markovHuffman.decode(encodedHuffman));

	const markovShannon = new Markov(str, grado, Shannon);
	const encodedShannon = markovShannon.encode(str);
	assert.strictEqual(str, markovShannon.decode(encodedShannon));

	const markovFano = new Markov(str, grado, Fano);
	const encodedFano = markovFano.encode(str);
	assert.strictEqual(str, markovFano.decode(encodedFano));

	console.log(encodedHuffman.length, '<', encodedFano.length, '<', encodedShannon.length, '<', str.length * 8);
}
