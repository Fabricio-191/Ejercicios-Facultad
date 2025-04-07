import { copySorted, substringCounts, mapObject } from "./utils";
import Fraction from "./fraction";

export class Source {
	constructor(probabilities: Record<string, Fraction>) {
		if(Fraction.sum(Object.values(probabilities)).subtract(1n).abs().valueOf()  > 0.01) {
			throw new Error('Probabilities must sum 1');
		}

		this.probabilities = copySorted(probabilities) as Record<string, Fraction>;
	}
	public probabilities: Record<string, Fraction>;

	get symbols() {
		return Object.keys(this.probabilities);
	}

	public entropy() {
		let entropy = Fraction.zero;
		for(const symbol in this.probabilities) {
			const prob = this.probabilities[symbol]!;
			entropy = entropy.add(prob.multiply(prob.inverse().log2()));
		}

		return entropy;
	}

	public extend(length = 2n){
		const newProbabilities: Record<string, Fraction> = {};

		for(const symbolA in this.probabilities) {
			for(const symbolB in this.probabilities) {
				newProbabilities[symbolA + symbolB] = this.probabilities[symbolA]!.multiply(this.probabilities[symbolB]!);
			}
		}
		
		return new Source(newProbabilities);
	}

	static fromString(str: string) {
		const probabilities = mapObject(
			substringCounts(str),
			count => new Fraction(count, str.length)
		);

		return new Source(probabilities);
	}
}

export interface Codification<T extends string | number | Fraction> {
	encode(str: string): T;
	decode(str: T): string;
}


export interface CodificationWithOne<T extends string | number | Fraction> extends Codification<T> {
	decodeOne(str: T): [string, T];
}

export abstract class SubstitutionCodification implements Codification<string> {
	constructor(source: Source, base: number = 2) {
		this.source = source;
		this.base = base;

		this._makeCodes();
		const codesList = Object.values(this.codes);

		for(const symbol of source.symbols) {
			if(!this.codes[symbol]) {
				throw new Error('All symbols must have a code');
			}

			const code = this.codes[symbol];
			if(codesList.some(c => code.startsWith(c) && code !== c)) {
				throw new Error('Codes must be prefix-free');
			}
		}
	}
	public readonly source: Source;
	public readonly codes: Record<string, string> = {};
	public readonly base: number;

	protected abstract _makeCodes(): void;

	public encodeOne(str: string): [string, string] {
		const symbol = this.source.symbols.find(symbol => str.startsWith(symbol));

		if(!symbol) throw new Error('Invalid symbol');
		
		return [symbol, this.codes[symbol]!];
	}

	public encode(str: string): string {
		let encoded = '';
		while(str.length) {
			const [symbol, code] = this.encodeOne(str);

			encoded += code;
			str = str.slice(symbol.length);
		}

		return encoded
	};

	public decodeOne(str: string): [string, string] {
		const symbol = this.source.symbols.find(symbol => str.startsWith(this.codes[symbol]!));

		if(!symbol) throw new Error('Invalid symbol');
		
		return [symbol, this.codes[symbol]!];
	}

	public decode(str: string): string {
		let decoded = '';
		while(str.length) {
			const [symbol, code] = this.decodeOne(str);

			decoded += symbol;
			str = str.slice(code.length);
		}

		return decoded;
	};

	public kraftInequality(): Fraction {
		const baseInv = new Fraction(1, this.base);
		return Fraction.sum(
			Object.values(this.codes).map(code => baseInv.pow(code.length))
		);
	}

	public averageLength(): Fraction {
		let sum = new Fraction(0);
		for(const symbol in this.source.symbols) {
			sum = sum.add(
				this.source.probabilities[symbol]!
					.multiply(this.codes[symbol]!.length)
			);
		}

		return sum;
	}
}

const src = Source.fromString('aeiioouuaeii');

console.log(src.entropy())
console.log(src.probabilities)